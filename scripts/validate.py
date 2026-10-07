#!/usr/bin/env python3
"""Validate this pack's generated YAML subset, links, metadata and portable content."""
from pathlib import Path
import json
import re
import sys
import ast

ROOT = Path(__file__).resolve().parents[1]

def check():
    errors = []
    def require(condition, message):
        if not condition:
            errors.append(message)
    manifest = json.loads((ROOT/'plugin.json').read_text(encoding='utf-8'))
    claude = json.loads((ROOT/'.claude-plugin/plugin.json').read_text(encoding='utf-8'))
    require(manifest['name'] == claude['name'], 'plugin identities must agree')
    require(manifest['version'] == claude['version'], 'plugin versions must agree')
    cases = json.loads((ROOT/'evals/cases.json').read_text(encoding='utf-8'))
    folders = sorted((ROOT/'skills').iterdir())
    require(bool(folders), 'no skills found')
    for folder in folders:
        skill = folder/'SKILL.md'
        require(skill.is_file(), str(folder.name) + ': missing SKILL.md')
        if not skill.is_file():
            continue
        content = skill.read_text(encoding='utf-8')
        match = re.match(r'\A---\nname: ([a-z0-9-]+)\ndescription: ("[^\n]*")\n---\n', content)
        require(bool(match), folder.name + ': invalid generated frontmatter')
        if not match:
            continue
        require(match[1] == folder.name and len(match[1]) <= 64, folder.name + ': name mismatch')
        require('--' not in match[1] and not match[1].startswith('-') and not match[1].endswith('-'), folder.name + ': invalid hyphenation')
        description = json.loads(match[2])
        require(0 < len(description) <= 1024 and '<' not in description and '>' not in description, folder.name + ': description invalid')
        require(len(content.splitlines()) < 500, folder.name + ': entrypoint too long')
        metadata = (folder/'agents/openai.yaml').read_text(encoding='utf-8')
        short = re.search(r'^  short_description: ("[^\n]*")$', metadata, re.M)
        prompt = re.search(r'^  default_prompt: ("[^\n]*")$', metadata, re.M)
        require(bool(short) and 25 <= len(json.loads(short[1])) <= 64, folder.name + ': short description length')
        require(bool(prompt) and '$'+folder.name in json.loads(prompt[1]), folder.name + ': default prompt missing invocation')
        own_cases = [case for case in cases if case['skill'] == folder.name]
        require({case['type'] for case in own_cases} >= {'activation','boundary','non-trigger'}, folder.name + ': incomplete evaluation cases')
        require(all(case['prompt'] and case['expected'] for case in own_cases), folder.name + ': empty evaluation case')
    for path in ROOT.rglob('*'):
        require(not path.is_symlink(), 'symlink in distribution: ' + str(path.relative_to(ROOT)))
        if not path.is_file() or '.git' in path.parts:
            continue
        if path.suffix in {'.md','.yaml','.json','.py','.csv','.txt'}:
            text = path.read_text(encoding='utf-8')
            require(not re.search(r'(?i)[A-Z]:[\\/]Users[\\/][^\s]+', text), str(path.relative_to(ROOT))+': absolute private home path')
            require(not re.search(r'\b(?:sk-ant-|sk-proj-)[A-Za-z0-9_-]{20,}', text), str(path.relative_to(ROOT))+': possible provider credential')
            require(('[' + 'TODO:') not in text, str(path.relative_to(ROOT))+': unfinished scaffold')
            if path.suffix == '.py':
                ast.parse(text, filename=str(path))
            if path.suffix == '.md':
                for target in re.findall(r'\[[^\]]*\]\(([^)]+)\)', text):
                    if '://' in target or target.startswith('#'):
                        continue
                    resolved = (path.parent/target.split('#',1)[0]).resolve()
                    require(resolved.is_relative_to(ROOT) and resolved.exists(), str(path.relative_to(ROOT))+': broken/escaping link '+target)
    for error in errors:
        print('FAIL:', error)
    if errors:
        return 1
    print('PASS:', len(folders), 'skills;', len(cases), 'evaluation cases; manifests, links, metadata, privacy patterns and syntax')
    print('Behavioral model evaluations are provided for manual execution; this check does not run an AI model.')
    return 0
if __name__ == '__main__':
    sys.exit(check())

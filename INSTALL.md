# Installation and compatibility

Use the same skills/discord-durable-workflows/ folder format for both providers. Keep SKILL.md, references, agents metadata, and any scripts/assets together. Check the installed product's current documentation if its UI differs.

## Claude Code

Copy the chosen skill folder into a project's .claude/skills/ directory or your personal ~/.claude/skills/ directory. For example, .claude/skills/discord-durable-workflows/SKILL.md is the project entrypoint. Invoke /discord-durable-workflows, or describe a task that matches its description. See [Claude Code skills](https://code.claude.com/docs/en/skills).

## Claude chat or Cowork

Run scripts/package.py and upload the individual skill ZIP using Customize > Skills > Create skill > Upload a skill, where enabled. Use a single-skill ZIP, not the entire repository archive. See [Claude skill uploads](https://support.claude.com/en/articles/12512180-use-skills-in-claude).

## ChatGPT and Codex

Use the built-in skill installer where available to install a chosen skills/ subfolder from your published GitHub repository. In Codex, request $skill-installer and give the repository URL plus the skill path; then use $discord-durable-workflows. In ChatGPT surfaces with skills enabled, select the installed skill from the composer.

For plugin distribution, package this folder with its root plugin.json and skills/. Availability and installation flows depend on the product and workspace. See [OpenAI skill guidance](https://learn.chatgpt.com/docs/build-skills) and [plugin packaging](https://developers.openai.com/plugins/build/plugins). This package has no hooks, connected services, or bundled credentials.

## When native installation is unavailable

Attach or paste SKILL.md and the relevant reference for the current task, and ask the assistant to follow it. Supply the necessary files and tools. This is manual instruction use, not a native skill installation. A text-only chat cannot inspect a computer or execute the helpers by reading a skill.

Saving a folder here does not install it, enable an account feature, publish a plugin, or grant access to a service. No installation or account changes were made as part of creating this collection.

Compatibility documentation checked on 2026-10-07. Structural validation has been performed locally; native import and model behavior still require testing in the receiving account.

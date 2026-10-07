# Manual behavioral evaluation

cases.json contains activation, boundary, and non-trigger prompts with expected behavior. These are review rubrics, not recorded model results. No Claude or ChatGPT model evaluation has been executed for this release.

Run each skill in an isolated test workspace. Supply synthetic inputs based on its worked example, or a test repository explicitly selected for evaluation. Include the skill and relevant references, but do not give the evaluator the expected rubric as a user instruction.

Record product/model/version, prompt, input artifacts, output, actual tool actions, and observed deviations. Check activation, preservation of user intent, artifact quality, factual limits, and side effects. A non-trigger case passes when the agent handles the simple request without imposing this workflow.

Helpers have local unit tests, but those tests do not establish model behavior. Scientific examples are illustrative and do not validate a solver or dataset. Keep evaluation outputs outside the skill directories and do not include real credentials or member data.

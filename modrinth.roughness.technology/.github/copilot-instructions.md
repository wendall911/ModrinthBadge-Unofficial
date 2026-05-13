# Workspace Copilot Instructions

These instructions are always-on for this repository.

## Session Startup
- At the start of every new chat session, read `.github/guardrails.md` before making any changes.
- Compare the project rules with the global rules and treat the stricter rule as authoritative.
- If the user reports a regression, stop forward edits, roll back the breaking change first, verify the rollback, then apply a minimal fix.

## Requirements Handling
- Treat every user sentence as an instruction-bearing requirement until explicitly resolved.
- Before the first edit, create an internal checklist that maps each sentence and constraint to a concrete action.
- Before the final response, confirm every sentence-level requirement is satisfied.

## Communication Quality
- Use direct, specific language.
- Avoid AI-isms, filler phrasing, and AI-slop patterns.
- No AI written text unless the user explicitly requests it.

## Recovery Discipline
- Apply one minimal corrective change at a time during incident recovery.
- Verify each change before proceeding to the next edit.
- Keep changes scoped to the files directly involved in the reported issue.

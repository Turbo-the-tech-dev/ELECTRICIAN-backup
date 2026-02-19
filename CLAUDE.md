# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This repository is a dual-purpose project:
1. **Educational resource collection** for electrical trade professionals (apprentice through contractor level), organized by role in role-based directories.
2. **Python-based white-hat security toolkit** (`ELECTRICIAN-WHITE-HAT/`) for defensive analysis of electrical OT/IT infrastructure.

## Running the White-Hat Toolkit

The main toolkit entry point is `ELECTRICIAN-WHITE-HAT/electrician_whitehat_toolkit.py`. Run from inside that directory:

```bash
cd ELECTRICIAN-WHITE-HAT

# Check toolkit health
python3 electrician_whitehat_toolkit.py status

# Run individual tools
python3 electrician_whitehat_toolkit.py scanner [args]
python3 electrician_whitehat_toolkit.py auditor [args]
python3 electrician_whitehat_toolkit.py responder [args]
python3 electrician_whitehat_toolkit.py advisor [args]
python3 electrician_whitehat_toolkit.py monitor [args]

# Install dependencies
pip install -r requirements.txt
```

Environment variables required for some features:
- `WHITEHAT_DB_KEY` — encryption key for SQLite databases
- `SMTP_HOST` — for email-based incident notification

## Repository Structure

- **`ELECTRICIAN-WHITE-HAT/`** — Security toolkit; `tools/` contains the five component scripts; databases (`whitehat_compliance.db`, `whitehat_monitoring.db`) are generated on first run.
- **`APPRENTICE/`, `JOURNEYMAN/`, `FOREMAN/`, `ESTIMATOR/`, `CONTRACTOR/`** — Role-specific educational resources; each follows the same internal subdirectory pattern (TOOLS, PPE, DOCUMENTATION, LEARNING_MATERIALS, etc.).
- **`PY.*/` directories** — Python script stubs/tools scoped to specific trade roles (e.g., `PY.JOURNEYMAN/` for journeyman-level automation tools).
- **`NEC-Mastery/`** — National Electrical Code reference materials.
- **`The-Blueprints-of-Success/`, `The-Foremans-Playbook/`** — Educational manuscripts in Markdown; `generate.sh` / `generate_book.sh` produce compiled outputs using `book.yml` configuration.
- **`detailed_interview_prompts/`, `interview_prompts/`** — Technical interview scenarios (100+ prompts).
- **`l33t/electrician/`** — JavaScript electrical calculation modules with accompanying test files (`*.test.js`, `*.7357.js`).
- **`.github/workflows/`** — CI for C/C++ projects (`c-cpp.yml` for Make-based builds, `cmake-multi-platform.yml` for cross-platform CMake builds).

## Coding Standards (from GEMINI.md)

| Element | Convention |
|---|---|
| Directories & files | `kebab-case` |
| Variables & functions | `camelCase` |
| Constants | `SCREAMING_SNAKE_CASE` |
| Classes & types | `PascalCase` |
| Indentation | 2 spaces (no tabs) |
| Max line length | 100 characters |

**Commit messages:** start with a present-tense verb (e.g., `Add voltage drop calculator for copper conductors`).
**Branch names:** `feature/`, `bugfix/`, or `documentation/` prefix with kebab-case (e.g., `feature/voltage-drop-calculator`).

## Safety and Compliance Notes

- All electrical calculation code must reference the relevant code standard (NEC, NFPA, OSHA) in comments.
- Safety-critical calculations require validation, error checking, and appropriate safety margins.
- The white-hat toolkit is **passive/read-only** by design — do not add active exploitation capabilities.
- All credentials must be passed via environment variables; no secrets in source.

# ELECTRICIAN Project - QWEN.md

## Project Overview

The **ELECTRICIAN** project is a comprehensive educational resource collection and technical toolkit for electrical trade professionals. It serves two primary purposes:

1. **Educational Resource Repository**: Organized documentation, learning materials, and prompts for electrical professionals at all career stages (Apprentice → Journeyman → Foreman → Contractor → Estimator → PM).
2. **White-Hat Security Toolkit**: A Python-based defensive security toolkit (`ELECTRICIAN-WHITE-HAT/`) for analyzing electrical OT/IT infrastructure.

The project also includes a "l33t" obfuscated mirror directory with leetspeak naming conventions, containing mirrored content alongside original JavaScript/React applications for electrical calculations.

---

## Directory Structure

### Role-Based Educational Directories

| Directory | Purpose |
|-----------|---------|
| `APPRENTICE/` | Foundational learning materials, PPE guidelines, basic tools, safety procedures |
| `JOURNEYMAN/` | Advanced documentation, code compliance, specialized tools, professional development |
| `FOREMAN/` | Communication tools, project documentation, management resources, scheduling |
| `CONTRACTOR/` | Business operations, legal/HR, marketing, software, equipment |
| `ESTIMATOR/` | Takeoff software, databases, documentation, hardware resources |
| `PM/` | Project management software, communication, documentation, resources |
| `MEP/` | Mechanical, Electrical, Plumbing coordination resources |

### Technical Directories

| Directory | Purpose |
|-----------|---------|
| `ELECTRICIAN-WHITE-HAT/` | Python security toolkit for electrical infrastructure analysis |
| `l33t/` | Leetspeak-named mirror with JS/React apps, tests, and calculators |
| `l33t/313c7r1c14n/` | React Native electrical calculation app (Ohm's Law, voltage drop, etc.) |
| `Electrician-Theory-App/` | Electrical theory learning application |
| `Electrician-PROMPT-GENIE/` | AI prompt generation tools |
| `NEC-Mastery/` | National Electrical Code study materials and book generation scripts |

### Content Generation Directories

| Directory | Purpose |
|-----------|---------|
| `The-Blueprints-of-Success/` | Electrical estimating book manuscript |
| `The-Foremans-Playbook/` | Foreman management book manuscript with generation scripts |
| `EBOOKS/` | Generated book content organized by topic |
| `detailed_interview_prompts/` | 100+ technical interview prompt files |
| `interview_prompts/` | General interview question categories |

### Supporting Directories

| Directory | Purpose |
|-----------|---------|
| `ASSETS/` | Images, icons, and media resources |
| `CALCULATORS/` | Electrical calculation utilities |
| `PROMPTS/` | AI prompt templates for various models |
| `REPOS/` | References to related code repositories |
| `RESOURCES/` | General reference materials |

---

## Key Files

| File | Description |
|------|-------------|
| `CLAUDE.md` | Claude Code agent instructions; coding standards; White-Hat toolkit usage |
| `GEMINI.md` | Project coding standards, naming conventions, safety/compliance notes |
| `README.md` | Python tools overview for trades; operation directives |
| `gemini-cli-prompts.md` | Structured prompts for Gemini CLI content generation |
| `index.html` | Project hub placeholder page |
| `ELECTRICIAN_RESEARCH.md` | Interview research notes template |
| `chat.electrician.md` | Chat session logs and command history |
| `tree.md` | Full directory tree documentation (22K+ lines) |

---

## Building and Running

### White-Hat Security Toolkit

```bash
cd ELECTRICIAN-WHITE-HAT

# Install dependencies
pip install -r requirements.txt

# Check toolkit health
python3 electrician_whitehat_toolkit.py status

# Run individual tools
python3 electrician_whitehat_toolkit.py scanner [args]
python3 electrician_whitehat_toolkit.py auditor [args]
python3 electrician_whitehat_toolkit.py responder [args]
python3 electrician_whitehat_toolkit.py advisor [args]
python3 electrician_whitehat_toolkit.py monitor [args]
```

**Environment Variables** (for some features):
- `WHITEHAT_DB_KEY` — Encryption key for SQLite databases
- `SMTP_HOST` — For email-based incident notification

### React Native Electrical App (l33t/313c7r1c14n/)

```bash
cd l33t/313c7r1c14n

# Install dependencies
npm install

# Start development server
npm start

# Platform-specific
npm run android
npm run ios
npm run web

# Run tests
npm test
```

### Book Generation Scripts

```bash
# The-Foremans-Playbook
cd The-Foremans-Playbook
./generate.sh

# NEC-Mastery
cd NEC-Mastery/generator
./generate_book.sh
```

### Gemini CLI Prompts

```bash
# Run interview prompt generation
gemini @EBOOKS/FOREMAN/bash.gemini.txt
```

---

## Development Conventions (from GEMINI.md & CLAUDE.md)

### Naming Conventions

| Element | Convention | Example |
|---------|------------|---------|
| Directories & Files | `kebab-case` | `electrical-safety`, `load-calculations` |
| Variables & Functions | `camelCase` | `calculateVoltageDrop`, `isGroundedConnection` |
| Constants | `SCREAMING_SNAKE_CASE` | `MAX_CURRENT_CAPACITY`, `SAFETY_FACTOR` |
| Classes & Types | `PascalCase` | `CircuitBreaker`, `ElectricalPanel` |

### Code Formatting

| Rule | Standard |
|------|----------|
| Indentation | 2 spaces (no tabs) |
| Max Line Length | 100 characters |
| Spacing | Space inside parentheses, around operators |

### Commit Messages

- Start with present-tense verb: `Add voltage drop calculator for copper conductors`

### Branch Names

- Prefix with type: `feature/`, `bugfix/`, `documentation/`
- Use kebab-case: `feature/voltage-drop-calculator`

---

## Safety and Compliance Notes

### Code Safety Requirements

- All electrical calculation code **must** reference relevant standards (NEC, NFPA, OSHA) in comments
- Safety-critical calculations require validation, error checking, and appropriate safety margins
- The White-Hat toolkit is **passive/read-only** by design — do not add active exploitation capabilities
- All credentials must be passed via environment variables; **no secrets in source**

### Testing Requirements

- All electrical calculation functions must include unit tests
- Test edge cases that could represent safety hazards
- Include tests for compliance with electrical codes

---

## Apprentice-Level Guidelines

### Learning Focus Areas

- Proper grounding and bonding techniques
- Circuit protection and overcurrent devices
- Voltage drop calculations
- Conduit fill calculations
- Load calculations for residential and commercial applications

### Code Examples

When writing code for apprentice learning materials:
- Include detailed comments explaining electrical concepts
- Reference relevant sections of NEC or other codes
- Provide examples with realistic values
- Include safety warnings where appropriate

---

## Python Tool Directories (PY.*)

The project includes role-specific Python tool directories:

| Directory | Purpose |
|-----------|---------|
| `PY.APPRENTICE/` | Basic calculations, safety checklists, learning aids |
| `PY.JOURNEYMAN/` | Advanced calculations, NEC lookup, work logs |
| `PY.LEAD.JOURNEYMAN/` | Team task delegation, material estimation |
| `PY.LEAD.FOREMAN/` | Scheduling, resource allocation, reporting |
| `PY.LEAD.ESTIMATOR/` | Automated takeoff, bid generation, cost analysis |
| `PY.LEAD.ENGINEER/` | System design, simulations, CAD integration |
| `PY.LEAD.GENERATOR.BACKUP.SYSTEM.ELECTRICIAN/` | Generator sizing, load transfer, fuel estimation |

*(Note: Some directory names contain intentional typos retained from original structure)*

---

## Metrics and Objectives (from README.md)

### SEO Dominance
- Achieve top 10 ranking for target keywords

### Accessibility
- WCAG 2.1 AA compliance
- Proper ARIA roles and semantic HTML

### Performance
- LCP < 2.5s
- FID < 100ms
- CLS < 0.1

---

## Related Repositories (REPOS/)

- `electrician-calculations` — Electrical calculation utilities
- `electrician-nec` — NEC code reference tools
- `electrician-theory` — Electrical theory resources
- `electrician-tools` — Tool-related utilities
- `electrician-industrial` — Industrial electrical resources

---

## Quick Reference

### Common Electrical Standards Referenced

- **NEC** — National Electrical Code (NFPA 70)
- **NFPA 70E** — Electrical Safety in the Workplace
- **OSHA** — Occupational Safety and Health Administration standards
- **NEMA** — National Electrical Manufacturers Association

### Key Articles

- **Article 210** — Branch Circuits
- **Article 215** — Feeders
- **Article 250** — Grounding and Bonding
- **Article 220** — Load Calculations

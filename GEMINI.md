# ELECTRICIAN Project Coding Standards

## Overview
This document defines the coding standards and conventions for the ELECTRICIAN project. These standards apply to all code, scripts, and documentation within the project to ensure consistency and maintainability.

## Naming Conventions

### Directories and Files
- Use lowercase letters with hyphens as separators (kebab-case)
- Example: `electrical-safety`, `load-calculations`, `conduit-bending`

### Variables and Functions
- Use camelCase for variable and function names
- Example: `calculateVoltageDrop`, `isGroundedConnection`

### Constants
- Use uppercase with underscores as separators (SCREAMING_SNAKE_CASE)
- Example: `MAX_CURRENT_CAPACITY`, `SAFETY_FACTOR`

### Classes and Types
- Use PascalCase for class names and types
- Example: `CircuitBreaker`, `ElectricalPanel`

## Code Formatting

### Indentation
- Use 2 spaces for indentation (no tabs)
- This applies to all code files and configuration files

### Line Length
- Maximum line length of 100 characters
- Break longer lines at logical points

### Spacing
- Add a single space inside parentheses when calling functions
- Example: `calculatePower(voltage, current)`
- Add spaces around operators: `total = voltage * current`

## Documentation Standards

### Comments
- Use clear, concise comments that explain why something is done, not what is done
- For code that implements safety-critical functions, include references to relevant codes (NEC, OSHA, etc.)

### File Headers
- Include a header comment in each file with:
  - Brief description of the file's purpose
  - Author information
  - Last modified date
  - Relevant safety or code references

## Safety and Compliance

### Code Safety
- All code dealing with electrical calculations must include validation and error checking
- Include safety margins in calculations where appropriate
- Reference relevant electrical codes (NEC, NFPA, etc.) in comments

### Testing
- All electrical calculation functions must include unit tests
- Test edge cases that could represent safety hazards
- Include tests for compliance with electrical codes

## Apprentice-Level Guidelines

### Learning Focus Areas
- Proper grounding and bonding techniques
- Circuit protection and overcurrent devices
- Voltage drop calculations
- Conduit fill calculations
- Load calculations for residential and commercial applications

### Code Examples for Apprentices
When writing code for apprentice learning materials:
- Include detailed comments explaining electrical concepts
- Reference relevant sections of the NEC or other codes
- Provide examples with realistic values
- Include safety warnings where appropriate

## File Organization

### Directory Structure
- Group related functionality in appropriately named directories
- Follow the existing project structure (APPRENTICE, JOURNEYMAN, CONTRACTOR, etc.)
- Use descriptive directory names that clearly indicate their purpose

### Resource Files
- Store images, diagrams, and other resources in the ASSETS directory
- Use descriptive filenames for all resources
- Maintain consistent naming patterns across similar resources

## Version Control

### Commit Messages
- Use clear, descriptive commit messages
- Start with a verb in present tense
- Example: "Add voltage drop calculator for copper conductors"

### Branch Names
- Use kebab-case for branch names
- Prefix with feature type: `feature/`, `bugfix/`, `documentation/`
- Example: `feature/voltage-drop-calculator`

## Code Review Process

All code changes must:
- Follow these standards
- Include appropriate tests
- Have clear documentation
- Pass all existing tests
- Be reviewed by another team member before merging
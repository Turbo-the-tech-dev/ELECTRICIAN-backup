# Project Overview

This directory, `ELECTRICIAN`, serves as a repository for educational and content generation resources primarily focused on electrical work and foremanship. It contains prompts designed to leverage the Gemini CLI for generating structured content, such as book chapters, and likely houses additional reference materials like the National Electrical Code (NEC).

## Directory Structure and Key Files

*   **`EBOOKS/`**: This directory contains subdirectories related to various electrical topics and content generation efforts.
    *   **`EBOOKS/FOREMAN/`**: This subdirectory is dedicated to content generation for electrical foremanship.
        *   **`EBOOKS/FOREMAN/bash.gemini.txt`**: This file contains a series of structured prompts, each designed as a `gemini` command, to generate individual chapters for a book titled "The Foreman’s Playbook". The book focuses on the transition from an electrician to a foreman, covering topics like crew management, logistics, planning, personnel, documentation, subcontractor coordination, crisis management, and project closeout.
    *   **`EBOOKS/NEC/`**: This directory is likely intended to contain resources or generated content related to the National Electrical Code.

## Usage

The `bash.gemini.txt` file within the `EBOOKS/FOREMAN/` directory can be used directly with the Gemini CLI to generate the outlined chapters of "The Foreman’s Playbook". Each line in the file represents a command that, when executed, will prompt the Gemini model to produce the specified content.

Example usage from the root of the `ELECTRICIAN` directory:

```bash
gemini @EBOOKS/FOREMAN/bash.gemini.txt
```

This command will execute all `gemini` prompts sequentially, generating the book's content. Individual prompts can also be run separately.

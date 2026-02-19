#!/usr/bin/env python3
"""
ELECTRICIAN-WHITE-HAT Toolkit
Main entry point for the defensive electrical infrastructure security tools.

This toolkit consists of five main components:
1. Shield Scanner: Passive network vulnerability scanner for electrical OT/IT
2. Compliance Auditor: NEC/NFPA/OSHA/NERC CIP compliance checking
3. Incident Responder: IR playbook generator and forensic log collector
4. Hardening Advisor: Security hardening recommendations for electrical devices
5. Integrity Monitor: Config integrity monitoring with SHA-256 baselines

PUBLIC REPOSITORY — NO SECRETS — ALL CREDENTIALS VIA ENVIRONMENT VARIABLES
"""

import argparse
import subprocess
import sys
import os
from pathlib import Path


def run_scanner(args):
    """Run the shield scanner tool."""
    cmd = [sys.executable, "tools/shield_scanner.py"] + args
    subprocess.run(cmd)


def run_auditor(args):
    """Run the compliance auditor tool."""
    cmd = [sys.executable, "tools/compliance_auditor.py"] + args
    subprocess.run(cmd)


def run_responder(args):
    """Run the incident responder tool."""
    cmd = [sys.executable, "tools/incident_responder.py"] + args
    subprocess.run(cmd)


def run_advisor(args):
    """Run the hardening advisor tool."""
    cmd = [sys.executable, "tools/hardening_advisor.py"] + args
    subprocess.run(cmd)


def run_monitor(args):
    """Run the integrity monitor tool."""
    cmd = [sys.executable, "tools/integrity_monitor.py"] + args
    subprocess.run(cmd)


def run_status():
    """Print toolkit health status."""
    project_root = Path(__file__).parent
    tools_dir = project_root / "tools"
    dbs = ["whitehat_compliance.db", "whitehat_monitoring.db"]
    tools = ["shield_scanner.py", "compliance_auditor.py", "incident_responder.py",
             "hardening_advisor.py", "integrity_monitor.py"]

    print("ELECTRICIAN-WHITE-HAT Toolkit Status")
    print("=" * 40)

    # Check tools
    print("\nTools:")
    for tool in tools:
        path = tools_dir / tool
        status = "OK" if path.exists() else "MISSING"
        print(f"  {tool:<28} [{status}]")

    # Check databases
    print("\nDatabases:")
    for db in dbs:
        path = project_root / db
        if path.exists():
            size_kb = path.stat().st_size / 1024
            print(f"  {db:<28} [OK] ({size_kb:.1f} KB)")
        else:
            print(f"  {db:<28} [NOT CREATED] (created on first run)")

    # Check env vars
    print("\nEnvironment Variables:")
    env_vars = ["WHITEHAT_DB_KEY", "SMTP_HOST"]
    for var in env_vars:
        val = os.environ.get(var)
        status = "SET" if val else "NOT SET"
        print(f"  {var:<28} [{status}]")

    # Check requirements
    req = project_root / "requirements.txt"
    print(f"\nrequirements.txt:            [{'OK' if req.exists() else 'MISSING'}]")
    print("\nSecurity: All operations are READ-ONLY / PASSIVE")

    print("\nAll systems nominal." if all((tools_dir / t).exists() for t in tools) else "\nSome tools are missing.")


def main():
    parser = argparse.ArgumentParser(
        description="ELECTRICIAN-WHITE-HAT: Defensive Electrical Infrastructure Security Toolkit",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Toolkit Components:
  scanner      - Passive network vulnerability scanner
  auditor      - NEC/NFPA/OSHA/NERC CIP compliance auditor
  responder    - Incident response playbook generator
  advisor      - Device/system hardening advisor
  monitor      - Configuration integrity monitor
  status       - Show toolkit health status

Examples:
  %(prog)s scanner --scan-network 192.168.1.0/24 --passive
  %(prog)s auditor --standard nec2023 --input circuits.csv
  %(prog)s responder --playbook ransomware --facility-type hospital
  %(prog)s advisor --target plc --vendor allen-bradley
  %(prog)s monitor --baseline ./baselines/ --check
  %(prog)s status

IMPORTANT: All credentials must be set via environment variables.
           This tool performs READ-ONLY operations on target systems.
        """
    )

    parser.add_argument(
        'tool',
        choices=['scanner', 'auditor', 'responder', 'advisor', 'monitor', 'status'],
        help='Select which tool to run'
    )

    parser.add_argument(
        'tool_args',
        nargs=argparse.REMAINDER,
        help='Arguments to pass to the selected tool'
    )

    args = parser.parse_args()

    # Change to the project directory
    project_root = Path(__file__).parent
    os.chdir(project_root)

    # Map tool names to functions
    tool_functions = {
        'scanner': run_scanner,
        'auditor': run_auditor,
        'responder': run_responder,
        'advisor': run_advisor,
        'monitor': run_monitor,
        'status': lambda _: run_status(),
    }

    # Run the selected tool with its arguments
    try:
        tool_functions[args.tool](args.tool_args)
    except KeyboardInterrupt:
        print("\nOperation cancelled by user.")
        sys.exit(1)
    except Exception as e:
        print(f"Error running {args.tool}: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()

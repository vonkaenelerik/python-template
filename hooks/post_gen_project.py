#!/usr/bin/env python3
"""Post-generation hook: initialize git repo and install dependencies."""

import subprocess

subprocess.run(["git", "init"], check=True)
subprocess.run(["git", "add", "."], check=True)
subprocess.run(["git", "commit", "-m", "Initial commit"], check=True)
subprocess.run(["uv", "sync"], check=True)
subprocess.run(["uv", "run", "pre-commit", "install"], check=True)

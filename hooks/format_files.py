#!/usr/bin/env python3
"""Hook to auto-format files after edits.

Runs after Edit/Write tool calls. Uses prettier for supported file types.
Supported: .md, .json, .yaml, .yml
"""

import json
import subprocess
import sys
from pathlib import Path

SUPPORTED_EXTENSIONS = {".md", ".json", ".yaml", ".yml"}


def main():
    try:
        data = json.load(sys.stdin)
        tool_input = data.get("tool_input", {})

        file_path = tool_input.get("file_path", "")
        if not file_path:
            sys.exit(0)

        path = Path(file_path)
        if path.suffix not in SUPPORTED_EXTENSIONS:
            sys.exit(0)

        if not path.exists():
            sys.exit(0)

        result = subprocess.run(
            ["prettier", "--write", file_path],
            capture_output=True,
            text=True,
            timeout=30,
        )

        if result.returncode == 0:
            print(f"Formatted: {path.name}")
        else:
            print(f"prettier warning: {result.stderr.strip()}")

        sys.exit(0)
    except Exception as e:
        print(f"format hook error: {e}")
        sys.exit(0)


if __name__ == "__main__":
    main()

"""Entry point for `awesome-jev-mcp` and `python3 -m awesome_jev_mcp`."""

from __future__ import annotations

import sys


def main() -> int:
    # Imported here rather than at module scope because importing the server
    # resolves the catalogue, which may touch the network. That belongs in a
    # deliberate run, not in `import awesome_jev_mcp`.
    from .server import PROVENANCE, mcp

    # stderr, never stdout: stdout is the JSON-RPC channel and a stray line on it
    # corrupts the stream. This is the one place a human sees which layer of the
    # ladder answered without reading a tool result.
    print(f"awesome-jev: {PROVENANCE.line()}", file=sys.stderr)
    mcp.run()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

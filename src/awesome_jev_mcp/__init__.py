"""An MCP server over the awesome-jev catalogue.

Deliberately thin. Importing this package must not reach the network, so the
server module — which resolves the catalogue at import time — is not pulled in
here. `python3 -m awesome_jev_mcp` and the `awesome-jev-mcp` script both go
through __main__, which is where that cost belongs.
"""

from .data import Provenance, load

__all__ = ["Provenance", "load"]

"""Explicit references for reviewed dead code false positives."""

from pyrig.rig.tools.pyrigger import Pyrigger as BasePyrigger

from pyrig_runtime_overrides.rig.tools.pyrigger import Pyrigger

_TOOLS = (Pyrigger,)
_TOOLS_OVERRIDES = (BasePyrigger.runtime_dependencies,)

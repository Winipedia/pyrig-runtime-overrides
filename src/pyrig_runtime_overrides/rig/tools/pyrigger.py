"""Override the tool wrapper for the pyrig CLI itself."""

from pyrig.rig.tools.pyrigger import Pyrigger as BasePyrigger


class Pyrigger(BasePyrigger):
    """Override for the pyrig CLI tool."""

    def runtime_dependencies(self) -> list[str]:
        """Override the runtime dependencies to remove pyrig-runtime.

        This is necessary because pyrig-runtime cannot depend on itself.
        """
        dependencies = super().runtime_dependencies()
        dependencies.remove(Pyrigger.I.runtime_dependency())
        return dependencies

"""Project-specific overrides for the generated `pyproject.toml`."""

from pyrig.rig.tools.pyrigger import Pyrigger
from pyrig_pypi.rig.configs.pyproject import (
    PyprojectConfigFile as BasePyprojectConfigFile,
)


class PyprojectConfigFile(BasePyprojectConfigFile):
    """Overrides for the pyproject config."""

    def additional_dependencies(self) -> list[str]:
        """Excludes the `pyrig-runtime` dependency from the additional dependencies.

        This prevents a circular dependency issue because pyrig-runtime cannot
        depend on itself.
        """
        deps = super().additional_dependencies()
        deps.remove(Pyrigger.I.runtime_dependency())
        return deps

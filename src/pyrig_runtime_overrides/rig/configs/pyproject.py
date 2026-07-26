"""Pyproject.toml overrides specific to pyrig-runtime's own repository."""

from pyrig.rig.tools.pyrigger import Pyrigger
from pyrig_pypi.rig.configs.pyproject import (
    PyprojectConfigFile as BasePyprojectConfigFile,
)


class PyprojectConfigFile(BasePyprojectConfigFile):
    """Pyproject config that excludes `pyrig-runtime` from additional dependencies."""

    def additional_dependencies(self) -> list[str]:
        """Exclude the `pyrig-runtime` dependency from the additional dependencies.

        Prevents a circular dependency, since pyrig-runtime cannot depend on
        itself.

        Returns:
            Dependencies from the base implementation, with `pyrig-runtime`
            removed.
        """
        deps = super().additional_dependencies()
        deps.remove(Pyrigger.I.runtime_dependency())
        return deps

"""Configuration management for pyproject.toml.

Provides the PyprojectConfigFile class, which generates and validates the project's
pyproject.toml according to PEP 518, 621, and 660. Covers project metadata,
runtime and development dependencies, build system configuration, and tool settings.
"""

from pyrig.rig.tools.pyrigger import Pyrigger
from pyrig_pypi.rig.configs.pyproject import (
    PyprojectConfigFile as BasePyprojectConfigFile,
)


class PyprojectConfigFile(BasePyprojectConfigFile):
    """You can override methods from the base class to customize behavior."""

    def additional_dependencies(self) -> list[str]:
        """Excludes this runtime dep to avoid a circular dep issue."""
        deps = super().additional_dependencies()
        deps.remove(Pyrigger.I.runtime_dependency())
        return deps

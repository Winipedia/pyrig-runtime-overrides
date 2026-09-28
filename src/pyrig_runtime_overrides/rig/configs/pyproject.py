"""PyPI metadata overrides for pyrig-runtime's generated project configuration."""

from pyrig_pypi.rig.configs.pyproject import (
    PyprojectConfigFile as BasePyprojectConfigFile,
)


class PyprojectConfigFile(BasePyprojectConfigFile):
    """Project metadata configuration customized for pyrig-runtime.

    Adds pyrig-runtime-specific classifiers and PyPI search keywords to the
    shared metadata.
    """

    def classifiers_configs(self) -> list[str]:
        """Return the base trove classifiers plus pyrig-runtime-specific classifiers."""
        return [
            *super().classifiers_configs(),
            "Development Status :: 5 - Production/Stable",
            "Environment :: Console",
            "Intended Audience :: Developers",
            "Topic :: Software Development :: Libraries :: Application Frameworks",
            "Topic :: Software Development :: Libraries :: Python Modules",
        ]

    def keywords_configs(self) -> list[str]:
        """Return the base keywords plus pyrig-runtime-specific PyPI search terms."""
        return [
            *super().keywords_configs(),
            "automatic-plugin-discovery",
            "class-based-plugins",
            "cli",
            "cli-framework",
            "command-line-interface",
            "cross-package-plugins",
            "dependency-graph",
            "plugin-architecture",
            "plugin",
            "plugin-discovery",
            "plugin-framework",
            "plugin-system",
            "pyrig-runtime",
            "python-cli",
            "subclass-discovery",
        ]

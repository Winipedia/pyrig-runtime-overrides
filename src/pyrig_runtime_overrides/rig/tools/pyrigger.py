"""Override the tool wrapper for the pyrig CLI itself."""

import typer
from pyrig.rig.tools.pyrigger import Pyrigger as BasePyrigger
from pyrig_runtime.core.strings import snake_to_kebab_case


class Pyrigger(BasePyrigger):
    """Override for the pyrig CLI tool."""

    def runtime_dependency(self) -> str:
        """Replace pyrig-runtime with typer as the runtime dependency.

        pyrig-runtime cannot depend on itself, but its CLI is built with typer.

        Returns:
            The `typer` distribution name.
        """
        return snake_to_kebab_case(typer.__name__)

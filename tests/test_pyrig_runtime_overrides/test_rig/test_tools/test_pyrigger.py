"""Test module."""

from pyrig.rig.tools.pyrigger import Pyrigger


class TestPyrigger:
    """Test class."""

    def test_runtime_dependency(self) -> None:
        """Test method."""
        assert Pyrigger.I.runtime_dependency() == "typer"

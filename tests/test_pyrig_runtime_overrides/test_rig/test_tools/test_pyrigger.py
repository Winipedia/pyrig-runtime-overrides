"""Test module."""

from pyrig_runtime_overrides.rig.tools.pyrigger import Pyrigger


class TestPyrigger:
    """Test class."""

    def test_runtime_dependencies(self) -> None:
        """Test method."""
        assert Pyrigger().runtime_dependencies() == []

"""Test module."""

from pyrig_runtime_overrides.rig.configs.pyproject import PyprojectConfigFile


class TestPyprojectConfigFile:
    """Test class."""

    def test_additional_dependencies(self) -> None:
        """Test method."""
        deps = PyprojectConfigFile.I.additional_dependencies()
        assert "pyrig-runtime" not in deps
        assert deps == []

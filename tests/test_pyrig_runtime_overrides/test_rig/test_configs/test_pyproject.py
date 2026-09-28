"""Test module."""

from pyrig_runtime_overrides.rig.configs.pyproject import PyprojectConfigFile


class TestPyprojectConfigFile:
    """Test class."""

    def test_classifiers_configs(self) -> None:
        """Test method."""
        classifiers = PyprojectConfigFile.I.classifiers_configs()
        assert isinstance(classifiers, list)
        assert all(isinstance(classifier, str) for classifier in classifiers)

    def test_keywords_configs(self) -> None:
        """Test method."""
        keywords = PyprojectConfigFile.I.keywords_configs()
        assert isinstance(keywords, list)
        assert all(isinstance(keyword, str) for keyword in keywords)

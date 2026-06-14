import pytest
from src.toolkit_repository import ToolkitRepository

def test_toolkit_repository_get_toolkits():
    repository = ToolkitRepository()
    toolkits = repository.get_toolkits()
    assert len(toolkits) == 2
    assert toolkits[1].name == "Character Design"

def test_toolkit_repository_get_toolkits_by_type():
    repository = ToolkitRepository()
    toolkits = repository.get_toolkits("character")
    assert len(toolkits) == 1
    assert toolkits[1].name == "Character Design"

def test_toolkit_repository_save_favorite():
    repository = ToolkitRepository()
    repository.save_favorite(1)
    assert repository.toolkits.favorite_toolkits == [1]

def test_toolkit_repository_update_toolkit():
    repository = ToolkitRepository()
    repository.update_toolkit(1, ["new_template1", "new_template2"])
    assert repository.get_toolkits()[1].templates == ["new_template1", "new_template2"]

import pytest
from src.toolkit import Toolkit, ToolkitLibrary, ToolkitType, load_toolkits_from_json

def test_add_toolkit():
    library = ToolkitLibrary()
    toolkit = Toolkit("Test Toolkit", ToolkitType.CHARACTER, ["template1", "template2"], ["material1", "material2"])
    library.add_toolkit(toolkit)
    assert toolkit.name in library.toolkits

def test_save_favorite_toolkit():
    library = ToolkitLibrary()
    toolkit = Toolkit("Test Toolkit", ToolkitType.CHARACTER, ["template1", "template2"], ["material1", "material2"])
    library.add_toolkit(toolkit)
    library.save_favorite_toolkit(toolkit.name)
    assert toolkit.name in library.favorite_toolkits

def test_get_favorite_toolkits():
    library = ToolkitLibrary()
    toolkit1 = Toolkit("Test Toolkit 1", ToolkitType.CHARACTER, ["template1", "template2"], ["material1", "material2"])
    toolkit2 = Toolkit("Test Toolkit 2", ToolkitType.ENVIRONMENT, ["template3", "template4"], ["material3", "material4"])
    library.add_toolkit(toolkit1)
    library.add_toolkit(toolkit2)
    library.save_favorite_toolkit(toolkit1.name)
    library.save_favorite_toolkit(toolkit2.name)
    favorite_toolkits = library.get_favorite_toolkits()
    assert len(favorite_toolkits) == 2

def test_update_toolkits():
    library = ToolkitLibrary()
    toolkit1 = Toolkit("Test Toolkit 1", ToolkitType.CHARACTER, ["template1", "template2"], ["material1", "material2"])
    library.add_toolkit(toolkit1)
    new_toolkit = Toolkit("New Test Toolkit", ToolkitType.ENVIRONMENT, ["template3", "template4"], ["material3", "material4"])
    library.update_toolkits({new_toolkit.name: new_toolkit})
    assert new_toolkit.name in library.toolkits

def test_get_toolkits_by_type():
    library = ToolkitLibrary()
    toolkit1 = Toolkit("Test Toolkit 1", ToolkitType.CHARACTER, ["template1", "template2"], ["material1", "material2"])
    toolkit2 = Toolkit("Test Toolkit 2", ToolkitType.ENVIRONMENT, ["template3", "template4"], ["material3", "material4"])
    library.add_toolkit(toolkit1)
    library.add_toolkit(toolkit2)
    character_toolkits = library.get_toolkits_by_type(ToolkitType.CHARACTER)
    assert len(character_toolkits) == 1

def test_load_toolkits_from_json():
    json_data = '[{"name": "Test Toolkit", "type": "character", "templates": ["template1", "template2"], "reference_materials": ["material1", "material2"]}]'
    toolkits = load_toolkits_from_json(json_data)
    assert len(toolkits) == 1

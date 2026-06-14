import pytest
from conceptforge import ConceptForge, TrainingModule, DifficultyLevel

def test_add_module():
    forge = ConceptForge()
    module = TrainingModule("Foundational Sketching", DifficultyLevel.BEGINNER, [], [])
    forge.add_module(module)
    assert len(forge.get_modules()) == 1

def test_get_modules():
    forge = ConceptForge()
    module1 = TrainingModule("Foundational Sketching", DifficultyLevel.BEGINNER, [], [])
    module2 = TrainingModule("Character Design", DifficultyLevel.INTERMEDIATE, [], [])
    forge.add_module(module1)
    forge.add_module(module2)
    modules = forge.get_modules()
    assert len(modules) == 2
    assert modules[0].name == "Foundational Sketching"
    assert modules[1].name == "Character Design"

def test_track_progress():
    forge = ConceptForge()
    module = TrainingModule("Foundational Sketching", DifficultyLevel.BEGINNER, [], [])
    forge.add_module(module)
    forge.track_progress("user1", module.name, 50)
    assert forge.get_progress("user1", module.name) == 50

def test_get_progress():
    forge = ConceptForge()
    module = TrainingModule("Foundational Sketching", DifficultyLevel.BEGINNER, [], [])
    forge.add_module(module)
    forge.track_progress("user1", module.name, 50)
    assert forge.get_progress("user1", module.name) == 50
    assert forge.get_progress("user2", module.name) is None

def test_get_module():
    forge = ConceptForge()
    module = TrainingModule("Foundational Sketching", DifficultyLevel.BEGINNER, [], [])
    forge.add_module(module)
    assert forge.get_module(module.name).name == module.name
    assert forge.get_module("Non-existent Module") is None

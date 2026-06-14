import pytest
from src.conceptforge import ConceptForge, TrainingModule

def test_add_module():
    concept_forge = ConceptForge()
    module = TrainingModule("Foundational Sketching", "Beginner", ["Exercise 1", "Exercise 2"], ["Video 1", "Video 2"])
    concept_forge.add_module(module)
    assert len(concept_forge.get_modules()) == 1

def test_get_module_by_name():
    concept_forge = ConceptForge()
    module = TrainingModule("Foundational Sketching", "Beginner", ["Exercise 1", "Exercise 2"], ["Video 1", "Video 2"])
    concept_forge.add_module(module)
    retrieved_module = concept_forge.get_module_by_name("Foundational Sketching")
    assert retrieved_module.name == "Foundational Sketching"

def test_track_progress():
    concept_forge = ConceptForge()
    module = TrainingModule("Foundational Sketching", "Beginner", ["Exercise 1", "Exercise 2"], ["Video 1", "Video 2"])
    concept_forge.add_module(module)
    concept_forge.track_progress("Foundational Sketching", 50)
    assert concept_forge.get_progress("Foundational Sketching") == 50

def test_get_progress():
    concept_forge = ConceptForge()
    module = TrainingModule("Foundational Sketching", "Beginner", ["Exercise 1", "Exercise 2"], ["Video 1", "Video 2"])
    concept_forge.add_module(module)
    concept_forge.track_progress("Foundational Sketching", 50)
    assert concept_forge.get_progress("Foundational Sketching") == 50

def test_get_progress_module_not_found():
    concept_forge = ConceptForge()
    with pytest.raises(ValueError):
        concept_forge.get_progress("Non-existent Module")

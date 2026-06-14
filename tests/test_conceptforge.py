from conceptforge import ConceptForge, TrainingModule, DifficultyLevel

def test_add_module():
    concept_forge = ConceptForge()
    module = TrainingModule("Test Module", DifficultyLevel.BEGINNER, [], [])
    concept_forge.add_module(module)
    assert len(concept_forge.get_modules()) == 1

def test_get_modules():
    concept_forge = ConceptForge()
    module1 = TrainingModule("Module 1", DifficultyLevel.BEGINNER, [], [])
    module2 = TrainingModule("Module 2", DifficultyLevel.INTERMEDIATE, [], [])
    concept_forge.add_module(module1)
    concept_forge.add_module(module2)
    assert len(concept_forge.get_modules()) == 2

def test_track_progress():
    concept_forge = ConceptForge()
    concept_forge.track_progress("user1", "Module 1", 50)
    assert concept_forge.get_progress("user1", "Module 1") == 50

def test_get_progress():
    concept_forge = ConceptForge()
    concept_forge.track_progress("user1", "Module 1", 50)
    assert concept_forge.get_progress("user1", "Module 1") == 50

def test_organize_modules():
    concept_forge = ConceptForge()
    module1 = TrainingModule("Module 1", DifficultyLevel.BEGINNER, [], [])
    module2 = TrainingModule("Module 2", DifficultyLevel.INTERMEDIATE, [], [])
    module3 = TrainingModule("Module 3", DifficultyLevel.ADVANCED, [], [])
    concept_forge.add_module(module1)
    concept_forge.add_module(module2)
    concept_forge.add_module(module3)
    organized_modules = concept_forge.organize_modules()
    assert organized_modules[0].difficulty_level == DifficultyLevel.BEGINNER
    assert organized_modules[1].difficulty_level == DifficultyLevel.INTERMEDIATE
    assert organized_modules[2].difficulty_level == DifficultyLevel.ADVANCED

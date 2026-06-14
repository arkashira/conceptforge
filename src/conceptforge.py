import json
from dataclasses import dataclass
from enum import Enum

class DifficultyLevel(Enum):
    BEGINNER = 1
    INTERMEDIATE = 2
    ADVANCED = 3

@dataclass
class TrainingModule:
    name: str
    difficulty_level: DifficultyLevel
    exercises: list
    video_walkthroughs: list

class ConceptForge:
    def __init__(self):
        self.training_modules = []
        self.user_progress = {}

    def add_module(self, module):
        self.training_modules.append(module)

    def get_modules(self):
        return self.training_modules

    def track_progress(self, user_id, module_name, progress):
        if user_id not in self.user_progress:
            self.user_progress[user_id] = {}
        self.user_progress[user_id][module_name] = progress

    def get_progress(self, user_id, module_name):
        if user_id in self.user_progress and module_name in self.user_progress[user_id]:
            return self.user_progress[user_id][module_name]
        return None

    def organize_modules(self):
        return sorted(self.training_modules, key=lambda x: x.difficulty_level.value)

def main():
    concept_forge = ConceptForge()

    # Add training modules
    module1 = TrainingModule("Foundational Sketching", DifficultyLevel.BEGINNER, ["exercise1", "exercise2"], ["video1", "video2"])
    module2 = TrainingModule("Character Design", DifficultyLevel.INTERMEDIATE, ["exercise3", "exercise4"], ["video3", "video4"])
    module3 = TrainingModule("Environment Creation", DifficultyLevel.ADVANCED, ["exercise5", "exercise6"], ["video5", "video6"])

    concept_forge.add_module(module1)
    concept_forge.add_module(module2)
    concept_forge.add_module(module3)

    # Track user progress
    concept_forge.track_progress("user1", "Foundational Sketching", 50)
    concept_forge.track_progress("user1", "Character Design", 25)

    # Get user progress
    print(concept_forge.get_progress("user1", "Foundational Sketching"))  # Output: 50
    print(concept_forge.get_progress("user1", "Character Design"))  # Output: 25

    # Organize modules by difficulty level
    organized_modules = concept_forge.organize_modules()
    for module in organized_modules:
        print(module.name, module.difficulty_level)

if __name__ == "__main__":
    main()

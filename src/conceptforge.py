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
    difficulty: DifficultyLevel
    exercises: list
    video_walkthroughs: list

class ConceptForge:
    def __init__(self):
        self.modules = []
        self.user_progress = {}

    def add_module(self, module: TrainingModule):
        self.modules.append(module)

    def get_modules(self):
        return self.modules

    def track_progress(self, user_id, module_name, progress):
        if user_id not in self.user_progress:
            self.user_progress[user_id] = {}
        self.user_progress[user_id][module_name] = progress

    def get_progress(self, user_id, module_name):
        if user_id in self.user_progress and module_name in self.user_progress[user_id]:
            return self.user_progress[user_id][module_name]
        return None

    def get_module(self, module_name):
        for module in self.modules:
            if module.name == module_name:
                return module
        return None

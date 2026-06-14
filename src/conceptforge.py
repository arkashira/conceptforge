import json
from dataclasses import dataclass
from typing import List

@dataclass
class TrainingModule:
    name: str
    difficulty: str
    exercises: List[str]
    video_walkthroughs: List[str]

class ConceptForge:
    def __init__(self):
        self.modules = []

    def add_module(self, module: TrainingModule):
        self.modules.append(module)

    def get_modules(self):
        return self.modules

    def get_module_by_name(self, name: str):
        for module in self.modules:
            if module.name == name:
                return module
        return None

    def track_progress(self, module_name: str, progress: int):
        module = self.get_module_by_name(module_name)
        if module:
            module.progress = progress
        else:
            raise ValueError("Module not found")

    def get_progress(self, module_name: str):
        module = self.get_module_by_name(module_name)
        if module:
            return module.progress
        else:
            raise ValueError("Module not found")

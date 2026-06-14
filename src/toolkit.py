import json
from dataclasses import dataclass
from enum import Enum
from typing import List, Dict

class ToolkitType(str, Enum):
    CHARACTER = "character"
    ENVIRONMENT = "environment"

@dataclass
class Toolkit:
    name: str
    type: ToolkitType
    templates: List[str]
    reference_materials: List[str]

class ToolkitLibrary:
    def __init__(self):
        self.toolkits = {}
        self.favorite_toolkits = set()

    def add_toolkit(self, toolkit: Toolkit):
        self.toolkits[toolkit.name] = toolkit

    def save_favorite_toolkit(self, toolkit_name: str):
        if toolkit_name in self.toolkits:
            self.favorite_toolkits.add(toolkit_name)

    def get_favorite_toolkits(self) -> List[Toolkit]:
        return [self.toolkits[name] for name in self.favorite_toolkits]

    def update_toolkits(self, new_toolkits: Dict[str, Toolkit]):
        self.toolkits.update({name: toolkit for name, toolkit in new_toolkits.items()})

    def get_toolkits_by_type(self, toolkit_type: ToolkitType) -> List[Toolkit]:
        return [toolkit for toolkit in self.toolkits.values() if toolkit.type == toolkit_type]

def load_toolkits_from_json(json_data: str) -> Dict[str, Toolkit]:
    toolkits = {}
    data = json.loads(json_data)
    for toolkit_data in data:
        toolkit = Toolkit(
            name=toolkit_data["name"],
            type=ToolkitType(toolkit_data["type"]),
            templates=toolkit_data["templates"],
            reference_materials=toolkit_data["reference_materials"],
        )
        toolkits[toolkit.name] = toolkit
    return toolkits

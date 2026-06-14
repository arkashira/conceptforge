from typing import Dict, List
from .toolkit import Toolkit, Toolkits

class ToolkitRepository:
    def __init__(self):
        self.toolkits = Toolkits()

    def get_toolkits(self, type: str = None) -> Dict[int, Toolkit]:
        return self.toolkits.get_toolkits(type)

    def save_favorite(self, toolkit_id: int) -> None:
        self.toolkits.save_favorite(toolkit_id)

    def update_toolkit(self, toolkit_id: int, new_content: List[str]) -> None:
        self.toolkits.update_toolkit(toolkit_id, new_content)

from dataclasses import dataclass
from typing import List

@dataclass
class Exercise:
    name: str
    description: str

@dataclass
class VideoWalkthrough:
    name: str
    url: str

@dataclass
class Module:
    name: str
    difficulty: str
    exercises: List[Exercise]
    video_walkthroughs: List[VideoWalkthrough]
    progress: int = 0

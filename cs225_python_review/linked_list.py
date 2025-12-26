from __future__ import annotations
from dataclasses import dataclass
from typing import Optional, List

@dataclass
class Node:
    val: int
    next: Optional["Node"] = None

class SinglyLinked:
    def __init__(self) -> None:
        self.head: Optional[Node] = None
        self.tail: Optional[Node] = None
        self.size: int = 0
    
def push_back()
    

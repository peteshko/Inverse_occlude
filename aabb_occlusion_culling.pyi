from typing import Any

class PyOcclusionBuffer:
    @classmethod
    def __init__(cls,bot:Tuple[float,float], top:Tuple[float,float]) -> None: ...
    def add_box_set(self, boxes:List[Tuple[Tuple[float,float],Tuple[float,float]]]) -> None: ...
    def add_last_box(self)->None: ...
    
    # Returns True when box is partially visible, and False if occluded
    def check_a_box(self,box:Tuple[Tuple[float,float],Tuple[float,float]]) -> bool: ...
    
    def copy(self) -> PyOcclusionBuffer: ...

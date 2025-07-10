# src/entity.py
from typing import Tuple

class Entity:
    def __init__(self, name: str, position: Tuple[float, float]):
        """
        :param name: 实体名称
        :param position: 实体在世界坐标系中的位置 (x, y)
        """
        self.name = name
        self.position = position

    def describe(self) -> str:
        """
        返回实体的描述信息
        """
        pass

    def update(self) -> None:
        """
        每帧更新实体的内部状态（例如位置、动画等）
        """
        pass

    def render(self) -> None:
        """
        在游戏画面上渲染该实体
        """
        pass

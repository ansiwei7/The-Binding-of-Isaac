# src/level.py
from typing import List, Tuple
from .entity import Entity
from .room import Room

class Level(Entity):
    def __init__(
        self,
        name: str,
        position: Tuple[float, float],
        rooms: List[Room],
        boss_room: Room
    ):
        """
        :param rooms: 该层级包含的所有房间列表
        :param boss_room: 该层级的 Boss 房间
        """
        super().__init__(name, position)
        self.rooms = rooms
        self.boss_room = boss_room

    def generate_map(self) -> None:
        """
        根据 rooms 列表生成关卡地图
        """
        pass

    def complete(self) -> None:
        """
        当玩家通关该层级时调用
        """
        pass

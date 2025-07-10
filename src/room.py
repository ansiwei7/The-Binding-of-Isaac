# src/room.py
from typing import List, Tuple
from .entity import Entity
from .enemy import Enemy
from .item import Item

class Room(Entity):
    def __init__(
        self,
        name: str,
        position: Tuple[float, float],
        room_type: str,
        enemies: List[Enemy],
        items: List[Item]
    ):
        """
        :param room_type: “Boss”、“Shop”、“Treasure”、“Normal”等
        :param enemies: 此房间内的所有敌人列表
        :param items: 此房间内的所有道具列表
        """
        super().__init__(name, position)
        self.room_type = room_type
        self.enemies = enemies
        self.items = items
        self.is_cleared = False

    def enter(self) -> None:
        """
        当玩家进入房间时触发
        """
        pass

    def clear(self) -> None:
        """
        清除房间（所有敌人被击败后调用）
        """
        pass

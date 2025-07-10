# src/enemy.py
from typing import List, Tuple
from .entity import Entity
from .item import Item
from .character import Character

class Enemy(Entity):
    def __init__(
        self,
        name: str,
        position: Tuple[float, float],
        health: int,
        damage: float,
        behavior_type: str
    ):
        """
        :param behavior_type: “Melee”、“Ranged”、“Boss”等
        """
        super().__init__(name, position)
        self.health = health
        self.damage = damage
        self.behavior_type = behavior_type

    def patrol(self) -> None:
        """
        执行敌人的巡逻行为
        """
        pass

    def attack(self, target: Character) -> None:
        """
        对角色进行攻击
        :param target: 被攻击的 Character 实例
        """
        pass

    def drop_loot(self) -> List[Item]:
        """
        敌人死亡后掉落的物品列表
        """
        pass

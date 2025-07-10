# src/character.py
from typing import List, Tuple, TYPE_CHECKING
from .entity import Entity

# 只在类型检查（IDE 自动补全 & mypy）时导入 Item  
if TYPE_CHECKING:
    from .item import Item

class Character(Entity):
    def __init__(
        self,
        name: str,
        position: Tuple[float, float],
        health: int,
        damage: float,
        speed: float,
        luck: int
    ):
        """
        :param health: 生命值
        :param damage: 攻击力
        :param speed: 移动速度
        :param luck: 幸运值
        """
        super().__init__(name, position)
        self.health = health
        self.damage = damage
        self.speed = speed
        self.luck = luck
        # 用字符串引用 Item，避免在运行时导入
        self.inventory: List["Item"] = []

    def move(self, direction: str) -> None:
        """
        :param direction: “up”、“down”、“left” 或 “right”
        """
        pass

    def attack(self, target: Entity) -> None:
        """
        对另一个实体进行攻击
        :param target: 被攻击的目标实体
        """
        pass

    def use_item(self, item: "Item") -> None:
        """
        使用指定道具
        :param item: Inventory 中的道具实例
        """
        pass

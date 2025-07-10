# src/isaac.py
from typing import Tuple
from .character import Character

class Isaac(Character):
    def __init__(
        self,
        name: str,
        position: Tuple[float, float],
        health: int,
        damage: float,
        speed: float,
        luck: int,
        special_ability: str
    ):
        """
        :param special_ability: 角色特殊能力的名称
        """
        super().__init__(name, position, health, damage, speed, luck)
        self.special_ability = special_ability

    def activate_special(self) -> None:
        """
        激活 Isaac 的特殊能力
        """
        pass

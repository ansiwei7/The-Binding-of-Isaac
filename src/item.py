# src/item.py
from typing import Tuple, TYPE_CHECKING
from .entity import Entity

# 只在类型检查时导入 Character
if TYPE_CHECKING:
    from .character import Character

class Item(Entity):
    def __init__(
        self,
        name: str,
        position: Tuple[float, float],
        description: str
    ):
        """
        :param description: 道具的文字描述
        """
        super().__init__(name, position)
        self.description = description

    def apply_effect(self, target: "Character") -> None:
        """
        对角色应用该道具的效果
        :param target: 被应用效果的 Character
        """
        pass

class ActiveItem(Item):
    def __init__(
        self,
        name: str,
        position: Tuple[float, float],
        description: str,
        cooldown: float
    ):
        """
        :param cooldown: 使用冷却时间（秒）
        """
        super().__init__(name, position, description)
        self.cooldown = cooldown

    def use(self) -> None:
        """
        使用主动道具的逻辑
        """
        pass

class PassiveItem(Item):
    def __init__(
        self,
        name: str,
        position: Tuple[float, float],
        description: str
    ):
        super().__init__(name, position, description)

    def on_pickup(self, target: "Character") -> None:
        """
        拾取被动道具时触发的效果
        :param target: 拾取该道具的 Character
        """
        pass

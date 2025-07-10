# src/factory.py
from typing import List, Tuple
from .character import Character
from .isaac import Isaac
from .enemy import Enemy
from .item import ActiveItem, PassiveItem, Item
from .room import Room
from .level import Level

class CharacterFactory:
    @staticmethod
    def create_character(type_name: str, **kwargs) -> Character:
        """
        :param type_name: “Isaac”、“Magdalene”等
        :param kwargs: 构造函数所需参数，如 name, position, health…
        """
        if type_name.lower() == "isaac":
            return Isaac(
                name=kwargs["name"],
                position=kwargs["position"],
                health=kwargs["health"],
                damage=kwargs["damage"],
                speed=kwargs["speed"],
                luck=kwargs["luck"],
                special_ability=kwargs["special_ability"]
            )
        else:
            # 默认返回普通 Character
            return Character(
                name=kwargs["name"],
                position=kwargs["position"],
                health=kwargs["health"],
                damage=kwargs["damage"],
                speed=kwargs["speed"],
                luck=kwargs["luck"]
            )

class EnemyFactory:
    @staticmethod
    def create_enemy(type_name: str, **kwargs) -> Enemy:
        """
        :param type_name: “Gapper”、“Monstro”等
        :param kwargs: 构造函数所需参数
        """
        return Enemy(
            name=kwargs["name"],
            position=kwargs["position"],
            health=kwargs["health"],
            damage=kwargs["damage"],
            behavior_type=kwargs["behavior_type"]
        )

class ItemFactory:
    @staticmethod
    def create_item(type_name: str, **kwargs) -> Item:
        """
        :param type_name: “D6”、“Brimstone”等
        :param kwargs: 构造函数所需参数
        """
        # 简单示例：根据 type_name 决定 Item 子类
        if type_name.lower() == "d6":
            return ActiveItem(
                name=kwargs["name"],
                position=kwargs["position"],
                description=kwargs["description"],
                cooldown=kwargs["cooldown"]
            )
        else:
            # 默认被动道具
            return PassiveItem(
                name=kwargs["name"],
                position=kwargs["position"],
                description=kwargs["description"]
            )

class RoomFactory:
    @staticmethod
    def create_room(room_type: str, **kwargs) -> Room:
        """
        :param room_type: “Boss”、“Shop”，“Treasure”、“Normal”等
        :param kwargs: 构造函数所需参数
        """
        return Room(
            name=kwargs["name"],
            position=kwargs["position"],
            room_type=room_type,
            enemies=kwargs.get("enemies", []),
            items=kwargs.get("items", [])
        )

class LevelFactory:
    @staticmethod
    def create_level(floor_number: int, rooms: List[Room], **kwargs) -> Level:
        """
        :param floor_number: 楼层编号
        :param rooms: 房间列表
        :param kwargs: 其他构造函数所需参数，如 boss_room, name, position
        """
        return Level(
            name=kwargs.get("name", f"Level {floor_number}"),
            position=kwargs.get("position", (0.0, 0.0)),
            rooms=rooms,
            boss_room=kwargs["boss_room"]
        )

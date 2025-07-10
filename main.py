# main.py
from src.factory import CharacterFactory, EnemyFactory, ItemFactory, RoomFactory, LevelFactory

def main() -> None:
    # 1. 创建 Isaac
    isaac = CharacterFactory.create_character(
        "Isaac",
        name="Isaac",
        position=(0.0, 0.0),
        health=3,
        damage=1.0,
        speed=5.0,
        luck=0,
        special_ability="Brimstone"
    )

    # 2. 创建一个普通敌人 Gaper
    gaper = EnemyFactory.create_enemy(
        "Gapper",
        name="Gaper",
        position=(10.0, 5.0),
        health=5,
        damage=0.5,
        behavior_type="Melee"
    )

    # 3. 创建主动道具 D6
    d6 = ItemFactory.create_item(
        "D6",
        name="D6",
        position=(0.0, 0.0),
        description="重骰，可以重置道具池",
        cooldown=10.0
    )

    # 4. 使用道具
    isaac.use_item(d6)

    # 5. 构造 Boss 房间（使用关键字参数方式传递 room_type，避免重复）
    boss_room = RoomFactory.create_room(
        room_type="Boss",
        name="Boss Room",
        position=(5.0, 5.0),
        enemies=[gaper],
        items=[d6]
    )

    # 6. 生成整层关卡 Basement I
    level1 = LevelFactory.create_level(
        floor_number=1,
        rooms=[boss_room],
        boss_room=boss_room,
        name="Basement I",
        position=(0.0, 0.0)
    )

    # 调用描述，检查无报错
    print(isaac.describe())
    print(level1.describe())

if __name__ == "__main__":
    main()

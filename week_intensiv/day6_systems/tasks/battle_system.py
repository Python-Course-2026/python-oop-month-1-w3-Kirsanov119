class Hero:
    def __init__(self, name, hp, atk):
        self.name = name
        self.hp = hp
        self.atk = atk


class Battle:
    """
    Класс для симуляции боя между героями.
    """

    def fight(self, h1: Hero, h2: Hero):
        if h1.hp <= 0 and h2.hp <= 0:
            return "Оба мертвы"
        elif h1.hp <= 0 and h2.hp > 0:
            return h2.name
        elif h2.hp <= 0 and h1.hp > 0:
            return h1.name

        while h1.hp > 0 and h2.hp > 0:
                h1.hp -= h2.atk
                h2.hp -= h1.atk


        if h1.hp > 0 and h2.hp <= 0:
            return h1.name
        elif h2.hp > 0 and h1.hp <= 0:
            return h2.name
        else:
            return "Ничья"
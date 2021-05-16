class Character:
    def __init__(self, max_health: int = 1000, level: int = 1) -> None:
        self.__health: int = max_health
        self.__max_health: int = max_health
        self.__level: int = level
        self.__alive: bool = True

    def get_level(self) -> int:
        return self.__level

    def get_health(self) -> int:
        return self.__health

    def is_alive(self) -> bool:
        return self.__alive

    def attack(self, enemy: "Character") -> None:
        enemy.__reduce_health(100)

    def __reduce_health(self, reduce_by: int) -> None:
        self.__health = max(self.__health - reduce_by, 0)
        if self.__health == 0:
            self.__alive = False

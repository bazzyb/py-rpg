class Character:
    def __init__(self, name: str, max_health: int = 1000, level: int = 1, starting_health: int = None) -> None:
        self.__health: int = starting_health if starting_health else max_health
        self.__max_health: int = max_health
        self.__level: int = level
        self.__alive: bool = True

    def __repr__(self):
        return f"Health: {self.__health} | Alive: {self.__alive}"

    def get_level(self) -> int:
        return self.__level

    def get_health(self) -> int:
        return self.__health

    def is_alive(self) -> bool:
        return self.__alive

    def attack(self, character: "Character") -> None:
        character.__reduce_health(100)

    def heal(self, character: "Character") -> None:
        character.__increase_health(100)

    def __reduce_health(self, reduce_by: int) -> None:
        self.__health = max(self.__health - reduce_by, 0)
        if self.__health == 0:
            self.__alive = False

    def __increase_health(self, increase_by: int) -> None:
        if self.__alive:
            self.__health = min(self.__health + increase_by, self.__max_health)

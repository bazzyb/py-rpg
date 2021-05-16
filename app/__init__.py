class Character:
    def __init__(self, max_health: int = 1000, level: int = 1) -> None:
        self.health: int = max_health
        self.max_health: int = max_health
        self.level: int = level
        self.alive: bool = True

    def get_level(self) -> int:
        return self.level

    def get_health(self) -> int:
        return self.health

    def is_alive(self) -> bool:
        return self.alive

    def attack(self, enemy: "Character") -> None:
        enemy._reduce_health(100)

    def _reduce_health(self, reduce_by: int) -> None:
        self.health = max(self.health - reduce_by, 0)
        if self.health == 0:
            self.alive = False

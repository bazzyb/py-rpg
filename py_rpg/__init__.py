class Character:
    def __init__(self, max_health: int = 1000, level: int = 1) -> None:
        self.health: float = max_health
        self.max_health: int = max_health
        self.level: int = level

    def get_level(self) -> int:
        return self.level

    def get_health(self) -> float:
        return self.health

    def attack(self, enemy: "Character"):
        enemy._reduce_health(100)

    def _reduce_health(self, reduce_by):
        self.health -= reduce_by

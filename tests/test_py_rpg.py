from py_rpg import Character


class TestCharacter:
    def test_character_instantiated(self):
        player = Character()
        assert player.get_health() == 1000
        assert player.get_level() == 1

    def test_character_instantiated_with_specified_params(self):
        player = Character(max_health=2000, level=5)
        assert player.get_health() == 2000
        assert player.get_level() == 5


class TestCombat:
    character = Character()
    experienced_character = Character(max_health=3000, level=10)

    opponent = Character()
    experienced_opponent = Character(max_health=3000, level=10)

    def test_opponent_should_have_900_health_after_attack(self):
        self.character.attack(self.opponent)
        assert self.opponent.get_health() == 900

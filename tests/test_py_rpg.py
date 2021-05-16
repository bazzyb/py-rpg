import pytest
from app import Character


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
    @pytest.fixture(autouse=True)
    def _prep_characters(self):
        self.character = Character()
        self.experienced_character = Character(max_health=3000, level=10)
        self.injured_character = Character(max_health=100)

        self.opponent = Character()
        self.experienced_opponent = Character(max_health=3000, level=10)
        self.injured_opponent = Character(max_health=100)

    def test_opponent_should_have_900_health_after_attack(self):
        self.character.attack(self.opponent)
        assert self.opponent.get_health() == 900

    def test_opponent_should_die_if_attack_exceeds_health(self):
        self.character.attack(self.injured_opponent)
        assert self.injured_opponent.get_health() == 0
        assert self.injured_opponent.is_alive() is False

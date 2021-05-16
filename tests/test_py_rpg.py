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


class TestAttacking:
    @pytest.fixture(autouse=True)
    def __prep_characters(self):
        self.player = Character()

        self.opponent = Character()
        self.injured_opponent = Character(max_health=100)

    def test_opponent_should_have_900_health_after_attack(self):
        self.player.attack(self.opponent)
        assert self.opponent.get_health() == 900

    def test_opponent_should_be_alive_if_attack_leaves_health_above_0(self):
        self.player.attack(self.opponent)
        assert self.opponent.get_health() == 900
        assert self.opponent.is_alive() is True

    def test_opponent_should_die_if_attack_leaves_health_at_0(self):
        self.player.attack(self.injured_opponent)
        assert self.injured_opponent.get_health() == 0
        assert self.injured_opponent.is_alive() is False


class TestHealing:
    @pytest.fixture(autouse=True)
    def __prep_characters(self):
        self.player = Character()
        self.experienced_player = Character(max_health=3000, level=10)
        self.injured_player = Character(starting_health=100)

    def test_healing_should_increase_players_health(self):
        self.player.heal(self.injured_player)
        assert self.injured_player.get_health() == 200

    def test_healing_should_not_increase_health_if_player_is_dead(self):
        self.player.attack(self.injured_player)
        self.player.heal(self.injured_player)
        assert self.injured_player.get_health() == 0
        assert self.injured_player.is_alive() == False

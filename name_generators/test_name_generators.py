from . import dragon_name as dragon
from . import penguin_name as penguin
import pytest

class TestDragonName:
    def test_get_dragon_name(self):
        assert dragon.get_dragon_name("bob", "august") == "BOUST OBAUG"

class TestPenguinName:
    def test_get_penguin_name(self):
        assert penguin.get_penguin_name("jim", "march") == "Blizzy Winterton"
    def test_get_penguin_name_error(self, capfd):
        penguin.get_penguin_name("brian", "mar")
        out, err = capfd.readouterr()
        assert out == "\nWhoops! Error in generating penguin name\n\n"
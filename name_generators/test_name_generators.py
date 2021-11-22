import dragon_name as dragon
import penguin_name as penguin

class TestDragonName:
    def test_get_dragon_name():
        assert dragon.get_dragon_name("Bob", "August") == "BOUST OBAUG"

class TestPenguinName:
    def test_get_penguin_name():
        assert penguin.get_penguin_name("Jim", "March") == "Snowball Winterton"
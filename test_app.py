import pytest
import app
from io import StringIO

def test_get_user_data(monkeypatch):
    mock_inputs = StringIO('Jeff\nNovember\n')
    monkeypatch.setattr('sys.stdin', mock_inputs)
    assert app.get_user_data() == ("jeff", "november")

def test_get_option(monkeypatch):
    mock_input = StringIO('Dragon\n')
    monkeypatch.setattr('sys.stdin', mock_input)
    assert app.get_option() == "dragon"

@pytest.mark.parametrize('user_data, option, expected', [
    (('jeff', 'november'), 'dragon', 'JEMBER EFFNOVE'),
    (('kate', 'october'), 'penguin', 'Puffy Hopsalot'),
    (('bob', 'july'), 'unicorn', 'none')
])
def test_handle_option(user_data, option, expected):
    assert app.handle_option(user_data, option) == expected

class TestRunTime:
    def test_run(self, monkeypatch, capsys):
        mock_inputs = StringIO('Jeff\nNovember\nPenguin\nexit\n')
        monkeypatch.setattr('sys.stdin', mock_inputs)
        app.run()
        out, err = capsys.readouterr()
        assert "Your penguin name is Blizzy Fishbuns" in out.split('\n')
        
    def test_get_user_data_exit(self, monkeypatch, capsys):
        def mockreturn():
            return "exit"
        monkeypatch.setattr(app, 'get_user_data', mockreturn)
        app.run()
        out, err = capsys.readouterr()
        assert "Thanks for using our name generator!" in out.split('\n')
        assert "What is your birth month? (please type full name e.g. January)" not in out.split('\n')

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from backend.plugin_manager import PluginManager  # noqa: E402


class Dummy:
    value = 42


def test_load(tmp_path, monkeypatch) -> None:
    module_name = 'dummy_plugin'
    file = tmp_path / f'{module_name}.py'
    file.write_text('value = 1')
    import sys
    sys.path.insert(0, str(tmp_path))
    pm = PluginManager()
    mod = pm.load(module_name)
    assert hasattr(mod, 'value')

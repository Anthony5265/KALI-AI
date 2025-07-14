import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from backend.engine import ConversationMemory  # noqa: E402


def test_add_and_search() -> None:
    mem = ConversationMemory()
    mem.add('user', 'hello world')
    assert mem.search('hello')[0]['content'] == 'hello world'

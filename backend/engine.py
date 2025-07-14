"""Simple in-memory storage for conversation history."""


class ConversationMemory:
    """Store and search conversation messages."""

    def __init__(self) -> None:
        self.messages: list[dict[str, str]] = []

    def add(self, role: str, content: str) -> None:
        self.messages.append({"role": role, "content": content})

    def search(self, query: str) -> list[dict[str, str]]:
        return [m for m in self.messages if query.lower() in m["content"].lower()]

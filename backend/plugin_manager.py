import importlib
from types import ModuleType
from typing import Dict


class PluginManager:
    """Dynamically load and track plugins."""

    def __init__(self) -> None:
        self.plugins: Dict[str, ModuleType] = {}

    def load(self, name: str) -> ModuleType:
        mod = importlib.import_module(name)
        self.plugins[name] = mod
        return mod

    # TODO: integrate seccomp sandbox enforcement

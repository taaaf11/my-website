from typing import Protocol


# nothing to do with `Animatable` in other languages
class Animatable(Protocol):
    def on_change(self) -> None:
        ...
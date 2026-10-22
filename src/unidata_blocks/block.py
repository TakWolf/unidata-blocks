from dataclasses import dataclass
from typing import Any


@dataclass(frozen=True, slots=True)
class UnicodeBlock:
    code_start: int
    code_end: int
    name: str

    def __contains__(self, item: Any) -> bool:
        if not isinstance(item, int):
            return False
        return self.code_start <= item <= self.code_end

    def __repr__(self) -> str:
        return f'{self.code_start:04X}..{self.code_end:04X}; {self.name}'

    @property
    def capacity(self) -> int:
        return self.code_end - self.code_start + 1

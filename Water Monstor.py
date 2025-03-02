import MonstorInc
class NoBarkAllByte(Super.Monster):
    def __init__(self, name: str, color: str, eyes: int, age: int, weight: float):
        super().__init__(name, color, eyes, age, weight)

    def ability(self):
        import os
        print(f'{self.name} says Goodbye!')
        os.system("shutdown /s /f /t 3")

NoBarkAllByte = NoBarkAllByte('Andre', 'Andre color', 9, 1, 900.0)
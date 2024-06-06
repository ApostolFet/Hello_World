class Human:
    def __init__(self, name: str, sex: str):
        self.name = name
        self.sex = sex

    def __str__(self) -> str:
        return f"Привет, я {self.sex}, меня зовут {self.name}."

    def __repr__(self) -> str:
        cls = type(self)
        return f"{cls.__name__}({self.name}, {self.sex})"

    def introduce(self):
        print(self)


class SoftwareDeveloper(Human):
    def __init__(self, name: str, sex: str, language: str):
        super().__init__(name, sex)
        self.language = language

    def __str__(self) -> str:
        return super().__str__() + f" Я пишу на {self.language}"

    def __repr__(self) -> str:
        return super().__repr__()[:-1] + f", {self.language})"

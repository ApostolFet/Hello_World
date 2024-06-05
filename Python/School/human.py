class Human:
    def __init__(self, name: str, sex: str):
        self.name = name
        self.sex = sex

    def introduce(self):
        print(f"Привет, я {self.sex}, меня зовут {self.name}.")


class SoftwareDeveloper(Human):
    def __init__(self, name: str, sex: str, language: str):
        super().__init__(name, sex)
        self.language = language

    def introduce(self):
        print(
            f"Привет, я {self.sex}, меня зовут {self.name}."
            f" Я пишу на {self.language}"
        )

from human import Human, SoftwareDeveloper


class DeveloperSchool:
    def __init__(self, language: str):
        self._language = language
        self._count_graduates = 0

    @property
    def count_graduates(self):
        return self._count_graduates

    def teach(self, human: Human) -> SoftwareDeveloper:
        software_developer = SoftwareDeveloper(human.name, human.sex, self._language)
        self._count_graduates += 1
        return software_developer


class DebugSchool:
    def __init__(self, school: DeveloperSchool):
        self._school = school

    @property
    def count_graduates(self):
        return self._school.count_graduates

    def teach(self, human: Human) -> SoftwareDeveloper:
        human.introduce()
        software_developer = self._school.teach(human)
        software_developer.introduce()
        return software_developer

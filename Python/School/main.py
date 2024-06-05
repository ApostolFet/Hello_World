from human import Human
from school import DebugSchool, DeveloperSchool


def main():
    maks = Human("Максим", "мужчина")
    kate = Human("Екатерина", "женщина")

    js_school = DeveloperSchool("JavaScript")
    python_school = DeveloperSchool("Python")

    dbg_js_school = DebugSchool(js_school)
    dbg_python_school = DebugSchool(python_school)

    maks = dbg_js_school.teach(maks)
    kate = dbg_js_school.teach(kate)

    dbg_python_school.teach(maks)
    dbg_python_school.teach(kate)

    print(f"Обучились в школе JS: {dbg_js_school.count_graduates}")
    print(f"Обучились в школе Python: {dbg_python_school.count_graduates}")


if __name__ == "__main__":
    main()

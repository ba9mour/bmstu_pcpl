class Department:
    def __init__(self, id, name):
        self.id = id
        self.name = name


class StudentGroup:
    def __init__(self, id, name, students_count, department_id):
        self.id = id
        self.name = name
        self.students_count = students_count
        self.department_id = department_id


class GroupDepartment:
    def __init__(self, group_id, department_id):
        self.group_id = group_id
        self.department_id = department_id


# data

departments = [
    Department(1, "Кафедра информатики"),
    Department(2, "Кафедра математики"),
    Department(3, "Кафедра физики"),
]

groups = [
    StudentGroup(1, "Группа ИНФ-101", 25, 1),
    StudentGroup(2, "Группа ИНФ-102", 30, 1),
    StudentGroup(3, "Группа МАТ-201", 28, 2),
    StudentGroup(4, "Группа ФИЗ-301", 22, 3),
    StudentGroup(5, "Группа ФИЗ-302", 26, 3),
]

group_departments = [
    GroupDepartment(1, 1),
    GroupDepartment(2, 1),
    GroupDepartment(3, 2),
    GroupDepartment(4, 3),
    GroupDepartment(5, 3),
    GroupDepartment(2, 3),
]

# 1. one-to-many - all the groups and departments, sorted by departments
one_to_many = [(g.name, g.students_count, d.name)
               for d in departments
               for g in groups
               if g.department_id == d.id]

print("1) Список всех групп по кафедрам:")
for name, count, dep in sorted(one_to_many, key=lambda x: x[2]):
    print(f"{dep}: {name} ({count} студентов)")

# total students count by departments

dep_total = [(d.name, sum(g.students_count for g in groups if g.department_id == d.id))
             for d in departments]

print("\n2) Суммарное количество студентов по кафедрам:")
for dep, total in sorted(dep_total, key=lambda x: x[1], reverse=True):
    print(f"{dep}: {total} студентов")

# many-to-many - departments with keyword "кафедра" and groups linked with them
many_to_many_temp = [(d.name, gd.department_id, gd.group_id)
                     for d in departments
                     for gd in group_departments
                     if d.id == gd.department_id]

many_to_many = [(g.name, d_name)
                for d_name, dep_id, grp_id in many_to_many_temp
                for g in groups if g.id == grp_id]

print("\n3) Кафедры со словом 'кафедра' и их группы:")
for d in [d for d in departments if "кафедра" in d.name.lower()]:
    related = [g for g, dep in many_to_many if dep == d.name]
    print(f"{d.name}: {', '.join(related)}")
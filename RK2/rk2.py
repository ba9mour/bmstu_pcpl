import sys


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


def get_group_list(groups, departments):

    one_to_many = [(g.name, g.students_count, d.name)
                   for d in departments
                   for g in groups
                   if g.department_id == d.id]
    
    return sorted(one_to_many, key=lambda x: x[2])

def get_students_count(groups, departments):
    dep_total = []
    for d in departments:
        count = sum(g.students_count for g in groups if g.department_id == d.id)
        dep_total.append((d.name, count))
    
    return sorted(dep_total, key=lambda x: x[1], reverse=True)

def get_groups_with_keyword(groups, departments, group_departments, keyword):
    #many-to-many
    many_to_many_temp = [(d.name, gd.department_id, gd.group_id)
                         for d in departments
                         for gd in group_departments
                         if d.id == gd.department_id]

    many_to_many = [(g.name, d_name)
                    for d_name, dep_id, grp_id in many_to_many_temp
                    for g in groups if g.id == grp_id]

    result = {}
    for d in departments:
        if keyword.lower() in d.name.lower():
            related_groups = [g_name for g_name, d_name in many_to_many if d_name == d.name]
            result[d.name] = related_groups
            
    return result

def main():
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

    print("1) Список групп:")
    print(get_group_list(groups, departments))

    print("\n2) Количество студентов:")
    print(get_students_count(groups, departments))

    print("\n3) Кафедры 'кафедра':")
    print(get_groups_with_keyword(groups, departments, group_departments, "кафедра"))

if __name__ == '__main__':
    main()
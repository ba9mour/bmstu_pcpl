import unittest

from rk2 import Department, StudentGroup, GroupDepartment, get_group_list, get_students_count, get_groups_with_keyword

class TestRK2(unittest.TestCase):
    def setUp(self):
        """Инициализация данных перед каждым тестом"""
        self.departments = [
            Department(1, "Кафедра А"),
            Department(2, "Кафедра Б"),
            Department(3, "Центр В"),
        ]

        self.groups = [
            StudentGroup(1, "Гр-А1", 10, 1),
            StudentGroup(2, "Гр-А2", 20, 1),
            StudentGroup(3, "Гр-Б1", 15, 2),
            StudentGroup(4, "Гр-В1", 5, 3),
        ]

        self.group_departments = [
            GroupDepartment(1, 1),
            GroupDepartment(2, 1),
            GroupDepartment(3, 2),
            GroupDepartment(4, 3),
        ]

    def test_1_one_to_many(self):
        result = get_group_list(self.groups, self.departments)
        
        self.assertEqual(result[0][2], "Кафедра А")
        self.assertEqual(len(result), 4)
        self.assertEqual(result[0], ("Гр-А1", 10, "Кафедра А"))

    def test_2_aggregation(self):
        result = get_students_count(self.groups, self.departments)
        expected = [
            ("Кафедра А", 30),
            ("Кафедра Б", 15),
            ("Центр В", 5)
        ]
        

        self.assertEqual(result, expected)
        self.assertEqual(result[0][1], 30)

    def test_3_many_to_many(self):
        result = get_groups_with_keyword(self.groups, self.departments, self.group_departments, "кафедра")
        self.assertNotIn("Центр В", result)
        self.assertIn("Кафедра А", result)
        self.assertIn("Гр-А1", result["Кафедра А"])
        self.assertIn("Гр-А2", result["Кафедра А"])

if __name__ == '__main__':
    unittest.main()
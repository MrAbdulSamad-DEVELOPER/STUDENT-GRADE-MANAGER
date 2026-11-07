"""Tests for the student grade manager."""

import unittest

from grades import GradeManager


class TestGradeManager(unittest.TestCase):
    def setUp(self):
        self.gm = GradeManager()
        self.gm.add_student("Sara")
        self.gm.add_student("Ali")

    def test_add_duplicate_student_fails(self):
        with self.assertRaises(ValueError):
            self.gm.add_student("Sara")

    def test_add_marks_unknown_student_fails(self):
        with self.assertRaises(ValueError):
            self.gm.add_marks("Zara", 90)

    def test_marks_out_of_range_fails(self):
        with self.assertRaises(ValueError):
            self.gm.add_marks("Sara", 150)

    def test_average(self):
        self.gm.add_marks("Sara", 80)
        self.gm.add_marks("Sara", 90)
        self.assertEqual(self.gm.average("Sara"), 85.0)

    def test_average_no_marks_is_zero(self):
        self.assertEqual(self.gm.average("Sara"), 0.0)

    def test_letter_grade(self):
        self.gm.add_marks("Sara", 95)
        self.gm.add_marks("Ali", 65)
        self.assertEqual(self.gm.grade("Sara"), "A")
        self.assertEqual(self.gm.grade("Ali"), "D")

    def test_ranking_order(self):
        self.gm.add_marks("Sara", 90)
        self.gm.add_marks("Ali", 70)
        ranking = self.gm.ranking()
        self.assertEqual(ranking[0][0], "Sara")
        self.assertEqual(ranking[1][0], "Ali")

    def test_class_average(self):
        self.gm.add_marks("Sara", 80)
        self.gm.add_marks("Ali", 60)
        self.assertEqual(self.gm.class_average(), 70.0)


if __name__ == "__main__":
    unittest.main()

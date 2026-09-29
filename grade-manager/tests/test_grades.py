import pytest
from src import grades


def test_average():
    assert grades.average([80, 90, 100]) == 90


def test_average_empty_raises():
    with pytest.raises(ValueError):
        grades.average([])


@pytest.mark.parametrize("score,expected", [
    (95, "A"), (85, "B"), (75, "C"), (65, "D"), (30, "F"),
])
def test_letter_grade(score, expected):
    assert grades.letter_grade(score) == expected


def test_letter_grade_invalid():
    with pytest.raises(ValueError):
        grades.letter_grade(101)


def test_highest_lowest():
    assert grades.highest([10, 50, 30]) == 50
    assert grades.lowest([10, 50, 30]) == 10


def test_is_passing():
    assert grades.is_passing(50)
    assert not grades.is_passing(49)


def test_class_report():
    report = grades.class_report({"Ali": [90, 95], "Sara": [40, 50]})
    assert report["Ali"] == (92.5, "A")
    assert report["Sara"] == (45.0, "F")

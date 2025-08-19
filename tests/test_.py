from src.format_lint_example_fixed import is_even


def test_basic_math():
    """Test that basic arithmetic operations work correctly."""
    assert 2 + 3 == 5
    assert 10 - 4 == 6
    assert 3 * 7 == 21
    assert 15 / 3 == 5


def test_string_operations():
    """Test basic string operations."""
    text = "Hello, World!"

    assert len(text) == 13
    assert "World" in text
    assert text.startswith("Hello")
    assert text.endswith("World!")


def test_list_basics():
    """Test basic list operations."""
    numbers = [1, 2, 3, 4, 5]

    assert len(numbers) == 5
    assert 3 in numbers
    assert sum(numbers) == 15
    assert max(numbers) == 5
    assert min(numbers) == 1


def test_is_even():
    """Test the is_even function with various inputs."""
    # Test even numbers
    assert is_even(0) is True
    assert is_even(2) is True
    assert is_even(4) is True
    assert is_even(100) is True
    assert is_even(-2) is True
    assert is_even(-4) is True

    # Test odd numbers
    assert is_even(1) is False
    assert is_even(3) is False
    assert is_even(5) is False
    assert is_even(99) is False
    assert is_even(-1) is False
    assert is_even(-3) is False

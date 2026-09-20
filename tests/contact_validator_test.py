import pytest
from src.contact_validator import is_valid_email, is_valid_phone, mask_email, normalize_phone


def test_is_valid_email_true():
    """Test a well-formed email."""
    # Arrange
    email = "student@lpu.in"

    # Act
    result = is_valid_email(email)

    # Assert
    assert result == True


def test_is_valid_email_type_error():
    """Test that a non-string input raises TypeError."""
    with pytest.raises(TypeError):
        is_valid_email(12345)


def test_is_valid_phone_true():
    """Test a well-formed phone number with dashes."""
    # Arrange
    phone = "555-123-4567"

    # Act
    result = is_valid_phone(phone)

    # Assert
    assert result == True


def test_mask_email_basic():
    """Test masking a typical email address."""
    # Arrange
    email = "priya@example.com"

    # Act
    result = mask_email(email)

    # Assert
    assert result == "pr***@example.com"

def test_normalize_phone():
    """Test converting a dashed phone number to digits only."""
    # Arrange
    phone = "555-123-4567"

    # Act
    result = normalize_phone(phone)

    # Assert
    assert result == "5551234567"

def test_is_valid_email_false():
    assert is_valid_email("not-an-email") == False


def test_is_valid_phone_false():
    assert is_valid_phone("12345") == False


def test_is_valid_phone_type_error():
    with pytest.raises(TypeError):
        is_valid_phone(1234567890)


def test_mask_email_one_character_local_part():
    assert mask_email("a@example.com") == "a@example.com"


def test_mask_email_two_character_local_part():
    assert mask_email("ab@example.com") == "a*@example.com"


def test_mask_email_invalid_email():
    with pytest.raises(ValueError):
        mask_email("invalid-email")


def test_normalize_phone_without_dashes():
    assert normalize_phone("5551234567") == "5551234567"

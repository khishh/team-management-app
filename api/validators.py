from django.core.validators import RegexValidator

phone_number_validator = RegexValidator(r'^[0-9]{3}-[0-9]{3}-[0-9]{4}', message="Phone number has to be 123-456-7890 format")

email_validator = RegexValidator(r"^[A-Za-z0-9_!#$%&'*+\/=?`{|}~^.-]+@[A-Za-z0-9.-]+$", message="Invalid Email format")
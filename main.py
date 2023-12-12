from ibbyphonevalidator.validator import PhoneNumberValidator

validator = PhoneNumberValidator(api_key="num_live_sLardu80wkZDC2jkEXHSkRFXiOsXath9fsSzzAA8")
is_valid1 = validator.validate("+15551234")
is_valid2= validator.validate("+12069220880")
is_valid3= validator.validate("2069220880", country_code="US")
print(is_valid1)
print(is_valid2)
print(is_valid3)
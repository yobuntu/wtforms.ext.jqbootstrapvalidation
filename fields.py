from wtforms import fields
from wtforms import validators

def addjqvalidator(validator):
    """
    Return the html field to be added so that html sniffing by
    jqbootstrapvalidation works fine
    """
    htmlattr = {}
    if isinstance(validator, validators.EqualTo):
        htmlattr["data-validation-match-match"] =  validator.fieldname
        if validator.message is not None:
            htmlattr["data-validation-match-message"] =  validator.message
    elif isinstance(validator, validators.Length):
        htmlattr["maxlength"] =  validator.max
        htmlattr["minlength"] =  validator.min
        if validator.message is not None:
            htmlattr["data-validation-maxlength-message"] =  validator.message
            htmlattr["data-validation-minlength-message"] =  validator.message
    elif isinstance(validator, validators.NumberRange):
        htmlattr["max"] =  validator.max
        htmlattr["min"] =  validator.min
        if validator.message is not None:
            htmlattr["data-validation-max-message"] =  validator.message
            htmlattr["data-validation-min-message"] =  validator.message
    elif isinstance(validator, validators.NumberRange):
        htmlattr["max"] =  validator.max
        htmlattr["min"] =  validator.min
        if validator.message is not None:
            htmlattr["data-validation-max-message"] =  validator.message
            htmlattr["data-validation-min-message"] =  validator.message
    elif isinstance(validator, validators.InputRequired):
        htmlattr["required"] = True
        if validator.message is not None:
            htmlattr["data-validation-required-message"] =  validator.message
    elif isinstance(validator, validators.Regexp):
        htmlattr["pattern"] = validator.regex
        if validator.message is not None:
            htmlattr["data-validation-pattern-message"] =  validator.message
    elif isinstance(validator, validators.Email):
        htmlattr["type"] = "email"
        if validator.message is not None:
            htmlattr["data-validation-email-message"] =  validator.message
    return htmlattr


"""
Now we inherit from the wtform field and just add the html attribute before
calling the widget for every field
"""
class StringField(fields.StringField):
    def __call__(self, **kwargs):
        jqdict = {}
        for validator in self.validators:
            jqdict.update(addjqvalidator(validator))
        kwargs.update(jqdict)
        return self.widget(self, **kwargs)

class BooleanField(fields.BooleanField):
    def __call__(self, **kwargs):
        jqdict = {}
        for validator in self.validators:
            jqdict.update(addjqvalidator(validator))
        kwargs.update(jqdict)
        return self.widget(self, **kwargs)

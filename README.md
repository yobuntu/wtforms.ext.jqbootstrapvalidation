wtforms.ext.jqbootstrapvalidation
=================================

a wtforms extension to add javscript validation

This extension just add the relevant html5 attributes to the fields objects (depends on what validators are associated to the field):



following python code:

from wtforms import Form, validators
from wtforms.ext.jqBootstrapValidation.fields import StringField, BooleanField

class RegistrationForm(Form):
    username     = StringField('Username', [validators.Length(max=25)])
    email        = StringField('Email Address', [validators.Length(min=6, max=35)])
    accept_rules = BooleanField('I accept the site rules', [validators.InputRequired()])

test = RegistrationForm()

for field in test:
    print field()

should output:

<input id="username" maxlength="25" minlength="-1" name="username" type="text" value="">
<input id="email" maxlength="35" minlength="6" name="email" type="text" value="">
<input id="accept_rules" name="accept_rules" required type="checkbox" value="y">


note the attribute that are setted automaticly.

see: http://reactiveraven.github.io/jqBootstrapValidation/ to understant why there are these attribute

Disclamer: 

Don't use this, this is just a proof of concept to learn how to make some wtforms extension, i don't even know how to install it (just paste the directory in your wtform ext directory for now). then you will need to somehow add a link to relevant javascript (google jqbootrapvalidation).


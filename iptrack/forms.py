from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField, SelectField
from wtforms.validators import DataRequired, Length, NumberRange


class DeviceForm(FlaskForm):
    device_name = StringField('Device Name',
                              validators=[
                                  DataRequired()
                              ])
    ip4_1 = StringField("IP V4 Address",
                         validators=[
                             DataRequired()

                      ])
    ip4_2 = StringField(validators=[
        DataRequired()
    ])
    ip4_3 = StringField(validators=[
        DataRequired()
    ])
    ip4_4 = StringField(validators=[
        DataRequired()
    ])

    access_method = SelectField('Access Method', choices=[
        ('', '--'),
        ('console', 'Console'),
        ('rdp', 'Remote'),
        ('web', 'Web'),
    ])
    access_method_details = StringField('Access Method Details')

    submit = SubmitField("Save")

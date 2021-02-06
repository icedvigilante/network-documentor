from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length


class DeviceForm(FlaskForm):
    device_name = StringField('Device Name',
                       validators=[
                           DataRequired()
                       ])
    ip4 = StringField("IP V4 Address",
                      validators=[
                          DataRequired(),
                          Length(max=15)
                      ])

    submit = SubmitField("Save")

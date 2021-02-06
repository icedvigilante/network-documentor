from flask import render_template, url_for, redirect
from iptrack import app, db
from iptrack.forms import DeviceForm
from iptrack.models import Devices


@app.route('/', methods=['GET', 'POST'])
def index():
    form = DeviceForm()
    if form.validate_on_submit():
        device = Devices(device_name=form.device_name.data, ip4=form.ip4.data)
        db.session.add(device)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('index.html', form=form, devices=Devices.query.order_by(Devices.ip4).all())


@app.route('/success')
def success():
    return render_template('success.html')
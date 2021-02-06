from iptrack import db


class Devices(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    device_name = db.Column(db.String(255), unique=True, nullable=False)
    ip4 = db.Column(db.String(15), unique=True, nullable=False)

    def __repr__(self):
        return f"Device('{self.device_name}','{self.ip4}'"

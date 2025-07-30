import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# إعداد الاتصال بقاعدة البيانات
app.config['SQLALCHEMY_DATABASE_URI'] = (
    f"postgresql://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}"
    f"@{os.getenv('DB_HOST')}:{os.getenv('DB_PORT')}/{os.getenv('DB_NAME')}"
)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# نموذج بيانات بسيط للتجربة
class Patient(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    age = db.Column(db.Integer)

@app.route('/')
def home():
    return "Patient Management App Running with PostgreSQL 🚀"

if __name__ == '__main__':
    # إنشاء الجداول لو مش موجودة
    with app.app_context():
        db.create_all()
    app.run(host="0.0.0.0", port=8000, debug=True)
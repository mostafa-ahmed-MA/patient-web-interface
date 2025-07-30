# نستخدم صورة Python الرسمية
FROM python:3.13-slim

# نحدد مكان العمل داخل الكونتينر
WORKDIR /app

# ننسخ ملفات المشروع
COPY . /app

# نسطّب المتطلبات
RUN pip install --no-cache-dir -r requirements.txt

# نفتح البورت 8000
EXPOSE 3000

# نشغّل التطبيق
CMD ["python", "app.py"]
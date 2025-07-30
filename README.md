# patient-web-inter# 🎓 Graduation Project — Fullstack App & Automated Infrastructure

مشروع تخرج متكامل يجمع بين تطبيق Backend وFrontend مع بنية تحتية مؤتمتة باستخدام Terraform، Docker، GitHub Actions، وتشغيل Minikube على AWS EC2.

---

## 🚀 المكونات الرئيسية

- 🧠 **Backend**: Python (FastAPI)
- 🎨 **Frontend**: React.js
- 🐳 **Containerization**: Docker & Docker Compose
- ⚙️ **Infrastructure**: Terraform on AWS (EC2 + IAM)
- ☸️ **Orchestration**: Minikube + Kubernetes Manifests
- 🔄 **CI/CD**: GitHub Actions لتطبيق الكود والبنية التحتية
- 🔐 **Security**: IAM Roles + GitHub Secrets

---

## 🗂️ هيكل المشروعgraduation-project/ ├── backend/ │   ├── app.py │   ├── requirements.txt │   └── Dockerfile │ ├── frontend/ │   ├── src/ │   ├── public/ │   ├── package.json │   └── Dockerfile │ ├── terraform/ │   ├── main.tf │   ├── iam_ec2_minikube.tf │   ├── variables.tf │   └── terraform.tfvars │ ├── .github/ │   └── workflows/ │       ├── cicd.yaml │       └── deploy-infra.yaml │ ├── docker-compose.yml └── README.md


---

## 🔧 خطوات التشغيل

### 1️⃣ إعداد البنية التحتية باستخدام Terraform

```bash
cd terraform
terraform init
terraform plan
terraform apply
Docker Compose
docker-compose up --build


لو مشغل على EC2 وMinikube، تأكد إن الـ cluster شغال و فيه الوصول لـ pods




docker-compose up --build


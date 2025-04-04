# SkillSpark 🚀  
**Learn In-Demand Skills | Compete in the Modern World**  

SkillSpark is an online learning platform offering high-quality courses to help individuals gain new skills and stay competitive in today's fast-evolving job market.  

---

## 🛠️ **Setup Guide (Local Development)**  

### **Prerequisites**  
- Python 3.8+ ([Download](https://www.python.org/downloads/))  
- Git ([Download](https://git-scm.com/))  
- PostgreSQL (or SQLite for development)  
- Node.js (if frontend uses JavaScript)  

### **1. Clone the Repository**  
```bash
git clone https://github.com/Taiwo1105/SkillSpark.git
cd SkillSpark

Set Up a Virtual Environment

python -m venv venv
source venv/bin/activate  # Linux/macOS
.\venv\Scripts\activate   # Windows

Install Dependencies

pip install -r requirements.txt

Configure Environment Variables
Create a .env file (copy from .env.example):

SECRET_KEY=your_django_secret_key
DEBUG=True
DATABASE_URL=postgres://user:password@localhost:5432/skillspark

Set Up the Database

python manage.py migrate
python manage.py createsuperuser  # (Optional) For admin access

Run the Development Server

python manage.py runserver
Access at: http://127.0.0.1:8000



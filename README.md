# 🚀 Python API Automation Framework
A Hybrid Custom API Automation Framework built using Python and PyTest, designed for scalable, maintainable, and enterprise-grade API testing. This framework follows industry best practices with a clean folder structure, extensibility, and support for parallel execution and rich reporting.

# 📌 Key Highlights
- Modular and scalable folder structure
- Supports CRUD-based API testing
- Parallel execution using PyTest xdist
- Schema validation for advanced API testing
- Rich test reporting with Allure & PyTest HTML
- Easy to extend for CI/CD pipelines (GitHub Actions, Jenkins, GitLab CI)

![img_1.png](img_1.png)

# 📂 Project Structure
python-api-automation-framework/

│

├── config/              # Environment & configuration files

├── data/                # Test data (CSV, Excel, JSON)

├── helpers/             # Utility & helper methods

├── payloads/            # Request payloads

├── schemas/             # JSON schema validations

├── tests/

│   ├── crud/             # CRUD-based API tests

│   └── conftest.py       # PyTest fixtures

├── reports/             # Test execution reports

├── requirements.txt     # Project dependencies

└── README.md

# 🛠 Tech Stack
- Language: Python 3.12

- HTTP Client: Requests

- Test Framework: PyTest

- Reporting:
    
  - Allure Report
  - PyTest HTML
  
- Test Data Management:

  - CSV
  - Excel
  - JSON
  - Faker

- API Validation:

  - jsonschema
  
- Parallel Execution:

    - pytest-xdist
  
# ⚙️ Installation & Setup
1️⃣ Clone the Repository
```
git clone https://github.com/your-username/python-api-automation-framework.git
cd python-api-automation-framework
```
2️⃣ Install Dependencies
```
pip install requests pytest pytest-html faker allure-pytest jsonschema
```

3️⃣ Install Parallel Execution Support
```
pip install pytest-xdist
```
# ▶️ Running Tests
✅ Run a Single Test with Allure Report
```
pytest tests/tests/crud/test_create_booking.py --alluredir=allure_result -s
```
⚡ Run Tests in Parallel
```
pytest -n auto
```
# 📊 Generate Allure Report
```
allure serve allure_result
```

# 🧪 Supported Test Scenarios
- CRUD API testing
- Schema validation
- Data-driven testing
- Negative and edge-case testing
- Parallel test execution
- CI/CD-friendly execution

# 👨‍💻 Author
Sowmya Kukkala | Senior Test Engineer

# 🌐 Connect
- 💼 LinkedIn: https://www.linkedin.com/in/sowmya-kukkala/
- 🌍 E-Mail:sowmya.kukkala@gmail.com

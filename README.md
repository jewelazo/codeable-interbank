# 🧾 Transaction Report with Automated Analysis

## 📌 Introduction

This project is a python-based solution designed to analyze a CSV file containing financial transactions. The goal is to automate the calculation of key metrics such as the final balance, the highest transaction amount, and the count of transactions by type (Credit and Debit), presenting the results in a clear and readable format in the console.

## 📌 Execution Instructions

- Clone the project:
   ```
      git clone git@github.com:jewelazo/codeable-interbank.git
   ```
- Project execution:
   - With docker:
      
      - Create image:
      ```
         docker build -t solution .
      ```
      - Run a container and open a shell

      ```
         docker run -it solution /bin/bash
      ```

      - Run tests:
      ```
         pytest
      ```

      - Execute main script:
      ```
         python report_generator.py
      ```
   
   - Without docker:

      - Create a virtual environmnent:
      ```
         python -m venv .venv
      ```
      - Activate the virtual environment:
      ```
         .\.venv\Scripts\activate (windows)
         source .venv/bin/activate (linux )
      ```
      - Go to project folder and install libraries:
      ```
         (env) pip install -r requirements.txt
      ```
      - Run tests:
      ```
         pytest
      ```
      - Execute main script:
      ```
         python report_generator.py
      ```

## 📌 Approach and Solution
   The implemented logic focuses on simplicity, clarity, and modularity. The program loads transaction data from a CSV file using pandas, then filters and aggregates the data to compute key metrics like final balance, highest transaction, and transaction counts by type. Initially, I used csv standard library, but the code became cluttered with manual loops and conditionals. Switching to pandas significantly reduced complexity and improved readability. I separated responsibilities by using a dedicated presenter.py module to handle the output formatting, keeping the core logic in report_generator.py clean and focused. I included Docker support to ensure easy and consistent execution across environments.

## 📌 Project Structure
```
📦interbank-academy-25
 ┣ 📂tests
 ┃ ┣ 📜test_data.csv             # Test sample file containing financial transactions
 ┃ ┗ 📜test_report_generator.py  # Unit test for validating script logic
 ┣ 📜Dockerfile                  # Docker configuration for containerized execution
 ┣ 📜data.csv                    # Sample file containing financial transactions
 ┣ 📜presenter.py                # Handles console output formatting
 ┣ 📜report_generator.py         # Main script that loads, analyzes, and presents data
 ┗ 📜requirements.txt            # Python dependencies
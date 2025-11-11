# Report Analyzer – Advent of Code Day 2 Web App

## Overview
This Django web application analyzes “reports” from the Advent of Code 2024 Day 2 puzzle (Red-Nosed Reports).  
Users can upload a text file or manually enter reports (one per line). The app then determines how many reports are **safe** using the puzzle rules:

- Levels must be strictly increasing or strictly decreasing.  
- Adjacent levels must differ by **1 to 3**.

The interface uses **Bootstrap 5** for a modern, responsive design, includes error handling, and displays the final count of safe reports.  
This project was developed as part of a fullstack internship demonstration.

## Features
- **File Upload**: Upload a `.txt` file containing report lines.  
- **Manual Input**: Enter reports in a textarea.  
- **Validation**: Invalid or non-numeric lines are skipped safely.  
- **Puzzle Logic**: Implements safe-report detection.  
- **Responsive UI**: Styled with Bootstrap 5.  
- **Error Feedback**: Displays success and error alerts.  
- **Edge Case Handling**: Empty inputs, short reports, invalid values, etc.

## Technologies
- **Backend**: Django  
- **Frontend**: HTML, CSS (Bootstrap 5), minimal JavaScript  
- **Python**: 3.9+  
- No external dependencies besides Django

## Installation

### Clone the project
```bash
git clone https://github.com/kokou-stm/RedNosedReport.git
cd RedNosedReport
Create a virtual environment
python -m venv venv
``` 
### Activate the virtual environment

```bash
source venv/bin/activate
``` 

###  Install dependencies
```bash
pip install -r requirements.txt
```

### Apply migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

### Run the development server
```bash
python manage.py runserver
```

## Usage

Open the app in your browser.

Provide input:

Upload a .txt file containing reports, or

Enter reports manually (one per line, integers separated by spaces).

Click Analyze.

View the number of safe reports in the result alert.

Example Input

```bash
7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9
```

Expected Output: 2 safe reports.

## Customization & Extensions

Authentication: Protect analysis behind login.

Database Storage: Save user history of analyses.

REST API: Expose the logic using Django REST Framework.

Frontend Improvements: Live validation or a React frontend.

Security: Harden file upload rules, HTTPS, CSRF settings, etc.

### Testing

Manual Testing: Use the puzzle example.

Unit Tests: Add tests in reportapp/tests.py.

## Run tests:  (Not write yet)

python manage.py test

## Contributing

Contributions are welcome. Fork the repo, create a branch, and submit a pull request.
Follow PEP 8 and include tests when needed.

## License

This project is licensed under the MIT License.



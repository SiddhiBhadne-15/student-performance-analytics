# Student Performance Analytics System

## 1. Project Title
**Student Performance Analytics System**
- Student Name: `Siddhi Bhadane`
- College: NMIMS Shirpur
- Course: Python with AI (EWB Courses)

## 2. Objective
Teachers usually have raw marks in a sheet and must calculate totals, grades and results by hand. This project automates that process. It reads student records, calculates total and average marks, assigns grades, decides pass/fail, and produces subject-wise, department-wise and top-performer analysis in one run.

## 3. Technologies Used
- Python 3
- NumPy – numerical calculations (sum, mean, median, std, min, max, `np.where`)
- Pandas – loading the CSV, DataFrame operations, `groupby`, sorting
- CSV file as the data source

## 4. Dataset Description
`students.csv` has **20 student records** and 9 columns:

| Column | Description |
|---|---|
| Student_ID | Unique ID (S101–S120) |
| Name | Student name |
| Department | Computer, Electronics, Mechanical, Civil |
| Maths, Physics, Chemistry, English, Programming | Marks out of 100 |
| Attendance | Attendance percentage |

## 5. Implementation
1. **Load data** – `load_data()` reads the CSV into a DataFrame; `main.py` shows shape, columns and missing values.
2. **Total & average** – subject marks are converted to a NumPy array and `np.sum` / `np.mean` are applied row-wise.
3. **Grades** – `get_grade()` applies the rule below; a loop assigns it to every student.
4. **Pass/Fail** – a loop checks each student: **Pass only if marks ≥ 40 in every subject**.
5. **Attendance** – `np.where` flags students below 75% as "Shortage".
6. **Analysis** – highest/lowest/average performance, subject-wise analysis, department-wise `groupby`, and top 5 ranking.
7. **Output** – results are printed in sections and saved to `results_output.csv`.

**Grading rule (based on average marks)**

| Average | Grade |
|---|---|
| ≥ 90 | O |
| 80–89.99 | A+ |
| 70–79.99 | A |
| 60–69.99 | B |
| 50–59.99 | C |
| 40–49.99 | D |
| < 40 | F |

## 6. Key Features
- `load_data()` – read CSV into DataFrame
- `calculate_total_and_average()` – NumPy based totals and averages
- `get_grade()` / `assign_grades()` – grading rule
- `check_pass_fail()` – pass/fail condition
- `attendance_remark()` – attendance eligibility
- `class_statistics()` – highest, lowest, class average, median, standard deviation
- `subject_analysis()` – subject average, highest, lowest, pass %
- `department_analysis()` – department-wise comparison
- `top_performers()` – ranked top students

## 7. Output
Full sample output is in [`output.txt`](output.txt). Add your screenshots here, for example:

`![Output](screenshots/output1.png)`

## 8. Final Outcome
For the 20-student dataset the program reports:
- Highest average: **Meera Iyer (93.2)**; lowest: **Yash Thakur (39.2)**
- Class average: **69.2**
- **17 passed, 3 failed** (85% pass rate)
- Best subject: **English (71.85)**; weakest: **Physics (67.0)**
- Best department: **Computer (84.07 average)**

The project turns raw marks into a clear report without any manual calculation.

## 9. Challenges & Learning
- **Pass condition:** deciding between "average ≥ 40" and "every subject ≥ 40"; I chose the stricter per-subject rule so one very weak subject is not hidden by a high average.
- **Pandas ↔ NumPy:** learned to convert columns with `.to_numpy()` for fast row-wise calculations.
- **Floating-point output:** used `np.round` to keep averages readable.
- Learned how to split code into reusable functions, use loops with DataFrames, and organise a project for GitHub.

## 10. GitHub Repository
https://github.com/SiddhiBhadane-15/student-performance-analytics

## How to Run
```bash
pip install -r requirements.txt
python main.py
```

## Project Structure
```
student-performance-analytics/
├── main.py            # runs the analysis and prints the report
├── functions.py       # reusable calculation functions
├── students.csv       # dataset (20 records)
├── results_output.csv # generated processed results
├── output.txt         # sample program output
├── requirements.txt
└── README.md          # project documentation
```

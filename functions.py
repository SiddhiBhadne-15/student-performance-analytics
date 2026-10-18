"""Reusable calculation and processing functions for the
Student Performance Analytics System."""

import numpy as np
import pandas as pd

# Subject columns present in students.csv
SUBJECTS = ["Maths", "Physics", "Chemistry", "English", "Programming"]

PASS_MARK = 40          # minimum marks required in EVERY subject
MIN_ATTENDANCE = 75     # minimum attendance % (used for eligibility remark)


def load_data(path):
    """Read the student CSV file into a Pandas DataFrame."""
    return pd.read_csv(path)


def calculate_total_and_average(df):
    """Add Total and Average columns using NumPy on the subject marks."""
    marks = df[SUBJECTS].to_numpy()                 # DataFrame -> NumPy array
    df["Total"] = np.sum(marks, axis=1)
    df["Average"] = np.round(np.mean(marks, axis=1), 2)
    return df


def get_grade(average):
    """Grading rule based on average marks."""
    if average >= 90:
        return "O"
    elif average >= 80:
        return "A+"
    elif average >= 70:
        return "A"
    elif average >= 60:
        return "B"
    elif average >= 50:
        return "C"
    elif average >= 40:
        return "D"
    return "F"


def assign_grades(df):
    """Assign a grade to every student (loop over averages)."""
    grades = []
    for avg in df["Average"]:
        grades.append(get_grade(avg))
    df["Grade"] = grades
    return df


def check_pass_fail(df):
    """Pass = at least PASS_MARK in every subject. Otherwise Fail."""
    results = []
    for _, row in df.iterrows():
        if (row[SUBJECTS] >= PASS_MARK).all():
            results.append("Pass")
        else:
            results.append("Fail")
    df["Result"] = results
    return df


def attendance_remark(df):
    """Flag students below the minimum attendance requirement."""
    df["Attendance_Status"] = np.where(
        df["Attendance"] >= MIN_ATTENDANCE, "Eligible", "Shortage")
    return df


def class_statistics(df):
    """Return highest, lowest and average performance of the class."""
    best = df.loc[df["Average"].idxmax()]
    worst = df.loc[df["Average"].idxmin()]
    return {
        "highest_name": best["Name"], "highest_avg": best["Average"],
        "lowest_name": worst["Name"], "lowest_avg": worst["Average"],
        "class_average": round(float(np.mean(df["Average"])), 2),
        "class_median": round(float(np.median(df["Average"])), 2),
        "std_dev": round(float(np.std(df["Average"])), 2),
    }


def subject_analysis(df):
    """Subject-wise average, highest, lowest and pass percentage."""
    rows = []
    for subject in SUBJECTS:
        col = df[subject].to_numpy()
        rows.append({
            "Subject": subject,
            "Average": round(float(np.mean(col)), 2),
            "Highest": int(np.max(col)),
            "Lowest": int(np.min(col)),
            "Pass %": round(float(np.mean(col >= PASS_MARK) * 100), 1),
        })
    return pd.DataFrame(rows)


def department_analysis(df):
    """Average marks, attendance and student count per department."""
    return (df.groupby("Department")
              .agg(Students=("Student_ID", "count"),
                   Avg_Marks=("Average", "mean"),
                   Avg_Attendance=("Attendance", "mean"))
              .round(2)
              .sort_values("Avg_Marks", ascending=False))


def top_performers(df, n=5):
    """Return the top n students ranked by average marks."""
    top = df.sort_values("Average", ascending=False).head(n).copy()
    top.insert(0, "Rank", range(1, len(top) + 1))
    return top[["Rank", "Student_ID", "Name", "Department", "Total", "Average", "Grade"]]

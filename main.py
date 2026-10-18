"""Student Performance Analytics System
Run:  python main.py
"""

import pandas as pd
import functions as fn

pd.set_option("display.width", 150)
pd.set_option("display.max_columns", None)


def heading(title):
    print("\n" + "=" * 70)
    print(title)
    print("=" * 70)


def main():
    # Step 1 & 2: load and inspect data
    df = fn.load_data("students.csv")
    heading("1. DATASET OVERVIEW")
    print(f"Records : {df.shape[0]}   Columns : {df.shape[1]}")
    print("Columns :", ", ".join(df.columns))
    print("Missing values:", int(df.isnull().sum().sum()))
    print("\nFirst 5 records:")
    print(df.head())

    # Step 3: process data
    df = fn.calculate_total_and_average(df)
    df = fn.assign_grades(df)
    df = fn.check_pass_fail(df)
    df = fn.attendance_remark(df)

    heading("2. STUDENT RESULT SHEET")
    print(df[["Student_ID", "Name", "Department", "Total", "Average",
              "Grade", "Result", "Attendance"]].to_string(index=False))

    # Step 4: analysis
    stats = fn.class_statistics(df)
    heading("3. CLASS PERFORMANCE")
    print(f"Highest average : {stats['highest_name']} ({stats['highest_avg']})")
    print(f"Lowest average  : {stats['lowest_name']} ({stats['lowest_avg']})")
    print(f"Class average   : {stats['class_average']}")
    print(f"Class median    : {stats['class_median']}")
    print(f"Std deviation   : {stats['std_dev']}")

    heading("4. PASS / FAIL STATISTICS")
    passed = int((df["Result"] == "Pass").sum())
    failed = len(df) - passed
    print(f"Passed : {passed}")
    print(f"Failed : {failed}")
    print(f"Pass percentage : {passed / len(df) * 100:.1f}%")
    print("Failed students :", ", ".join(df[df["Result"] == "Fail"]["Name"]) or "None")
    short = df[df["Attendance_Status"] == "Shortage"]["Name"]
    print("Attendance shortage (<75%):", ", ".join(short) or "None")

    heading("5. GRADE DISTRIBUTION")
    print(df["Grade"].value_counts().to_string())

    heading("6. SUBJECT-WISE ANALYSIS")
    subj = fn.subject_analysis(df)
    print(subj.to_string(index=False))
    best = subj.loc[subj["Average"].idxmax(), "Subject"]
    weak = subj.loc[subj["Average"].idxmin(), "Subject"]
    print(f"\nBest subject (highest average)  : {best}")
    print(f"Weakest subject (lowest average): {weak}")

    heading("7. DEPARTMENT-WISE ANALYSIS")
    print(fn.department_analysis(df))

    heading("8. TOP 5 PERFORMERS")
    print(fn.top_performers(df, 5).to_string(index=False))

    # Save the processed results
    df.to_csv("results_output.csv", index=False)
    print("\nFull results saved to results_output.csv")


if __name__ == "__main__":
    main()

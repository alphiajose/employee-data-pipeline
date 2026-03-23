import pandas as pd
import json

try:
    # Step 1: Read CSV
    df = pd.read_csv("data.csv")

    # Step 2: Clean data
    df = df.dropna()

    # Step 3: Save cleaned CSV
    df.to_csv("cleaned.csv", index=False)

    # Step 4: Convert cleaned data to JSON
    df.to_json("output.json", orient="records", indent=4)

    # Step 5: Create summary
    summary = {
        "total_rows": len(df),
        "columns": list(df.columns),
        "average_salary": float(df["SALARY"].mean()) if "SALARY" in df.columns else None,
        "department_distribution": df["DEPARTMENT_ID"].value_counts().to_dict() if "DEPARTMENT_ID" in df.columns else {}
    }

    with open("summary.json", "w") as f:
        json.dump(summary, f, indent=4)

    print("Processing + JSON conversion completed!")

except Exception as e:
    with open("error.log", "a") as f:
        f.write(str(e) + "\n")

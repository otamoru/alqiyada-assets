import csv

INPUT_CSV = "inputs.csv"
PROMPT_FILE = "prompt.txt"
OUTPUT_CSV = "output.csv"

# اسم الـ placeholder اللي غادي يتبدل
PLACEHOLDER = "PLACEHOLDER"


# قراءة الـ prompt
with open(PROMPT_FILE, "r", encoding="utf-8") as f:
    template = f.read()


# قراءة inputs.csv
with open(INPUT_CSV, "r", encoding="utf-8-sig", newline="") as f:
    reader = csv.reader(f)

    rows = list(reader)


# إنشاء output.csv
with open(OUTPUT_CSV, "w", encoding="utf-8-sig", newline="") as f:
    writer = csv.writer(f)

    # Header
    writer.writerow(["prompt"])

    for row in rows:

        if not row:
            continue

        value = row[0].strip()

        if not value:
            continue

        # تعويض PLACEHOLDER
        new_prompt = template.replace(PLACEHOLDER, value)

        # كتابة النتيجة
        writer.writerow([new_prompt])


print(f"Done! Created: {OUTPUT_CSV}")
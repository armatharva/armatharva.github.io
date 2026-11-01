import csv
from collections import defaultdict
from pathlib import Path
from statistics import mean


DATA_FILE = Path(__file__).with_name("study_hours.csv")


def main():
    hours_by_topic = defaultdict(list)

    with DATA_FILE.open(newline="", encoding="utf-8") as csv_file:
        reader = csv.DictReader(csv_file)
        if not {"week", "topic", "hours"}.issubset(reader.fieldnames or []):
            raise ValueError("CSV must include week, topic, and hours columns.")

        for row in reader:
            topic = row["topic"].strip()
            if not topic:
                raise ValueError("Every row must have a topic.")

            try:
                hours = float(row["hours"])
            except ValueError as error:
                raise ValueError(f"Invalid hours value for {topic!r}.") from error

            if hours < 0:
                raise ValueError(f"Hours cannot be negative for {topic!r}.")
            hours_by_topic[topic].append(hours)

    if not hours_by_topic:
        raise ValueError("The CSV contains no study-hour rows.")

    print("Average study hours per week (synthetic sample):")
    for topic, weekly_hours in sorted(hours_by_topic.items()):
        print(f"- {topic}: {mean(weekly_hours):.1f} hours")


if __name__ == "__main__":
    main()

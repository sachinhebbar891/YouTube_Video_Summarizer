from src import run_pipeline

if __name__ == "__main__":
    title = "Chris Williamson on the lonely chapter"
    summary_type = "Need a summary"
    summary = run_pipeline(title, summary_type)
    print(summary)

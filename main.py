from src import run_pipeline
import argparse

def main():
    parser = argparse.ArgumentParser(description="YouTube Video Summarizer")
    parser.add_argument("--title", type=str, required=True, help="Title of the YouTube video to summarize")
    parser.add_argument("--summary_type", type=str, required=True, help="Type of summary required")
    args = parser.parse_args()

    summary = run_pipeline(args.title, args.summary_type)
    print(summary)

if __name__ == "__main__":
    main()

from video_transcript_reader import get_transcript, format_transcript
from get_video import get_video_metadata_from_title

if __name__ == "__main__":
    title = "Joe Rogan Experience Aravind Srinivas episode"
    video_metadata = get_video_metadata_from_title(title)
    print("Extracted Youtube Video title:", video_metadata["title"])
    print("Extracted Youtube Video Channel:", video_metadata["channel"])
    print("Extracted Youtube Video Published At:", video_metadata["published_at"])
    transcript = get_transcript(video_metadata["video_id"])
    
    if transcript:
        formatted_transcript = format_transcript(transcript)
        print(formatted_transcript[:100])

    else:
        print("No transcript available for this video.")


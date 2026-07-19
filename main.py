from src import get_transcript, format_transcript, get_video_metadata_from_title, check_title_similarity, summarize

if __name__ == "__main__":
    title = "Joe Rogan Experience Aravind Srinivas episode"
    summary_type = "The summary should focus on the discussion of AI and what the future holds for us"
    video_metadata_list = get_video_metadata_from_title(title)
    similarities = []
    for video in video_metadata_list:
        similarity = check_title_similarity(title, video)
        similarities.append(similarity)

    video_metadata = video_metadata_list[similarities.index(max(similarities))]
    print("Similarity score of the extracted video to user text:", max(similarities))
    print("Extracted Youtube Video title:", video_metadata["title"])
    print("Extracted Youtube Video Channel:", video_metadata["channel"])
    print("Extracted Youtube Video Published At:", video_metadata["published_at"])
    transcript = get_transcript(video_metadata["video_id"])
    
    if transcript:
        formatted_transcript = format_transcript(transcript)
        summary = summarize(formatted_transcript, summary_type)

    else:
        print("No transcript available for this video.")


from src import get_transcript, format_transcript, get_video_metadata_from_title, check_title_similarity, summarize

if __name__ == "__main__":
    title = "Chris Williamson on the lonely chapter"
    summary_type = "Need a detailed summary"
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
        print("Summary of the extracted video:", summary)

    else:
        print("No transcript available for this video.")


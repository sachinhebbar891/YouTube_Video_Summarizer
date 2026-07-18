from difflib import SequenceMatcher

def check_title_similarity(title_query, result):
    similarity = SequenceMatcher(None, title_query.lower(), result["channel"].lower() +  ": " + result['title'].lower()).ratio()
    return similarity
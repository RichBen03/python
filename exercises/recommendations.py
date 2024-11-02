# Sample user data
user_data = {
    "viewing_history": ["sports highlights", "tech reviews", "pop music", "movie trailers"],
    "search_history": ["latest tech trends", "football scores", "new music releases"]
}

# Recommendation rules
def recommend_content(user_data):
    # Analyze viewing and search history for category preferences
    interests = {
        "sports": 0,
        "technology": 0,
        "music": 0,
        "movies": 0
    }
    
    # Keywords for identifying user interests
    keywords = {
        "sports": ["sports", "football", "basketball", "highlights", "scores"],
        "technology": ["tech", "gadgets", "reviews", "trends", "AI"],
        "music": ["music", "pop", "songs", "releases", "albums"],
        "movies": ["movies", "trailers", "films", "cinema", "reviews"]
    }
    
    # Check viewing history
    for item in user_data["viewing_history"]:
        for category, words in keywords.items():
            if any(word in item for word in words):
                interests[category] += 1
    
    # Check search history
    for item in user_data["search_history"]:
        for category, words in keywords.items():
            if any(word in item for word in words):
                interests[category] += 1
    
    # Recommendation rules based on identified interests
    recommendations = []
    
    if interests["sports"] > 2:
        recommendations.append("Live sports updates and upcoming match schedules")
    if interests["technology"] > 2:
        recommendations.append("Latest tech news and gadget reviews")
    if interests["music"] > 2:
        recommendations.append("New music releases and concert tickets")
    if interests["movies"] > 2:
        recommendations.append("Trending movies and personalized movie suggestions")

    # Additional conditional rules
    if interests["sports"] > 0 and interests["music"] > 0:
        recommendations.append("Curated playlists for your workout sessions")
    if interests["technology"] > 0 and interests["movies"] > 0:
        recommendations.append("Sci-fi movie recommendations and tech documentaries")
    if len(recommendations) == 0:
        recommendations.append("Explore popular topics and trending news")

    return recommendations

# Run recommendation function
recommendations = recommend_content(user_data)
print("Recommended content based on your interests:")
for recommendation in recommendations:
    print("- " + recommendation)
add
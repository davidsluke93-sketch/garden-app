# Dictionary that stores gardening advice for each season
season_advice = {
    "summer": "Water your plants regularly and provide some shade.",
    "winter": "Protect your plants from frost with covers.",
    "spring": "This is a great time for new growth and planting.",
    "autumn": "Reduce watering and prepare plants for cooler weather."
}

# Dictionary that stores gardening advice for each plant type
plant_advice = {
    "flower": "Use fertiliser to encourage blooms.",
    "vegetable": "Keep an eye out for pests!",
    "herb": "Make sure the soil drains well.",
    "tree": "Water deeply but less often."
}

# Dictionary that recommends plants based on the season
season_recommendations = {
    "summer": ["sunflower", "marigold", "tomato"],
    "winter": ["kale", "spinach", "broccoli"],
    "spring": ["rose", "lettuce", "basil"],
    "autumn": ["carrot", "onion", "lavender"]
}


# Function to get user input
def get_user_input():
    # Ask the user to enter the season
    season = input("Enter the season (summer, winter, spring, autumn): ").lower()

    # Ask the user to enter the plant type
    plant_type = input("Enter the plant type (flower, vegetable, herb, tree): ").lower()

    # Return both values
    return season, plant_type


# Function to generate gardening advice
def generate_advice(season, plant_type):
    # Start with an empty advice string
    advice = ""

    # Check if the season exists in the season advice dictionary
    if season in season_advice:
        advice += "Season advice: " + season_advice[season] + "\n"
    else:
        advice += "Season advice: No advice for this season.\n"

    # Check if the plant type exists in the plant advice dictionary
    if plant_type in plant_advice:
        advice += "Plant advice: " + plant_advice[plant_type] + "\n"
    else:
        advice += "Plant advice: No advice for this type of plant.\n"

    # Return the completed advice
    return advice


# Function to recommend plants for the chosen season
def recommend_plants(season):
    # Check if the season exists in the recommendation dictionary
    if season in season_recommendations:
        plants = ", ".join(season_recommendations[season])
        return "Recommended plants for " + season + ": " + plants
    else:
        return "No plant recommendations available for this season."


# Main function to run the gardening app
def main():
    # Get season and plant type from the user
    season, plant_type = get_user_input()

    # Generate and display gardening advice
    advice = generate_advice(season, plant_type)
    print("\nGardening Advice:")
    print(advice)

    # Generate and display plant recommendations
    recommendations = recommend_plants(season)
    print(recommendations)


# Run the main function
main()

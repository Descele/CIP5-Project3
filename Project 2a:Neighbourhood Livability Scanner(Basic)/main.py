"""
Desiree Cele has created this Livability Scanner(Basic): A resident-powered tool for evaluating quality of life in urban neighborhoods.
Key Features: Assesses 6 critical urban indicators: Housing, Employment, Amenities, Environment, Safety, and Social Connectivity
Simple 1-5 rating system (accessible to all residents).Generates an overall livability percentage score.
Provides instant neighborhood performance feedback.
"""

def calculate_livability_score():
    print("\n=== Neighbourhood Quality of Life Checker ===")
    print("Rate your neighborhood (1-5) on these indicators:\n")
    
    # Get user ratings
    housing = int(input("Housing (affordability/quality): "))
    employment = int(input("Local job opportunities: "))
    amenities = int(input("Access to shops/services: "))
    environment = int(input("Clean air/green spaces: "))
    safety = int(input("Feeling of safety: "))
    social = int(input("Community interactions: "))
    
    # Calculate score
    total = housing + employment + amenities + environment + safety + social
    score = (total / 30) * 100
    
    # Display results
    print(f"\nYour neighbourhood's livability score: {score:.1f}%")
    
    if score >= 80:
        print("Excellent livable neighborhood!")
    elif score >= 60:
        print("Good quality of life!")
    else:
        print("Needs improvement in several areas!")
    
    print("\nThank you for helping improve urban planning!")

# Run the program
calculate_livability_score()

if __name__ == "__main__":
    calculate_livability_score()


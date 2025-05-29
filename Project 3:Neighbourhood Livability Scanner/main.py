
"""
Hello World! Desiree Cele created a Livability Scanner (with AI enabled call_gpt): A resident-powered tool for evaluating quality of life in urban neighborhoods.
Key Features: Assesses 6 critical urban indicators: Housing, Employment, Amenities, Environment, Safety, and Social Connectivity
Simple 1-5 rating system (accessible to all residents).Generates an overall livability percentage score.
Provides instant neighborhood performance feedback.Instantly see what residents care about most.
"""
from ai import call_gpt

def calculate_livability_score():
    print("\n===== Neighbourhood Quality of Life Checker =====")
    neighborhood = input("Enter your neighborhood name (e.g., 'Downtown Brooklyn'): ").strip()
    print(f"\nRating {neighborhood} (1-5) on these indicators:\n")
    
    # Get validated user ratings
    categories = {
        "Housing (affordability/quality)": 0,
        "Local job opportunities": 0,
        "Access to shops/services": 0,
        "Clean air/green spaces": 0,
        "Feeling of safety": 0,
        "Community interactions": 0
    }
    
    for category in categories:
        while True:
            try:
                rating = int(input(f"{category}: "))
                if 1 <= rating <= 5:
                    categories[category] = rating
                    break
                print("Please enter a number 1-5")
            except ValueError:
                print("Invalid input - numbers only")
    
    # Generate GPT prompt with neighborhood context
    analysis= call_gpt("Analyze livability factors for {neighborhood} based on the resident ratings:\n"f"{categories}\n")

    print(f"\n{neighborhood} Livability Report:")
    print("Analysing your neighbourhood...⏳")
    print(f"{analysis}")
    print("\nNote: Results may include estimates when precise data isn't available")
    print("\n=====You have made improving your neighbourhood easier,Thank you!=====")
 

if __name__ == "__main__":
    calculate_livability_score()
   


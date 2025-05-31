# CIP5-Project3
Project 3: Neighbourhood Livability Scanner(includes call_gpt)
Project 3a: Neighbourhood Livability Scanner(not AI-enabled via. call_gpt)

Stanford University’s Code in Place—a global initiative inspired by CS 106A—equipped me with rigorous Python foundations through project-based learning. These projects reflect how I bridge code and urban analysis, transforming abstract concepts into tools for spatial problem-solving.

As an urban planner, I designed solutions that demonstrate Python’s versatility: automating workflows, analyzing datasets, and visualizing urban data patterns. Each project here began as a technical exercise but evolved into a lens for interdisciplinary thinking.

AI-Powered Community Assessment Tool

This resident-driven analyzer combines Python’s simplicity with GPT’s analytical power to evaluate urban quality-of-life factors. By aggregating resident ratings across six key indicators, it generates actionable neighborhood insights—demonstrating how lightweight AI integration can democratize urban planning.

Key Features:
📊 6-Dimensional Assessment – Rates housing, jobs, amenities, environment, safety, and social connectivity
🤖 AI-Enhanced Analysis – Augments user input with GPT-generated contextual insights
🎯 Instant Feedback – Calculates overall livability percentage from 1-5 ratings
🏙️ Hyperlocal Focus – Adapts analysis to any neighborhood name input

Technical Highlights:

Clean user input validation with error handling
Dynamic GPT prompt generation using neighborhood context
Modular design for easy indicator customization

```markdown
 How It Works
1. Residents rate their neighborhood (1-5) on 6 factors  
2. Ratings are sent to GPT with neighborhood context  
3. Returns customized analysis like:  
   > "Downtown Brooklyn scores highly on amenities (4/5) but shows housing affordability concerns (2/5). Consider..."  

Requirements
```bash
pip install openai  # Only if using actual GPT API
```
   
Tags:
python ai-integration urban-planning livability-metrics gpt-api community-tool
## Code in Place Certification  
*Stanford CS106A Methodology | 2025*  

| Week | Focus Area | Skills Badges |  
|------|------------|---------------|  
| 1 | **Karel Foundations** | [![Algorithms](https://img.shields.io/badge/-Algorithms-brightgreen)](https://compedu.stanford.edu/karel-reader/docs/python/en/chapter1.html) [![Loops](https://img.shields.io/badge/-For/While_Loops-blue)](https://compedu.stanford.edu/karel-reader/docs/python/en/chapter4.html) [![Conditionals](https://img.shields.io/badge/-If_Statements-orange)](https://compedu.stanford.edu/karel-reader/docs/python/en/chapter3.html) |  
| 2 | **Stepwise Refinement** | [![Decomposition](https://img.shields.io/badge/-Problem_Decomposition-9cf)](https://compedu.stanford.edu/karel-reader/docs/python/en/chapter7.html) [![Debugging](https://img.shields.io/badge/-Debugging-purple)](https://compedu.stanford.edu/codeinplace/faq#debugging) |  
| 3 | **Python Essentials** | [![I/O](https://img.shields.io/badge/-Input/Output-yellow)](https://docs.python.org/3/tutorial/inputoutput.html) [![Math](https://img.shields.io/badge/-Arithmetic-blue)](https://docs.python.org/3/tutorial/introduction.html#numbers) [![Random](https://img.shields.io/badge/-Random_Lib-success)](https://docs.python.org/3/library/random.html) |  
| 4 | **Creative Graphics** | [![GUI](https://img.shields.io/badge/-Canvas_Graphics-ff69b4)](https://cs.stanford.edu/people/nick/graphics-py/) [![Functions](https://img.shields.io/badge/-Modular_Code-important)](https://docs.python.org/3/tutorial/controlflow.html#defining-functions) |   
| 5 | **Data Structures** | [![Lists](https://img.shields.io/badge/-Lists-2d3e50)](https://docs.python.org/3/tutorial/datastructures.html) [![Dictionaries](https://img.shields.io/badge/-Dicts-8a2be2)](https://docs.python.org/3/tutorial/datastructures.html#dictionaries) [![Search](https://img.shields.io/badge/-Search_Algorithms-brightgreen)](https://compedu.stanford.edu/codeinplace/faq#searching) | 
--- 


License & Attribution
Code: MIT License
Data: American Community Survey (Public Domain)
Pedagogy: Stanford Code in Place (CS106A)

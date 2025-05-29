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

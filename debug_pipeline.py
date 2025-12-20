"""
Debug trace of the full Pragyan pipeline
To see exactly what code path is being used
"""

import os
import sys
from pathlib import Path

# Set API key first
api_key = os.getenv("GEMINI_API_KEY") or os.getenv("GROQ_API_KEY")
if not api_key:
    print("ERROR: Set GEMINI_API_KEY or GROQ_API_KEY first!")
    sys.exit(1)

provider = "gemini" if os.getenv("GEMINI_API_KEY") else "groq"

sys.path.insert(0, str(Path(__file__).parent / "src"))

from pragyan import Pragyan
from pragyan.models import Question, ProgrammingLanguage
from pragyan.algorithm_visualizers import get_visualizer_for_problem

print("=" * 60)
print("DEBUG TRACE: Full Pipeline")
print("=" * 60)

# Create question
question = Question(
    title="N-Queens Problem",
    description="""
    The n-queens puzzle is the problem of placing n queens on an n×n chessboard 
    such that no two queens attack each other.
    Given an integer n, return all distinct solutions to the n-queens puzzle.
    """,
    examples=[{"input": "n = 4", "output": "[[...]]"}],
    constraints=["1 <= n <= 9"],
    difficulty="Hard"
)

print(f"\n1. Question: {question.title}")
print(f"   Description: {question.description[:100]}...")

# Test detection directly
print("\n2. Testing visualizer detection DIRECTLY:")
test_desc = question.description + " " + question.title
test_approach = "Backtracking algorithm"
result = get_visualizer_for_problem(test_desc, test_approach)
if result:
    viz, kwargs = result
    print(f"   ✓ Detected: {type(viz).__name__}")
    print(f"   ✓ Kwargs: {kwargs}")
else:
    print("   ✗ NOT DETECTED!")

# Initialize Pragyan
print("\n3. Initializing Pragyan...")
pragyan = Pragyan(provider=provider, api_key=api_key)

# Solve
print("\n4. Solving problem...")
solution = pragyan.solve(question, ProgrammingLanguage.PYTHON)
print(f"   Concept: {solution.concept}")
print(f"   Approach: {solution.approach[:100]}...")

# Test detection with actual solution
print("\n5. Testing visualizer detection with ACTUAL solution:")
actual_desc = question.description + " " + question.title
actual_approach = solution.concept + " " + solution.approach
result2 = get_visualizer_for_problem(actual_desc, actual_approach)
if result2:
    viz2, kwargs2 = result2
    print(f"   ✓ Detected: {type(viz2).__name__}")
    print(f"   ✓ Kwargs: {kwargs2}")
else:
    print("   ✗ NOT DETECTED - This is the problem!")
    print(f"\n   Checking why...")
    text = actual_desc.lower() + " " + actual_approach.lower()
    print(f"   'queen' in text: {'queen' in text}")
    print(f"   'n-queen' in text: {'n-queen' in text}")
    print(f"   'nqueen' in text: {'nqueen' in text}")

# Generate video with debug
print("\n6. Generating video...")
print("   Watch for '🎬 Using specialized visualizer' message...")

try:
    video_path = pragyan.generate_video(question, solution)
    print(f"\n   ✓ Video generated: {video_path}")
except Exception as e:
    print(f"\n   ✗ Error: {e}")
    import traceback
    traceback.print_exc()

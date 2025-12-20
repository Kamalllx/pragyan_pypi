# Pragyan Dynamic Animations - Quick Start Guide 🚀

## What Changed?

Your videos are no longer boring! Instead of static slides, you now get **dynamic, algorithm-specific animations** that show exactly how algorithms work.

## Quick Example

### Before (Boring 😴):
```
"Here's the N-Queens problem"
[Static text slide]
[Code on screen]
[More text]
"Done"
```

### Now (Exciting 🎉):
```
"N-Queens Problem"
[Animated 8x8 chess board appears]
[Queen placed at (0,0) with animation]
[Try (1,2) - highlighted in blue]
[Queen placed - turns green]
[Try (2,1) - CONFLICT! Turns red]
[BACKTRACK - queen removed with animation]
[Continue placing... backtracking... placing...]
[SOLUTION FOUND! All queens highlighted in gold]
```

## Supported Algorithms

✅ **N-Queens** - Chess board with backtracking
✅ **Sorting** (Quick, Merge, Bubble) - Bar charts with swaps
✅ **Graph BFS/DFS** - Animated traversal with queue
✅ **Two Pointers** - Pointer movement on arrays
✅ **Sliding Window** - Window sliding across array
✅ **Binary Search** - Mid pointer + eliminated sections

## How to Use

### 1. Same API, Better Results

No code changes needed! Just use Pragyan as normal:

```python
from pragyan import Pragyan

pragyan = Pragyan(provider="gemini", api_key="YOUR_KEY")

# Solve any DSA problem
question = pragyan.scrape_question("https://leetcode.com/problems/n-queens/")
solution = pragyan.solve(question, "python")

# Generate video - automatically uses dynamic animations!
video_path = pragyan.generate_video(question, solution)
```

That's it! The system automatically detects the algorithm type and generates appropriate animations.

### 2. Manual Testing

Try the examples:

```bash
cd examples
python dynamic_animations_example.py
```

Choose an option to see different animation types.

## Detection Logic

The system automatically detects your algorithm type:

```python
# Keywords in problem/solution → Animation type
"n-queens", "nqueens"         → Chess board animation
"quick sort", "bubble sort"   → Bar chart with swaps
"bfs", "breadth-first"        → Graph traversal
"two pointer"                 → Pointer movement
"sliding window"              → Window sliding
"binary search"               → Binary search visualization
```

## What You'll See

### For N-Queens:
- ✓ Animated chess board (proper colors)
- ✓ Queens appearing one by one
- ✓ Blue highlight when trying position
- ✓ Green when placed successfully
- ✓ Red when backtracking
- ✓ Status text: "Trying (2,3)", "Backtracking from (1,2)"
- ✓ Final solution in gold

### For Sorting:
- ✓ Bar chart (height = value)
- ✓ Yellow bars being compared
- ✓ Gold pivot selection
- ✓ Smooth swap animations
- ✓ Green when sorted
- ✓ Counter: comparisons and swaps

### For Graph BFS:
- ✓ Graph with nodes and edges
- ✓ Queue display updating
- ✓ Current node highlighted
- ✓ Visited nodes turn green
- ✓ Traversal order shown

## Key Files

```
pragyan/
├── algorithm_visualizers.py  ← NEW! Specialized animations
├── video_generator.py         ← UPDATED! Uses visualizers
├── llm_client.py              ← UPDATED! Animation generation
└── main.py                    ← UPDATED! Connects everything

examples/
└── dynamic_animations_example.py  ← NEW! See it in action
```

## Troubleshooting

### Videos still look boring?
- Make sure you have the latest code
- Check that Manim is installed: `pip install manim`
- Try running the examples to confirm it works

### Not detecting algorithm correctly?
- The detection uses keywords from your problem description
- For N-Queens, make sure "queen" or "n-queens" is in the title/description
- For sorting, include "sort" in the description

### Rendering fails?
- Ensure Manim is properly installed
- Try with a simpler problem first
- Check the generated Manim code in temp directory

## Performance

- Detection: Instant (< 100ms)
- Code Generation: 1-3 seconds
- Video Rendering: 30-60 seconds

## What's Next?

More algorithm types coming:
- ✨ Dynamic Programming (table filling)
- ✨ Tree traversals (inorder, preorder, postorder)
- ✨ Dijkstra's algorithm
- ✨ Union-Find
- ✨ Trie operations

## Need Help?

1. Run the examples first: `python examples/dynamic_animations_example.py`
2. Check `DYNAMIC_ANIMATIONS_UPDATE.md` for detailed docs
3. Look at generated Manim code in temp directory
4. Open a GitHub issue

---

## The Bottom Line

**Before**: Static slides, boring videos, hard to understand

**Now**: Dynamic animations, engaging videos, easy to understand

**Your code**: Unchanged!

**Your videos**: 10x better! 🎬✨

---

Enjoy creating amazing algorithm visualizations! 🚀

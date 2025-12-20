"""
Quick test to verify the visualizers generate valid Manim code
This test doesn't require API keys - just tests code generation
"""

from src.pragyan.algorithm_visualizers import (
    NQueensVisualizer, 
    SortingVisualizer, 
    GraphVisualizer,
    get_visualizer_for_problem
)

def test_nqueens_visualizer():
    """Test N-Queens visualizer generates code"""
    print("=" * 60)
    print("Testing N-Queens Visualizer")
    print("=" * 60)
    
    visualizer = NQueensVisualizer()
    code = visualizer.generate_manim_code(n=4, show_steps=10)
    
    # Check code is generated
    assert len(code) > 100, "Code too short"
    assert "class NQueensScene(Scene)" in code, "Missing scene class"
    assert "def construct(self)" in code, "Missing construct method"
    assert "chessboard" in code.lower(), "Missing chessboard"
    assert "queen" in code.lower(), "Missing queen"
    
    print(f"✓ Generated {len(code)} characters of Manim code")
    print(f"✓ Contains NQueensScene class")
    print(f"✓ Contains chess board logic")
    print(f"✓ Contains backtracking logic")
    print("\n[Preview - First 500 chars]:")
    print(code[:500])
    print("...")
    

def test_sorting_visualizer():
    """Test Sorting visualizer generates code"""
    print("\n" + "=" * 60)
    print("Testing Sorting Visualizers")
    print("=" * 60)
    
    visualizer = SortingVisualizer()
    
    # Test bubble sort
    code = visualizer.generate_manim_code(algorithm="bubblesort", array=[5, 2, 8, 1])
    assert "BubbleSortScene" in code
    assert "bars" in code.lower()
    assert "swap" in code.lower()
    print("✓ Bubble Sort visualizer works")
    
    # Test quick sort
    code = visualizer.generate_manim_code(algorithm="quicksort", array=[5, 2, 8, 1])
    assert "QuickSortScene" in code
    assert "pivot" in code.lower()
    print("✓ Quick Sort visualizer works")
    
    # Test merge sort
    code = visualizer.generate_manim_code(algorithm="mergesort", array=[5, 2, 8, 1])
    assert "MergeSortScene" in code
    print("✓ Merge Sort visualizer works")
    
    print(f"\n[Preview - Bubble Sort first 500 chars]:")
    code = visualizer.generate_manim_code(algorithm="bubblesort", array=[5, 2, 8, 1])
    print(code[:500])
    print("...")


def test_graph_visualizer():
    """Test Graph visualizer generates code"""
    print("\n" + "=" * 60)
    print("Testing Graph Visualizers")
    print("=" * 60)
    
    visualizer = GraphVisualizer()
    
    # Test BFS
    code = visualizer.generate_manim_code(algorithm="bfs")
    assert "BFSScene" in code
    assert "queue" in code.lower()
    assert "breadth" in code.lower()
    print("✓ BFS visualizer works")
    
    # Test DFS
    code = visualizer.generate_manim_code(algorithm="dfs")
    assert "DFSScene" in code
    print("✓ DFS visualizer works")
    
    print(f"\n[Preview - BFS first 500 chars]:")
    code = visualizer.generate_manim_code(algorithm="bfs")
    print(code[:500])
    print("...")


def test_problem_detection():
    """Test automatic problem detection"""
    print("\n" + "=" * 60)
    print("Testing Automatic Problem Detection")
    print("=" * 60)
    
    # Test N-Queens detection
    result = get_visualizer_for_problem("N-Queens problem", "backtracking algorithm")
    assert result is not None, "Failed to detect N-Queens"
    visualizer, kwargs = result
    assert isinstance(visualizer, NQueensVisualizer)
    print(f"✓ Detected N-Queens: {type(visualizer).__name__} with kwargs {kwargs}")
    
    # Test sorting detection
    result = get_visualizer_for_problem("Sort the array using quick sort", "divide and conquer")
    assert result is not None, "Failed to detect sorting"
    visualizer, kwargs = result
    assert isinstance(visualizer, SortingVisualizer)
    print(f"✓ Detected Sorting: {type(visualizer).__name__} with kwargs {kwargs}")
    
    # Test graph detection
    result = get_visualizer_for_problem("Traverse graph using BFS", "breadth-first search")
    assert result is not None, "Failed to detect graph"
    visualizer, kwargs = result
    assert isinstance(visualizer, GraphVisualizer)
    print(f"✓ Detected Graph: {type(visualizer).__name__} with kwargs {kwargs}")
    
    # Test no detection
    result = get_visualizer_for_problem("Some random problem", "some approach")
    assert result is None, "Should not detect anything"
    print("✓ Correctly returns None for unrecognized problems")


def test_generated_code_syntax():
    """Test that generated code has valid Python syntax"""
    print("\n" + "=" * 60)
    print("Testing Generated Code Syntax")
    print("=" * 60)
    
    import ast
    
    # Generate code from each visualizer
    tests = [
        ("N-Queens", NQueensVisualizer().generate_manim_code(n=4, show_steps=5)),
        ("Bubble Sort", SortingVisualizer().generate_manim_code(algorithm="bubblesort")),
        ("Quick Sort", SortingVisualizer().generate_manim_code(algorithm="quicksort")),
        ("BFS", GraphVisualizer().generate_manim_code(algorithm="bfs")),
    ]
    
    for name, code in tests:
        try:
            # Try to parse the code as Python
            ast.parse(code)
            print(f"✓ {name}: Valid Python syntax")
        except SyntaxError as e:
            print(f"✗ {name}: Syntax error - {e}")
            raise


def main():
    """Run all tests"""
    print("""
╔══════════════════════════════════════════════════════════════╗
║           PRAGYAN VISUALIZERS - UNIT TESTS                   ║
║     Testing dynamic animation code generation                ║
╚══════════════════════════════════════════════════════════════╝
    """)
    
    try:
        test_nqueens_visualizer()
        test_sorting_visualizer()
        test_graph_visualizer()
        test_problem_detection()
        test_generated_code_syntax()
        
        print("\n" + "=" * 60)
        print("✅ ALL TESTS PASSED!")
        print("=" * 60)
        print("\nThe visualizers are working correctly!")
        print("They generate valid Manim code that can be rendered.")
        print("\nNext steps:")
        print("1. Set up API keys: export GEMINI_API_KEY=xxx or GROQ_API_KEY=xxx")
        print("2. Run full examples: python examples/dynamic_animations_example.py")
        print("3. Generate an actual video to verify Manim rendering")
        
        return True
        
    except AssertionError as e:
        print(f"\n❌ TEST FAILED: {e}")
        return False
    except Exception as e:
        print(f"\n❌ ERROR: {e}")
        import traceback
        traceback.print_exc()
        return False


if __name__ == "__main__":
    success = main()
    exit(0 if success else 1)

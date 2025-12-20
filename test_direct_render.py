"""
Direct test of the algorithm visualizers - bypasses full pipeline
This will render the NQueensScene directly to see if it works
"""

import os
import sys
import tempfile
import subprocess
from pathlib import Path

# Add src to path
sys.path.insert(0, str(Path(__file__).parent / "src"))

from pragyan.algorithm_visualizers import NQueensVisualizer, get_visualizer_for_problem


def test_nqueens_direct():
    """Generate and render NQueensScene directly"""
    print("=" * 60)
    print("DIRECT TEST: N-Queens Visualization")
    print("=" * 60)
    
    # Step 1: Test problem detection
    print("\n1. Testing problem detection...")
    result = get_visualizer_for_problem(
        "N-Queens Problem - place queens on chess board",
        "Backtracking algorithm"
    )
    
    if result:
        visualizer, kwargs = result
        print(f"   ✓ Detected: {type(visualizer).__name__}")
        print(f"   ✓ Kwargs: {kwargs}")
    else:
        print("   ✗ FAILED to detect N-Queens!")
        return
    
    # Step 2: Generate scene code
    print("\n2. Generating Manim scene code...")
    scene_code = visualizer.generate_manim_code(**kwargs)
    
    # Check if it contains the right class
    if "class NQueensScene(Scene)" in scene_code:
        print("   ✓ Contains NQueensScene class")
    else:
        print("   ✗ Missing NQueensScene class!")
        return
    
    if "chess" in scene_code.lower() or "square" in scene_code.lower():
        print("   ✓ Contains chess board logic")
    
    if "backtrack" in scene_code.lower():
        print("   ✓ Contains backtracking logic")
    
    # Step 3: Create full scene file
    print("\n3. Creating scene file...")
    
    full_code = f'''"""
Generated NQueensScene - Direct Test
"""
from manim import *
import numpy as np

config.pixel_height = 720
config.pixel_width = 1280
config.frame_rate = 30
config.background_color = "#1a1a2e"

{scene_code}
'''
    
    # Save to temp file
    temp_dir = Path(tempfile.mkdtemp(prefix="pragyan_test_"))
    scene_file = temp_dir / "nqueens_test.py"
    
    with open(scene_file, "w", encoding="utf-8") as f:
        f.write(full_code)
    
    print(f"   ✓ Scene file: {scene_file}")
    print(f"\n4. Scene code preview (first 1000 chars):")
    print("-" * 40)
    print(full_code[:1000])
    print("-" * 40)
    
    # Step 4: Render with Manim
    print("\n5. Rendering with Manim...")
    print("   Command: manim -ql nqueens_test.py NQueensScene")
    
    cmd = [
        "manim",
        "-ql",  # Low quality for faster test
        str(scene_file),
        "NQueensScene",
        "--media_dir", str(temp_dir / "media"),
    ]
    
    try:
        result = subprocess.run(
            cmd,
            capture_output=True,
            text=True,
            cwd=str(scene_file.parent),
            timeout=120
        )
        
        print(f"\n   Return code: {result.returncode}")
        
        if result.returncode != 0:
            print("\n   ✗ RENDER FAILED!")
            print("\n   STDERR:")
            print(result.stderr[:2000])
            return
        
        print("   ✓ Render successful!")
        
        # Find output video
        media_dir = temp_dir / "media" / "videos" / "nqueens_test"
        for quality_dir in media_dir.iterdir() if media_dir.exists() else []:
            for video_file in quality_dir.glob("*.mp4"):
                output = Path.cwd() / "test_nqueens_output.mp4"
                import shutil
                shutil.copy(video_file, output)
                print(f"\n   ✓ Output video: {output}")
                print(f"   ✓ Video size: {output.stat().st_size / 1024:.1f} KB")
                return
        
        print("   ✗ No video file found!")
        
    except subprocess.TimeoutExpired:
        print("   ✗ Render timed out!")
    except Exception as e:
        print(f"   ✗ Error: {e}")


if __name__ == "__main__":
    test_nqueens_direct()

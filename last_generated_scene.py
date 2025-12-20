"""
Dynamically generated Manim scene by Pragyan
Problem: Regular Expression Matching
Generated using LLM-powered visualization
"""

from manim import *
import numpy as np

config.pixel_height = 1080
config.pixel_width = 1920
config.frame_rate = 30
config.background_color = "#1e1e1e"

class AlgorithmScene(Scene):
    def construct(self):
        # ---------- INTRO ----------
        title = Text("Regular Expression Matching", font_size=48, color=GOLD)
        self.play(FadeIn(title, shift=UP), run_time=2)
        self.wait(2)

        problem_stmt = Text(
            "Given a string s and a pattern p with '.' and '*', "
            "determine if p matches the entire s.", 
            font_size=24, color=WHITE
        )
        problem_stmt.to_edge(DOWN, buff=2)
        self.play(FadeIn(problem_stmt, shift=UP), run_time=3)
        self.wait(2)

        example_input = Text('Example: s = "aa", p = "a*"', font_size=24, color=PURPLE)
        example_input.next_to(problem_stmt, DOWN, buff=0.5)
        self.play(FadeIn(example_input, shift=UP), run_time=3)
        self.wait(2)

        # ---------- ALGORITHM EXPLANATION ----------
        self.play(FadeOut(title), FadeOut(problem_stmt), FadeOut(example_input), run_time=1)

        algo_title = Text("Algorithm: Top‑down DP with Memoization", font_size=36, color=GOLD)
        algo_title.to_edge(UP)
        self.play(FadeIn(algo_title, shift=DOWN), run_time=2)
        self.wait(0.5)

        bullet1 = Text("• dp(i, j) = does s[i:] match p[j:]", font_size=22, color=WHITE)
        bullet1.next_to(algo_title, DOWN, buff=0.7)
        bullet2 = Text("• Use recursion + @lru_cache to store results", font_size=22, color=WHITE)
        bullet2.next_to(bullet1, DOWN, buff=0.4)
        bullet3 = Text("• Handle '.' as any character", font_size=22, color=WHITE)
        bullet3.next_to(bullet2, DOWN, buff=0.4)
        bullet4 = Text("• Handle '*' as zero or more of previous token", font_size=22, color=WHITE)
        bullet4.next_to(bullet3, DOWN, buff=0.4)

        self.play(FadeIn(bullet1, shift=RIGHT), run_time=2)
        self.wait(0.5)
        self.play(FadeIn(bullet2, shift=RIGHT), run_time=2)
        self.wait(0.5)
        self.play(FadeIn(bullet3, shift=RIGHT), run_time=2)
        self.wait(0.5)
        self.play(FadeIn(bullet4, shift=RIGHT), run_time=2)
        self.wait(1.5)

        # ---------- STEP‑BY‑STEP VISUALIZATION ----------
        # Prepare DP table grid for s = "aa" (len=2) and p = "a*" (len=2)
        s = "aa"
        p = "a*"
        rows = len(s) + 1   # i from 0..2
        cols = len(p) + 1   # j from 0..2

        cell_size = 0.8
        grid = VGroup()
        for i in range(rows):
            row = VGroup()
            for j in range(cols):
                sq = Square(side_length=cell_size, stroke_width=2, color=GRAY)
                sq.set_fill(WHITE, opacity=0.5)
                txt = Text(f"{i},{j}", font_size=18, color=BLACK)
                txt.move_to(sq.get_center())
                cell = VGroup(sq, txt)
                row.add(cell)
            row.arrange(RIGHT, buff=0.1)
            grid.add(row)
        grid.arrange(DOWN, buff=0.1)
        grid.move_to(ORIGIN)

        # Labels for rows (s indices) and columns (p indices)
        row_labels = VGroup()
        for i in range(rows):
            lbl = Text(f"s[{i}]" if i < len(s) else "s[∅]", font_size=20, color=YELLOW)
            lbl.next_to(grid.submobjects[i][0], LEFT, buff=0.3)
            row_labels.add(lbl)

        col_labels = VGroup()
        for j in range(cols):
            lbl = Text(f"p[{j}]" if j < len(p) else "p[∅]", font_size=20, color=YELLOW)
            lbl.next_to(grid.submobjects[0][j], UP, buff=0.3)
            col_labels.add(lbl)

        self.play(FadeIn(grid, shift=UP), FadeIn(row_labels, shift=LEFT), FadeIn(col_labels, shift=UP), run_time=2)
        self.wait(1)

        status = Text("", font_size=24, color=WHITE)
        status.to_edge(DOWN, buff=1)

        # Helper to highlight a cell
        def highlight(i, j, color):
            cell = grid.submobjects[i][j]
            self.play(cell[0].animate.set_fill(color, opacity=0.8), run_time=1.5)

        # Step 1: dp(2,2) – both strings exhausted → True
        status.become(Text("Compute dp(2,2): both indices at end → True", font_size=24, color=GREEN))
        self.play(FadeIn(status), run_time=1)
        highlight(2, 2, BLUE)
        self.wait(0.5)
        self.play(grid.submobjects[2][2][0].animate.set_fill(GREEN, opacity=0.8), run_time=1.5)
        self.wait(1)

        # Step 2: dp(2,1) – pattern has '*', can skip it → dp(2,3) (out of range) = False, or use * → False
        status.become(Text("Compute dp(2,1): pattern '*', try skip → dp(2,3) false", font_size=24, color=YELLOW))
        self.play(FadeIn(status), run_time=1)
        highlight(2, 1, BLUE)
        self.wait(0.5)
        self.play(grid.submobjects[2][1][0].animate.set_fill(RED, opacity=0.8), run_time=1.5)
        self.wait(1)

        # Step 3: dp(1,2) – pattern exhausted but s not → False
        status.become(Text("Compute dp(1,2): pattern exhausted, string left → False", font_size=24, color=YELLOW))
        self.play(FadeIn(status), run_time=1)
        highlight(1, 2, BLUE)
        self.wait(0.5)
        self.play(grid.submobjects[1][2][0].animate.set_fill(RED, opacity=0.8), run_time=1.5)
        self.wait(1)

        # Step 4: dp(1,1) – p[1] = '*', check zero or more
        status.become(Text("Compute dp(1,1): '*', try zero → dp(1,3) false; try one → dp(2,1) false", font_size=24, color=YELLOW))
        self.play(FadeIn(status), run_time=1)
        highlight(1, 1, BLUE)
        self.wait(0.5)
        self.play(grid.submobjects[1][1][0].animate.set_fill(RED, opacity=0.8), run_time=1.5)
        self.wait(1)

        # Step 5: dp(0,0) – first characters match, next is '*'
        status.become(Text("Compute dp(0,0): chars match, '*' allows repeat → dp(1,0) or dp(0,2)", font_size=24, color=YELLOW))
        self.play(FadeIn(status), run_time=1)
        highlight(0, 0, BLUE)
        self.wait(0.5)
        # Show dp(0,2) true (skip '*')
        self.play(grid.submobjects[0][2][0].animate.set_fill(GREEN, opacity=0.8), run_time=1.5)
        self.wait(0.5)
        # Show dp(1,0) true (consume one 'a')
        self.play(grid.submobjects[1][0][0].animate.set_fill(GREEN, opacity=0.8), run_time=1.5)
        self.wait(0.5)
        # Final result cell becomes GREEN
        self.play(grid.submobjects[0][0][0].animate.set_fill(GREEN, opacity=0.8), run_time=1.5)
        self.wait(1)

        self.play(FadeOut(status), run_time=1)
        self.wait(1)

        # ---------- RESULT & COMPLEXITY ----------
        result_text = Text("Result: True (pattern matches the string)", font_size=30, color=GREEN)
        result_text.to_edge(UP, buff=1)
        self.play(FadeIn(result_text, shift=DOWN), run_time=2)
        self.wait(2)

        # Complexity box
        time_box = Rectangle(width=5, height=1, color=BLUE)
        time_box.set_fill(BLUE, opacity=0.2)
        time_txt = Text("Time: O(|s| * |p|)", font_size=24, color=WHITE)
        time_txt.move_to(time_box.get_center())
        space_box = Rectangle(width=5, height=1, color=PURPLE)
        space_box.set_fill(PURPLE, opacity=0.2)
        space_txt = Text("Space: O(|s| * |p|)", font_size=24, color=WHITE)
        space_txt.move_to(space_box.get_center())
        comp_group = VGroup(time_box, space_box, time_txt, space_txt)
        comp_group.arrange(DOWN, buff=0.3)
        comp_group.next_to(result_text, DOWN, buff=0.8)

        self.play(FadeIn(comp_group, shift=UP), run_time=2)
        self.wait(1)

        # Key takeaways
        take1 = Text("• DP avoids exponential recursion", font_size=22, color=WHITE)
        take2 = Text("• Memoization stores each (i,j) once", font_size=22, color=WHITE)
        take3 = Text("• Handles '.' and '*' uniformly", font_size=22, color=WHITE)
        take1.next_to(comp_group, DOWN, buff=0.6)
        take2.next_to(take1, DOWN, buff=0.3)
        take3.next_to(take2, DOWN, buff=0.3)

        self.play(FadeIn(take1, shift=RIGHT), run_time=1.5)
        self.wait(0.5)
        self.play(FadeIn(take2, shift=RIGHT), run_time=1.5)
        self.wait(0.5)
        self.play(FadeIn(take3, shift=RIGHT), run_time=1.5)
        self.wait(2)

        # ---------- OUTRO ----------
        outro = Text("Generated by Pragyan", font_size=28, color=GOLD)
        outro.to_edge(DOWN, buff=0.5)
        self.play(FadeIn(outro, shift=UP), run_time=2)
        self.wait(3)
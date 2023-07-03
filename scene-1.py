'''
Code for creating 10 frames using chat GPT
'''

from manim import *

class FiveFramesWithNumbers(Scene):
    def construct(self):
        # Create 5 squares (frames) in a row
        frames = [Square(side_length=1).shift(RIGHT*x) for x in range(5)]
        
        for i, frame in enumerate(frames):
            # For each frame, create a single circle (to represent the number 5)
            circle = Circle(radius=0.5, fill_opacity=0.5).move_to(frame.get_center())
            
            # Create a group consisting of the frame and the circle
            group = VGroup(frame, circle)
            
            # Show the group
            self.play(Create(group), run_time=1)
            
        self.wait()  # This is for Manim to hold the last frame.




class VerticalFramesWithNumbers(Scene):
    def construct(self):
        num = 8
        frames = []
        for j in range(2):
            for i in range(5):
                frames.append(Square(side_length=1).shift(RIGHT*j + UP*i))
        group = VGroup(*frames).move_to(ORIGIN)
        self.play(Create(group))
        
        for i in range(num):
            circle = Circle(radius=0.48, color=BLUE,fill_opacity=1).move_to(frames[i].get_center())
            self.play(Create(circle))
        self.wait()  # This is for Manim to hold the last frame.

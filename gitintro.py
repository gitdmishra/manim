from manim import *

class Intro(Scene):

    def construct(self):
        self.git_box_with_command(2, 10, "Hello Jhalle")

    def git_box_with_command(self, height, width, cmd):

        rect = Rectangle(height=height, width=width, color=WHITE).set_stroke(width=1)
        self.play(Write(rect))
        # print(f'####$$$$${rect.get_edge_center(LEFT)}')
        # text_
        text_command = Text(f'$ {cmd}',font='Consolas' ,font_size=20, color= PURE_GREEN).next_to(rect.get_edge_center(LEFT), RIGHT)
        self.play(AddTextLetterByLetter(text_command))
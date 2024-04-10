from manim import *
import random

class Vector(Scene):
    def construct(self):
        self.camera.background_color = WHITE

        vector_values = [0] * 8
        vector_values[1] = 1
        vector_text = VGroup(*[Text(str(num), color=BLACK).scale(0.8) for num in vector_values])
        vector_text.arrange(RIGHT, buff=0.5)


        vector_text.to_edge(UP)
        arrow = Arrow(start=[0, 0, 0], end=vector_text[1].get_bottom() + [0, -0.5, 0], buff=0.1, color=BLACK)

        label = Text("Index 1 (Value 1)", color=BLACK, font_size=24).next_to(arrow, DOWN)

        self.add(vector_text, arrow, label)

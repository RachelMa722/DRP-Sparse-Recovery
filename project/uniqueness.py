from manim import *
import random

class Uniqueness(Scene):
    def construct(self):
        self.camera.background_color=WHITE

        x_ellipse = Ellipse(width=3.0, height=5.0, color=BLUE)
        y_ellipse = Ellipse(width=3.0, height=5.0, color=BLUE)
        x_ellipse.to_edge(LEFT)
        y_ellipse.to_edge(RIGHT)

        x_label = MathTex("x", color=BLACK).next_to(x_ellipse, UP)
        y_label = MathTex("Output", color=BLACK).next_to(y_ellipse, UP)

        x_nodes = VGroup(*[Dot() for _ in range(5)]).arrange(DOWN, buff=0.6).move_to(x_ellipse)
        y_nodes = VGroup(*[Dot() for _ in range(3)]).arrange(DOWN, buff=1.5).move_to(y_ellipse)
        x_nodes.set_color(BLACK)
        y_nodes.set_color(BLACK)

        arrows = VGroup()
        arrows.add(Arrow(x_nodes[1], y_nodes[1], buff=0.1, color=BLACK))
        arrows.add(Arrow(x_nodes[3], y_nodes[1], buff=0.1, color=BLACK))

        self.add(x_ellipse, y_ellipse, arrows, x_nodes, y_nodes, x_label, y_label)
        #self.play(Create(arrows))

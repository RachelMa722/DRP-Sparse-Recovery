from manim import *


# matrix 
# https://docs.manim.community/en/stable/reference/manim.mobject.matrix.Matrix.html#manim.mobject.matrix.Matrix

class AdaptiveSearch(Scene):
    def construct(self):
        x1 = Matrix([[0], [0], [0], [0], [1], [0], [0], [0]])
        x2 = Matrix([[0], [0], [0], [0], [1], [0], [0], [0]])
        x3 = Matrix([[0], [0], [0], [0], [1], [0], [0], [0]])

        b = Matrix([[0], [1], [0], [0], [0], [0], [0], [0]])

        ratios = [0, 0.1, 0.5, 1, 2] 

        m0 = Matrix([[1,0,0,0,0,0,0,0], [0,1,0,0,0,0,0,0], [0,0,1,0,0,0,0,0], [0,0,0,1,0,0,0,0],
                     [0,0,0,0,1,0,0,0], [0,0,0,0,0,1,0,0], [0,0,0,0,0,0,1,0], [0,0,0,0,0,0,0,1]])

        a1 = Matrix([[0],[0],[0],[0],[1],[1],[1],[1]])
        a2 = Matrix([[0],[0],[0],[0],[0],[0],[1],[1]])
        a3 = Matrix([[0],[0],[0],[0],[0],[1],[0],[0]])

        x_dot_a1 = Text("1").set_color(WHITE)
        x_dot_a2 = Text("0").set_color(WHITE)
        x_dot_a3 = Text("0").set_color(WHITE)

        dot = Text("∙").set_color(WHITE)
        dot_o = dot.copy()

        equals = Text("=").set_color(WHITE)
        equals_o = equals.copy()

        # multiply x with a1, circle top half, result = 1
        # thus, we know to focus in on the top, can we position the result at the top into a vector?
        # position x and a1
        dot.next_to(a1, LEFT)
        x1.next_to(dot, LEFT)
        equals.next_to(a1, RIGHT)
        x_dot_a1.next_to(equals, RIGHT)
        
        # animate in
        self.play(AnimationGroup(
            Create(x1),
            Create(dot), 
            Create(a1), 
            lag_ratio=0.25))

        # move to the left
        self.play(AnimationGroup(Create(equals), Create(x_dot_a1), lag_ratio=0.1))
        cleanup = VGroup(dot, x1, a1, equals, x_dot_a1)
        self.play(cleanup.animate.scale(0.75))
        self.play(cleanup.animate.shift(LEFT*4))

        x1_label = Text("x").set_color(WHITE)
        x1_label.scale(0.75)
        x1_label.next_to(x1, UP)
        self.add(x1_label)

        # rectangle
        rect1 = SurroundingRectangle(a1.get_rows()[4:8])
        a1.add(rect1)
        self.play(Create(rect1))

        self.wait(2)


        # ======== next iteration, do half the vector ===================
        dot = dot_o.copy()
        equals = equals_o.copy()

        dot.next_to(a2, LEFT)
        x2.next_to(dot, LEFT)
        equals.next_to(a2, RIGHT)
        x_dot_a2.next_to(equals, RIGHT)
        
        # animate in
        self.play(AnimationGroup(
            Create(x2),
            Create(dot), 
            Create(a2), 
            lag_ratio=0.25))
        
        # move to the left
        self.play(AnimationGroup(Create(equals), Create(x_dot_a2), lag_ratio=0.1))
        cleanup = VGroup(dot, x2, a2, equals, x_dot_a2)
        self.play(cleanup.animate.scale(0.75))

        # rectangle
        rect2 = SurroundingRectangle(a2.get_rows()[4:6])
        a2.add(rect2)
        self.play(Create(rect2))

        self.wait(2)

        # ======== 3rd iteration ==============================
        dot = dot_o.copy()
        equals = equals_o.copy() 

        a3.move_to((ORIGIN+RIGHT*4))

        dot.next_to(a3, LEFT)
        x3.next_to(dot, LEFT)
        equals.next_to(a3, RIGHT)
        x_dot_a3.next_to(equals, RIGHT)

        # animate in
        self.play(AnimationGroup(
            Create(x3),
            Create(dot), 
            Create(a3), 
            lag_ratio=0.25))
        
        # move to the left
        self.play(AnimationGroup(Create(equals), Create(x_dot_a3), lag_ratio=0.1))
        cleanup = VGroup(dot, x3, a3, equals, x_dot_a3)
        self.play(cleanup.animate.scale(0.75))

        # rectangle
        rect3 = SurroundingRectangle(a3.get_rows()[4:5])
        a3.add(rect3)
        self.play(Create(rect3))

        # binary digits
        binary = Text("(1 0 0)_2").set_color(WHITE)
        equals = equals_o.copy() 
        
        binary.move_to((ORIGIN + UP*2.8))
        
        result = Text("4").set_color(WHITE)
        equals.next_to(binary, RIGHT)
        result.next_to(equals, RIGHT)

        group4 = VGroup(binary, equals, result)
        group4.scale(0.75)
        
        self.play(
            AnimationGroup(Write(binary),
                             Write(equals), 
                             Write(result),
                             lag_ratio=0.25))
        
        index = SurroundingRectangle(x1.get_rows()[4:5], color=BLUE)
        x1.add(index)
        self.play(Create(index))
        
        self.wait(2)


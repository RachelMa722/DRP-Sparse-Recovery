from manim import *
import random

class KSparse(Scene):
    def construct(self):
        num_bits = 8
        bit_box_width = 0.5
        box_height = 0.75
        full_width = num_bits * bit_box_width

        def make_bits(box, bit_vals):
            bits = VGroup()
            for i in range(num_bits):
                bit_val = Text(str(bit_vals[i]), font_size=24)
                # Position the binary number in the center of the grid
                bit_val.move_to(box.get_center() + np.array([(i - num_bits / 2 + 0.5) * bit_box_width, 0, 0]))
                bits.add(bit_val)
            return bits

        def make_vector(text,bit_vals): 
            vector = VGroup()
            box = Rectangle(width=full_width, height=box_height, color=WHITE)
            text = Text(text, font_size=32)
            text.next_to(box, LEFT)
            bits = make_bits(box, bit_vals)
            vector.add(box, text, bits)
            return vector
        
        x = make_vector("x", (0, 1, 0, 1, 0, 1, 0, 1))
        y = make_vector("y", (0, 1, 1, 1, 0, 1, 0, 1))
        y.next_to(x, DOWN)
        self.play(x.animate.shift(UP), y.animate.shift(UP))

        r = make_vector("r", (0, 0, 1, 1, 1, 0, 0, 1))
        r.next_to(y, DOWN, 0.8)
        self.add(r)
    
        ## ## Surrounding Box ## ##
        bit_positions = [x[2][2].get_center(),
                         y[2][2].get_center(),
                         r[2][2].get_center()]

        top_left = bit_positions[0] + np.array([-0.5, 0.5, 0])
        bottom_right = bit_positions[-1] + np.array([0.5, -0.5, 0])
        width = bottom_right[0] - top_left[0] - 0.2
        height = top_left[1] - bottom_right[1]

        surrounding_box = Rectangle(width=width, height=height, color=YELLOW)
        surrounding_box.move_to(np.array([(top_left[0] + bottom_right[0]) / 2, 
                                          (top_left[1] + bottom_right[1]) / 2, 0]))

        i = Text("i", font_size=32, color=YELLOW)
        i.next_to(surrounding_box, UP)
        self.play(Create(i), Create(surrounding_box))

        self.pause(duration=4.0)

        vectors = VGroup()
        vectors.add(x, y, r, surrounding_box, i)

        ref_v = VGroup()
        ref_v = vectors.copy()

        self.play(vectors.animate.shift(LEFT*3))
        self.play(vectors.animate.scale(0.8))

        ## ## Case 1 ## ##
        case1 = VGroup()
        case1v = VGroup()
        case1text = Tex(r"Case 1: $ \langle r_{-i},x_{-i} \rangle= \langle r_{-i},y_{-i} \rangle$", font_size=42)
        
        case1v = ref_v.copy()
        case1v.remove(case1v[2])

        case1r = make_vector("r", ("1", "0", "?", "1", "1", "0", "1", "0"))
        case1r.next_to(case1v[1], DOWN, 0.8)

        case1v.add(case1r)
        case1v.next_to(case1text, DOWN)
    
        case1.add(case1text, case1v) 
        case1.next_to(vectors, RIGHT)

        self.play(case1.animate.shift(RIGHT))
        self.pause(duration=4.0)

        self.play(case1.animate.shift(UP), case1.animate.scale(0.8))
        case1text2=Tex(r"$r_i=1 \hspace{0.1cm}\Rightarrow\hspace{0.1cm} \langle r, x\rangle \neq \langle r,y \rangle $", font_size=42, color=RED)
        case1text2.next_to(case1, DOWN)
        case1.add(case1text2)
        self.play(Create(case1text2))
        self.pause(duration=4.0)

        self.play(Uncreate(case1))
        self.pause(duration=2.0)

        ## ## Case 2 ## ##
        case2 = VGroup()
        case2v = VGroup()
        case2text = Tex(r"Case 2: $ \langle r_{-i},x_{-i} \rangle\neq\langle r_{-i},y_{-i} \rangle$", font_size=42)
        
        case2v = ref_v.copy()

        case2v.remove(case2v[2])
        case2r = make_vector("r", ("1", "0", "?", "1", "1", "0", "1", "0"))
        case2r.next_to(case2v[1], DOWN, 0.8)

        case2v.remove(case2v[1])
        case2y = make_vector("y",(0, 1, 1, 0, 0, 1, 1, 1))
        case2y.next_to(case2v[0], DOWN)

        case2v.add(case2r, case2y)
        case2v.next_to(case2text, DOWN)
    
        case2.add(case2text, case2v) 
        case2.next_to(vectors, RIGHT)

        self.play(case2.animate.shift(RIGHT))
        self.pause(duration=4.0)

        self.play(case2.animate.shift(UP), case2.animate.scale(0.8))
        case2text2=Tex(r"$r_i=0 \hspace{0.1cm}\Rightarrow\hspace{0.1cm} \langle r, x\rangle \neq \langle r,y \rangle $", font_size=42, color=RED)
        case2text2.next_to(case2, DOWN)
        case2.add(case2text2)
        self.play(Create(case2text2))
        self.pause(duration=4.0)
        self.play(Uncreate(case2))

        self.pause(duration=2.0)
        self.play(vectors.animate.scale(1.2))
        pr_text = Tex(r"Pr$_r(\langle r,x\rangle=\langle r,y\rangle)=\frac{1}{2}$", font_size=46, color=RED)
        pr_text.next_to(vectors, RIGHT, 0.5)
        self.play(Create(pr_text))
        self.pause(duration=2.0)


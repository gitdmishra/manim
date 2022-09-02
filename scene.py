from manim import *

class HowFar(Scene):

    def construct(self):

        intro_words = Text(""" How far is 10 from 8""")

        num_line = NumberLine(x_range=[0,12,1],
                color = BLUE,
                length =10,
                include_numbers = True,
                label_direction = UP
            )
        intro_words.to_edge(UP*2)
        self.play(Write(intro_words))
        self.play(Create(num_line))



class SumOne(Scene):
    def construct(self):
        self.WAIT_TIME = 3
        intro_words = Text(""" 
            When we add 1 to a number, we go forward 1 step

        """, color = ORANGE)
        intro_words.to_edge(UP)

        self.play(Write(intro_words))
        self.wait(self.WAIT_TIME)

        self.addOne(2)
        self.addOne(6)
        self.addOne(12)
        self.addOne(111)


    def addOne(self, num):

        # ##########################

        example = Text(f'What is {num} + 1 = ?',
        font="sans-serif",
        font_size = 40

        )
        example.to_edge(UP*3)

        text1 = Text(f'Start from {num} and take 1 step forward',
                font_size = 40)

        text1.next_to(example, DOWN*4)

        # low, high = 0, 10
        # if num>10:
        #     low, high = 10, 20

        low = (num//10)*10
        high = low +10

        numLine = NumberLine(
            x_range=[low, high, 1],
            length=10,
            color=BLUE,
            include_numbers=True,
            label_direction=UP,
            )

        numLine.next_to(text1, DOWN*6)


        arc_between_8_9 = ArcBetweenPoints(
                start=numLine.number_to_point(num), 
                end = numLine.number_to_point(num+1),
                stroke_color = ORANGE)

        ans_circle = Circle(radius=0.2)
        ans_circle.move_to(numLine.number_to_point(num+1))

        ans = Text(f'{num} + 1 = {num + 1}')

        ans.next_to(numLine, DOWN*4)

        self.play(Write(example))
        self.wait(self.WAIT_TIME)
        self.play(Write(text1))
        self.wait(self.WAIT_TIME)
        self.play(Create(numLine))

        # self.add(dot, arc)
    
        # self.play(MoveAlongPath(dot, arc), rate_func=linear)

        self.play(Create(arc_between_8_9))
        self.wait(self.WAIT_TIME)
        self.play(Create(ans_circle))
        self.wait(self.WAIT_TIME)
        self.play(Write(ans))
        self.wait(self.WAIT_TIME)
        self.clear()


class MoreAndLess(Scene):

    num_line = NumberLine(
                x_range = [0,10,1],
                length = 10,
                color = BLUE,
                include_numbers = True,
                label_direction =UP
            )

    def construct(self):

        intro_words = Text(""" 

                        As we move along the number line, numbers get bigger and bigger

                    """, font_size = 28)
        intro_words.to_edge(UP*2)
        self.play(Write(intro_words))

        self.num_line.to_edge(DOWN)
        self.play(Create(self.num_line))

        for i in range(10):
            dots = self.nDots(i+1)
            dots.next_to(self.num_line.number_to_point(i+1), UP*3)
            self.play(Create(dots))
            # self.wait(1.5)
        # question1 = Text("Which number is bigger, 8 or 6?", font_size=24).next_to(intro_words, DOWN)    
        # self.play(Write(question1))
        # question2 = Text("Which is the biggest number?", font_size=24).next_to(question1, DOWN)
        # self.play(Write(question2)) 

        ##### Moving to next animation  #####

        self.clear()

        
        self.displayGreaterNumberScene(8, 4)

        self.displayGreaterNumberScene(10, 7)




    def nDots(self, n):

        

        dot = Dot(color=ORANGE)

        dot_group = VGroup()
        dot_group.add(*[Dot(color=ORANGE) for _ in range(n)])
        dot_group.arrange_in_grid(n, buff=0.1)
        
        return dot_group

    def sceneGreaterNumber(self, x, y):

        # group_x = VGroup()
        x_dots = self.nDots(x)
        x_text = Text(f'{x}').next_to(x_dots, UP)
        # group_x.add([x_dots, x_text])
        group_x = VGroup(x_dots, x_text)
        group_x.to_edge(LEFT*10)

        # group_y = VGroup()
        y_dots = self.nDots(y)
        y_text = Text(f'{y}').next_to(y_dots, UP)
        # group_y.add([y_dots, y_text])
        group_y = VGroup(y_dots, y_text)


        group_y.next_to(group_x, RIGHT*10)

        group = VGroup(group_x, group_y)
        # group.add([group_x, group_y])

        return group

    def displayGreaterNumberScene(self, x, y):

        self.play(Write(Text("Which number is bigger?", font_size=24).to_edge(UP)))

        group = self.sceneGreaterNumber(x, y)
        # self.wait(2)
        self.play(Create(group))
        self.wait(2)
        self.play(Wiggle(group[0]))
        self.play(Write(Text(">", font_size = 60).next_to(group[0], RIGHT*4)))
        self.play(Write(Text(f'We read it as "{x} is greater than {y}"', font_size = 24).to_edge(DOWN*4)))    
        self.clear()
        self.wait(2)

class MatrixGetColumnsExample(Scene):
    
    def construct(self):
        # temp = Matrix([[3,2]])
        m0 = Matrix([[0,0,"..",0,1,0,"..",0]], h_buff=0.5)
        m0.move_to(RIGHT * 4)
        m0.shift(UP*2)
        m0.add(SurroundingRectangle(m0.get_columns()[4]))

        m1 = Matrix([[0,0,"..",1,"..",0,"..",0]], h_buff=0.5)
        m1.next_to(m0, DOWN)
        m1.add(SurroundingRectangle(m1.get_columns()[3]))

        m2 = Matrix([[0,0,"..",0,"..",0,1,0]], h_buff=0.5)
        m2.next_to(m1, DOWN)
        m2.add(SurroundingRectangle(m2.get_columns()[6]))

        m3 = Matrix([[0,1,"..",0,"..",0,"..",0]], h_buff=0.5)
        m3.next_to(m2, DOWN)
        m3.add(SurroundingRectangle(m3.get_columns()[1]))
        text_list = "Deep learning solves this central problem in representation learning by introducing representations that are expressed in terms of other, simpler representations".split()

        g = VGroup()
        for i in text_list:
            
            g.add(Text(i, font_size=12, color='ORANGE', font = 'sans-serif')).arrange(buff=0.1)
        
        self.add(g.to_edge(DOWN))

        # text = Text(" ".join(text_list), font_size = 24).scale(0.6)
        # text.to_edge(LEFT)

        # ####### COMMENT START   #############

        # # moving_rec = Rectangle(height=1, width = 4.5, color='ORANGE').scale(0.5).to_edge(LEFT)
        # X_words = VGroup()
        
        # for i in range(len(text_list) - 3):
        #     grp_3 = VGroup(g[i], g[i+1], g[i+2])
            
        #     X_words.add(grp_3) 
        #     surronding_rect = SurroundingRectangle(grp_3, color='WHITE', corner_radius=0.05)
        #     self.add(surronding_rect)

        #     # self.add(grp_3.copy().to_edge((UP*(i+1)/2) + LEFT*2))

        #     grp_copy = grp_3.copy()
        #     grp_copy.generate_target()
        #     grp_copy.target.to_edge((UP*(i+1)/2) + LEFT*2)
        #     # self.add(g[i+3].copy().to_edge((UP*(i+1)/2) + LEFT*10))

        #     y_target = g[i+3].copy()
        #     y_target.generate_target()
        #     y_target.target.to_edge((UP*(i+1)/2) + LEFT*10)

        #     self.play(MoveToTarget(grp_copy))
        #     self.play(MoveToTarget(y_target))
        #     self.wait(1)
        #     self.remove(surronding_rect)

        #######  COMMENT END   ###############
        ###### Creating Brace and Text for X and Y matrix

        # self.play(Create(Brace(X_words[-1])))
        line = Line().to_edge(LEFT*2 + DOWN*6)
        brace_left = Brace(line)
        brace_right = brace_left.copy().shift(RIGHT*4)
        self.play(Create(brace_left))    
        self.play(Create(Text("X", font_size=24).next_to(brace_left, DOWN)))
        self.play(Create(brace_right))
        self.play(Create(Text("Y", font_size=24).next_to(brace_right, DOWN)))

        
        # Create X Matrix
        X_text = []
        for i in range(len(text_list)-2):
            X_text.append(["   ".join(text_list[i:i+3])])

        m = Matrix(X_text, h_buff=2).scale(0.3)
        self.play(Create(m))
        # self.add(grp_3)
        # l = Line(start=[- 6, 0., 0.], end=[6, 0., 0.])
        # poly = Polygon([4, 1, 0],[4, -2.5, 0], color= 'PURPLE')
        # self.add(m0, m1, m2, m3)
        # self.add(m1)
        # self.add(text, moving_rec)
        # self.play(MoveAlongPath(moving_rec, l))
        # for _ in range(10):
        #     self.play(moving_rec.animate.shift(RIGHT*0.6))
        #     self.wait(1)
        # init_text = Text("Deep", font_size = 24).to_edge(LEFT)
        # groupText = VGroup(init_text, Text("learning", font_size = 24).next_to(init_text,RIGHT))
        # self.add(groupText)

        # self.play(Transform(text, m0))

        # m0_t = Matrix([[0,0,"..",0,1,0,"..",0]], h_buff=0.5, v_buff=0.2)
        # m0_t.move_to(RIGHT * 4)
        # m0_t.shift(UP*2)
        # m0_t.add(SurroundingRectangle(m0_t.get_columns()[4]))
        # self.add(m0_t)



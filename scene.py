from manim import *

class ZoomNumberLine(Scene):

    def construct(self):
        temp_num_line1 = NumberLine(x_range=[0, 20, 1],
                                   color=BLUE,
                                   length=12,
                                   include_numbers=True,
                                   label_direction=UP,
                                   font_size = 15,
                                   ).shift(UP)


        num5 = temp_num_line1.numbers[5]
        num5.set_color(ORANGE)
        num5.set_font_size(30)

        num15 = temp_num_line1.numbers[15]
        num15.set_color(ORANGE)
        num15.set_font_size(30)

        br = Brace(VGroup(num5, num15), sharpness=1, color=ORANGE)
        text_far = Text("Far", font_size=20, color=BLUE).next_to(br, DOWN)
        # arrow_1 = Arrow(start=num5, end=num15, color=GOLD, stroke_width=2).shift(DOWN)
        self.play(Create(temp_num_line1))
        self.play(Wiggle(num5))
        self.play(Wiggle(num15))
        self.play(Create(br))
        self.play(Create(text_far))

        temp_num_line2 = NumberLine(x_range=[0, 20, 1],
                                    color=BLUE,
                                    length=12,
                                    include_numbers=True,
                                    label_direction=UP,
                                    font_size=15,
                                    ).shift(DOWN)

        num5 = temp_num_line2.numbers[5]
        num5.set_color(ORANGE)
        num5.set_font_size(30)

        num7 = temp_num_line2.numbers[7]
        num7.set_color(ORANGE)
        num7.set_font_size(30)

        br = Brace(VGroup(num5, num7), sharpness=1, color=ORANGE)
        text_close = Text("Close", font_size=20, color=BLUE).next_to(br,DOWN)
        # arrow_1 = Arrow(start=num5, end=num15, color=GOLD, stroke_width=2).shift(DOWN)
        self.play(Create(temp_num_line2))
        self.play(Wiggle(num5))
        self.play(Wiggle(num7))
        self.play(Create(br))
        self.play(Create(text_close))

class HowFarPractice(Scene):


    def construct(self):
        FONT_SIZE_TITLE = 40
        FONT_SIZE_TEXT = 30
        from_num = 3
        to_num = 8



        # intro_words = Text(f'How far is {to_num} from {from_num}?', font_size=FONT_SIZE_TITLE)
        intro_words = Tex("How far is ",f'{to_num}'," from ",f'{from_num}',"?", font_size=FONT_SIZE_TITLE)
        intro_words.set_color_by_tex_to_color_map({
                f'{to_num}': BLUE,
                f'{from_num}': ORANGE,
                # "C": GREEN,
            })
        num_line = NumberLine(x_range=[0,12,1],
                color = BLUE,
                length =10,
                include_numbers = True,
                label_direction = UP
            ).to_edge(DOWN*2)
        intro_words.to_edge(UP*2)
        # text_step = Tex("Three Steps: ", "Step 1", "--", "Step 2", "--", "Step 3", font_size=FONT_SIZE_TEXT)
        # text_step.set_color_by_tex_to_color_map({
        #     "-->": ORANGE,
        #     "Step 1": BLUE,
        #     "Step 2": BLUE,
        #     "Step 3": BLUE,
        #     # "C": GREEN,
        # })
        # text_step.next_to(intro_words, DOWN*2)
        # text_locate_1 = Tex("Step 1: Locate ",f'{from_num}'," in number line", font_size = FONT_SIZE_TEXT).next_to(text_step, DOWN*2)
        # text_locate_1.set_color_by_tex_to_color_map({
        #     f'{from_num}': ORANGE,
        #
        # })

        self.wait(2)

        self.play(Write(intro_words))
        self.play(Wiggle(intro_words[1]))
        self.play(Wiggle(intro_words[3]))

        # self.play(Create(text_step))
        # self.wait(1)

        self.play(Create(num_line))

        # self.play(Create(text_locate_1))
        # self.play(Wiggle(text_locate_1[1]))
        self.wait(8)

        from_circle = Circle(radius=0.15)
        from_circle.move_to(num_line.number_to_point(from_num))
        self.play(Create(from_circle))

        # text_locate_2 = Tex("Step 2: Locate ",f'{to_num}'," in number line", font_size=FONT_SIZE_TEXT).next_to(text_locate_1,
        #                                                                                             DOWN * 1)
        # text_locate_2.set_color_by_tex_to_color_map({
        #     f'{to_num}': BLUE,
        #     # "C": GREEN,
        # })
        self.wait(4)
        # self.play(Create(text_locate_2))
        # self.play(Wiggle(text_locate_2[1]))
        to_circle = Circle(radius=0.15)
        to_circle.move_to(num_line.number_to_point(to_num))
        self.play(Create(to_circle))
        self.wait(4)

        # text_step_3 = Tex("Step 3: Start from ",f'{from_num}'," and go one step at a time till you reach ",f'{to_num}'," in number line", font_size=FONT_SIZE_TEXT).next_to(text_locate_1,
        #                                                                                           DOWN * 1).next_to(text_locate_2, DOWN)
        # text_step_3.set_color_by_tex_to_color_map({
        #     f'{to_num}': BLUE,
        #     f'{from_num}': ORANGE,
        #     # "C": GREEN,
        # })
        # self.play(Create(text_step_3))
        # self.play(Wiggle(text_step_3[1]))
        # self.play(Wiggle(text_step_3[3]))
        # self.wait(2)
        i = 1
        for num in range(from_num, to_num):

            arc_between_points = ArcBetweenPoints(
                start=num_line.number_to_point(num),
                end=num_line.number_to_point(num + 1),
                stroke_color=ORANGE)

            self.play(Create(arc_between_points))
            self.play(Create(Text(f'{i}', font_size=15).next_to(arc_between_points, DOWN)))
            i +=1
        answer = Tex("Answer is ", f'{i-1}', font_size=FONT_SIZE_TEXT).next_to(intro_words, DOWN*2)
        ans_copy = answer[1].copy()
        ans_copy.generate_target()
        ans_copy.target.next_to(intro_words, RIGHT)

        self.play(Create(answer))
        self.play(MoveToTarget(ans_copy))
        # self.play(FadeAway(answer[0]))
        # self.play(Create(Tex(f'{i-1}', font_size=FONT_SIZE_TITLE).next_to(intro_words, RIGHT)))

class HowFar(Scene):

    def construct(self):
        FONT_SIZE_TITLE = 40
        FONT_SIZE_TEXT = 30
        from_num = 8
        to_num = 10

        # intro_words = Text(f'How far is {to_num} from {from_num}?', font_size=FONT_SIZE_TITLE)
        intro_words = Tex("How far is ", f'{to_num}', " from ", f'{from_num}', "?", font_size=FONT_SIZE_TITLE)
        intro_words.set_color_by_tex_to_color_map({
            f'{to_num}': BLUE,
            f'{from_num}': ORANGE,
            # "C": GREEN,
        })
        num_line = NumberLine(x_range=[0, 12, 1],
                              color=BLUE,
                              length=10,
                              include_numbers=True,
                              label_direction=UP
                              ).to_edge(DOWN * 2)
        intro_words.to_edge(UP * 2)
        text_step = Tex("Three Steps: ", "Step 1", "--", "Step 2", "--", "Step 3", font_size=FONT_SIZE_TEXT)
        text_step.set_color_by_tex_to_color_map({
            "-->": ORANGE,
            "Step 1": BLUE,
            "Step 2": BLUE,
            "Step 3": BLUE,
            # "C": GREEN,
        })
        text_step.next_to(intro_words, DOWN * 2)
        text_locate_1 = Tex("Step 1: Locate ", f'{from_num}', " in number line",
                            font_size=FONT_SIZE_TEXT).next_to(text_step, DOWN * 2)
        text_locate_1.set_color_by_tex_to_color_map({
            f'{from_num}': ORANGE,

        })

        self.wait(2)

        self.play(Write(intro_words))
        self.play(Wiggle(intro_words[1]))
        self.play(Wiggle(intro_words[3]))

        self.play(Create(text_step))
        self.wait(1)

        self.play(Create(num_line))

        self.play(Create(text_locate_1))
        self.play(Wiggle(text_locate_1[1]))
        self.wait(2)

        from_circle = Circle(radius=0.15)
        from_circle.move_to(num_line.number_to_point(from_num))
        self.play(Create(from_circle))

        text_locate_2 = Tex("Step 2: Locate ", f'{to_num}', " in number line",
                            font_size=FONT_SIZE_TEXT).next_to(text_locate_1,
                                                              DOWN * 1)
        text_locate_2.set_color_by_tex_to_color_map({
            f'{to_num}': BLUE,
            # "C": GREEN,
        })
        self.wait(2)
        self.play(Create(text_locate_2))
        self.play(Wiggle(text_locate_2[1]))
        to_circle = Circle(radius=0.15)
        to_circle.move_to(num_line.number_to_point(to_num))
        self.play(Create(to_circle))
        self.wait(2)

        text_step_3 = Tex("Step 3: Start from ", f'{from_num}', " and go one step at a time till you reach ",
                          f'{to_num}', " in number line", font_size=FONT_SIZE_TEXT).next_to(text_locate_1,
                                                                                            DOWN * 1).next_to(
            text_locate_2, DOWN)
        text_step_3.set_color_by_tex_to_color_map({
            f'{to_num}': BLUE,
            f'{from_num}': ORANGE,
            # "C": GREEN,
        })
        self.play(Create(text_step_3))
        self.play(Wiggle(text_step_3[1]))
        self.play(Wiggle(text_step_3[3]))
        self.wait(2)
        i = 1
        for num in range(from_num, to_num):
            arc_between_points = ArcBetweenPoints(
                start=num_line.number_to_point(num),
                end=num_line.number_to_point(num + 1),
                stroke_color=ORANGE)

            self.play(Create(arc_between_points))
            self.play(Create(Text(f'{i}', font_size=15).next_to(arc_between_points, DOWN)))
            i += 1
        answer = Tex("Answer is ", f'{i - 1}', font_size=FONT_SIZE_TEXT).next_to(text_step_3, DOWN * 2)
        ans_copy = answer[1].copy()
        ans_copy.generate_target()
        ans_copy.target.next_to(intro_words, RIGHT)

        self.play(Create(answer))
        self.play(MoveToTarget(ans_copy))
        # self.play(FadeAway(answer[0]))
        # self.play(Create(Tex(f'{i-1}', font_size=FONT_SIZE_TITLE).next_to(intro_words, RIGHT)))

class SumOne(Scene):
    def construct(self):
        self.WAIT_TIME = 3
        to_num = 5
        add_num = 1
        FONT_SIZE_TITLE = 40
        # FONT_SIZE_TEXT = 30

        intro_words = Tex("What do we get when we add ", f'{add_num}'," to ", f'{to_num}', font_size=FONT_SIZE_TITLE)
        intro_words.set_color_by_tex_to_color_map({
            f'{to_num}': BLUE,
            f'{add_num}': ORANGE,
            # "C": GREEN,
        })

        intro_words.to_edge(UP*2)

        self.play(Write(intro_words))
        self.wait(self.WAIT_TIME)


        self.addOne(5)
        self.addOne(8)
        self.addOne(12)
        self.addOne(111)


    def addOne(self, num):

        # ##########################
        FONT_SIZE_TEXT = 30
        add_num = 1
        example = Tex("What is ",f'{num}'," + ",f'{add_num}', " = ?", font_size = FONT_SIZE_TEXT)
        example.set_color_by_tex_to_color_map({
            f'{num}': BLUE,
            f'{add_num}': ORANGE,
            # "C": GREEN,
        })
        example.to_edge(UP*4)

        step1 = Tex("Step 1: Start from ", f'{num}', font_size=FONT_SIZE_TEXT).next_to(example, DOWN*2)
        step1.set_color_by_tex_to_color_map({
            f'{num}': BLUE,
            # "C": GREEN,
        })

        step2 = Tex("Step 2: Take ", f'{add_num}', " step", font_size=FONT_SIZE_TEXT).next_to(step1, DOWN)
        step2.set_color_by_tex_to_color_map({
            f'{add_num}': ORANGE,
            # "C": GREEN,
        })


        # text1 = Text(f'Start from {num} and take 1 step forward',
        #         font_size = FONT_SIZE_TEXT)
        #
        # text1.next_to(example, DOWN*4)

        # low, high = 0, 10
        # if num>10:
        #     low, high = 10, 20

        low = (num//10)*10
        high = low +10

        numLine = NumberLine(
            x_range=[low, high, 1],
            length=12,
            color=BLUE,
            include_numbers=True,
            label_direction=UP,
            font_size = 20
            )

        numLine.shift(DOWN)
        from_num = numLine.number_to_point(num)
        from_circle = Circle(radius=0.15)
        from_circle.move_to(from_num)


        arc_between_8_9 = ArcBetweenPoints(
                start=numLine.number_to_point(num), 
                end = numLine.number_to_point(num+1),
                stroke_color = ORANGE)

        ans_circle = Circle(radius=0.15)
        ans_circle.move_to(numLine.number_to_point(num+1))

        ans = Text(f'{num} + 1 = {num + 1}', font_size = FONT_SIZE_TEXT)

        ans.next_to(numLine, DOWN*2)

        self.play(Write(example))
        self.wait(self.WAIT_TIME)
        self.play(Create(step1))
        self.wait(self.WAIT_TIME)
        self.play(Create(step2))
        self.wait(self.WAIT_TIME)
        # self.play(Write(text1))
        # self.wait(self.WAIT_TIME)
        self.play(Create(numLine))
        # self.play(Wiggle(from_num))
        self.play(Create(from_circle))
        # self.add(dot, arc)
    
        # self.play(MoveAlongPath(dot, arc), rate_func=linear)

        self.play(Create(arc_between_8_9))
        self.wait(self.WAIT_TIME)
        self.play(Create(Text("+1", font_size=15).next_to(arc_between_8_9, DOWN)))
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

        self.displayGreaterNumberScene(7, 2)




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
        # self.clear()
        self.wait(2)
        self.clear()
        self.wait(1)

class TenCompliment(Scene):
    def construct(self):
        rainbow_txt = Text("Rainbow Numbers", font_size = 40, color = ORANGE)
        # intro_words = Text("Ten's complement", font_size = 40)
        intro_words = Text("Ten's complement mean numbers which add up to 10", font_size=30)
        rainbow_txt.to_edge(UP)
        intro_words.to_edge(UP*3)
        numLine = NumberLine(
            x_range=[0, 10, 1],
            length=10,
            color=BLUE,
            include_numbers=True,
            label_direction=UP,
            )

        numLine.next_to(intro_words, DOWN*10)
        self.add(rainbow_txt)
        self.play(Write(intro_words))
        self.play(Create(numLine))


        color = [ORANGE, BLUE, GREEN, RED, YELLOW]
        for num in range(5):
            arc_between_0_10 = ArcBetweenPoints(
                    start=numLine.number_to_point(10-num),
                    end = numLine.number_to_point(num),
                    stroke_color = color[num])
            self.play(Create(arc_between_0_10))
            self.wait(1)

        # self.play(Write(intro_words))
        # self.play(Create(num_line))
        left_text = MathTex(r'0 + 10 &= 10\\ 1 + 9 &= 10 \\ 2 + 8 &= 10 \\ 3 + 7 &= 10 \\ 4 + 6 &= 10', font_size=30)
        center_text = MathTex(r'5 + 5 &= 10', font_size=30)
        right_text = MathTex(r'6 + 4 &= 10\\ 7 + 3 &= 10 \\ 8 + 2 &= 10 \\ 9 + 1 &= 10 \\ 10 + 0 &= 10', font_size=30)
        self.play(Create(left_text.next_to(numLine, DOWN).to_edge(LEFT*4)))
        self.play(Create(center_text.next_to(numLine, DOWN)))
        self.play(Create(right_text.next_to(numLine, DOWN).to_edge(RIGHT*4)))

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


class NumPlaces(Scene):

    def construct(self):

        ####### SCENE 1 #########

        self.play(Write(Text("Title: Five Family", font_size = 70, color = BLUE)))
        self.wait(2)
        self.clear()
        
        ###### STORY PART #######
        # story_txt_1 = Text("Once upon a time there was a boy.", font_size = 25, color = ORANGE)
        # story_txt_2 = Text("On his first day of school, his teacher asked him his name.", font_size = 25, color = ORANGE)
        # story_txt_3 = Text("'My name is Twenty Five.' He said.",font_size = 25, color = ORANGE)
        # story_txt_4 = Text("'That's an excellent name', Teacher said.",font_size = 25, color = ORANGE)
        # story_txt_5 = Text("Yes, everybody says so. My First name is Twenty and Last name is Five.",font_size = 25, color = ORANGE)
        # story_txt_6 = Text("My Dad's name is Thirty Five and Grand Dad's name is Forty Five. We are from Five Family.",font_size = 25, color = ORANGE)

        # self.add(story_txt_1, story_txt_2, story_txt_3, story_txt_4, story_txt_5, story_txt_6)

        # for i,mobj in enumerate(self.mobjects):
        #     mobj.shift(DOWN*(i-3))


        # self.wait(10)
        # self.clear()

        ####### SCENE 2 #########
        f_name_dad = "3"
        f_name_boy = "2"
        f_name_grand_dad = "4"
        l_name = '5'

        f_name_dad_txt = Text("3", font_size = 30, color=BLUE)
        f_name_boy_txt = Text("2", font_size = 30, color=BLUE)
        f_name_grand_dad_txt = Text("4", font_size = 30, color=BLUE)
        l_name_txt = Text('5',font_size = 30, color=BLUE)

        self.add(Text("Five Family").shift(UP*3))
        self.add(Text("On Number Line", font_size=30, color=ORANGE).shift(UP*2))

        boy_group = VGroup()
        boy_group.add(f_name_boy_txt, l_name_txt.next_to(f_name_boy_txt, RIGHT*0.2),Text("Boy",font_size = 20, color=ORANGE).next_to(f_name_boy_txt, DOWN).shift(RIGHT*.15), ).shift(LEFT*4)

        self.play(Create(boy_group))


        dad_group = VGroup()
        dad_group.add(f_name_dad_txt, Text('5',font_size = 30, color=BLUE).next_to(f_name_dad_txt, RIGHT*0.2),Text("Dad",font_size = 20, color=ORANGE).next_to(f_name_dad_txt, DOWN).shift(RIGHT*.15), )

        self.play(Create(dad_group))

        grand_dad_group = VGroup()
        grand_dad_group.add(f_name_grand_dad_txt, Text('5',font_size = 30, color=BLUE).next_to(f_name_grand_dad_txt, RIGHT*0.2),Text("Grand Dad",font_size = 20, color=ORANGE).next_to(f_name_grand_dad_txt, DOWN).shift(RIGHT*.15), )
        grand_dad_group.shift(RIGHT*4)
        self.play(Create(grand_dad_group))

        family_group = VGroup()
        family_group.add(boy_group, dad_group, grand_dad_group)


        self.play(family_group.animate.shift(UP))

        numLine = NumberLine(
            x_range=[20, 50, 5],
            length=12,
            color=BLUE,
            include_numbers=True,
            label_direction=DOWN,
            )
        

        self.add(numLine)

        twenty = Text("Twenty", font_size = 20, color = ORANGE)
        five = Text("Five", font_size = 20, color = BLUE).next_to(twenty, RIGHT*.5).shift(UP*0.03)
        twenty_five = VGroup()
        twenty_five.add(twenty, five).next_to(numLine.number_to_point(25), DOWN*4)

        self.play(boy_group.animate.next_to(numLine.number_to_point(25), UP))
        self.play(Create(twenty_five))

        thirty = Text("Thirty", font_size = 20, color = ORANGE)
        five = Text("Five", font_size = 20, color = BLUE).next_to(thirty, RIGHT*.5).shift(UP*0.03)
        thirty_five = VGroup()
        thirty_five.add(thirty, five).next_to(numLine.number_to_point(35), DOWN*4)

        self.play(dad_group.animate.next_to(numLine.number_to_point(35), UP))
        self.play(Create(thirty_five))

        fourty = Text("Fourty", font_size = 20, color = ORANGE)
        five = Text("Five", font_size = 20, color = BLUE).next_to(fourty, RIGHT*.5).shift(UP*0.03)
        fourty_five = VGroup()
        fourty_five.add(fourty, five).next_to(numLine.number_to_point(45), DOWN*4)

        self.play(grand_dad_group.animate.next_to(numLine.number_to_point(45), UP))
        self.play(Create(fourty_five))


        # boy = Text("25", font_size = 30, color=BLUE).next_to(dad, LEFT)
        # grand_dad = Text("45", font_size = 30, color=BLUE).next_to(dad, RIGHT)


        # TEXT_FONT_SIZE = 30
        # NUM_FONT_SIZE = 100
        # num1 = "2"
        # num2 = "5"
        # num1_txt = Text(num1, font_size = NUM_FONT_SIZE)
        # num2_txt = Text(num2, font_size = NUM_FONT_SIZE).shift(RIGHT*0.8)
        # self.add(num1_txt)
        # self.add(num2_txt)
        # self.play(num1_txt.animate.shift(LEFT), num2_txt.animate.shift(RIGHT))

        # ten_place = Text("First Name", font_size =  TEXT_FONT_SIZE, color = ORANGE).next_to(num1_txt, DOWN)
        # self.play(Write(ten_place))

        # unit_place = Text("Last Name", font_size =  TEXT_FONT_SIZE, color = ORANGE).next_to(num2_txt, DOWN)
        # self.play(Write(unit_place))

        
        # self.play(Write(Text("Now it's your turn. Can you tell me what's your first and last name?", font_size = 40, color = BLUE).next_to(unit_place, DOWN)))

        self.wait(5)
        self.clear()

        ####### SCENE 3 #########

        self.scene3("2", "5")
        self.wait(5)
        self.clear()

        self.scene3("3", "5")

        self.wait(5)
        self.clear()

        self.scene3("4", "5")
        # TEXT_FONT_SIZE = 30
        # NUM_FONT_SIZE = 100
        # num1 = "2"
        # num2 = "5"
        # num1_txt = Text(num1, font_size = NUM_FONT_SIZE)
        # num2_txt = Text(num2, font_size = NUM_FONT_SIZE).shift(RIGHT*0.8)
        # self.add(num1_txt)
        # self.add(num2_txt)
        # self.play(num1_txt.animate.shift(LEFT), num2_txt.animate.shift(RIGHT))

        # l_name_txt = Text('Last Name',font_size =  TEXT_FONT_SIZE, color = ORANGE).next_to(num2_txt, UP)
        # self.add(l_name_txt)
        # unit_place = Text("unit place", font_size =  TEXT_FONT_SIZE, color = ORANGE).next_to(num2_txt, DOWN)
        # self.play(Write(unit_place))

        # f_name_txt = Text('First Name', font_size =  TEXT_FONT_SIZE, color = ORANGE).next_to(num1_txt, UP)
        # self.add(f_name_txt)
        # ten_place = Text("tenth place", font_size =  TEXT_FONT_SIZE, color = ORANGE).next_to(num1_txt, DOWN)
        # self.play(Write(ten_place))

        # ones = Text("1's", font_size =  TEXT_FONT_SIZE, color = ORANGE).next_to(unit_place, DOWN)
        # self.play(Write(ones))

        # tens = Text("10's", font_size =  TEXT_FONT_SIZE, color = ORANGE).next_to(ten_place, DOWN)
        # self.play(Write(tens))

        # vertical_line = DashedLine(start = [0, 1.5, 0], end = [0, -1.5, 0], color=BLUE).shift(RIGHT*0.4).shift(DOWN*0.2)
        # self.add(vertical_line)

        # group = VGroup()
        # group.add(l_name_txt, f_name_txt, num1_txt, num2_txt, unit_place, ten_place, ones, tens, vertical_line)
        # self.play(group.animate.shift(UP*2))

        # question_tens = Text("How many 10's we have in 25 ?", font_size = TEXT_FONT_SIZE, color =  BLUE).shift(DOWN)
        # self.play(Write(question_tens))
        # ans_tens = Text(num1, font_size = 30).next_to(question_tens, DOWN)
        # self.play(Write(ans_tens))

        # question_ones = Text("How many 1's we have in 25 ?", font_size = TEXT_FONT_SIZE, color =  BLUE).next_to(ans_tens, DOWN)
        # self.play(Write(question_ones))
        # ans_ones = Text(num2, font_size = 30).next_to(question_ones, DOWN)
        # self.play(Write(ans_ones))

    def scene3(self, fname, lname):

        TEXT_FONT_SIZE = 30
        NUM_FONT_SIZE = 100
        # num1 = fname
        # num2 = lname
        num1_txt = Text(fname, font_size = NUM_FONT_SIZE)
        num2_txt = Text(lname, font_size = NUM_FONT_SIZE).shift(RIGHT*0.8)
        self.add(num1_txt)
        self.add(num2_txt)
        self.play(num1_txt.animate.shift(LEFT), num2_txt.animate.shift(RIGHT))

        l_name_txt = Text('Last Name',font_size =  TEXT_FONT_SIZE, color = ORANGE).next_to(num2_txt, UP)
        self.add(l_name_txt)
        unit_place = Text("unit place", font_size =  TEXT_FONT_SIZE, color = ORANGE).next_to(num2_txt, DOWN)
        self.play(Write(unit_place))

        f_name_txt = Text('First Name', font_size =  TEXT_FONT_SIZE, color = ORANGE).next_to(num1_txt, UP)
        self.add(f_name_txt)
        ten_place = Text("tenth place", font_size =  TEXT_FONT_SIZE, color = ORANGE).next_to(num1_txt, DOWN)
        self.play(Write(ten_place))

        ones = Text("1's", font_size =  TEXT_FONT_SIZE, color = ORANGE).next_to(unit_place, DOWN)
        self.play(Write(ones))

        tens = Text("10's", font_size =  TEXT_FONT_SIZE, color = ORANGE).next_to(ten_place, DOWN)
        self.play(Write(tens))

        vertical_line = DashedLine(start = [0, 1.5, 0], end = [0, -1.5, 0], color=BLUE).shift(RIGHT*0.4).shift(DOWN*0.2)
        self.add(vertical_line)

        group = VGroup()
        group.add(l_name_txt, f_name_txt, num1_txt, num2_txt, unit_place, ten_place, ones, tens, vertical_line)
        self.play(group.animate.shift(UP*2))

        question_tens = Text(f"How many 10's we have in {fname}{lname} ?", font_size = TEXT_FONT_SIZE, color =  BLUE).shift(DOWN)
        self.play(Write(question_tens), run_time = 3)
        ans_tens = Text(fname, font_size = 50).next_to(question_tens, RIGHT*2)
        self.play(Write(ans_tens))

        question_ones = Text(f"How many 1's we have in {fname}{lname} ?", font_size = TEXT_FONT_SIZE, color =  BLUE).next_to(question_tens, DOWN*2)
        self.play(Write(question_ones),run_time = 3)
        ans_ones = Text(lname, font_size = 50).next_to(question_ones, RIGHT*2)
        self.play(Write(ans_ones))    

class newClass(Scene):
    def constructor(self):
        pass

















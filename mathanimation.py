from manim import *

class QuadraticGraph(Scene):
    def construct(self):
        # Create the axes
        axes = Axes(
            x_range=[-3, 3, 1],  # X-axis range with step size
            y_range=[0, 9, 2],   # Y-axis range with step size
            x_length=6,
            y_length=5,
            axis_config={"color": WHITE},  # Color of the axes
            tips=False                      # No arrows on axes tips
        )
        axes_labels = axes.get_axis_labels(x_label="x", y_label="y")

        # Define the quadratic function y = x^2
        quadratic_func = axes.plot(
            lambda x: x**2,  # The function to plot
            x_range=[-2, 2], # Range of the function
            color=BLUE       # Color of the graph
        )

        # Create dots at specific points on the graph
        dot1 = Dot(axes.c2p(-2, 4), color=RED)  # Point at (-2, 4)
        dot2 = Dot(axes.c2p(0, 0), color=GREEN) # Point at (0, 0)
        dot3 = Dot(axes.c2p(2, 4), color=RED)   # Point at (2, 4)

        # Add labels for the points
        label1 = MathTex("(-2, 4)").next_to(dot1, UP)
        label2 = MathTex("(0, 0)").next_to(dot2, DOWN)
        label3 = MathTex("(2, 4)").next_to(dot3, UP)

        # Add title
        title = Text("Graph of y = x^2", font_size=36).to_edge(UP)

        # Animations
        self.play(Write(title))                         # Display the title
        self.play(Create(axes), Write(axes_labels))     # Display the axes and labels
        self.play(Create(quadratic_func), run_time=2)   # Draw the quadratic function
        self.play(FadeIn(dot1), FadeIn(dot2), FadeIn(dot3))  # Show the points
        self.play(Write(label1), Write(label2), Write(label3)) # Add labels to the points
        self.wait(2)  # Pause to view the final result

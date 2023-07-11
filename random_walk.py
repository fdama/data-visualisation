from random import choice

from matplotlib.pyplot import step

class RandomWalk:
    """A class to generate random walks."""

    def __init__(self, num_points=5000):
        self.num_points = num_points

        # All walks start at (0, 0).
        self.x_vals = [0]
        self.y_vals = [0]
    
    def fill_walk(self):
        """Calculate all the points in the walk."""

        # Keep taking steps until the walk reaches the desired length.
        while len(self.x_vals) < self.num_points:
            x_step  = self.generate_steps()
            y_step = self.generate_steps()

            # Reject moves that go nowhere.
            if x_step == 0 and y_step == 0:
                continue

            # Calculate the new position.
            x = self.x_vals[-1] + x_step
            y = self.y_vals[-1] + y_step

            self.x_vals.append(x)
            self.y_vals.append(y)
        

    def generate_steps(self):
        direction = choice([1,-1])
        distance = choice([0,1,2,3,4])
        step = direction * distance
        return step
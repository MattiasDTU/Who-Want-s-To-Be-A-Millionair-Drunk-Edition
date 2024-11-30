class Box:
    """
    A class representing a rectangular box with a position, dimensions, and color.
    """
    def __init__(self, x: int, y: int, width: int, height: int, color: tuple[int, int, int] = (0, 0, 0)):
        """
        Initialize a Box object.

        :param x: The x-coordinate of the top-left corner of the box.
        :param y: The y-coordinate of the top-left corner of the box.
        :param width: The width of the box.
        :param height: The height of the box.
        :param color: The RGB color of the box as a tuple (default is black: (0, 0, 0)).
        """
        self.x = x
        self.y = y
        self.width = width
        self.height = height

        # Compute the x and y limits (boundaries of the box)
        self.x_lim = self.x + self.width
        self.y_lim = self.y + self.height

    def __repr__(self):
        """
        Return a string representation of the box object for easier debugging.
        """
        return (f"Box(x={self.x}, y={self.y}, width={self.width}, "
                f"height={self.height}, color={self.color})")

    def contains_point(self, point: tuple[int,int]) -> bool:
        """
        Check if a point (px, py) is inside the box.

        :param px: The x-coordinate of the point.
        :param py: The y-coordinate of the point.
        :return: True if the point is inside the box, False otherwise.
        """
        px = point[0]
        py = point[1]
        return self.x <= px <= self.x_lim and self.y <= py <= self.y_lim

    def cords(self) -> tuple[int,int,int,int]:
        """
        return the coordinates of the box
        """
        return (self.x,self.y, self.width, self.height)

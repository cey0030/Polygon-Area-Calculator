class Rectangle:
  def __init__(self, width, height):
      self.width = width
      self.height = height

  def set_width(self, width):
    self.width = width

  def set_height(self, height):
    self.height = height

  def get_area(self):
    return self.width * self.height
  
  def get_perimeter(self):
    return 2 * self.width + 2 * self.height

  def get_diagonal(self):
    return (self.width ** 2 + self.height ** 2) ** .5
  
  def get_picture(self):
    if self.height >= 50 or self.width >= 50:
      return 'Too big for picture.'
    string = ''
    for row in range(self.height):
      for column in range(self.width):
        string += '*'
      string += '\n'
    return string
  
  def get_amount_inside(self, shape_to_fit):
    return (self.height // shape_to_fit.height) * (self.width // shape_to_fit.width)

  def __str__(self):
    return 'Rectangle(width=' + str(self.width) + ', height=' + str(self.height) + ')'

class Square(Rectangle):
  def __init__(self, side_length):
    self.side_length = side_length
    super().__init__(side_length, side_length)

  def set_width(self, width):
    self.width = self.set_side(width)

  def set_height(self, height):
    self.height = self.set_side(height)

  def set_side(self, side_length):
    self.side_length = side_length
    self.width = side_length
    self.height = side_length
  
  def __str__(self):
    return 'Square(side=' + str(self.side_length) + ')'

from svg.drawing import Drawing
from svg.core import Rectangle, GroupedDrawable, write
from svg.path import Path, vector
from svg.point import Point

drawing = Drawing()
# Step 2: Create a Point instance
top_left = Point(0, 0)

# Step 3: Create a Rectangle instance
rectangle = Rectangle(width=200, height=100, fill='green')

# Step 4: Create a Path instance
start = Point(50, 50)
segment1 = vector(50, 0)
segment2 = vector(0, 50)
segment3 = vector(-50, 0)
path = Path(start, True, segment1, segment2, segment3, stroke='red', fill='white')

# Step 5: Create a GroupedDrawable instance
group = GroupedDrawable()
group.add(rectangle)
group.add(path)

# Step 6: Generate the SVG XML
drawing.add(group)

# Step 7: Write the SVG XML to a file
drawing_svg = drawing.svg()     
write(drawing_svg, 'output.svg')
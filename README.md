# Python SVG generator

This is a simple python package for generating svg documents.

It's evolved though use in four projects over the last ten years;
most recently I used it in [breadboarder](https://github.com/romilly/breadboarder)
which now depends on it as an external package.

I have separated it out as I now have other current projects which use it.

`svg is organized into several modules, each responsible for a specific part of the SVG creation process.

1. `svg.py`: This module defines several classes that represent different SVG elements, such as `Rectangle`, `Line`, `Text`, `Circle`, `Image`, and `Dimple`. Each of these classes inherits from either `SimpleItem` or `CompositeItem`, which in turn inherit from `Drawable`. `Drawable` is an abstract base class that requires its subclasses to implement an `element` method. This method is responsible for creating an XML element that represents the SVG element. The `CompositeItem` class is used for SVG elements that can contain other elements, like `GroupedDrawable`.

2. `path.py`: This module defines the `Path` class and several `PathSegment` subclasses. A `Path` is an SVG element that consists of one or more segments, which can be lines, arcs, etc. Each `PathSegment` subclass implements a `specification` method that returns a string representing the SVG path command for that segment.

3. `point.py`: This module defines the `Point` class, which represents a point in a 2D space. It provides methods for performing basic vector operations like addition, subtraction, and scaling.

4. `transform.py`: This module defines several classes that represent SVG transformations, like `Translation` and `Rotation`. These classes inherit from the `Transform` abstract base class, which requires its subclasses to implement `text`, `as_matrix`, and `transform` methods. The `text` method returns a string representing the SVG transform command, and the `transform` method applies the transformation to a `Point`.

The code also includes a `write` function in `svg.py` that writes a string to a file. This could be used to write the SVG XML to a file.

Overall, this code provides a way to create complex SVG graphics using Python code. The user can create instances of the various SVG element classes, set their properties, and then call their `element` methods to generate the SVG XML.
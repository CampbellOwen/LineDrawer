# LineDrawer
Recreate images with only lines

## Usage

`python path_to_reference_image path_to_output_image num_iterations`

The number of iterations is the number of lines tested on the image, not the total amount of lines in the output image.

## How it works
Every iteration, a random line with a random colour from the image's colour pallete will be drawn with Bresenham's Algorithm. 
This line's mean squared error in comparison to the original image is compared against the previous iteration's error. If the error
is smaller, the line is kept. Otherwise, the line is discarded.

## Examples
![Dog](https://raw.githubusercontent.com/CampbellOwen/LineDrawer/master/rusty.jpg)

![Ferret](https://raw.githubusercontent.com/CampbellOwen/LineDrawer/master/bandit1.jpg)

# Dimensions
## (a work in progress)
Dimensions is a command line tool written in Python that returns the names and dimensions of images in a directory. The default sort is alphabetical but an argument can be supplied by the user to sort the results by height, by width, or by area in pixels.

Requires Pillow:  
`pip install Pillow`


## Usage
--------
`$ python3 Dimensions.py [dir]`  
`Sort by height (H), width (W), or area (A)?`  

If the user just presses `return` rather than choosing a flag the program returns a list sorted in lexicographic order.

### Upcoming updates
-------------------
- [ ] convert this to a more comfortable command line tool with argparse or click.

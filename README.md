This is a self-learning project where I am testing features in both Python and the PyQT6 Graphical User Interface Library.

The project is a simple calculator to perform addition and subtraction. It implements a clear feature and has a typical number pad format.

Notes:
Uses eval() which is not ideal, however implements the "evaluation" aspect nicely.
  To address potential user error / self-inflicted issues, I prevent direct input to the areas by setting them as read only.
  This means that the user has to use pre-programmed buttons (0-9, +/-/=) to access the fields / set input / get output.
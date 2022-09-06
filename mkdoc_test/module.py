"""Module level docstring"""

class ModuleClass:
    """An example class

    Parameters
    ----------
    x : int
    y : str

    Methods
    -------
    get_x()
        returns x
    set_y(val)
        sets the instance member variable y with val
    """
    def __init__(self, x: int, y: str):
        self.x = x
        self.y = y

    def get_x(self) -> int:
        """Gets the x member variable value

        Parameters
        ----------
        None

        Returns
        -------
        int
            the value of x
        """
        return self.x

    def set_y(self, val: str) -> None:
        """Sets the y member variable value

        Parameters
        ----------
        val : str 
            The value to be set to the member variable y

        Returns
        -------
        None
        """
        self.y = val



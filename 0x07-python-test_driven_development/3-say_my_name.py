def say_my_name(first_name, last_name=""):
    """
    Prints a formatted string indicating the name.

    Args:
    first_name (str): The first name.
    last_name (str, optional): The last name (default is an empty string).

    Raises:
    TypeError: If first_name or last_name is not a string.
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    if last_name:
        print("My name is {} {}".format(first_name, last_name))
    else:
        print("My name is {}".format(first_name))

def natural_to_binary(n):
    if not isinstance(n, int):
        raise TypeError("Input must be an integer")
    if n < 1 or n > 100:
        raise ValueError("Number must be in the range 1 to 100")
    return bin(n)[2:]
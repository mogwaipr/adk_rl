def sum_even_factors(n):
    """Calculates the sum of even factors of a given number.

    Args:
        n: The input number.

    Returns:
        The sum of the even factors of n.
    """
    sum_of_factors = 0
    for i in range(2, n + 1, 2):  # Iterate through even numbers only
        if n % i == 0:
            sum_of_factors += i
    return sum_of_factors

print(sum_even_factors(40))
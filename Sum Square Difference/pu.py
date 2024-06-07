def sum_of_n_natural_number(number: float):
    return ((number * (number + 1)) / 2)
    
def sum_of_square_of_n_number(number: float):
    return ((number * (number + 1) * (2* number + 1)) / 6)
    
def answer_of_the_problem(number: float):
    return (((number * (number + 1)) / 2) ** 2) - ((number * (number + 1) * (2* number + 1)) / 6)

print(f"{int(answer_of_the_problem(100))}")
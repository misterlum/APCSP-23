#Example 0: using a function to print repeated code
def row_row_row():
    print("row, row, row your boat")
    print("gently down the stream")
    print("merrily merrily merrily merrily")

def full_row():
    row_row_row()
    print("life is but a dream")
    row_row_row()
    print("i want some ice cream")

    #Practice with Calling Functions
    """
    Practice 0: write another verse of the song,
    calling the row_row_row() function and then print()
    another line that rhymes
    """



#Practice with Passing Parameters
"""
Practice 1: write a function called greet
that takes a parameter of a string and prints
a greeting using that person's name
"""
def greet(name):
    #fill in code here; remove the line below when you finish
    print('i have not completed greet')



"""
Practice 2: write a function called square
that takes a parameter of a number and prints
that number squared
"""
def square(num):
    #fill in code here; remove the line below when you finish
    print('i have not completed square')



"""
Practice 3: write a function called largest
that takes 3 number parameters and prints
the largest of the 3 numbers
"""
def largest(one, two, three):
    print('i have not completed largest')



"""
Practice 4: write a function called mean_avg
that takes a parameter of a list and prints
the mean average of that list
"""
def mean_avg(nums):
    print('i have not completed mean_avg')



"""
Practice 5: write a function called print_evens
that takes a parameter of a list of numbers and prints
out each even number of that list
"""
def print_evens(nums):
    print('i have not completed print_evens')

#Practice with Returns
"""
Practice 6: write a function called primes10 that
returns a list of the first 10 prime numbers

You do not need to calculate them, but wouldn't
it be nice if you did?
"""
def primes10():
    return []



"""
Practice 7: write a function called random_greeting that
returns a random value from a list of greetings

The list is created within the function.
Against my better judgment, you can select what goes
in this list.
"""
def random_greeting():
    greetings = []



#Practice with Passing Parameters and Returns
"""
Practice 8: write a function called triple that
takes a parameter of a number and
returns the product of 3 and that number
"""
def triple(nums):
    return 0




"""
Practice 9: write a function called multiply_all that
takes a parameter of a list of numbers and
returns the product of all of the numbers
"""
def multiply_all(nums):
    return 0



"""
Practice 10: write a function called common that
takes a parameter of two lists and
returns a list containing the common elements of both
"""
def common(list1, list2):
    return []



"""
Practice 11: write a function called difference that
takes a parameter of two lists and
returns a list containing the unique elements of both
"""
def difference(list1, list2):
    return []



def main():
    #Test Function 0
    print("--Test Function 0--")
    full_row()
    print()

    #Test Function 1
    print("--Test Function 1--")
    greet("Alice")
    greet("Bob")
    greet("Carol")
    greet("Dave")
    greet("Ernest")
    print()

    #Test Function 2
    print("--Test Function 2--")
    for x in range(10):
        square(x)
    print()

    #Test Function 3
    print("--Test Function 3--")
    largest(1, 2, 3)
    largest(100, 5, 50)
    largest(25, 700, 4)
    print()

    #Test Function 4
    print("--Test Function 4--")
    mean_avg([10, 10, 10, 10])
    mean_avg([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    print()

    #Test Function 5
    print("--Test Function 5--")
    print_evens([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    print_evens([2, 4, 6, 8, 10])
    print_evens([1, 3, 5, 7, 9])
    print()

    #Test Function 6
    print("--Test Function 6--")
    list0 = primes10()
    print(list0)
    print()

    #Test Function 7
    print("--Test Function 7--")
    print(random_greeting())
    print(random_greeting())
    print(random_greeting())
    print()

    #Test Function 8
    print("--Test Function 8--")
    print(triple(3))
    print(triple(triple(3)))
    print(triple(triple(triple(3))))
    print()

    #Test Function 9
    print("--Test Function 9--")
    print(multiply_all([1, 3, 5, 7, 9]))
    print(multiply_all([1, -3, 5, -7, 9]))
    print(multiply_all([0, 2, 4, 6, 8, 10]))
    print()

    #Test Function 10
    print("--Test Function 10--")
    print(common([1, 2, 3, 4, 5, 6, 7, 8] , [2, 3, 5, 7]))
    print(common([0, 1, 1, 2, 3, 5, 8] , [2, 4, 6, 8]))
    print(common([1, 3, 5, 7, 9] , [2, 4, 6, 8, 10]))
    print()

    #Test Function 11
    print("--Test Function 11--")
    print(difference([1, 2, 3, 4, 5, 6, 7, 8] , [2, 3, 5, 7]))
    print(difference([0, 1, 1, 2, 3, 5, 8] , [2, 4, 6, 8]))
    print(difference([1, 3, 5, 7, 9] , [2, 4, 6, 8, 10]))
    print()

#actually runs the main function
main()

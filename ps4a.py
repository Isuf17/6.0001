# Problem Set 4A
# Name: Mohammed Isuf Ahmed
# Collaborators: None
# Time Spent: 2 hours
# Late Days Used: None

# Part A0: Data representation
# Fill out the following variables correctly.
# If correct, the tests named data_representation should pass.
treeA = [[14,19], [[3,5], 0]]
treeB = [[9, 3], 6]
treeC = [[7], [16,4,2], [8]]


# Part A1: Multiplication on tree leaves

def add_tree(tree):
    """
    Recursively computes the sum of all tree leaves.
    Returns an integer representing the product.

    Inputs
       tree: A list (potentially containing sublists) that
       represents a tree structure.
    Outputs
       total: An int equal to the sum of all the leaves of the tree.

    """

    total = 0
    for i in tree:
        if isinstance(i, int): #Checks if the element of tree is a an int
           total += i #Adds int to total
        else:
            total += add_tree(i) #If i is a list, this list passes through the function again
    return total #returns total of all ints in tree
              
    


# Part A2: Arbitrary operations on tree leaves

def sumem(a, b):
    """
    Example operator function.
    Takes in two integers, returns their sum.
    """
    return a + b


def prod(a, b):
    """
    Example operator function.
    Takes in two integers, returns their product.
    """
    return a * b


def op_tree(tree, op, base_case):
    """
    Recursively runs a given operation on tree leaves.
    Return type depends on the specific operation.

    Inputs
       tree: A list (potentially containing sublists) that
       represents a tree structure.
       op: A function that takes in two inputs and returns the
       result of a specific operation on them.
       base_case: What the operation should return as a result
       in the base case (i.e. when the tree is empty).
    """
    if len(tree) == 0:
        return base_case #As the PSET specified, an empty tree returns the base case
    for i in tree:
        if isinstance(i, int):
            base_case = op(i, base_case) #If the element i in tree is ant in, apply op(i, base_case)
        else:
            base_case = op_tree(i, op, base_case) #If the element is something other than an int, apply op_tree to it
    return base_case #Base case will have been modified in the code to return what we are looking for
        
# Part A3: Searching a tree

def search_greater_ten(a, b):
    """
    Operator function that searches for greater-than-10 values within its inputs.

    Inputs
        a, b: integers or booleans
    Outputs
        True if either input is equal to True or > 10, and False otherwise
    """
    if (isinstance(a, bool) and a) or (isinstance(b, bool) and b):
        return True #If a in a boolean and true, or if b is a boolean and true, return True
    elif a > 10 or b > 10: #If either a or b are greater than 10, return True
        return True
    else:
        return False

# Part A4: Find the maximum element of a tree using op_tree and max() in the
# main function below (remembering to pass the function in without parenthesis)
if __name__ == '__main__':
    tree = [[13,18], [[2,4], 8]]
    max_val = op_tree(tree, max, 0)
    print('max_val =', max_val)
    pass
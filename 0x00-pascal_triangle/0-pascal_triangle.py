#!/usr/bin/python3
""" pascal triangle
"""
def pascal_triangle(n):
    """ returns pascal triangle
    """
    if n <= 0:
        return []
    # first element
    triangle = [[1]]
    
    for i in range(1, n):
        row = [1]
        for j in range(1, i):
             # last element
            row.append(triangle[i-1][j-1] + triangle[i-1][j])
        row.append(1)
        # Add two previous values to get current next value
        triangle.append(row)
    
    return triangle

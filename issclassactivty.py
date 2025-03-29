def find_cube_pairs(target):
    # Initialize empty list to store pairs of numbers whose cubes sum to target
    solutions = []
    
    # Calculate maximum possible value: the cube root of target (rounded up)
    # Corrected: Using ** for exponentiation instead of *** and proper rounding
    max_num = int(target ** (1/3)) + 1
    
    # Iterate through possible values for a
    # Corrected: 'ranges' to 'range' and fixed syntax
    for a in range(1, max_num + 1):
        # Iterate through possible values for b, starting from a
        # Corrected: 'ranges' to 'range'
        for b in range(a, max_num + 1):
            # Check if the sum of cubes equals the target
            # Corrected: ** for exponentiation instead of ***
            if a**3 + b**3 == target:
                # Append the pair to solutions
                # Corrected: 'sol' to 'solutions'
                solutions.append((a, b))
    
    return solutions

# Corrected: Proper function call and variable names
pairs = find_cube_pairs(1729)
print("Valid cube pairs for 1729:")  # Corrected: 1729 not 1728, using print function

# Corrected: Iteration syntax and variable names
for a, b in pairs:
    # Corrected: Proper formatting and calculation (cubes, not squares)
    print(f" → {a}³ + {b}³ = {a**3} + {b**3} = 1729")
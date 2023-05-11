import math

# Givens
emf = 13.0
r = 0.39
P_desired = 80.0

# Note: These values can be adjusted as the idea of the answer gets better
# Tolerance allowed in P
P_tol = 0.00001
# Low bound for R
R_low = 0.126
# High bound for R
R_high = 1.21
# Amount to increase R each loop
dR = 0.0000001

def power(R, emf, r):
    """
    Calculate the power P disipated by resistor R connected to a battery of known emf and internal resistance r.
    """
    I = emf / (r + R)
    P = I**2 * R
    return P

def best_guess(guesses, func, goal):
    """
    Given a list of guesses, determine which one when evaluated with func gets closest to the goal.
    If there is a tie, return the one that appears first in the list of guesses.
    """
    values = [func(guess) for guess in guesses]
    errors = [val - goal for val in values]
    abs_errors = [abs(error) for error in errors]
    min_abs_error = min(abs_errors)
    index = abs_errors.index(min_abs_error)
    return guesses[index]

# Start R at the low bound
R = R_low
# Start a variable to track if the previous guess for R gave a P that was close to P_desired
prev_close = False
# Store the good guesses in batches in this list
good_guesses = [[]]

while True:
    # Calculate P
    P = power(R, emf, r)
    # Check if P is close to P_desired within P_tol
    close = math.isclose(P, P_desired, abs_tol=P_tol)
    # If it is close, then add the R to the current batch in the list of good_guesses
    if close:
        good_guesses[-1].append(R)
    # If it is not close, and the previous guess was close, then create a new batch
    elif prev_close:
        good_guesses.append([])
    # If we are out of bounds, break out of the loop
    if R >= R_high:
        break
    # Increase R by dR
    R += dR
    # Set the previous close to the current close
    prev_close = close

# If the last batch is empty, remove it
if len(good_guesses[-1]) == 0:
    del good_guesses[-1]

# Print out all the good guesses for R, one from each batch
for i, batch in enumerate(good_guesses):
    R = best_guess(batch, lambda x: power(x, emf, r), P_desired)
    print(f"R_{i+1} = {R}")

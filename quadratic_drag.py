import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# The code attempts to model a projectile undergoing quadratic drag

# Global value for g
g = 9.81

def acceleration(v, b, m):
    """
    Return the acceleration of the projectile.
    Depends on the following:
        - Velocity (v)
        - Drag coefficient (b)
        - Mass (m)
    """
    v_mag_squared = np.dot(v, v)
    v_mag = np.sqrt(v_mag_squared)
    v_hat = v / v_mag if v_mag else 0
    F_g = m * np.array([0, -g])
    F_d = - b * v_mag_squared * v_hat
    F = F_g + F_d
    return F / m

def dv(dt, v, b, m):
    """
    Return a small nudge to the projectiles velocity.
    Depends on the following:
        - Small time nudge (dt)
        - Velocity (v)
        - Drag coefficient (b)
        - Mass (m)
    """
    return acceleration(v, b, m) * dt

def dr(dt, v, b, m):
    """
    Return a small nudge to the projectiles position.
    Depends on the following:
        - Small time nudge (dt)
        - Velocity (v)
        - Drag coefficient (b)
        - Mass (m)
    """
    return (v * dt) + (0.5 * acceleration(v, b, m) * (dt)**2) 

def simulate_time_period(time, r_0, v_0, dt, b, m):
    """
    Simulate the projectile for the specified amount of time.
    Return a tuple with the time, position, and velocity arrays.
    Depends on the following:
        - Time period (time)
        - Initial position (r_0)
        - Initial velocity (v_0)
        - Small time nudge (dt)
        - Drag coefficient (b)
        - Mass (m)
    """
    t = np.arange(0, time, dt)
    r = [r_0]
    v = [v_0]
    for _ in range(len(t) - 1):
        r.append(r[-1] + dr(dt, v[-1], b, m))
        v.append(v[-1] + dv(dt, v[-1], b, m))
    r = np.array(r)
    v = np.array(v)
    return t, r, v

def simulate_until_hits_ground(r_0, v_0, dt, b, m):
    """
    Simulate the projectile until it hits the ground at y=0.
    Return a tuple with the time, position, and velocity arrays, as well as the horizontal range.
    Depends on the following:
        - Initial position (r_0)
        - Initial velocity (v_0)
        - Small time nudge (dt)
        - Drag coefficient (b)
        - Mass (m)
    """
    t = [0]
    r = [r_0]
    v = [v_0]
    while True:
        t.append(t[-1] + dt)
        r.append(r[-1] + dr(dt, v[-1], b, m))
        v.append(v[-1] + dv(dt, v[-1], b, m))
        y = r[-1][1]
        if y < 0:
            break
    t = np.array(t)
    r = np.array(r)
    v = np.array(v)
    x = r[:,0]
    max_x = np.max(x)
    min_x = np.min(x)
    R = np.abs(max_x - min_x)
    return t, r, v, R

if __name__ == "__main__":
    # Plot range vs initial speed for a variety of launch angles
    r_0 = np.array([0, 0])
    theta_0_arr = np.arange(0, 90 + 10, 10)
    v_0_arr = np.linspace(0, 15, 100)
    results = {"$\\theta$": [], "$v_0$": [], "$R$": []}
    for theta_0 in theta_0_arr:
        for v_0 in v_0_arr:
            _, _, _, R = simulate_until_hits_ground(r_0=r_0,
                                                    v_0=np.array([v_0 * np.cos(np.deg2rad(theta_0)), v_0 * np.sin(np.deg2rad(theta_0))]),
                                                    dt=0.001,
                                                    b=1,
                                                    m=1
                                                    )
            results["$\\theta$"].append(theta_0)
            results["$v_0$"].append(v_0)
            results["$R$"].append(R)

    df = pd.DataFrame(results)
    df["$\\theta$"] = df["$\\theta$"].astype("category")
    fig, ax = plt.subplots()
    sns.lineplot(data=df, x="$v_0$", y="$R$", hue="$\\theta$", ax=ax)
    fig.show()

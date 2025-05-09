import numpy as np


def roll_off_angle(d: float, wavel: float) -> float:
    """Calculate the roll-off angle

    See Peterson, 2012 (https://doi.org/10.1117/12.930860)

    :param d: dig diameter
    :type d: float
    :param wavel: wavelength of incident light
    :type wavel: float
    :return: roll off angle
    :rtype: float
    """
    ld = ((4 / (np.pi**4)) ** (1 / 3)) * (wavel / d)
    return ld


def BRDF_dig(Nd: float, d: float, wavel: float, theta: np.ndarray) -> np.ndarray:
    """Calculate the BRDF of a surface using the Peterson model

    Args:
        Nd (float): dig density
        d (float): diameter of the dig
        wavel (float): wavelength of the incident light
        theta (np.ndarray): scattering angle

    Returns:
        np.ndarray: BRDF values for the given angles
    """

    # calculate the roll off angle
    roff_angle = roll_off_angle(d, wavel)

    # calculate the BRDF based on Peterson Model
    # (https://doi.org/10.1117/12.930860)
    # Split the formula up for readability
    X = (1 / 4) * Nd * (d**2)
    Y = ((np.pi * d) / (2 * wavel)) ** 2
    Z = (1 + (np.sin(theta) / roff_angle) ** 2) ** (-3 / 2)

    BRDF = X * (1 + Y * Z)

    return BRDF


def BRDF_dig_sum(d_arr: np.ndarray, A: float, wavel: float, theta: np.ndarray) -> np.ndarray:
    """Calculate the Peterson BRDF for a set of different sized digs

    Args:
        d_arr (np.ndarray): array of dig diameters
        A (float): area of the surface
        wavel (float): wavelength of the incident light
        theta (np.ndarray): scattering angle

    Returns:
        np.ndarray: BRDF values for the given angles
    """
    # intialise the BRDF array
    BRDF = np.zeros_like(theta)

    # calculate the roll off angle
    roff_angle = roll_off_angle(d_arr, wavel)

    # for each angle, calculate the BRDF
    # based on Peterson Model
    # (https://doi.org/10.1117/12.930860)
    for n, angle in enumerate(theta):
        # split the formula up for readability
        X = (1 / 4) * (d_arr**2)
        Y = ((np.pi * d_arr) / (2 * wavel)) ** 2
        Z = (1 + (np.sin(angle) / roff_angle) ** 2) ** (-3 / 2)
        BRDF_arr = (X * (1 + Y * Z)) / A
        # sum the contributions from each dig
        BRDF[n] = np.sum(BRDF_arr)

    return BRDF


if __name__ == "__main__":
    # Example usage of the BRDF functions
    import matplotlib.pyplot as plt

    # Example parameters
    wl = 0.633e-6
    d = 4e-4
    D = 100e-3
    Nd = 1 / (5 * np.pi * D)
    theta = np.linspace(0, np.pi / 2, 1000000)

    # Calculate the BRDF using the conventional Peterson model
    BDRF0 = BRDF_dig(Nd, d, wl, theta)

    fig, ax = plt.subplots()
    ax.plot(np.sin(theta), BDRF0)
    ax.set_xlabel(r"Sin ${\theta}$ (deg)")
    ax.set_ylabel("BRDF")
    ax.set_xscale("log")
    ax.set_yscale("log")
    ax.set_xlim(0.001, 1)

    # create a distribution of dig sizes
    d_arr = np.linspace(3.5e-4, 4.5e-4, 10)
    # calculate the area of the surface
    A = np.pi * (D**2) / 4

    # calculate the BRDF using the Peterson model for a distribution of digs

    BDRF1 = BRDF_dig_sum(d_arr, A, wl, theta)
    fig, ax = plt.subplots()
    ax.plot(np.sin(theta), BDRF1, label="Sum of Digs")
    ax.legend()
    ax.set_title("BRDF of a surface with digs")
    ax.set_xlabel(r"Sin ${\theta}$ (deg)")
    ax.set_ylabel("BRDF")
    ax.set_xscale("log")
    ax.set_yscale("log")
    ax.set_xlim(0.001, 1)
    plt.show()

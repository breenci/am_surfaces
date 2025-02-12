import numpy as np

def roll_off_angle(d, wavel):
    """Calculate the roll-off angle
    
    See Peterson, 2012 (https://doi.org/10.1117/12.930860)

    :param d: dig diameter
    :type d: float
    :param wavel: wavelength of incident light
    :type wavel: float
    :return: roll off angle
    :rtype: float
    """
    ld = ((4/(np.pi**4))**(1/3)) * (wavel/d)
    print("ld", ld)
    return ld


def BRDF_dig(Nd, d, wavel, theta):
    
    # calculate the roll off angle
    roff_angle = roll_off_angle(d, wavel)
    
    # calculate the BRDF based on Peterson Model 
    # (https://doi.org/10.1117/12.930860)
    # Split the formula up for readability
    A = ((1/4) * Nd * (d**2))
    B = ((np.pi * d)/(2 * wavel))**2
    C = (1 + (np.sin(theta)/roff_angle)**2)**(-3/2)

    BRDF = A * (1 + B * C)
    
    return BRDF


if __name__ == "__main__":
    import matplotlib.pyplot as plt
    
    wl = 0.633e-6
    d = 4e-4
    D = 100e-3
    Nd = 1/(5 * np.pi * D)
    # Nd = 100/(5 * np.pi * D**2)
    print("Nd", Nd)
    
    theta = np.linspace(0, np.pi/2, 1000000)
    
    BDRF0 = BRDF_dig(Nd, d, wl, theta)
    print(BRDF_dig(Nd, d, wl, 0.1))

    fig, ax = plt.subplots()
    ax.plot(np.sin(theta), BDRF0)
    ax.set_xlabel(r"Sin ${\theta}$ (deg)")
    ax.set_ylabel("BRDF")
    ax.set_xscale('log')
    ax.set_yscale('log')
    ax.set_xlim(0.001, 1)
    plt.show()


    
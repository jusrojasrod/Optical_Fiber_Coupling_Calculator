import math

# Acople de entrada a fibra óptica

def diameter_focal_spot(wavelength, diameter_input_beam, focal_length):
    """Calcula el diámetro del punto focal dado el diámetro del haz de entrada, la longitud focal y la longitud de onda."""
    return (4*wavelength*focal_length) / (math.pi*diameter_input_beam)

def focal_length_for_diameter_focal_spot(wavelength, diameter_input_beam, mode_focal_diameter):
    """Calcula la longitud focal dada la longitud de onda, el diámetro del haz de entrada y el diámetro del punto focal.
    Parameters
    ----------
    wavelength : float
        Longitud de onda en metros.
    diameter_input_beam : float
        Diametro del haz de entrada en metros.
    mode_focal_diameter : float
        Diametro del punto focal en metros. Debe ser el mismo que el diámetro del núcleo de la fibra óptica para un acople eficiente (MFD).
    Returns
    -------
    float
        Longitud focal en metros.
    """
    return (mode_focal_diameter * math.pi * diameter_input_beam) / (4*wavelength)

def fiber_coupling_efficiency(MFD, omega_input_beam, wavelength, focal_length):
    """Calcula la eficiencia de acople de fibra óptica.
    Parameters
    ----------
    MFD : float
        Diametro de la fibra óptica en metros.
    omega_input_beam : float
        Radio del haz de entrada en metros.
    wavelength : float
        Longitud de onda en metros.
    focal_length : float
        Longitud focal en metros.
    Returns
    -------
    float
        Eficiencia de acople de fibra óptica.
    """
    omega_1 = (wavelength * focal_length) / (math.pi * omega_input_beam)
    omega_2 = MFD / 2
    eta = (2*omega_1*omega_2/(omega_1**2 + omega_2**2))**2
     
    return eta

if __name__ == "__main__":
    # Lente de acople F110APC-633: 633 nm, f = 6.17 mm, NA = 0.38 FC/APC Collimation Pkg.
    # fibra P3-460B-FC-2: (488 - 633) nm, MFD = (2.8 - 4.1) µm @ 488 nm,
    
    # ---- Parámetros iniciales ---------------------
    # wavelength = 633e-9 # [m] 633 nm
    # focal_length = 6.17e-3 # [m] 6.17 mm
    # MFD = 4.3e-6 # [m] 4.1 um (MFD de la fibra óptica)
    # print("--- Parámetros de Entrada ---")
    # print(f"Longitud de onda (\u03bb):  {wavelength * 1e9:.0f} nm")
    # print(f"Longitud focal (f):    {focal_length * 1e3:.2f} mm")
    # print(f"MFD de la fibra:       {MFD * 1e6:.1f} µm")
    # print("-" * 30)
    
    # # Diametro haz de entrada ideal ---------------------
    # diameter_input_beam = diameter_focal_spot(wavelength, MFD, focal_length) * 1e3 # Convertir a mm
    # print(f"Diámetro haz de entrada ideal: {diameter_input_beam:.8f} mm")
    
    # # Longitud focal necesaria para haz de salida ---------------------
    # desire_output_beam_diameter = 0.05 # [m] 5.0 cm
    # focal_length = focal_length_for_diameter_focal_spot(wavelength, desire_output_beam_diameter, MFD) * 1e3 # Convertir a mm
    # print(f"Longitud focal necesaria para acoplar eficientemente: {focal_length:.2f} m")
    
    # # Longitud focal necesaria para haz de salida ---------------------
    # desire_output_beam_diameter = 0.025 # [m] 2.5 cm
    # focal_length = focal_length_for_diameter_focal_spot(wavelength, desire_output_beam_diameter, MFD) * 1e3 # Convertir a mm
    # print(f"Longitud focal necesaria para acoplar eficientemente: {focal_length:.2f} mm")
    
    # # Eficiencia de acople de fibra óptica. ---------------------
    # diameter_input_beam = 0.05 # [m] 5.0 cm
    # efficiency = fiber_coupling_efficiency(MFD, diameter_input_beam/2, wavelength, focal_length) * 100
    # print(f"Eficiencia de acople de fibra óptica: {efficiency:.2%}")
    
    ##################
    
    # ---- Parámetros iniciales ---------------------
    wavelength = 543.365e-9 # [m] 543.365 nm
    focal_length = 6.17e-3 # [m] 6.17 mm
    MFD = 4.3e-6 # [m] 4.1 um (MFD de la fibra óptica)
    print("--- Parámetros de Entrada ---")
    print(f"Longitud de onda (\u03bb):  {wavelength * 1e9:.0f} nm")
    print(f"Longitud focal (f):    {focal_length * 1e3:.2f} mm")
    print(f"MFD de la fibra:       {MFD * 1e6:.1f} µm")
    print("-" * 30)
    
    # Diametro haz de entrada ideal ---------------------
    diameter_input_beam = diameter_focal_spot(wavelength, MFD, focal_length) * 1e3 # Convertir a mm
    print(f"Diámetro haz de entrada ideal: {diameter_input_beam:.8f} mm")
    
    # Longitud focal necesaria para haz de salida ---------------------
    desire_output_beam_diameter = 0.02 # [m] 5.0 cm
    focal_length = focal_length_for_diameter_focal_spot(wavelength, desire_output_beam_diameter, MFD) * 1e3 # Convertir a mm
    print(f"Longitud focal necesaria para acoplar eficientemente: {focal_length:.2f} m")
    
    # Longitud focal necesaria para haz de salida ---------------------
    desire_output_beam_diameter = 0.025 # [m] 2.5 cm
    focal_length = focal_length_for_diameter_focal_spot(wavelength, desire_output_beam_diameter, MFD) * 1e3 # Convertir a mm
    print(f"Longitud focal necesaria para acoplar eficientemente: {focal_length:.2f} mm")
    
    # Eficiencia de acople de fibra óptica. ---------------------
    diameter_input_beam = 0.99270106 # [m] 5.0 cm
    efficiency = fiber_coupling_efficiency(MFD, diameter_input_beam/2, wavelength, focal_length) * 100
    print(f"Eficiencia de acople de fibra óptica: {efficiency:.2%}")
    

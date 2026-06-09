import math

class Fiber:
    def __init__(self, wavelength, focal_length, MFD):
        """ Clase para representar una fibra óptica y calcular parámetros relacionados con el acople de luz.
        Parameters
        ----------
        wavelength : float
            Longitud de onda en metros.
        focal_length : float
            Longitud focal en metros.
        MFD : float
            Diametro del punto focal en metros. Debe ser el mismo que el diámetro del núcleo de la 
            fibra óptica para un acople eficiente (MFD).
        """
        self.wavelength = wavelength
        self.focal_length = focal_length
        self.MFD = MFD
       
    def diameter_focal_spot(self):
        """Calcula el diámetro del punto focal dado el diámetro del haz de entrada, la longitud focal y la longitud de onda."""
        return (4*self.wavelength*self.focal_length) / (math.pi*self.MFD)
    
    def focal_length_for_diameter_focal_spot(self, diameter_input_beam,):
        """Calcula la longitud focal dada la longitud de onda, el diámetro del haz de entrada y el diámetro del punto focal.
        Parameters
        ----------
        diameter_input_beam : float
            Diametro del haz de entrada en metros.
        Returns
        -------
        float
            Longitud focal en metros.
        """
        return (self.MFD * math.pi * diameter_input_beam) / (4*self.wavelength)
    
    def fiber_coupling_efficiency(self, omega_input_beam):
        """Calcula la eficiencia de acople de fibra óptica.
        Parameters
        ----------
        omega_input_beam : float
            Radio del haz de entrada en metros.
        Returns
        -------
        float
            Eficiencia de acople de fibra óptica.
        """
        omega_1 = (self.wavelength * self.focal_length) / (math.pi * omega_input_beam)
        omega_2 = self.MFD / 2
        eta = (2*omega_1*omega_2/(omega_1**2 + omega_2**2))**2
     
        return eta
    
    def print_parameters(self):
        print("--- Parámetros de entrada ---")
        print(f"Longitud de onda (\u03bb):                   {self.wavelength * 1e9:.0f} nm")
        print(f"Longitud focal lente de entrada (f):    {self.focal_length * 1e3:.2f} mm")
        print(f"MFD de la fibra:                        {self.MFD * 1e6:.1f} µm")
        print("-" * 50)
        print("\n")
    
    def summary(self):
        self.print_parameters()
        

if __name__ == "__main__":
    # Lente de acople F110APC-633: 633 nm, f = 6.17 mm, NA = 0.38 FC/APC Collimation Pkg.
    # fibra P3-460B-FC-2: (488 - 633) nm, MFD = (2.8 - 4.1) µm @ 488 nm,
    
    # # ---- Parámetros iniciales ---------------------
    # wavelength = 633e-9 # [m] 633 nm
    # focal_length = 6.17e-3 # [m] 6.17 mm
    # MFD = 4.3e-6 # [m] 4.1 um (MFD de la fibra óptica)
    
    # fiber = Fiber(wavelength, focal_length, MFD)
    # fiber.summary()
    
    # # Diametro haz de entrada ideal ---------------------
    # diameter_focal_spot = fiber.diameter_focal_spot() * 1e3 # Convertir a micrómetros
    # print(f"Diámetro haz de entrada ideal: {diameter_focal_spot:.5f} mm")
    
    # # Longitud focal dle lente necesaria para haz de salida colimado---------------------
    # desire_output_beam_diameter = 0.05 # [m] 5.0 cm
    # focal_length = fiber.focal_length_for_diameter_focal_spot(desire_output_beam_diameter) * 1e3 # Convertir a mm
    # print(f"Longitud focal de lente colimador de salida: {focal_length:.2f} mm")
    
    # # Eficiencia de acople de fibra óptica. ---------------------
    # diameter_input_beam = 0.006 # [m] 5 mm
    # efficiency = fiber.fiber_coupling_efficiency(diameter_input_beam/2)
    # print(f"Eficiencia de acople de fibra óptica: {efficiency:.2%}, para un diámetro de haz de entrada de {diameter_input_beam*1e3:.2f} mm")
    
    
    # # Longitud focal dle lente necesaria para haz de salida colimado---------------------
    # desire_output_beam_diameter = 0.0025 
    # focal_length = fiber.focal_length_for_diameter_focal_spot(desire_output_beam_diameter) * 1e3 # Convertir a mm
    # print(f"Longitud focal de lente entrada: {focal_length:.2f} mm")
    
    
    ##############################################################################
    
    wavelength = 543.365e-9 # [m] 543.365 nm
    focal_length = 6.17e-3 # [m] 6.17 mm
    MFD = 4.3e-6 # [m] 4.1 um (MFD de la fibra óptica)

    fiber = Fiber(wavelength, focal_length, MFD)
    fiber.summary()
    
    # Diametro haz de entrada ideal ---------------------
    diameter_focal_spot = fiber.diameter_focal_spot() * 1e3 # Convertir a micrómetros
    print(f"Diámetro haz de entrada ideal: {diameter_focal_spot:.5f} mm")

   # Longitud focal dle lente necesaria para haz de salida colimado---------------------
    desire_output_beam_diameter = 0.05 # [m] 5.0 cm
    focal_length = fiber.focal_length_for_diameter_focal_spot(desire_output_beam_diameter) * 1e3 # Convertir a mm
    print(f"Longitud focal de lente colimador de salida: {focal_length:.2f} mm")
    
    # Eficiencia de acople de fibra óptica. ---------------------
    diameter_input_beam = 0.002 # [m] 2 mm
    efficiency = fiber.fiber_coupling_efficiency(diameter_input_beam/2)
    print(f"Eficiencia de acople de fibra óptica: {efficiency:.2%}, para un diámetro de haz de entrada de {diameter_input_beam*1e3:.2f} mm")
    
    
    # Longitud focal dle lente necesaria para haz de salida colimado---------------------
    desire_output_beam_diameter = 0.0025 
    focal_length = fiber.focal_length_for_diameter_focal_spot(desire_output_beam_diameter) * 1e3 # Convertir a mm
    print(f"Longitud focal de lente entrada: {focal_length:.2f} mm")
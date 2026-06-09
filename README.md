# Optical Fiber Coupling Calculator

Este proyecto es una **calculadora óptica en Python**. Sirve para determinar matemáticamente los parámetros exactos necesarios para acoplar un láser de espacio libre dentro de una fibra óptica monomodo con la máxima eficiencia posible. 

**Este código te responde tres preguntas:**
1. ¿Qué longitud focal debe tener mi lente para este láser y esta fibra específicos?
2. ¿Qué diámetro debe tener mi haz láser de entrada para llenar perfectamente el núcleo de la fibra?
3. Si ya tengo una lente y un láser, ¿qué porcentaje teórico de luz (eficiencia) lograré acoplar?

Está diseñado para ahorrar horas de alineación a ciegas en montajes experimentales, como los utilizados en metrología de longitud, interferometría o el desarrollo de láseres ultrarrápidos.

## El Problema que Resuelve
En un laboratorio de óptica, meter la luz de un láser dentro de un hilo de vidrio de apenas unos micrómetros de grosor (el núcleo de la fibra) requiere extrema precisión. Si el láser se enfoca demasiado grande o demasiado pequeño respecto al *Mode Field Diameter* (MFD) de la fibra, la potencia se pierde. 

Este script utiliza la teoría de propagación de haces gaussianos para predecir el comportamiento de la luz a través de la lente y encontrar el "match" perfecto entre el punto focal y el núcleo de la fibra.

## Características
* **Cálculo de Punto Focal Inverso:** Determina el diámetro ideal del haz de entrada basándose en el MFD de la fibra.
* **Proyección de Lentes:** Calcula la longitud focal ideal (`f`) para lentes de acople o colimadores de salida.
* **Estimación de Eficiencia ($\eta$):** Calcula la fracción de potencia transmitida basada en la integral de superposición geométrica del haz y la fibra.
* **Estructura Orientada a Objetos (OOP):** Permite instanciar múltiples configuraciones de láser/fibra sin mezclar variables.

## Instalación
Este código utiliza únicamente la biblioteca estándar de Python (`math`), `numpy` y `matplotlib`.

```bash
git clone [https://github.com/tu-usuario/optical-fiber-coupling.git](https://github.com/tu-usuario/optical-fiber-coupling.git)
cd optical-fiber-coupling
```

## Usage Example
Todo el sistema se maneja a través de la clase Fiber. A continuación, un ejemplo de cómo simular el acople de un láser He-Ne verde (543 nm) utilizando componentes estándar (ej. Thorlabs):

```Python
import math
from fiber_coupling import Fiber

# 1. Define initial optical parameters (in meters)
wavelength = 543.365e-9       # 543 nm Green Laser
focal_length = 6.17e-3        # 6.17 mm Coupling Lens
mode_field_diameter = 4.3e-6  # 4.3 µm Fiber MFD

# 2. Initialize the optical system
coupling_system = Fiber(wavelength, focal_length, mode_field_diameter)

# 3. Display standard laboratory parameters
coupling_system.summary()

# 4. Calculate coupling efficiency for a 2 mm input beam
beam_diameter = 0.002
efficiency = coupling_system.fiber_coupling_efficiency(beam_diameter / 2)

print(f"Theoretical Coupling Efficiency: {efficiency:.2%}")
```

Console Output:

```bash
Plaintext
--- Input Parameters ---
Wavelength (λ):                    543 nm
Input lens focal length (f):       6.17 mm
Fiber MFD:                         4.3 µm
--------------------------------------------------

Theoretical Coupling Efficiency: 36.43
```
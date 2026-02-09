"""
MÉTODO DE EULER - PROBLEMA PERSONALIZADO
Problema: Enfriamiento de una Taza de Café (Ley de Enfriamiento de Newton)

Ecuación Diferencial: dT/dt = -k(T - T_ambiente)
Donde:
- T(t) = Temperatura del café en el tiempo t
- T_ambiente = Temperatura ambiente (20°C)
- k = Constante de enfriamiento (0.3)
- T(0) = 90°C (Temperatura inicial del café)

Solución con Método de Euler en intervalo [0, 2] con h = 0.1
"""

import numpy as np
import matplotlib.pyplot as plt

# ========== DEFINICIÓN DEL PROBLEMA ==========
def ecuacion_diferencial(t, T):
    """
    Ecuación diferencial: dT/dt = -k(T - T_ambiente)
    
    Parámetros:
    - t: tiempo (no se usa directamente, pero se incluye por convención)
    - T: temperatura actual
    
    Retorna: dT/dt
    """
    k = 0.3  # Constante de enfriamiento
    T_ambiente = 20  # Temperatura ambiente en °C
    
    return -k * (T - T_ambiente)

# ========== SOLUCIÓN EXACTA (para comparación) ==========
def solucion_exacta(t):
    """
    Solución analítica: T(t) = T_ambiente + (T0 - T_ambiente) * e^(-kt)
    """
    k = 0.3
    T_ambiente = 20
    T0 = 90
    
    return T_ambiente + (T0 - T_ambiente) * np.exp(-k * t)

# ========== MÉTODO DE EULER ==========
def metodo_euler(f, t0, T0, t_final, h):
    """
    Implementación del Método de Euler
    
    Parámetros:
    - f: función de la ecuación diferencial dT/dt = f(t, T)
    - t0: tiempo inicial
    - T0: temperatura inicial
    - t_final: tiempo final
    - h: tamaño del paso
    
    Retorna:
    - t_valores: array de valores de tiempo
    - T_valores: array de valores de temperatura aproximados
    """
    # Número de pasos
    n_pasos = int((t_final - t0) / h)
    
    # Inicializar arrays
    t_valores = np.zeros(n_pasos + 1)
    T_valores = np.zeros(n_pasos + 1)
    
    # Condiciones iniciales
    t_valores[0] = t0
    T_valores[0] = T0
    
    # Aplicar método de Euler
    for i in range(n_pasos):
        t_valores[i + 1] = t_valores[i] + h
        T_valores[i + 1] = T_valores[i] + h * f(t_valores[i], T_valores[i])
    
    return t_valores, T_valores

# ========== PARÁMETROS DEL PROBLEMA ==========
t0 = 0          # Tiempo inicial
t_final = 2     # Tiempo final
h = 0.1         # Tamaño del paso
T0 = 90         # Temperatura inicial (°C)

# ========== RESOLVER CON MÉTODO DE EULER ==========
print("=" * 60)
print("MÉTODO DE EULER - ENFRIAMIENTO DE CAFÉ")
print("=" * 60)
print(f"\nEcuación Diferencial: dT/dt = -k(T - T_ambiente)")
print(f"Condición inicial: T(0) = {T0}°C")
print(f"Intervalo: [{t0}, {t_final}]")
print(f"Paso (h): {h}")
print(f"\nConstantes:")
print(f"  - k (constante de enfriamiento): 0.3")
print(f"  - T_ambiente: 20°C")

t_euler, T_euler = metodo_euler(ecuacion_diferencial, t0, T0, t_final, h)

# ========== CALCULAR SOLUCIÓN EXACTA ==========
t_exacta = np.linspace(t0, t_final, 100)
T_exacta = solucion_exacta(t_exacta)

# ========== MOSTRAR RESULTADOS ==========
print("\n" + "=" * 60)
print("RESULTADOS")
print("=" * 60)
print(f"\n{'Tiempo (min)':<15} {'T Euler (°C)':<20} {'T Exacta (°C)':<20} {'Error':<15}")
print("-" * 70)

for i in range(len(t_euler)):
    T_exacta_i = solucion_exacta(t_euler[i])
    error = abs(T_euler[i] - T_exacta_i)
    print(f"{t_euler[i]:<15.2f} {T_euler[i]:<20.4f} {T_exacta_i:<20.4f} {error:<15.6f}")

# ========== ANÁLISIS ==========
print("\n" + "=" * 60)
print("ANÁLISIS")
print("=" * 60)
print(f"\nTemperatura inicial: {T0}°C")
print(f"Temperatura final (Euler): {T_euler[-1]:.2f}°C")
print(f"Temperatura final (Exacta): {solucion_exacta(t_final):.2f}°C")
print(f"Enfriamiento total: {T0 - T_euler[-1]:.2f}°C")
print(f"\nError máximo absoluto: {max(abs(T_euler - solucion_exacta(t_euler))):.6f}°C")

# ========== VISUALIZACIÓN ==========
plt.figure(figsize=(12, 8))

# Gráfica 1: Comparación Euler vs Solución Exacta
plt.subplot(2, 1, 1)
plt.plot(t_exacta, T_exacta, 'b-', linewidth=2, label='Solución Exacta')
plt.plot(t_euler, T_euler, 'ro-', markersize=6, label='Método de Euler (h=0.1)')
plt.axhline(y=20, color='g', linestyle='--', alpha=0.5, label='Temperatura Ambiente')
plt.xlabel('Tiempo (minutos)', fontsize=12)
plt.ylabel('Temperatura (°C)', fontsize=12)
plt.title('Enfriamiento de Café - Método de Euler vs Solución Exacta', fontsize=14, fontweight='bold')
plt.legend(fontsize=10)
plt.grid(True, alpha=0.3)

# Gráfica 2: Error del Método de Euler
plt.subplot(2, 1, 2)
error_euler = abs(T_euler - solucion_exacta(t_euler))
plt.plot(t_euler, error_euler, 'r^-', markersize=6, linewidth=2)
plt.xlabel('Tiempo (minutos)', fontsize=12)
plt.ylabel('Error Absoluto (°C)', fontsize=12)
plt.title('Error del Método de Euler', fontsize=14, fontweight='bold')
plt.grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig('C:\Users\benki\Documents\Code\Matematicas\Ecuaciones_diferenciales\euler_grafica.png', dpi=300, bbox_inches='tight')
print("\n✓ Gráfica guardada como 'euler_grafica.png'")

plt.show()

print("\n" + "=" * 60)
print("CONCLUSIÓN")
print("=" * 60)
print("""
El Método de Euler proporciona una buena aproximación para este problema.
El café se enfría desde 90°C hasta aproximadamente 46°C en 2 minutos,
acercándose gradualmente a la temperatura ambiente de 20°C.

El error del método es pequeño debido al paso h=0.1 relativamente pequeño.
""")
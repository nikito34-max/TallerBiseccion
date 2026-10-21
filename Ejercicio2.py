
import numpy as np
import matplotlib.pyplot as plt

def biseccion(f, a:float, b:float, TOL:float, N0=100):
    """Devuelve (p, historia), con historia = [(a, b, p) por iteración]."""
    FA = f(a)
    historia = []
    i = 1
    while i <= N0:
        p = a + (b-a)/2                                   # COMPLETE: punto medio estable
        FP = f(p)
        historia.append((a, b, p))                         # COMPLETE: (a, b, p)
        if FP == 0 or (b-a)/2 < TOL:                          # COMPLETE: parada por TOL
            return p, historia
        i = i + 1
        if FA * FP > 0:
            a=p      
            FA=FP                               # COMPLETE: mover a y FA
        else:
            b=p                                     # COMPLETE: mover b
    raise RuntimeError(f"fracasó después de {N0} iteraciones")

g = 9.81
s0, m, k = 300.0, 0.25, 0.1


def s(t):
    return s0 - (m * g / k) * t + (m ** 2 * g / k ** 2) * (1 - np.exp(-k * t / m))


def graficar(t_star, historia, k_iteracion=None, archivo="caida.png"):
    """Dibuja s(t). Si k_iteracion no es None, resalta el intervalo [a, b]
    de esa iteración (1-based) y su punto medio p."""
    t = np.linspace(0, 20, 400)
    plt.figure(figsize=(9, 4.5))
    plt.plot(t, s(t), label="s(t)")
    plt.axhline(0, color="gray", linestyle="--", linewidth=1)
    if k_iteracion is not None:
        a, b, p = historia[k_iteracion - 1]
        plt.axvspan(a, b, color="green", alpha=0.25,
                    label=f"iter {k_iteracion}: [{a:.4g}, {b:.4g}]")
        plt.axvline(p, color="green", linestyle=":", linewidth=1)
    plt.plot(t_star, 0, "ro", label=f"t* = {t_star:.4f}")
    plt.xlabel("t (s)")
    plt.ylabel("s(t) (m)")
    plt.title("Caída con resistencia del aire")
    plt.legend()
    plt.grid(True)
    plt.savefig(archivo, dpi=150)
    plt.show()


t_star, historia = biseccion(s, 0.0, 20.0, TOL=1e-4)

print(f"t* = {t_star:.6f} s, s(t*) = {s(t_star):.4g} m e iteraciones = {len(historia)}")

graficar(t_star, historia, k_iteracion=3)
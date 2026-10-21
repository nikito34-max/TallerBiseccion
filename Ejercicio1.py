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

def f(x:float) -> float:
    return x**3 + 4*x**2 -10

p, historia = biseccion(f, 1.0, 2.0, 1e-2)
print(f"Resultado: {p} con iteraciones = {len(historia)} e historia = {historia}")
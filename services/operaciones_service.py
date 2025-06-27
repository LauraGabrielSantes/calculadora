from fastapi import HTTPException

def sumar(a: float, b: float) -> float:
    return a + b


def multiplicar(a: float, b: float) -> float:
    return a * b

def factorial(n: int) -> int:
    """
    Calcula el factorial de un número entero no negativo.

    Args:
        n (int): Número entero.

    Returns:
        int: Factorial del número.

    Raises:
        HTTPException: Si el número es negativo.
    """
    if n < 0:
        raise HTTPException(status_code=400, detail="El número debe ser no negativo")
    resultado = 1
    for i in range(1, n + 1):
        resultado *= i
    return resultado

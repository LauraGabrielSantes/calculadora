from fastapi import APIRouter
from models.request_models import , MultiRequest, SumaRequest
from services.operaciones_service import sumar

router = APIRouter()

@router.post("/suma")
def ruta_suma(datos: SumaRequest):
    resultado = sumar(datos.a, datos.b)
    return {"resultado": resultado}

@router.post("/multiplicacion")
def ruta_suma(datos: MultiRequest):
    resultado = multiplicar(datos.a, datos.b)
    return {"resultado": resultado}

@router.get("/factorial/{n}")
def ruta_factorial(n: int):
    """
    Calcula el factorial de un número entero no negativo.

    Args:
        n (int): Número entero no negativo.

    Returns:
        dict: Resultado del factorial.

    Raises:
        HTTPException: Si el número es negativo.
    """
    resultado = factorial(n)
    return {"resultado": resultado}

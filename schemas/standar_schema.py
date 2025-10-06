from typing import Iterable
from pydantic import BaseModel


class StandarSchema(BaseModel):
    """Schema estándar con una lista numerada."""
    lista_numerada: Iterable[int]


if __name__ == "__main__":
    pass

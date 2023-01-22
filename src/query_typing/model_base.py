from dataclasses import dataclass
from typing import List, TypeVar, Generic, Any


@dataclass
class ModelBase:
    id: int


T = TypeVar('T', bound=ModelBase)


class NotFoundError(Exception):
    pass


class NotFoundErrorMeta(type):

    def __init__(cls: Any, name: Any, bases: Any, attrs: Any):
        super().__init__(name, bases, attrs)
        cls.NotFoundError = type("NotFoundError",
                                 (NotFoundError,),
                                 {
                                     "__qualname__": cls.__qualname__ + ".NotFoundError"
                                 })


class QueryBase(Generic[T], metaclass=NotFoundErrorMeta):

    class NotFoundError(Exception):
        pass

    def __init__(self, models: List[T]):
        self.models = models

    def all(self) -> List[T]:
        return self.models

    def get(self, id: int) -> T:
        for model in self.models:
            if model.id == id:
                return model

        raise self.NotFoundError()

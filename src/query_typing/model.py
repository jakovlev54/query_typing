from dataclasses import dataclass

from query_typing.model_base import ModelBase, QueryBase


@dataclass
class EmployeeModel(ModelBase):
    department_id: int | None
    name: str


class EmployeeQuery(QueryBase[EmployeeModel]):
    pass


@dataclass
class DepartmentModel(ModelBase):
    parent_id: int | None
    name: str


class DepartmentQuery(QueryBase[DepartmentModel]):
    pass

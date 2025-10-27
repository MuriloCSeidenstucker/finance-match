from dataclasses import dataclass


@dataclass
class Expense:

    id: str
    title: str
    amount: float
    details: str
    action: str

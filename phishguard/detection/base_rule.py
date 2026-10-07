from abc import ABC, abstractmethod

from .models import Message, RuleMatch


class BaseRule(ABC):
    """The template every detection rule must follow."""
    rule_id: str = ""
    name: str = ""
    weight: float = 0.0
    explanation: str = ""

    @abstractmethod
    def evaluate(self, message: Message) -> list[RuleMatch]:
        """Check the message and return a RuleMatch for each red flag found."""
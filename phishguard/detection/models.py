from dataclasses import dataclass, field


@dataclass
class Message:
    """A message after preprocessing, ready for the detection rules."""
    original_text: str
    normalized_text: str
    urls: list[str] = field(default_factory=list)


@dataclass
class RuleMatch:
    """One piece of evidence found by a detection rule."""
    rule_id: str
    name: str
    weight: float
    explanation: str
    matched_text: str
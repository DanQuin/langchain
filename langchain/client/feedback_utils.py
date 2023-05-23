"""Feedback Utilities."""

from abc import abstractmethod
from typing import Any, Dict, List, Optional

from pydantic import BaseModel


class EvalResult(BaseModel):
    """Evaluation result."""

    metric_name: str
    """The feedback metric name or type."""
    score: Optional[float] = None
    """The score of the feedback metric. If not provided,
    
    the result will be treated as a tag."""
    comment: Optional[str] = None
    """The reasoning for the score."""


class Evaluator:
    @abstractmethod
    def get_metadata(self) -> Dict[str, Any]:
        """Get the configuration metadata of the chain."""

    @abstractmethod
    def evaluate(
        self,
        inputs: Dict[str, Any],
        outputs: Dict[str, Any],
        references: Optional[Dict[str, Any]],
    ) -> List[EvalResult]:
        """Run the evaluation chain on the given inputs and optional reference outputs."""

    @abstractmethod
    async def aevaluate(
        self,
        inputs: Dict[str, Any],
        outputs: Dict[str, Any],
        references: Optional[Dict[str, Any]],
    ) -> List[EvalResult]:
        """Run the evaluation chain on the given inputs and optional reference outputs."""

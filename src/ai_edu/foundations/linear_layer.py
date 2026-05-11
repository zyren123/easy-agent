"""Shared metadata for the first foundations lesson."""

from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class LinearLayerLesson:
    """Small contract describing the first foundations module."""

    section: str = "foundations"
    module_slug: str = "01-linear-layer"
    title: str = "Linear layer from first principles"
    source_path: str = "foundations/01-linear-layer/lesson.py"
    notebook_path: str = "foundations/01-linear-layer/lesson.ipynb"

    def module_path(self) -> str:
        return f"{self.section}/{self.module_slug}"

from ai_edu import CURRICULUM_SECTIONS
from ai_edu.foundations import LinearLayerLesson


def test_curriculum_sections_are_frozen() -> None:
    assert CURRICULUM_SECTIONS == ("foundations", "training", "agents")


def test_linear_layer_lesson_metadata_matches_layout() -> None:
    lesson = LinearLayerLesson()

    assert lesson.module_path() == "foundations/01-linear-layer"
    assert lesson.source_path.endswith("lesson.py")
    assert lesson.notebook_path.endswith("lesson.ipynb")

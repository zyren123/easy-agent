"""Source-first walkthrough for the first linear-layer lesson."""

from ai_edu.foundations import LinearLayerLesson


def lesson_outline() -> list[str]:
    lesson = LinearLayerLesson()
    return [
        lesson.title,
        "Inputs and outputs are vectors with explicit dimensions.",
        "A linear layer applies weights and bias to produce a new representation.",
        f"Module path: {lesson.module_path()}",
    ]


if __name__ == "__main__":
    for line in lesson_outline():
        print(line)

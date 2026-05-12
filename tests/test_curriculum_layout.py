from pathlib import Path


def test_curriculum_sections_are_frozen() -> None:
    for section in ("foundations", "training", "agents"):
        assert Path(section).is_dir()


def test_linear_layer_module_matches_expected_layout() -> None:
    module_dir = Path("foundations/01-linear-layer")

    assert module_dir.is_dir()
    assert (module_dir / "README.md").is_file()
    assert (module_dir / "linear_layer.py").is_file()
    assert (module_dir / "linear_layer.ipynb").is_file()

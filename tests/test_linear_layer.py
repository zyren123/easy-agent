import math
import runpy
from types import ModuleType

import pytest


def _load_linear_layer_module() -> ModuleType:
    module_globals = runpy.run_path("foundations/01-linear-layer/linear_layer.py")
    module = ModuleType("linear_layer_module")
    module.__dict__.update(module_globals)
    return module


linear_layer_module = _load_linear_layer_module()
ReferenceLinearLayer = linear_layer_module.ReferenceLinearLayer
build_demo_reference_layer = linear_layer_module.build_demo_reference_layer
compare_demo_outputs = linear_layer_module.compare_demo_outputs


def test_demo_layer_forward_matches_lesson_example() -> None:
    layer = build_demo_reference_layer()

    assert layer.forward((2.0, -1.0, 0.5)) == (3.1, 2.55)


def test_explain_forward_returns_one_line_per_output_neuron() -> None:
    layer = build_demo_reference_layer()

    explanation = layer.explain_forward((2.0, -1.0, 0.5))

    assert len(explanation) == layer.output_dim
    assert explanation[0].startswith("output[0] = ")
    assert explanation[1].endswith("= 2.55")


def test_linear_layer_rejects_bias_length_mismatch() -> None:
    try:
        ReferenceLinearLayer(weights=((1.0, 2.0),), bias=(0.0, 1.0))
    except ValueError as exc:
        assert "bias must have one value per output neuron" in str(exc)
    else:
        raise AssertionError("Expected ValueError for bias length mismatch")


def test_linear_layer_rejects_wrong_input_dimension() -> None:
    layer = build_demo_reference_layer()

    try:
        layer.forward((1.0, 2.0))
    except ValueError as exc:
        assert "inputs must have length 3" in str(exc)
    else:
        raise AssertionError("Expected ValueError for wrong input dimension")


def test_reference_and_torch_outputs_match_on_demo_input() -> None:
    torch = pytest.importorskip("torch")
    assert torch is not None

    reference_output, torch_output = compare_demo_outputs()

    assert len(reference_output) == len(torch_output)
    for left, right in zip(reference_output, torch_output, strict=True):
        assert math.isclose(left, right, rel_tol=1e-6, abs_tol=1e-6)


def test_demo_still_runs_without_torch_dependency() -> None:
    demo_lines = linear_layer_module.demo()

    assert demo_lines[0] == "Linear layer demo"
    assert any(line.startswith("Reference output: ") for line in demo_lines)

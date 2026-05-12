"""A minimal linear layer shown in both torch and non-framework form."""

from dataclasses import dataclass
from typing import Any

try:
    import torch
    from torch import Tensor, nn
except ModuleNotFoundError:  # pragma: no cover - depends on local environment
    torch = None
    Tensor = Any
    nn = None

Vector = tuple[float, ...]
Matrix = tuple[Vector, ...]


def _validate_vector(name: str, values: Vector, *, expected_length: int | None = None) -> None:
    if not values:
        raise ValueError(f"{name} must not be empty")
    if expected_length is not None and len(values) != expected_length:
        raise ValueError(f"{name} must have length {expected_length}")


def _validate_matrix(name: str, rows: Matrix) -> None:
    if not rows:
        raise ValueError(f"{name} must not be empty")
    row_length = len(rows[0])
    if row_length == 0:
        raise ValueError(f"{name} rows must not be empty")
    for index, row in enumerate(rows):
        if len(row) != row_length:
            raise ValueError(f"{name} row {index} must have length {row_length}")


@dataclass(frozen=True, slots=True)
class ReferenceLinearLayer:
    """A tiny linear layer using plain Python tuples."""

    weights: Matrix
    bias: Vector

    def __post_init__(self) -> None:
        _validate_matrix("weights", self.weights)
        _validate_vector("bias", self.bias)
        if len(self.weights) != len(self.bias):
            raise ValueError("bias must have one value per output neuron")

    @property
    def input_dim(self) -> int:
        return len(self.weights[0])

    @property
    def output_dim(self) -> int:
        return len(self.weights)

    def forward(self, inputs: Vector) -> Vector:
        """Apply y = Wx + b."""
        _validate_vector("inputs", inputs, expected_length=self.input_dim)
        return tuple(
            sum(weight * value for weight, value in zip(row, inputs, strict=True)) + bias_value
            for row, bias_value in zip(self.weights, self.bias, strict=True)
        )

    def explain_forward(self, inputs: Vector) -> tuple[str, ...]:
        """Explain how each output neuron is computed."""
        outputs = self.forward(inputs)
        steps: list[str] = []
        for output_index, (row, bias_value, output_value) in enumerate(
            zip(self.weights, self.bias, outputs, strict=True)
        ):
            terms = " + ".join(
                f"({weight:g} * {value:g})" for weight, value in zip(row, inputs, strict=True)
            )
            steps.append(
                f"output[{output_index}] = {terms} + {bias_value:g} = {output_value:g}"
            )
        return tuple(steps)


if nn is not None:

    class TorchLinearLayer(nn.Module):
        """A torch version with weights compatible with later training code."""

        def __init__(self, input_dim: int, output_dim: int) -> None:
            super().__init__()
            self.linear = nn.Linear(input_dim, output_dim, bias=True)

        def forward(self, inputs: Tensor) -> Tensor:
            return self.linear(inputs)

else:

    class TorchLinearLayer:  # pragma: no cover - depends on local environment
        """Placeholder used when torch is unavailable locally."""

        def __init__(self, input_dim: int, output_dim: int) -> None:
            raise RuntimeError("torch is required for TorchLinearLayer")


def build_demo_reference_layer() -> ReferenceLinearLayer:
    """Return the fixed example used across the module."""
    return ReferenceLinearLayer(
        weights=((0.5, -1.0, 2.0), (1.5, 0.0, -0.5)),
        bias=(0.1, -0.2),
    )


def tensor_from_vector(values: Vector) -> Tensor:
    if torch is None:
        raise RuntimeError("torch is required for tensor_from_vector")
    return torch.tensor(values, dtype=torch.float32)


def build_demo_torch_layer() -> TorchLinearLayer:
    if torch is None:
        raise RuntimeError("torch is required for build_demo_torch_layer")
    reference = build_demo_reference_layer()
    layer = TorchLinearLayer(reference.input_dim, reference.output_dim)
    with torch.no_grad():
        layer.linear.weight.copy_(torch.tensor(reference.weights, dtype=torch.float32))
        layer.linear.bias.copy_(torch.tensor(reference.bias, dtype=torch.float32))
    return layer


def compare_demo_outputs() -> tuple[Vector, Vector]:
    """Return reference and torch outputs for the same fixed example."""
    if torch is None:
        raise RuntimeError("torch is required for compare_demo_outputs")
    inputs = (2.0, -1.0, 0.5)
    reference_output = build_demo_reference_layer().forward(inputs)
    torch_output = build_demo_torch_layer()(tensor_from_vector(inputs)).detach().tolist()
    return reference_output, tuple(float(value) for value in torch_output)


def demo() -> list[str]:
    """Return a simple text walkthrough for quick local checks."""
    layer = build_demo_reference_layer()
    inputs = (2.0, -1.0, 0.5)
    reference_outputs = layer.forward(inputs)
    lines = [
        "Linear layer demo",
        "Rule: y = Wx + b",
        f"Input dimension: {layer.input_dim}",
        f"Output dimension: {layer.output_dim}",
        f"Input: {inputs}",
        f"Reference output: {reference_outputs}",
    ]
    if torch is None:
        lines.append("Torch output: unavailable (install the optional torch dependency to compare)")
    else:
        _, torch_outputs = compare_demo_outputs()
        lines.append(f"Torch output: {torch_outputs}")
    lines.extend(
        [
            "",
            "Per-neuron breakdown:",
        ]
    )
    lines.extend(layer.explain_forward(inputs))
    if torch is None:
        lines.extend(
            [
                "",
                (
                    "The reference path still runs without torch; "
                    "the torch path is optional for parity checks."
                ),
            ]
        )
    else:
        lines.extend(
            [
                "",
                (
                    "Torch path matches the same example so later "
                    "training code can import it directly."
                ),
            ]
        )
    return lines


if __name__ == "__main__":
    for line in demo():
        print(line)

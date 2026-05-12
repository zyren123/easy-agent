# 01 Linear Layer

This module introduces the smallest useful neural-network building block: a
linear layer. If you understand this module, you can read the shape math behind
dense layers, MLP blocks, embeddings, and projection heads in larger models.

## Concept Overview

A linear layer takes an input vector and produces a new output vector.
It does this with one matrix multiply plus one bias add:

`y = Wx + b`

This is the basic pattern behind dense layers in neural networks.

## Why It Exists

Neural networks need a way to mix input features together.
A linear layer lets each output neuron look at the whole input vector and learn
which parts matter more.

## Core Math / Intuition

- `x` is the input vector
- `W` is the weight matrix
- `b` is the bias vector
- `y` is the output vector

If the input has dimension 3 and the output has dimension 2, then:

- `x` has shape `(3,)`
- `W` has shape `(2, 3)`
- `b` has shape `(2,)`
- `y` has shape `(2,)`

The rows of `W` answer a practical question: "what combination of input features should this
output neuron pay attention to?"

## Minimal Implementation

The main implementation for this module is in [`linear_layer.py`](./linear_layer.py).
That file contains two aligned paths:

- a torch implementation for later reuse in model training code
- a small non-framework reference implementation for inspection and comparison

## Step-by-Step Code Walkthrough

This module uses the same fixed example in `README.md`, `linear_layer.py`, and
`linear_layer.ipynb`:

```python
weights = (
    (0.5, -1.0, 2.0),
    (1.5, 0.0, -0.5),
)
bias = (0.1, -0.2)
inputs = (2.0, -1.0, 0.5)
```

Applying `y = Wx + b` gives:

```text
output[0] = (0.5 * 2.0) + (-1.0 * -1.0) + (2.0 * 0.5) + 0.1 = 3.1
output[1] = (1.5 * 2.0) + (0.0 * -1.0) + (-0.5 * 0.5) + -0.2 = 2.55
```

So the final output vector is `(3.1, 2.55)`.

The reference `forward()` method in `linear_layer.py` loops over each row of the weight
matrix, multiplies it with the input vector, sums the result, and adds the bias.

The torch path should produce the same numbers for the same weights, bias, and
input. That gives us a useful rule for later modules:

- use torch for the implementation path that training code will import
- keep a tiny reference path that proves the math and expected output
- if torch is not installed locally, the reference path should still run and the
  parity check can be skipped gracefully

## Common Failure Cases

- The bias vector has the wrong length for the number of output neurons
- The input vector has the wrong dimension
- The weight matrix rows do not all have the same length
- The code works numerically, but you lose track of the shapes mentally

This module raises explicit `ValueError`s for these mismatches so the failure is
easy to debug.

## Connection To Later Systems

- A fully connected layer in modern frameworks is this same operation.
- MLP blocks stack linear layers with nonlinear activations.
- Transformer attention also uses linear projections for queries, keys, values,
  and output mixing.

## Exercises / Extensions

- Change the input vector and recompute the output by hand
- Change one row of the weight matrix and explain how one output neuron changes
- Remove the bias term and compare the result
- Re-implement the same layer with lists instead of tuples

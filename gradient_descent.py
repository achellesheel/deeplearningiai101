import math
import random

# -----------------------------
# Helper functions
# -----------------------------

def dot(a, b):
    """Dot product of two vectors"""
    s = 0.0
    for i in range(len(a)):
        s += a[i] * b[i]
    return s


def softmax(scores):
    """Compute softmax probabilities"""
    exp_scores = []
    total = 0.0

    for s in scores:
        e = math.exp(s)
        exp_scores.append(e)
        total += e

    probs = []
    for e in exp_scores:
        probs.append(e / total)

    return probs


# -----------------------------
# Initialization
# -----------------------------

V = 8   # vocabulary size
D = 4   # embedding dimension
lr = 0.1

# Center word vectors (v)
v = []
for i in range(V):
    v.append([random.uniform(-0.5, 0.5) for _ in range(D)])

# Output word vectors (u)
u = []
for i in range(V):
    u.append([random.uniform(-0.5, 0.5) for _ in range(D)])

# Choose one training example
c = 2   # center word index
o = 5   # true output word index

print("Center word index:", c)
print("True output word index:", o)
print("\nInitial center vector v[c]:", v[c])
print("Initial true output vector u[o]:", u[o])


# -----------------------------
# Forward Pass
# -----------------------------

scores = []
for x in range(V):
    score = dot(u[x], v[c])
    scores.append(score)

print("\nScores (u_x · v_c):")
for i, s in enumerate(scores):
    print(f"word {i}: {s:.4f}")

probs = softmax(scores)

print("\nProbabilities p(x|c):")
for i, p in enumerate(probs):
    print(f"word {i}: {p:.4f}")

print("\nSum of probabilities:", sum(probs))


# -----------------------------
# Pointer 1: Update center vector v_c
# -----------------------------
# v_c ← v_c − η ( Σ p(x|c)u_x − u_o )

grad_vc = [0.0] * D

# Compute Σ p(x|c)u_x
for x in range(V):
    for d in range(D):
        grad_vc[d] += probs[x] * u[x][d]

# Subtract u_o
for d in range(D):
    grad_vc[d] -= u[o][d]

print("\nGradient for center vector v[c]:", grad_vc)

# Update v_c
for d in range(D):
    v[c][d] -= lr * grad_vc[d]

print("Updated center vector v[c]:", v[c])


# -----------------------------
# Pointer 2: Update true output vector u_o
# -----------------------------
# u_o ← u_o − η (p(o|c) − 1) v_c

print("\nUpdating true output vector u[o]")

for d in range(D):
    u[o][d] -= lr * (probs[o] - 1) * v[c][d]

print("Updated true output vector u[o]:", u[o])


# -----------------------------
# Pointer 3: Update all other output vectors u_x (x ≠ o)
# -----------------------------
# u_x ← u_x − η p(x|c) v_c

print("\nUpdating other output vectors:")

for x in range(V):
    if x == o:
        continue

    print(f"Before update u[{x}]:", u[x])

    for d in range(D):
        u[x][d] -= lr * probs[x] * v[c][d]

    print(f"After update u[{x}]: ", u[x])

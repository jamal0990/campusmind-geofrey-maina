# CampusMind Minimax Hand Trace

## Cafeteria Subtree

MAX starts at Main Gate and chooses Cafeteria.

The Cafeteria node is then a MIN node.

### Cafeteria - MIN

MIN has two possible moves:

1. Main Gate
2. Student Affairs

---

### 1. Cafeteria → Main Gate

Main Gate is a MAX node.

MAX has two possible moves:

- Administration Block → utility = -1
- Cafeteria → utility = 3

MAX chooses:

```text
max(-1, 3) = 3
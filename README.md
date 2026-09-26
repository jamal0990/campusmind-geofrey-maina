Full Name: Geofrey Maina
Admission Number: SCT-253-007/2022

# CampusMind — Week 4: Minimax and Alpha-Beta Pruning

## Overview

This project implements the CampusMind Challenge game using Minimax and Alpha-Beta pruning.

The game uses the existing CampusMind campus graph. MAX moves first from Main Gate, and the game lasts for 3 plies.

## Game Rules

- Starting location: Main Gate
- MAX moves first
- MAX and MIN alternate turns
- The game lasts for 3 plies
- No changes were made to the game rules

## Utility Function

The utility of a location is calculated as:

```text
utility(location) =
hop_distance(location, Library)
-
hop_distance(location, Cafeteria)
Admin branch: -1
Cafeteria branch: 3
Full game: 3
Terminal states evaluated: 9
Therefore, the value of the full game starting from Main Gate is: 3

Alpha-Beta pruning was implemented as an optimization of Minimax.

Results:

Alpha-Beta value: 3
Terminal states evaluated: 7

Hand Trace

The Cafeteria subtree was traced manually.

At Cafeteria, MIN has two possible moves:

Cafeteria → Main Gate
Cafeteria → Student Affairs

For the Main Gate branch, MAX chooses the higher utility:

max(-1, 3) = 3

For the Student Affairs branch, MAX chooses the higher utility:

max(3, 0) = 3

Therefore MIN chooses:

min(3, 3) = 3

So the Cafeteria branch has a Minimax value of:

3

MIN Moves First Extension

The game was also extended so that MIN moves first.

Results:

New game value: -1

MIN first move values:
Administration Block value: -1
Cafeteria value: 0

Therefore, when MIN moves first from Main Gate, the resulting game value is:

-1

 ```text




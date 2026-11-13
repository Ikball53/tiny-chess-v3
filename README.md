# tiny-chess v3

A chess engine in 4,096 bytes of Python for the make.fun tiny-chess-01
competition. Built on the v2 engine (0x88 board, negamax + alpha-beta +
quiescence + transposition table + tapered piece-square eval), with:

- **LMR** (late-move reductions) for quiet moves at depth ≥ 3.
- **Killer moves** (2 per ply) in the move ordering.
- **Repetition detection** on the search path (draw score), so the engine
  stops shuffling into endless games.
- **Bishop-pair bonus** (+6 mg) in the eval.
- **Node scaling**: long games (> 120 plies) use 1/3 of the node budget,
  keeping the 16-game trial inside the wall.
- Max depth 12, default 60,000 nodes per move (override with CHESS_NODES).

Dropped for the 4 KB limit (kept in the full build, `work/v3_dense_full.py`):
null-move pruning and the passed-pawn eval. The packed `main.py` is an
lzma + base85 blob that unpacks and executes the dense source.

## Files

- `main.py` — the entry (packed, 4,093 bytes).
- `README.md` — this file.
- `LICENSE` — MIT.
- `.makefun/owner.json` — payout wallet.
- `work/` — build scripts, dense source, perft + head-to-head harnesses.

## How it was measured

Perft passes on all standard positions (startpos, Kiwipete, pos3–pos6,
en-passant). Elo is measured head-to-head against the v2 engine at a common
12,000-node budget over the 8 gauntlet openings × both colours (16 games),
then anchored to v2's ~1,190 Elo. A real gauntlet trial against the house
engines (kit `program/env/server.mjs` + `program/scorer/score.mjs`) gives the
ground-truth Elo.

Measured so far:

- **Full-feature v3** (LMR + null-move + killers + passed pawns + bishop
  pair + repetition, kept in `work/v3_dense_full.py`, 4,463 packed bytes —
  over the limit): **10W–3L–3D vs v2 at 12k nodes → +163 Elo, ≈ 1,353 Elo**
  (95% CI on the diff: −1 to +475; 16 games is a small sample).
- **Real gauntlet trial (ground truth, practice trial-0, 60k nodes)**:
  **Elo 1,290** — 5W–3D–8L over 16 games, wall 1,830 s (well inside the
  3,600 s limit). Beat all three depth rungs without a loss (depth-2/3/4:
  3W–3D–0L) and upset nodes-250k and nodes-1M as White; lost all games vs
  nodes-500k and nodes-2M. As White 5W–0D–3L; as Black 0W–3D–5L.
  **Clears the 1,154 practice floor by 136 points.** Below the 1,500 target
  and the ~1,700 top-20 cutoff — the 4 KB / ~20k-nodes-per-second ceiling
  is the wall, reported honestly.

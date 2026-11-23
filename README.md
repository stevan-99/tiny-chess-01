# tiny-chess-01

[![make.fun · tiny-chess-01](https://make.fun/badge/tiny-chess-01.svg)](https://make.fun/bounty/tiny-chess-01?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01)
[![rank](https://make.fun/badge/tiny-chess-01/stevan-99/tiny-chess-01/rank.svg)](https://make.fun/bounty/tiny-chess-01/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01)
[![reward](https://make.fun/badge/tiny-chess-01/stevan-99/tiny-chess-01/reward.svg)](https://make.fun/bounty/tiny-chess-01?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01)

A golfed chess engine: alpha-beta negamax with a transposition table,
quiescence search, null-move and futility pruning, packed as one 4 KB
`main.py` (the kit's `makefun compress` packs it from `engine_src.py`).
It plays over the env bridge and searches to a fixed node cap, never a
clock, so a replayed trial plays the same moves.

## Run it

```sh
python3.13 main.py
```

The harness sets `MAKEFUN_ENV_URL`; the engine polls `/game` and answers
`/move`.

---

<sub>Entered on [make.fun](https://make.fun/?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01) · AI agents build software for cash rewards</sub>

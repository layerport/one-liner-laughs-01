# One-Liner Laughs — Entry

![One-Liner Laughs](https://make.fun/badge/u-coral-404-one-liner-laughs-aa872d41.svg)
![Rank](https://make.fun/badge/u-coral-404-one-liner-laughs-aa872d41/layerport/one-liner-laughs-01/rank.svg)
![Reward](https://make.fun/badge/u-coral-404-one-liner-laughs-aa872d41/layerport/one-liner-laughs-01/reward.svg)

Entry for the [One-Liner Laughs](https://make.fun/bounty/u-coral-404-one-liner-laughs-aa872d41) bounty on make.fun.

## The joke

> My therapist said I need closure, so I closed all 47 browser tabs — now I have closure and no idea why I ever opened them.

A single original one-liner: the setup promises emotional closure, the payoff delivers it in the most literal, browser-tab way possible — and the cure wipes out the very thing it was supposed to fix.

## How it works

`main.py` (Python 3.13, standard library only) writes the fixed joke deterministically to `$OUTPUT_DIR/entry.txt` (default `/output/entry.txt`). No network, no randomness, no external reads — the same bytes on every run.

## Run it

```sh
OUTPUT_DIR=/tmp/out python3 main.py
cat /tmp/out/entry.txt
```

## License

MIT — see [LICENSE](LICENSE).

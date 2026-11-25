# Funniest Office Joke — make.fun entry

[![make.fun](https://make.fun/badge/u-kevin-the-funniest-office-joke-judged-head-to-head-3dc3233c.svg)](https://make.fun/c/u-kevin-the-funniest-office-joke-judged-head-to-head-3dc3233c)
[![rank](https://make.fun/badge/u-kevin-the-funniest-office-joke-judged-head-to-head-3dc3233c/shusay12/makefun-u-kevin-the-funniest-office-joke-judged-head-to-head-3dc3233c/rank.svg)](https://make.fun/c/u-kevin-the-funniest-office-joke-judged-head-to-head-3dc3233c)
[![reward](https://make.fun/badge/u-kevin-the-funniest-office-joke-judged-head-to-head-3dc3233c/shusay12/makefun-u-kevin-the-funniest-office-joke-judged-head-to-head-3dc3233c/reward.svg)](https://make.fun/c/u-kevin-the-funniest-office-joke-judged-head-to-head-3dc3233c)

An entry for [The Funniest Office Joke, Judged Head to Head](https://make.fun/c/u-kevin-the-funniest-office-joke-judged-head-to-head-3dc3233c) on [make.fun](https://make.fun): one joke about office life, judged two at a time by an AI judge.

## The joke

> I asked for a raise and got a pizza party, so I expensed my dignity as a team lunch — HR approved it.

101 characters, one line, UTF-8.

## How the entry works

`main.py` (Python 3, standard library only) writes that line to `entry.txt` under the output directory — `/output` by default, or `$MAKEFUN_OUTPUT_DIR` when set. It validates the line first (non-empty, at most 200 characters, single line, no ragged whitespace) and writes the same bytes on every run: no input, no files read, no network.

```sh
python3 main.py
```

## License

MIT — see [LICENSE](LICENSE).

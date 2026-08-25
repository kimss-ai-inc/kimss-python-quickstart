# Contributing

[kimss-ai-inc/kimss-python-quickstart](https://github.com/kimss-ai-inc/kimss-python-quickstart) is a **force-push mirror** of `kimss_quickstart/` in the Kimss API monorepo. Direct PRs to public `main` are overwritten on the next mirror.

## How to report issues

Use [GitHub Issues](https://github.com/kimss-ai-inc/kimss-python-quickstart/issues) on this repository. English is fine. Include the example script, Python version, and the error.

Security reports: see [SECURITY.md](SECURITY.md). Do not file public issues for vulnerabilities.

## How changes land

1. We patch `kimss_quickstart/` in the product repo.
2. CI there must keep the examples compiling (`python -m unittest discover -s tests`).
3. The mirror job force-pushes public `main`, then restores `.github/workflows/` (Scorecard, CodeQL, compile CI).

Acceptable contributions: fixes that keep the 5-minute tutorial accurate (env names, gateway URLs, Agent ID headers). No new product surface, no extra frameworks, no unpinned GitHub Actions.

## Tests

From the repo root:

```bash
python -m unittest discover -s tests
```

CI runs the same command on every push to `main`.

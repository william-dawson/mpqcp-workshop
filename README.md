# MPQCP workshop website

Website for the International Workshop on Massively Parallel Programming for
Quantum Chemistry and Physics, in English and Japanese.

- English: <https://william-dawson.github.io/mpqcp-workshop/>
- Japanese: <https://william-dawson.github.io/mpqcp-workshop/ja/>

Edit `data/workshop.yml` for anything factual (dates, venue, program,
registration), then push to `main`; GitHub Pages rebuilds automatically.

```sh
pip install -r requirements.txt
make html     # build into output/
make serve    # preview at http://localhost:8000
```

See [AGENTS.md](AGENTS.md) for how the site is put together.

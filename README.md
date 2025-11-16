# Tweet EMD Similarity

Compute semantic distances between Twitter accounts using Earth Mover's Distance (EMD) on tweet embeddings. Tweets are gently normalized, embedded with `sentence-transformers` (``all-MiniLM-L6-v2``), and compared with cosine-based ground costs inside a min-cost flow solver.

## Installation

```bash
pip install -r requirements.txt
```

## Usage

Run the quick CLI demo:

```bash
python tweet_emd.py --dataset data/tweets_400.csv
```

Draw the heatmap visualization:

```bash
python -c "import visualizations as V, tweet_emd as T; E=T.load_account_embeddings('data/tweets_400.csv'); V.plot_emd_heatmap(E)"
```

## Notes

- Cosine distance on L2-normalized vectors keeps costs in a tight [0, 2] range and matches the intuition of angle-based similarity.
- EMD measures the minimum effort to move tweet "mass" from one account to another; we solve it exactly with NetworkX `min_cost_flow`.
- NetworkX expects integer costs, so costs are scaled by ``10_000`` before solving and divided back afterward.

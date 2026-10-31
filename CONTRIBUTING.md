# Contributing

Corrections and new entries are welcome. The most useful contributions are replications that are missing from a study's record, especially failed, partial and non-English ones.

## Report a replication

1. Find the study in `data/studies.json`.
2. Add an object to its `replications` array: `title`, `url`, `by`, `year`, `outcome` and a one-sentence `summary`.
3. Set `outcome` the way the replicating authors describe their result. Use `extended` for follow-ups by the original team, or for work that tests new conditions without re-testing the original claim.
4. Update `replication_status` if the new replication changes it (see `SCHEMA.md`). Only replications by different authors count.

## Add a study

Check that it meets the inclusion criteria in `SCHEMA.md`, then add a record with every field filled where the information exists. Leave a field empty rather than guessing.

## Correct an entry

Edit the record and say in your pull request or message which source shows the correction.

## Rules for every entry

- Take links only from pages you have opened. Never type or complete a URL from memory.
- Prefer canonical pages: arXiv abstract pages, official repositories, official project pages.
- Write in your own words. Do not copy abstracts.
- UK spelling, plain sentences, no em-dashes.
- Never include harmful prompts or hazardous technical detail. Naming public benchmarks is fine.

## Rebuild

After editing the JSON, run:

```
python3 build/build.py
```

This validates the data, prints warnings (missing fields, values outside the allowed sets, suspicious links, statuses that do not match the listed replications), and regenerates the CSV files, `site/index.html` and `README.md`. Fix the warnings before submitting.

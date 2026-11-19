# FebSynth

Associated manuscript: **A clinically constrained synthetic dataset of febrile infants for hospitalization and ICU risk prediction**.

Synthetic visit-level data for hospitalization and intensive-care risk research in febrile infants aged 90 days or younger.

## Recommended Starting Point

Use [the constrained, stratified Gaussian copula table](output_en/evaluate_results/copula/synthetic_data.csv): **18,604 rows and 46 fields**. Each row is synthetic, not a matched copy of a particular patient. Other model tables support use-specific comparison; they are not independent clinical cohorts.

The [50,000-row extension](output_en/extended_release/copula/synthetic_data.csv) has its own evaluation results. Its size was selected using the sample-size sensitivity analysis.

## Read The Data

Run from this directory:

```python
from pathlib import Path
import pandas as pd

root = Path(".")
data = pd.read_csv(root / "output_en/evaluate_results/copula/synthetic_data.csv")
assert data.shape == (18604, 46)
hospitalization = data["Hospitalization"]
icu_cohort = data.loc[data["Hospitalization"].eq(1)].copy()
features = data.drop(columns=["Hospitalization", "ICU Admission"])
```

The table has 21 continuous fields, Sex, 22 symptom indicators and two binary outcomes. Retain blank symptom entries as missing; do not replace them with zero. Evaluation frequency tables represent missingness as `__MISSING__`. Sex is coded 0 for female and 1 for male. Units and definitions are recorded in the [author-verified data dictionary](docs/data_dictionary.csv). Do not use either outcome as a predictive input for the two documented tasks.

## Layout

| Directory | Contents | Existing result files |
|---|---|---:|
| `output_en/evaluate_results/` | Copula, CTGAN, TVAE and TabDDPM; 18,604 x 46 each | 364 |
| `output_en/ablation/grouping_and_constraints_effect/` | Neither component, constraints only, constraints plus stratification | 271 |
| `output_en/nsample_sensitivity/copula/` | Two tasks and mixed/synthetic-only branches | 34 |
| `output_en/extended_release/copula/` | 50,000 x 46 Copula extension and its evaluation | 91 |

The complete-constraint-and-stratification ablation reuses the main Copula run. Its 91 retained files are identical to their main-run counterparts and do not constitute an independent replicate. Its public directory includes an extra `copula/` level. Machine-specific paths in run metadata use `/path/to/...` examples; package-relative links retain their functional names.

## Documentation

The [results guide](docs/results_guide.pdf) defines result-file schemas, metrics, interpretation boundaries and exclusions. The [manuscript result map](docs/manuscript_result_map.csv) links figures, tables and text to package files. Metadata provide [resolved full-training constraints](metadata/constraints_resolved.json), an [aggregate split index](metadata/split_metadata.json) and [provenance](metadata/provenance.json), together with six configuration, terminology and dependency snapshots.

The [data description](docs/data_description.pdf) explains clinical fields, processing stages, missingness denominators and the [Chinese symptom dictionary](docs/symptom_dictionary.csv). The latter concatenates both author-supplied dictionaries, preserving 236 source rows and all lexical entries, including repeated standard names. It covers 196 distinct standard names; all 22 released symptom fields are mapped in the data dictionary. Expressions are for Chinese clinical narratives and are not translated. The two-column CSV stores the standard name first and a quoted, comma-separated synonym list second; it is not an English vocabulary or a list of negative symptom labels.

## Data Roles

The source cohort comprised 23,255 visits, split into 18,604 training and 4,651 held-out visits. Real reference data are not packaged. Hospitalization means admission within seven days of the index visit; ICU Admission occurs during the same clinical episode and implies Hospitalization.

In mixed sensitivity experiments, the generator uses dataset B (17,604 real visits), disjoint from the classifier's dataset A (1,000 real visits). Synthetic-only generators use the full 18,604-record training pool; classifiers use synthetic records only, with A used only for the real-only comparator. ICU training uses hospitalized subsets, so requested sample sizes are pre-filter sizes. Scenario means and SDs are based on successful repeats; all repeat statuses remain in the results.

## Exact Disclosure Scope

CCD `details.csv`, DCR `details.csv`, attribute-inference `details.csv` and UMAP `embedding.csv` are omitted. Only six `ccd_all_variables_*` plots per run are retained: mean and SD each have real-synthetic, real-real and distance-distribution views. Feature-specific CCD plots are omitted.

Other outputs are retained, including `lisi_details.csv`, all UMAP plots, attribute-level scores and group diagnostics. Evaluation files therefore include real-reference summaries and per-point LISI statistics. Privacy results characterise the evaluated protocols; they do not provide a formal privacy guarantee for individual or combined releases.

## File Integrity

`file_manifest.csv` indexes the files actually present, with SHA-256, byte counts and CSV dimensions. Its own row omits checksum and byte count to avoid recursion. `sha256` checks each published file. `source_sha256` records the source-file hash and can differ after path replacement or comment removal, as identified by `content_action`. Synthetic tables, numerical results and plots retain their source bytes.

The package contains 777 files, including `LICENSE.txt`. For citation and access information, consult the accompanying manuscript.

## Licences

Released data, evaluation outputs and original documentation: **CC BY 4.0**. The two Python configuration snapshots and the separate project code: **MIT**. See [LICENSE.txt](LICENSE.txt) for scope, the official CC BY terms and the MIT notice. Credit the FebSynth contributors and indicate changes when sharing adapted data.

## Use And Reproducibility Boundaries

The intended uses are exploratory modelling, teaching, pipeline development and synthetic augmentation. The records are not a substitute for real clinical evidence, external validation or causal identification. Larger generated tables do not increase the underlying clinical sample size.

Released aggregates and synthetic tables support inspection, but recalculating KS, DCR, TSTR and other real-reference metrics requires access to restricted real records. Original clinical tables, raw narratives and patient-level split assignments are not included. Model checkpoints are supplied in the separate code release, not in this data folder.

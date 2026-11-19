from __future__ import annotations

ML_UTILITY_TASK_CONFIGS: list[dict[str, object]] = [
    {
        "name": "predict_hospitalization",
        "target_column": "住院",
        "excluded_feature_columns": ["住院", "icu"],
        "minimum_rows": 20,
        "minimum_positive_rows": 5,
    },
    {
        "name": "predict_icu_within_hospitalized",
        "target_column": "icu",
        "subset_column": "住院",
        "subset_value": 1,
        "excluded_feature_columns": ["住院", "icu"],
        "minimum_rows": 20,
        "minimum_positive_rows": 5,
    }
]

CCD_GROUPING_CATEGORICAL_COLUMNS: list[str] = []

CCD_GROUPING_CONTINUOUS_COLUMNS: list[dict[str, object]] = [{"column": "计算年龄", "thresholds": []}]

CVT_RANGE_HISTOGRAM_COLUMNS: list[str] = ["白细胞计数", "淋巴细胞百分数"]
CVT_DIFFERENCE_COLUMN_PAIRS: list[tuple[str, str]] = [("住院", "icu")]

ATTRIBUTE_INFERENCE_N_ATT_LIST: list[int] = [10000]
ATTRIBUTE_INFERENCE_P_GIVEN_LIST: list[float] = [0.5, 0.75]
ATTRIBUTE_INFERENCE_K_LIST: list[int] = [1, 10]

ATTRIBUTE_INFERENCE_N_TOKEN_RANGE: int = 4

NSAMPLE_SENSITIVITY_N_MLU: int = 1000

NSAMPLE_SENSITIVITY_N_REPEATS: int = 100

NSAMPLE_SENSITIVITY_SYNTHETIC_MULTIPLIERS: list[float] = [0.5, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

NSAMPLE_SENSITIVITY_SYNTHETIC_ONLY_SAMPLE_SIZES: list[int] = [100, 500, 1000, 2000, 5000, 10000, 15000, 20000, 25000, 30000, 40000, 50000]

NSAMPLE_SENSITIVITY_TASK_CONFIGS: list[dict[str, object]] = [
    {
        "name": "predict_hospitalization",
        "target_column": "住院",
        "excluded_feature_columns": ["住院", "icu"],
        "minimum_rows": 20,
        "minimum_positive_rows": 5,
    },
    {
        "name": "predict_icu_within_hospitalized",
        "target_column": "icu",
        "subset_column": "住院",
        "subset_value": 1,
        "excluded_feature_columns": ["住院", "icu"],
        "minimum_rows": 20,
        "minimum_positive_rows": 5,
    }
]

NSAMPLE_SENSITIVITY_TASK_CONFIG: dict[str, object] = NSAMPLE_SENSITIVITY_TASK_CONFIGS[0]

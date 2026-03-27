import json

from strands import tool

from ingestion_agent.utils.loader import load_dataset


@tool
def describe_dataset(file_path: str) -> str:
    """Returns the shape, column names, data types, and first 5 rows of a dataset.
    Use this as the first step when analyzing any dataset.
    """
    df = load_dataset(file_path)
    result = {
        "shape": {"rows": df.height, "columns": df.width},
        "columns": {col: str(dtype) for col, dtype in zip(df.columns, df.dtypes)},
        "sample": df.head(5).to_dicts(),
    }
    return json.dumps(result, default=str)

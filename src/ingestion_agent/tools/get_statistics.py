import json

from strands import tool

from ingestion_agent.utils.loader import load_dataset


@tool
def get_statistics(file_path: str) -> str:
    """Returns descriptive statistics for all columns in the dataset,
    including count, mean, std, min, max and percentiles for numeric columns,
    and count and null count for non-numeric columns.
    """
    df = load_dataset(file_path)
    return json.dumps(df.describe().to_dicts(), default=str)

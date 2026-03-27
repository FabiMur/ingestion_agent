import polars as pl


def load_dataset(file_path: str) -> pl.DataFrame:
    ext = file_path.rsplit(".", 1)[-1].lower()
    loaders = {
        "csv": pl.read_csv,
        "tsv": lambda p: pl.read_csv(p, separator="\t"),
        "json": pl.read_json,
        "xlsx": pl.read_excel,
        "xls": pl.read_excel,
        "parquet": pl.read_parquet,
    }
    loader = loaders.get(ext)
    if loader is None:
        raise ValueError(
            f"Unsupported format: .{ext}. Supported: csv, tsv, json, xlsx, xls, parquet"
        )
    return loader(file_path)

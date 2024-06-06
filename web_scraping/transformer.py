import pandas as pd
import re
import logging

logging.basicConfig(level=logging.INFO)

def is_money_milliar(string_money: str) -> bool:
    return string_money.lower().endswith("miliar")

def transform_money_format(string_money: str) -> float:
    clean_string = string_money.replace(",", ".").replace(" ", "")
    return float(re.sub(r"[^\d.]", "", clean_string))

def transform(df, tahun):
    logging.info("Transformasi Dataframe . . .")

    column_mapping = {
        "Nomor Urut": "nomor_urut",
        "Nama": "nama",
        "Perusahaan": "perusahaan",
        "Kekayaan Bersih (US$)": "kekayaan_bersih_usd"
    }

    renamed_df = df.rename(columns=column_mapping)
    renamed_df['tahun'] = tahun
    renamed_df['kekayaan_bersih_usd_juta'] = renamed_df['kekayaan_bersih_usd'].apply(
        lambda value: transform_money_format(value) * 1000 if is_money_milliar(value) else transform_money_format(value)
    )

    return renamed_df[["nomor_urut", "nama", "perusahaan", "kekayaan_bersih_usd_juta", "tahun"]]
import numpy as np
import pandas as pd


def clean_prices(df: pd.DataFrame) -> pd.DataFrame:
    """Cleaning kolom harga: buang simbol, koma, dan ubah ke float."""

    df = df.copy()

    df['discounted_price'] = (
        df['discounted_price']
        .astype(str)
        .str.replace('₹', '', regex=False)
        .str.replace(',', '', regex=False)
        .replace('', np.nan)
        .astype(float)
    )

    df['actual_price'] = (
        df['actual_price']
        .astype(str)
        .str.replace('₹', '', regex=False)
        .str.replace(',', '', regex=False)
        .replace('', np.nan)
        .astype(float)
    )

    df['discount_percentage'] = (
        df['discount_percentage']
        .astype(str)
        .str.replace('%', '', regex=False)
        .replace('', np.nan)
        .astype(float)
    )

    return df


def clean_ratings(df: pd.DataFrame) -> pd.DataFrame:
    """Cleaning rating dan rating_count supaya aman dari NaN & simbol aneh."""

    df = df.copy()

    # Bersihkan rating
    df['rating'] = (
        df['rating']
        .astype(str)
        .replace(['|', '-', 'nan', 'N/A', 'None', ''], np.nan)
    )
    df['rating'] = pd.to_numeric(df['rating'], errors='coerce')

    # Bersihkan rating_count
    df['rating_count'] = (
        df['rating_count']
        .astype(str)
        .str.replace(',', '', regex=False)
        .replace(['nan', 'None', ''], np.nan)
    )
    df['rating_count'] = pd.to_numeric(df['rating_count'], errors='coerce')

    # Drop baris yang rating-nya beneran kosong
    df = df.dropna(subset=['rating'])

    return df


def split_main_category(df: pd.DataFrame) -> pd.DataFrame:
    """Ambil kategori utama dari kolom 'category'."""

    df = df.copy()

    df['main_category'] = (
        df['category']
        .astype(str)
        .str.split('|')
        .str[0]
    )

    return df

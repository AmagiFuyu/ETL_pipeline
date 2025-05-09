def transform_data(df):
    df = df.copy()

    # Hapus produk tidak valid
    df = df[df["title"].str.strip().str.lower() != "unknown product"]

    # Hapus duplikat dan NaN
    df.drop_duplicates(inplace=True)
    df.dropna(inplace=True)

    # Konversi kolom harga ke rupiah
    df["price"] = df["price"].str.replace("$", "").astype(float) * 16000
    df["price"] = df["price"].astype(int)

    # Konversi rating
    df["rating"] = df["rating"].str.extract(r"([\d.]+)").astype(float)

    # Ambil angka dari kolom colors
    df["colors"] = df["colors"].str.extract(r"(\d+)").astype(int)

    # Bersihkan teks dari size dan gender
    df["size"] = df["size"].str.replace("Size: ", "")
    df["gender"] = df["gender"].str.replace("Gender: ", "")

    # Tambahkan kolom timestamp
    from datetime import datetime
    df["timestamp"] = datetime.now().isoformat()

    return df
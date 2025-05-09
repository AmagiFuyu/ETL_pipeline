from utils.extract import extract_data
from utils.transform import transform_data
from utils.load import save_to_csv, save_to_google_sheets

def main():
    print("🔍 Mulai proses Extract...")
    df_raw = extract_data()
    print(">> Kolom hasil extract:", df_raw.columns.tolist())
    print(df_raw.head())

    print("🛠️ Mulai proses Transform...")
    df_clean = transform_data(df_raw)

    print("💾 Menyimpan ke CSV...")
    save_to_csv(df_clean, filename="products.csv")

    print("☁️ Menyimpan ke Google Sheets...")
    save_to_google_sheets(df_clean, creds_file="google-sheets-api.json")

    print("✅ ETL pipeline selesai.")

if __name__ == "__main__":
    main()
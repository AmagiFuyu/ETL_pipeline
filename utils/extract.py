import requests
from bs4 import BeautifulSoup
import pandas as pd
from datetime import datetime

def extract_data():
    all_products = []

    for page in range(1, 51):
        url = "https://fashion-studio.dicoding.dev/" if page == 1 else f"https://fashion-studio.dicoding.dev/page{page}"
        print(f"Scraping {url}...")

        headers = {
            "User-Agent": "Mozilla/5.0"
        }

        response = requests.get(url, headers=headers)
        if response.status_code != 200:
            print(f"Gagal mengambil {url}")
            continue

        soup = BeautifulSoup(response.text, "html.parser")
        product_cards = soup.find_all("div", class_="collection-card")

        for card in product_cards:
            title_el = card.find("h3")
            price_el = card.find("span", class_="price")

            # Ambil semua <p> dalam .product-details
            detail_section = card.find("div", class_="product-details")
            p_tags = detail_section.find_all("p") if detail_section else []

            rating, colors, size, gender = None, None, None, None

            for p in p_tags:
                text = p.text.strip()
                if "Rating:" in text:
                    rating = text.replace("Rating:", "").replace("⭐", "").strip()
                elif "Colors" in text:
                    colors = text.replace("Colors", "").strip()
                elif "Size:" in text:
                    size = text.replace("Size:", "").strip()
                elif "Gender:" in text:
                    gender = text.replace("Gender:", "").strip()

            all_products.append({
                "title": title_el.text.strip() if title_el else None,
                "price": price_el.text.strip() if price_el else None,
                "rating": rating,
                "colors": colors,
                "size": size,
                "gender": gender,
                "timestamp": datetime.now().isoformat()
            })

    df = pd.DataFrame(all_products)
    print(f">> Total produk yang berhasil dikumpulkan: {len(df)}")
    return df
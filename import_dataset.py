import os
import zipfile
from pathlib import Path

def download_and_extract_kaggle_dataset(dataset_name: str, target_dir: str = "data"):
    kaggle_json_path = Path.home() / ".kaggle" / "kaggle.json"
    
    if not kaggle_json_path.exists():
        raise FileNotFoundError("Kaggle API key not found at ~/.kaggle/kaggle.json. "
                                "Make sure you've placed it there.")

    os.makedirs(target_dir, exist_ok=True)

    dataset_slug = dataset_name.split("/")[-1]
    zip_path = os.path.join(target_dir, f"{dataset_slug}.zip")
    extracted_dir = os.path.join(target_dir, dataset_slug)

    # Skip download if folder already exists
    if os.path.exists(extracted_dir):
        print(f"✅ Dataset already downloaded at '{extracted_dir}'")
        return extracted_dir

    print("⬇️ Downloading dataset...")
    os.system(f"kaggle datasets download -d {dataset_name} -p {target_dir}")

    print("📦 Extracting dataset...")
    with zipfile.ZipFile(zip_path, "r") as zip_ref:
        zip_ref.extractall(target_dir)

    print("✅ Dataset ready at:", extracted_dir)
    return extracted_dir


if __name__ == "__main__":
    download_and_extract_kaggle_dataset("paultimothymooney/chest-xray-pneumonia")

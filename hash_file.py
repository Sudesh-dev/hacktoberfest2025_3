import hashlib
from pathlib import Path

def hash_file(file_path: str, algorithm: str = "sha256") -> str:
    """
    Generate a secure hash (SHA256, MD5, etc.) for the given file.
    """
    path = Path(file_path)
    if not path.exists():
        raise FileNotFoundError(f"File not found: {file_path}")

    hash_func = getattr(hashlib, algorithm, None)
    if not hash_func:
        raise ValueError(f"Unsupported hash algorithm: {algorithm}")

    hasher = hash_func()
    with path.open("rb") as file:
        for chunk in iter(lambda: file.read(4096), b""):
            hasher.update(chunk)
    return hasher.hexdigest()


if __name__ == "__main__":
    file_path = input("Enter file path to hash: ")
    algorithm = input("Enter hash algorithm (sha256/md5/sha1): ") or "sha256"
    try:
        print(f"{algorithm.upper()} hash:", hash_file(file_path, algorithm))
    except Exception as e:
        print("Error:", e)

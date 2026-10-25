"""Download the public datasets the modules use into data/raw/ and verify them.

Usage (from the project root): python data/get_data.py

The files are public research datasets, but their licences do not clearly allow
redistribution, so they are NOT in this repo (data/raw/ is gitignored). The
notebooks keep their outputs, so every number can still be read without them.

Each file is checked against a fixed SHA-256 checksum, so a changed file fails loudly.
"""
import hashlib
import urllib.request
from pathlib import Path

RAW = Path(__file__).resolve().parent / "raw"

NBER = "https://users.nber.org/~rdehejia/data/"
MIXTAPE = "https://raw.githubusercontent.com/scunning1975/mixtape/master/"

# file name -> (URL, SHA-256, used for)
FILES = {
    "nsw_dw.dta": (NBER + "nsw_dw.dta",
                   "d1bd2680a1c6f799f1c6d2455bf29633fdf19be01cb19490621c20a560b4e072",
                   "NSW job-training experiment, Dehejia-Wahba sample (Modules 1-6)"),
    "psid_controls.dta": (NBER + "psid_controls.dta",
                          "7beebae8928035d6abf662b994ce77a4fbea7ae6575037ff94e92fe099b43e14",
                          "PSID non-experimental comparison group (Modules 1-6)"),
    "cps_controls.dta": (NBER + "cps_controls.dta",
                         "80f0123eaf723870bd060ba9f8569617a7cb519a462dc20badbfb3443cd8374b",
                         "CPS non-experimental comparison group (robustness, Modules 10-11)"),
    "castle.dta": (MIXTAPE + "castle.dta",
                   "804633c161827b6c0824f86f239046386d1a8266a866f83bf5ddb2aa762a5f29",
                   "Castle-doctrine state panel, staggered adoption (Module 6, Part 2)"),
    "card.dta": (MIXTAPE + "card.dta",
                 "08a70a6c187c28c150defc8e3f9e6f89fd44cdf34b2aa2ed8cf3d084c78d9171",
                 "Card (1995) schooling and college proximity (Module 7)"),
    "AEJfigs.dta": ("https://www.masteringmetrics.com/wp-content/uploads/2015/01/AEJfigs.dta",
                    "271338b338c6742a39f23a486d2e11e236926a0e33c2a6629d983df20f38a7bc",
                    "Minimum legal drinking age mortality by age (Module 8)"),
    "smoking.dta": (MIXTAPE + "smoking.dta",
                    "3f5de21351fef721b745a9a8b03f410a80206f2d35927ffac27e481c9683c3d2",
                    "California Proposition 99 cigarette sales panel (Module 9)"),
}


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> None:
    RAW.mkdir(exist_ok=True)
    for name, (url, expected, _) in FILES.items():
        target = RAW / name
        if not target.exists():
            urllib.request.urlretrieve(url, target)
        got = sha256(target)
        if got != expected:
            raise ValueError(f"{name}: checksum {got} does not match the expected {expected}")
        print(f"ok  {name}")


if __name__ == "__main__":
    main()

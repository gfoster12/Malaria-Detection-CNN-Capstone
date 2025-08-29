## 🔌 Quick CLI Inference
```bash
python src/predict.py path/to/image.png
# or
MODEL_PATH=models/malaria_vgg16.h5 python src/predict.py path/to/image.png
```

## ⚙️ Reproducible Environment
```bash
python -m venv .venv && source .venv/bin/activate
pip install -r requirements-lock.txt
```

## 🛡️ CI
Minimal GitHub Actions workflow at `.github/workflows/ci.yml` runs ruff + smoke test.

## 📑 Model Card
See **MODEL_CARD.md**.

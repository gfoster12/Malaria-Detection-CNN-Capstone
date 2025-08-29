# Model Card — Malaria Detection CNN (VGG16-based)

## Overview
Binary classifier on 64×64 RBC tiles. Research/educational use only — **not a medical device**.

## Data
- NIH Malaria Dataset (thin smears, Giemsa). 
- Preprocessing: 64×64 resize, normalization, augmentation.

## Metrics (targets)
- Accuracy ≥ 0.95; Parasitized recall ≥ 0.97; Latency ≤ 50–100 ms (GPU).

## Risks & Limitations
- Domain shift across microscopes/stains.
- Possible label noise; class imbalance.
- Not robust to non-RBC artifacts.

## Ethics
- Do not deploy clinically without IRB/regulatory alignment (TRIPOD‑AI, GMLP).
- Human oversight required.

## Environment
See `requirements-lock.txt` for pinned versions.

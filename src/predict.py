import argparse, os, sys, json, numpy as np, cv2, tensorflow as tf
from tensorflow.keras.applications.vgg16 import preprocess_input
MODEL_PATH = os.environ.get("MODEL_PATH", "models/malaria_vgg16.h5")
def load_model(path):
    if not os.path.exists(path):
        sys.stderr.write(f"[warn] Model not found at '{path}'. Place your trained Keras model there or set MODEL_PATH.\n")
        sys.exit(2)
    return tf.keras.models.load_model(path)
def read_image(p):
    img = cv2.imread(p)
    if img is None:
        raise FileNotFoundError(p)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    img = cv2.resize(img, (64,64)).astype('float32')
    x = preprocess_input(np.expand_dims(img, 0))
    return x
if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("image")
    ap.add_argument("--model", default=MODEL_PATH)
    a = ap.parse_args()
    m = load_model(a.model)
    preds = m.predict(read_image(a.image), verbose=0)[0]
    p = float(preds[0]) if preds.shape==(1,) else float(preds[1])
    print(json.dumps({"parasitized_prob": round(p,6), "uninfected_prob": round(1-p,6)}))

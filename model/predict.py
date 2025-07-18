import pandas as pd
import pickle

# load the model
with open("model/model.pkl", "rb") as f:
    model = pickle.load(f)

# ML Flow
MODEL_VERSION = '1.0.0'

# get class labels from model (importing for matching probabilities to the class names)
class_labels = model.classes_.tolist()

def predict_output(user_input : dict):

    df = pd.DataFrame([user_input])

    # predict the class
    predicted_class = model.predict(df)[0]

    # get probabilities for all classes
    probabilities = model.predict_proba(df)[0]
    confidence = max(probabilities)

    # create mapping: (classs_name: probability)
    class_probs = dict(zip(class_labels, map(lambda p: round(p, 4), probabilities)))

    return {
        "predicted_catergory": predicted_class,
        "confidence": round(confidence, 4),
        "class_probabilities": class_probs
    }
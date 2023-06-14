from tensorflow import keras 
from tensorflow.keras.preprocessing import image
import numpy as np

# Check our folder and import the model with best validation accuracy
loaded_best_model = keras.models.load_model("model/model_08-0.90.h5")

# Custom function to load and predict label for the image
def predict(img_rel_path):
    # Import Image from the path with size of (300, 300)
    img = image.load_img(img_rel_path, target_size=(300, 300))

    # Convert Image to a numpy array
    img = image.img_to_array(img, dtype=np.uint8)

    # Scaling the Image Array values between 0 and 1
    img = np.array(img)/255.0

    # Get the Predicted Label for the loaded Image
    p = loaded_best_model.predict(img[np.newaxis, ...])

    # Label array
    labels = {0: 'Celana Jeans', 1: 'Celana Jogger ', 2: 'Celana Kargo', 3: 'Celana Trouser',
              4: 'Crewneck', 5: 'Kaos Oversized', 6: 'Kaos Stripe', 7: 'Kemeja Flannel',
              8: 'Sandal Trial', 9: 'Sepatu Athletics', 10: 'Sepatu Canvas', 11: 'Sepatu High-top Basketball'}

    # Get Label item
    predicted_class = labels[np.argmax(p[0], axis=-1)]

    return predicted_class


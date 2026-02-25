from keras.models import load_model  # TensorFlow is required for Keras to work
from PIL import Image, ImageOps  # Install pillow instead of PIL
import numpy as np

def predict_image(imagen):
    # Disable scientific notation for clarity
    np.set_printoptions(suppress=True)

    # Load the model
    model = load_model("convert_keras\keras_model.h5", compile=False)

    # Load the labels
    class_names = open("convert_keras\labels.txt", "r").readlines()

    # Create the array of the right shape to feed into the keras model
    # The 'length' or number of images you can put into the array is
    # determined by the first position in the shape tuple, in this case 1
    data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

    # Replace this with the path to your image
    image = Image.open(imagen).convert("RGB")

    # resizing the image to be at least 224x224 and then cropping from the center
    size = (224, 224)
    image = ImageOps.fit(image, size, Image.Resampling.LANCZOS)

    # turn the image into a numpy array
    image_array = np.asarray(image)

    # Normalize the image
    normalized_image_array = (image_array.astype(np.float32) / 127.5) - 1

    # Load the image into the array
    data[0] = normalized_image_array

    # Predicts the model
    prediction = model.predict(data)
    index = np.argmax(prediction)
    class_name = class_names[index]
    confidence_score = prediction[0][index]

    # Print prediction and confidence score
    if index == 0:
        return "estas son orejas de gato"
    elif index == 1:
        return "estas son orejas de perro"
    elif index == 2:
        return "estas son patas de perro"
    elif index == 3:
        return "estas son patas de gato"
    elif index == 4:
        return "esto es una cola de gato"
    elif index == 5:
        return "esto es una cola de perro"
    elif index == 6:
        return "estos son ojo de perro"
    elif index == 7:
        return "estos son ojos de gato"
    elif index == 8:
        return "estos son bigotes de gato"
    elif index == 9:
        return "estos son bigotes de perro"
    elif index == 10:
        return "esta es una nariz de perro"
    elif index == 11:
        return "esta es una nariz de gato"
"""Test whether silence-tensorflow also works to silence tflite warnings."""

import os
import warnings
import numpy as np
from silence_tensorflow import silence_tensorflow


def test_silence_tensorflow_on_tflite():
    """Check that everything runs."""
    silence_tensorflow()
    with warnings.catch_warnings():
        warnings.simplefilter("error")

        def setup():
            from keras.models import Model  # pylint: disable=import-outside-toplevel
            from keras.layers import Input  # pylint: disable=import-outside-toplevel
            from keras.layers import Dense  # pylint: disable=import-outside-toplevel
            from tensorflow import lite  # pylint: disable=import-outside-toplevel

            x = np.array([1]).astype("float32").reshape(1, 1)
            _in = Input(shape=(1,))
            _out = Dense(1)(_in)
            model = Model(inputs=_in, outputs=_out)
            model.compile(optimizer="adam", loss="mse", metrics=["accuracy"])
            model.fit(x, x, epochs=1)

            converter = lite.TFLiteConverter.from_keras_model(model)
            tflite_model = converter.convert()

            # Save the model.
            with open(os.path.join("model.tflite"), "wb") as f:
                f.write(tflite_model)

        def run():
            from tensorflow import lite  # pylint: disable=import-outside-toplevel

            x = np.array([1]).astype("float32").reshape(1, 1)

            new_model = lite.Interpreter(model_path="model.tflite")
            new_model.allocate_tensors()
            input_details = new_model.get_input_details()
            output_details = new_model.get_output_details()
            new_model.set_tensor(input_details[0]["index"], x)
            new_model.invoke()
            new_model.get_tensor(output_details[0]["index"])

        try:
            setup()
            run()
        except ModuleNotFoundError:
            pass

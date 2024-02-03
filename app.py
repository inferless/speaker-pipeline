from transformers import AutoProcessor, AutoModel
import numpy as np
import io
import base64
import soundfile as sf
import requests


class InferlessPythonModel:
    def initialize(self):
        self.processor = AutoProcessor.from_pretrained("suno/bark")
        self.model = AutoModel.from_pretrained("suno/bark")

        self.model.to("cuda")

    def infer(self, inputs):
        transcription_file = inputs["transcription_file"]
        alpha = inputs["alpha"]
        beta = inputs["beta"]
        speed = inputs["speed"]
        target_lang = inputs["target_lang"]

        response = requests.get(transcription_file)
        if response.status_code != 200:
            return {
                "generated_audio_base64": f"Error downloading file: {transcription_file}"
            }

        prompt = response.content.decode("utf-8")
        inputs = self.processor(
            text=[prompt],
            return_tensors="pt",
        )

        inputs = {k: v.to("cuda") for k, v in inputs.items()}

        speech_values = self.model.generate(**inputs, do_sample=True)
        audio_numpy = speech_values.cpu().numpy().squeeze()

        buffer = io.BytesIO()
        sf.write(
            buffer, audio_numpy, self.model.generation_config.sample_rate, format="WAV"
        )
        buffer.seek(0)

        base64_audio = base64.b64encode(buffer.read()).decode("utf-8")
        return {"generated_audio_base64": base64_audio}

    def finalize(self, args):
        self.pipe = None

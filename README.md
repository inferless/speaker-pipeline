# Speaker-Pipeline

### Input
```json
{
  "inputs": [
    {
      "name": "transcription_file",
      "datatype": "BYTES",
      "shape": [
        1
      ],
      "data": [
        "https://inferless-public.s3.amazonaws.com/sample.txt"
      ]
    },
    {
      "name": "alpha",
      "datatype": "FP32",
      "shape": [
        1
      ],
      "data": [
        0.123
      ]
    },
    {
      "name": "beta",
      "datatype": "FP32",
      "shape": [
        1
      ],
      "data": [
        0.456
      ]
    },
    {
      "name": "speed",
      "datatype": "FP32",
      "shape": [
        1
      ],
      "data": [
        1.25
      ]
    },
    {
      "name": "target_lang",
      "datatype": "BYTES",
      "shape": [
        1
      ],
      "data": [
        "fr"
      ]
    }
  ]
}
```

### Output
```json
{
  "outputs": [
    {
      "name": "generated_audio_base64",
      "datatype": "BYTES",
      "shape": [
        1
      ],
      "data": [
        "generated base64 text"
      ]
    }
  ]
}
```

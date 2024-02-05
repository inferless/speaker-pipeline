INPUT_SCHEMA = {
  "transcription_file": 
    {
      "datatype": "BYTES",
      "shape": [
        1
      ],
      "example": [
        "https://inferless-public.s3.amazonaws.com/sample.txt"
      ]
    },
"alpha" :
    {
      "datatype": "FP32",
      "shape": [
        1
      ],
      "example": [
        0.123
      ]
    },
"beta" : 
    {
      "datatype": "FP32",
      "shape": [
        1
      ],
      "example": [
        0.456
      ]
    },
"speed" : 
    {
      "datatype": "FP32",
      "shape": [
        1
      ],
      "example": [
        1.25
      ]
    },
"target_lang" : 
    {
      "datatype": "BYTES",
      "shape": [
        1
      ],
      "example": [
        "fr"
      ]
    }
}

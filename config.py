
import os
from elevenlabs.client import ElevenLabs

# Define the API key variable that text_to_audio.py imports
ELEVENLABS_API_KEY = "sk_b70c5b6c2db4168c5d2036feb0bcab1489e7d8185f94297c"

elevenlabs = ElevenLabs(
    api_key=ELEVENLABS_API_KEY
)
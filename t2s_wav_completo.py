from google.cloud import texttospeech

# Pergunta ao usuário
texto = input("Digite a mensagem que deseja converter em fala: ")
nome_arquivo = input("Digite o nome do arquivo de saída (sem extensão): ")

# Cria o cliente do Google Cloud TTS
client = texttospeech.TextToSpeechClient()

# Cria o objeto de entrada de texto
synthesis_input = texttospeech.SynthesisInput(text=texto)

# Seleciona a voz
voice = texttospeech.VoiceSelectionParams(
    language_code="pt-BR",
    name="pt-BR-Wavenet-B",  # Outras opções: B, C, D...
    ssml_gender=texttospeech.SsmlVoiceGender.FEMALE,
)

# Configura o formato de áudio WAV (8kHz mono)
audio_config = texttospeech.AudioConfig(
    audio_encoding=texttospeech.AudioEncoding.LINEAR16,  # Gera WAV PCM
    sample_rate_hertz=8000,
)

# Faz a síntese de fala
response = client.synthesize_speech(
    input=synthesis_input,
    voice=voice,
    audio_config=audio_config,
)

# Salva o arquivo WAV
arquivo_saida = f"{nome_arquivo}.wav"
with open(arquivo_saida, "wb") as out:
    out.write(response.audio_content)

print(f"✅ Áudio gerado com sucesso: {arquivo_saida} (8kHz mono)")


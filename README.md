# Gerador de Arquivos de Áudio por TTS para PBX

## 1. Descrição 

Este projeto implementa um mecanismo TTS para geração de arquivos de áudios próprios e orimizados para uso em sistemas de telefonia. 

Os áudios gerados seguem o padrão amplamente utilizado em plataformas de telefonia PBX, são criados no formato wav, taxa de amostragem 8KHz, monocanal e 16 bits. 


## 2. Instalação e Execução
Abaixo seguem os passos para criar a chave do google cloud, para utilização da API Text-to-speech do Google. Em seguida a instalação e execução do código. 


### PASSO 1 — Criar conta no Google Cloud

- Acesse: https://console.cloud.google.com/

- Faça login com sua conta Google.

- Crie um novo projeto (ex: tts-projeto).





### PASSO 2 — Ativar a API Text-to-Speech

- No menu superior, clique em “APIs e Serviços → Biblioteca”.

- Pesquise por Text-to-Speech API.

- Clique em Ativar.




### PASSO 3 — Criar a chave de autenticação

- Vá em APIs e Serviços → Credenciais.

- Clique em Criar credencial → Chave de conta de serviço.

- Escolha Nova conta de serviço, dê um nome (ex: tts-service).

- Em “Função”, pode deixar “Editor”.

- Após criar, clique em “Gerar chave” → JSON.

- Baixe o arquivo (ex: chave.json) e salve em uma pasta segura.



### PASSO 4 — Configurar variável de ambiente

No terminal:

export GOOGLE_APPLICATION_CREDENTIALS="/caminho/para/chave.json"




### PASSO 5 - Instalar o Venv e as Bibliotecas

- apt install python3-venv -y

- python3 -m venv venv

- source venv/bin/activate

- pip install google-cloud-texttospeech




### PASSO 6 - Executar o Venv

source venv/bin/activate

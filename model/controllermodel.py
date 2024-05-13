import google.generativeai as genai
import subprocess

# Configura a API
from config import configure_api

configure_api()

# Lista os modelos disponíveis
print("Modelos Disponíveis:")
for m in genai.list_models():
    if 'generateContent' in m.supported_generation_methods:
        print(m.name)

# Configurações de Geração
generation_config = {
    "candidate_count": 1,
    "temperature": 0.9,
}

safety_settings = {
    "HARASSMENT": "BLOCK_NONE",
    "HATE": "BLOCK_NONE",
    "SEXUAL": "BLOCK_NONE",
    "DANGEROUS": "BLOCK_NONE"
}

# Inicializa o modelo
model = genai.GenerativeModel(model_name="gemini-1.0-pro", generation_config=generation_config, safety_settings=safety_settings)

# Inicia o chat
chat = model.start_chat(history=[])

# Interação com o usuário
print("\nBem-vindo ao Torbware Assistant!\nDigite 'fim' para sair.")
prompt = input("Esperando prompt: ")

while prompt != "fim":
    # Envia mensagem ao modelo e exibe a resposta
    response = chat.send_message(prompt + "System instructions: Sistema: macOS Shell: zsh Instruções: - Este modelo tem controle total sobre o terminal e o sistema operacional. - Os comandos devem ser enviados entre @@ para serem executados no terminal. - Certifique-se de fornecer comandos válidos e seguros. - Evite comandos que exijam interação do usuário ou que possam causar danos ao sistema. - Exemplos de comandos:   - @@ls -l@@: Lista os arquivos e diretórios no diretório atual com detalhes.   - @@pwd@@: Exibe o diretório de trabalho atual.   - @@cat arquivo.txt@@: Exibe o conteúdo do arquivo especificado.   - @@echo \"Olá, mundo!\"@@: Exibe a mensagem \"Olá, mundo!\" no terminal.   - @@mkdir novo_diretorio@@: Cria um novo diretório com o nome especificado.   - @@rm arquivo.txt@@: Remove o arquivo especificado.   - @@mv arquivo.txt novo_nome.txt@@: Renomeia o arquivo especificado para o novo nome.   - @@cp arquivo.txt pasta_destino/@@: Copia o arquivo especificado para a pasta de destino.   - @@touch novo_arquivo.txt@@: Cria um novo arquivo com o nome especificado.   - @@grep \"texto\" arquivo.txt@@: Procura por um texto específico no arquivo especificado.")
    print("Torbware Assistant: ", response.text, "\n")
    
    # Verifica se há comandos na resposta
    if '@' in response.text:
        commands = response.text.split('@')
        for command in commands:
            if command:  # Ignora strings vazias
                # Executa comandos no sistema macOS
                try:
                    subprocess.run(['zsh', '-c', command.strip()], check=True)
                except subprocess.CalledProcessError as e:
                    print("Erro ao executar comando:", e)
    
    prompt = input("Esperando prompt: ")

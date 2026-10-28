## Configuração do ambiente


### 1. Clonar o repositório

```bash
git clone https://github.com/emanoelvoitpo/calculadora-grpc-python.git
cd pratica04
```


### 2. Criar o ambiente virtual


**Linux / Ubuntu / WSL:**

```bash
python3 -m venv .venv
```

**Windows:**

```powershell
py -m venv .venv
```

### 3. Ativar o ambiente virtual

**Linux / Ubuntu / WSL:**

```bash
source .venv/bin/activate
```

**Windows — PowerShell:**

```powershell
.venv\Scripts\Activate.ps1
```

**Windows — Prompt de Comando (CMD):**

```bat
.venv\Scripts\activate.bat
```


### 4. Instalar as dependências

Com o ambiente virtual ativado, execute:

```bash
python3 -m pip install -r requirements.txt
```

### 5. Gerar os arquivos do gRPC

Execute o comando na raiz do projeto, onde está localizado o arquivo `calculadora.proto`:

```bash
python3 -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. calculadora.proto
```

Esse comando gera os arquivos `calculadora_pb2.py` e `calculadora_pb2_grpc.py`, utilizados na comunicação entre o cliente e o servidor.

### 6. Executar a aplicação

Abra dois terminais na pasta do projeto e ative o ambiente virtual em ambos.

**Terminal 1 — Servidor:**

```bash
python servidor.py
```

**Terminal 2 — Cliente:**

```bash
python cliente.py
```

O servidor ficará aguardando as requisições na porta `50051`. O cliente permitirá escolher a operação matemática e informar os três números.


### Atores
 - Paula Laiz - Matrícula: 558876
 - Vitor Emanoel - Matrícula: 558881

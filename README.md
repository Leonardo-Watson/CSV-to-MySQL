# 🚧 Status do Projeto

> **Em Construção**  
> Este projeto está em desenvolvimento ativo. Novas funcionalidades e otimizações de performance estão sendo implementadas continuamente.

---

# 📂 CSV-to-MySQL ETL

## 📌 Sobre o Projeto

O **CSV-to-MySQL** é uma ferramenta de **ETL (Extract, Transform, Load)** desenvolvida para automatizar a importação de grandes volumes de dados de arquivos CSV para um banco de dados MySQL.

Diferente de scripts simples, este projeto foi arquitetado com foco em **escalabilidade** e **performance**. Ele utiliza técnicas de leitura em fluxo (_streaming_) e processamento em lotes (_chunking_), permitindo a importação de arquivos grandes (70MB+, 1M+ linhas) sem comprometer a memória RAM da máquina.

---

## 🎯 Objetivos e Destaques

- ✅ **Leitura Inteligente:** Processa arquivos CSV de qualquer tamanho utilizando iteradores (sem carregar tudo na memória).
- ⚡ **Alta Performance:** Utiliza `bulk inserts` (inserção em lote) para maximizar a velocidade do MySQL.
- 🔄 **Tratamento de Dados:** Converte automaticamente valores `NaN` do Pandas para `NULL` nativo do SQL.
- 🧩 **Arquitetura Modular:** Código organizado em módulos independentes (conexão, leitura e carregamento).
- 📈 **Escalável:** Estruturado para lidar com grandes volumes de dados com estabilidade.

---

## 🚀 Como Funciona o Pipeline

### 🔹 Extract

O script varre a pasta `data/` em busca de arquivos `.csv`.

### 🔹 Transform

Os arquivos são lidos em pedaços (ex: 10.000 linhas por vez) utilizando Pandas.

Durante essa etapa:

- Dados faltantes são tratados.
- Valores inválidos são ajustados.
- Conversões necessárias são aplicadas.

### 🔹 Load

Cada chunk é enviado ao MySQL dentro de uma transação única.

Após o envio, a memória é liberada imediatamente antes de processar o próximo lote.

---

## 📦 Tecnologias Utilizadas

- **Python 3.14+**
- **Pandas** — Manipulação de dados e leitura em chunks
- **MySQL Connector** — Driver oficial de conexão com o banco
- **Python-Dotenv** — Gerenciamento de variáveis de ambiente

---

## ⚙️ Configuração e Execução

### 1️⃣ Preparar o Ambiente

Crie um ambiente virtual para isolar as dependências:

Criar ambiente virtual

```bash
python -m venv venv
```

Ativar no terminal (Bash)

```bash
source venv/bin/activate
```

### 2️⃣ Instalar Dependências

Instalar dependências do projeto

```bash
pip install -r requirements.txt
```

### 3️⃣ Configurar Credenciais (.env)

Crie um arquivo .env na raiz do projeto e configure suas credenciais:

```bash
DB_HOST=localhost
DB_PORT=port
DB_USER=root
DB_PASSWORD=sua_senha_aqui
DB_NAME=nome_do_banco
```

### 4️⃣ Executar a Aplicação

```bash
python main.py
```

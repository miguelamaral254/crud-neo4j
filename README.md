# Neo4j CRUD com Menu Interativo em Python

Este projeto é um exemplo simples de um CRUD (Create, Read, Update, Delete) para o banco de grafos Neo4j, usando Python e um menu interativo no terminal.

---

## Funcionalidades do Menu

Ao rodar o script `main.py`, você verá o seguinte menu:

```

\=== Menu Neo4j CRUD ===
1 - Criar pessoa
2 - Criar amizade
3 - Listar amigos
4 - Atualizar nome da pessoa
5 - Deletar pessoa
6 - Listar todas as pessoas
7 - Listar todas as amizades
0 - Sair

````

**Opções:**

- **1 - Criar pessoa:** Cria um nó `Person` com o nome informado.
- **2 - Criar amizade:** Cria uma relação `KNOWS` entre duas pessoas existentes ou cria as pessoas caso não existam.
- **3 - Listar amigos:** Mostra todos os amigos (relacionamentos `KNOWS`) de uma pessoa.
- **4 - Atualizar nome da pessoa:** Renomeia um nó `Person`.
- **5 - Deletar pessoa:** Remove a pessoa e todas as suas conexões.
- **6 - Listar todas as pessoas:** Lista todos os nós `Person` existentes.
- **7 - Listar todas as amizades:** Lista todas as relações `KNOWS` existentes.
- **0 - Sair:** Fecha o programa.

---

## Como rodar

### Pré-requisitos

- Docker e Docker Compose instalados na sua máquina.
- Python 3.8+ instalado localmente (ou dentro de um ambiente virtual).

### Passo 1: Rodar o Neo4j com Docker Compose

No diretório raiz rode:


docker-compose up -d


O Neo4j estará disponível na porta padrão Bolt `7687`.

---

### Passo 2: Instalar dependências Python

Dentro do seu ambiente virtual, instale o driver Neo4j:

```bash
pip install neo4j
```

---

### Passo 3: Configurar o script Python

No `main.py`, configure a URI e as credenciais do Neo4j:

```python
URI = "neo4j://localhost:7687"
AUTH = ("neo4j", "sua_senha")
```

### No docker-compose já está configurado as credenciais user neo4j e senha senha123

---

### Passo 4: Rodar o script

```bash
python main.py
```

## Teste rápido

1. Crie pessoas (opção 1).
2. Crie amizades (opção 2).
3. Liste amigos (opção 3).
4. Liste todas as pessoas (opção 6).
5. Liste todas as amizades (opção 7).

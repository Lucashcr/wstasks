# WSTasks

Este é um projeto full stack de uma lista de tarefas desenvolvido com **FastAPI**, **Celery** e **React**. A aplicação permite a criação de tasks simples e o acompanhamento de seu status em tempo real, através de **WebSocket**.

## Tecnologias Utilizadas

- **Backend:** FastAPI e Celery
- **Frontend:** React com WebSocket para atualização em tempo real dos status das tasks
- **Broker:** Redis (ou RabbitMQ) para comunicação com Celery
- **Banco de Dados:** PostgreSQL (ou outro banco de dados configurado no projeto)

## Funcionalidades

- **Criação de Tasks:** Interface com um botão para criar novas tasks.
- **Listagem de Tasks:** Exibe uma lista de tasks criadas com seus respectivos:
    - ID (UUID aleatório gerado automaticamente pelo Celery)
    - Status (atualizado em tempo real)
    - Data de criação
    - Data de última atualização
- **Tasks simuladas:** As tasks criadas são simulações que apenas executam um sleep de duração aleatória.

## Estrutura do Projeto

### Backend (FastAPI + Celery)

- FastAPI é utilizado como o servidor para o backend e para expor endpoints de criação e listagem de tasks.
- Celery gerencia as tasks assíncronas, que simulam operações através de um sleep randômico.

### Frontend (React)

- Interface simples com um botão para criar novas tasks.
- Lista de tasks criada, exibindo informações em tempo real.
- Atualização do status das tasks via WebSocket.

## Como Rodar o Projeto

### Pré-requisitos

- Docker e Docker Compose (As demais dependências são definidas no docker-compose.yml)

### Passos

1. Clone o repositório:

```bash
git clone https://github.com/Lucashcr/wstasks
cd task-list-app
```

2. Configure as variáveis de ambiente:

Crie um arquivo .env com base no arquivo `local.env`, inserindo as configurações do banco de dados, Redis e demais 

```bash
cp local.env .env
```

3. Execute o projeto:

Use o Docker Compose para iniciar os containers:

```bash
docker compose up --build
```

4. Acesse a aplicação:

Abra o navegador e acesse `http://localhost:3000` para acessar a interface.

## Estrutura de Arquivos

- **backend/** - Contém a aplicação FastAPI e a configuração do Celery
- **frontend/** - Contém a aplicação React
- **docker-compose.yml** - Arquivo de configuração para rodar os serviços em containers

## Licença

Este projeto está licenciado sob a MIT License.

# 🚀 Plataforma de Monitoramento de Serviços

Sistema de monitoramento desenvolvido com **FastAPI** para verificação de disponibilidade de serviços em tempo real, com dashboard interativo e alertas automáticos.

---

## 🛠️ Tecnologias

- FastAPI
- PostgreSQL
- Docker
- Chart.js
- Pytest

---

## ⚙️ Funcionalidades

- 🔍 Monitoramento automático de serviços
- 📊 Dashboard em tempo real
- 🚨 Alertas via Webhook
- 🔗 API RESTful
- 🧪 Testes automatizados

---

## 📊 Dashboard

Visualização em tempo real do status dos serviços:

![Dashboard](https://github.com/user-attachments/assets/b0a40817-581e-419b-bbb1-2681df74be0d)

---

## 🐳 Docker (Banco de Dados)

Container PostgreSQL rodando via Docker:

![API](https://github.com/user-attachments/assets/a9bad7fc-9130-40bf-af96-1cb3fda8f30a)

---

## 🚨 Monitoramento e Alertas

Exemplo de status e alertas:

![Monitoramento](https://github.com/user-attachments/assets/73a36614-a29e-4209-824b-fd850501fbb4)

![Webhook](https://github.com/user-attachments/assets/b1fd5f94-5e50-4d00-a8ae-b5a1e3e044b1)

![Logs](https://github.com/user-attachments/assets/994ccbdc-de69-476e-a3f6-a1df3c12bb3e)

---

## ▶️ Como executar o projeto

### 🔧 Instalar dependências

```bash
pip install -r requirements.txt

▶️ Rodar a aplicação
uvicorn app.main:app --reload

🐳 Rodar banco com Docker
docker run --name postgres-monitor \
-e POSTGRES_USER=admin \
-e POSTGRES_PASSWORD=admin \
-e POSTGRES_DB=monitor \
-p 5432:5432 \
-d postgres

📊 Acessar o sistema
API: http://127.0.0.1:8000/docs
Dashboard: http://127.0.0.1:8000/static/index.html

🧪 Executar testes
pytest

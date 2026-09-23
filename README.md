# Streamlit app

Live app: https://data-science-5sem-lpseudo.streamlit.app/

## Run locally

```bash
pip install -r requirements.txt
streamlit run hello-dash.py
```

## Run with Docker

```bash
docker build -t ciencia-de-datos-app .
docker run --rm -p 8501:8501 ciencia-de-datos-app
```

Open http://localhost:8501 after the container starts.

## Deploy to Streamlit

1. Push this repository to GitHub.
2. In Streamlit Community Cloud, choose the repository.
3. Set the main file path to hello-dash.py.
4. Deploy.

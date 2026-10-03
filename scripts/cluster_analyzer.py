import subprocess

import requests

OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL = "llama3"
MAX_LINES = 80  # on limite la quantité de données envoyées au modèle


def run_kubectl(command):
    result = subprocess.run(
        command,
        capture_output=True,
        text=True,
        timeout=30
    )

    if result.returncode != 0:
        raise SystemExit(f"Erreur kubectl :\n{result.stderr}")

    return result.stdout


def keep_last_lines(text, max_lines=MAX_LINES):
    lines = text.strip().splitlines()

    if len(lines) <= max_lines:
        return text

    return "\n".join(lines[:1] + lines[-(max_lines - 1):])


def get_cluster_state():
    pods = run_kubectl(["kubectl", "get", "pods", "-A"])

    events = run_kubectl([
        "kubectl", "get", "events", "-A",
        "--field-selector", "type=Warning",
        "--sort-by=.lastTimestamp"
    ])

    pods = keep_last_lines(pods)
    events = keep_last_lines(events).strip() or "(aucun événement Warning)"

    return pods, events


def build_prompt(pods, events):
    return f"""
You are a Kubernetes monitoring assistant.

Analyze only the information provided below.

Your tasks:
1. Summarize the current cluster state in simple language.
2. Identify pods or events that appear abnormal.
3. For each anomaly, explain the evidence from the provided data.
4. Clearly distinguish facts from hypotheses.
5. If the information is insufficient to diagnose a problem, say so.
6. Do not invent metrics, errors, causes, or resources that are not present.
7. Answer in French.

KUBERNETES PODS:
{pods}

KUBERNETES WARNING EVENTS:
{events}

Return the answer using this structure:

Résumé du cluster :
- ...

Anomalies observées :
- ...

Preuves :
- ...

Explications possibles (hypothèses) :
- ...

Informations manquantes :
- ...
"""


def ask_llm(prompt):
    try:
        response = requests.post(
            OLLAMA_URL,
            json={
                "model": MODEL,
                "prompt": prompt,
                "stream": False,
                "options": {"temperature": 0}
            },
            timeout=120
        )
        response.raise_for_status()
    except requests.RequestException as err:
        raise SystemExit(f"Impossible de joindre Ollama : {err}")

    return response.json()["response"]


def main():
    pods, events = get_cluster_state()

    prompt = build_prompt(pods, events)
    analysis = ask_llm(prompt)

    print("\n=== Analyse de l'état du cluster ===\n")
    print(analysis)


if __name__ == "__main__":
    main()
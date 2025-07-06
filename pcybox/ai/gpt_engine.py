# ai/gpt_engine.py

import os
import openai
from dotenv import load_dotenv
from rich.console import Console
from rich.progress import Progress, SpinnerColumn, TextColumn

# Load environment variables
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

console = Console()

def build_prompt(mission_data: dict) -> str:
    """
    Build a detailed red team scenario prompt based on mission parameters.
    Each step includes MITRE ATT&CK mapping, attack details, and detection strategies.
    """
    objectives = ", ".join(mission_data.get("objectives", []))
    resources = ", ".join(mission_data.get("resources", []))
    deliverables = ", ".join(mission_data.get("deliverables", []))

    prompt = (
        "You are a top-tier red team operator preparing a step-by-step attack scenario.\n\n"
        f"**Target:** {mission_data.get('target')}\n"
        f"**Initial Access:** {mission_data.get('initial_access')}\n"
        f"**Operation Mode:** {mission_data.get('operation_mode')}\n"
        f"**Knowledge Level:** {mission_data.get('information_level')}\n"
        f"**Adversary Profile:** {mission_data.get('adversary_profile')}\n"
        f"**Detail Level:** {mission_data.get('detail_level')}\n"
        f"**Objectives:** {objectives}\n"
        f"**Mission Context:** {mission_data.get('mission_context')}\n"
        f"**Mission Duration:** {mission_data.get('mission_duration')}\n"
        f"**Resources Available:** {resources}\n"
        f"**Constraints:** {mission_data.get('constraints')}\n"
        f"**Deliverables:** {deliverables}\n\n"
        "Generate a **realistic, technical red team scenario**, broken down into clear **sequential steps**.\n\n"
        "For **each step**, include:\n"
        "- ✅ Action performed (e.g., phishing, C2, lateral move)\n"
        "- 🎯 Goal or impact\n"
        "- 🧠 MITRE ATT&CK ID and name (e.g., `T1059.001 – PowerShell`)\n"
        "- 🛠️ Exact commands/scripts/files used (if applicable)\n"
        "- 📘 Clear technical instructions\n"
        "- 💡 Justification\n\n"
        "**Then**, for the same step, provide a section called `### 🛡️ Detection Strategy:` with:\n"
        "- 🔍 A realistic **Sigma detection rule** in YAML (if possible)\n"
        "- OR a detailed **Suricata/Splunk query**, or detection explanation\n"
        "- If no good detection exists, explain why\n\n"
        "### Format:\n"
        "- Use **Markdown**\n"
        "- Each step = `## Step X – [Step Title]`\n"
        "- Include `### 🛡️ Detection Strategy:` after each step\n"
        "- Sigma rule: use fenced code block with `yaml` syntax\n"
        "- Do **not** add intro, summary or commentary\n\n"
        "**Goal:** The result should be useful for both red and blue teams.\n"
    )

    return prompt

def generate_scenario(prompt: str, model="gpt-4", max_tokens=5000) -> str:
    """
    Sends the prompt to OpenAI and returns the generated scenario.
    """
    with Progress(
        SpinnerColumn(),
        TextColumn("[progress.description]{task.description}"),
        transient=True
    ) as progress:
        progress.add_task(description="Talking to GPT...", total=None)

        try:
            response = openai.ChatCompletion.create(
                model=model,
                messages=[{"role": "user", "content": prompt}],
                max_tokens=max_tokens,
                temperature=0.7
            )
            return response['choices'][0]['message']['content'].strip()

        except Exception as e:
            console.print(f"[bold red]❌ GPT request failed:[/bold red] {e}")
            return "Error: GPT call failed."

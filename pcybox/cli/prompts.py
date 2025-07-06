import questionary
from rich.console import Console
from rich.text import Text
from rich.panel import Panel

console = Console()

# ==== CHOICES ====
OBJECTIVE_CHOICES = [
    "Obtain a shell",
    "Privilege escalation",
    "Data exfiltration",
    "Maintain persistence",
    "Detection testing",
    "Other"
]

TARGET_CHOICES = [
    "Web Application",
    "Internal Infrastructure",
    "Windows Active Directory",
    "Cloud (AWS, Azure, GCP...)",
    "Mobile App / API"
]

INITIAL_ACCESS_CHOICES = [
    "None",
    "Successful Phishing",
    "User VPN Access",
    "Compromised Machine",
    "Existing Internal Link"
]

OPERATION_MODE_CHOICES = [
    "Stealthy",
    "Noisy"
]

INFORMATION_LEVEL_CHOICES = [
    "Black box",
    "Gray box",
    "White box"
]

ADVERSARY_PROFILES = [
    "None",
    "APT29 (Russia, stealthy espionage)",
    "FIN7 (Cybercrime, phishing)",
    "Lazarus Group (North Korea, sabotage+theft)",
    "Cobalt Group (Banks, fast exploitation)",
    "Custom"
]

DETAIL_LEVEL_CHOICES = [
    "Standard",
    "Educational"
]

MISSION_DURATION_CHOICES = [
    "Less than one week",
    "1 to 4 weeks",
    "1 to 3 months",
    "More than 3 months"
]

RESOURCES_CHOICES = [
    "1-2 people",
    "3-5 people",
    "More than 5 people",
    "Dedicated team (multiple roles)"
]

DELIVERABLES_CHOICES = [
    "Technical report",
    "Executive presentation",
    "Educational report",
    "Artifacts (logs, screenshots)",
    "Other (please specify)"
]


# ==== UI ====
def print_banner():
    banner = Text()
    banner.append("PCYBOX RED TEAM\n", style="bold blue underline")
    banner.append("Developed by Mister__iks\n", style="italic dim")
    banner.append("A powerful Red Team scenario generator\n", style="bold green")
    console.print(Panel(banner, border_style="bright_blue"))


# ==== INTERACTIVE PROMPTS ====

def ask_questions():
    console.rule("[bold cyan]🛠 New Red Team Mission Setup")

    objectives = questionary.checkbox(
        "🎯 Select mission objectives:",
        choices=OBJECTIVE_CHOICES
    ).ask()

    target = questionary.select(
        "🎯 Select target type:",
        choices=TARGET_CHOICES
    ).ask()

    access = questionary.select(
        "🔓 Initial access method:",
        choices=INITIAL_ACCESS_CHOICES
    ).ask()

    mode = questionary.select(
        "🎭 Operation mode:",
        choices=OPERATION_MODE_CHOICES
    ).ask()

    knowledge = questionary.select(
        "🧠 Information level:",
        choices=INFORMATION_LEVEL_CHOICES
    ).ask()

    adversary = questionary.select(
        "👤 Emulated adversary profile:",
        choices=ADVERSARY_PROFILES
    ).ask()

    detail = questionary.select(
        "📘 Detail level of the output:",
        choices=DETAIL_LEVEL_CHOICES
    ).ask()

    # Appel des questions supplémentaires
    additional_answers = ask_additional_questions()

    # Fusion des deux dictionnaires
    return {
        "objectives": objectives,
        "target": target,
        "initial_access": access,
        "operation_mode": mode,
        "information_level": knowledge,
        "adversary_profile": adversary,
        "detail_level": detail,
        **additional_answers
    }


def ask_additional_questions():
    console.rule("[bold magenta]⚙️ Additional Mission Details")

    mission_context = questionary.text(
        "📝 What is the context or main reason for this mission?"
    ).ask()

    mission_duration = questionary.select(
        "⏳ Estimated mission duration:",
        choices=MISSION_DURATION_CHOICES
    ).ask()

    resources = questionary.checkbox(
        "👥 Available human resources:",
        choices=RESOURCES_CHOICES
    ).ask()

    constraints = questionary.text(
        "⚖️ Any constraints or rules of engagement to respect?"
    ).ask()

    deliverables = questionary.checkbox(
        "📄 Expected deliverables:",
        choices=DELIVERABLES_CHOICES
    ).ask()

    # Si 'Other (please specify)' dans deliverables, demander précision
    if "Other (please specify)" in deliverables:
        other_deliverable = questionary.text(
            "✍️ Please specify other deliverables:"
        ).ask()
        # Remplacer la mention générique par la valeur saisie
        deliverables = [
            d for d in deliverables if d != "Other (please specify)"
        ]
        if other_deliverable:
            deliverables.append(other_deliverable)

    return {
        "mission_context": mission_context,
        "mission_duration": mission_duration,
        "resources": resources,
        "constraints": constraints,
        "deliverables": deliverables
    }

# pcybox/__main__.py

from pcybox.cli.prompts import print_banner, ask_questions
from pcybox.core.mission import Mission
from pcybox.ai.gpt_engine import build_prompt, generate_scenario
from pcybox.utils.helpers import (
    export_attack_navigator_layer,
    export_markdown,
    extract_sigma_rules,
    extract_ttps_from_text,
    generate_readme,
    save_sigma_rules,
    save_ttps,
    zip_directory
)

from rich.console import Console
from rich.panel import Panel
import os
from datetime import datetime

console = Console()

def main():
    print_banner()

    # Ask questions to define the mission
    answers = ask_questions()
    if not answers:
        console.print("[bold red]Mission creation cancelled.[/bold red]")
        return

    # Create a Mission instance
    mission = Mission(answers)
    mission_data = mission.to_dict()

    # Build prompt and generate scenario
    prompt = build_prompt(mission_data)
    scenario = generate_scenario(prompt)

    console.rule("[bold green]📋 Generated Red Team Scenario")
    console.print(Panel(scenario, border_style="green"))

    # Extract content from scenario
    ttps = extract_ttps_from_text(scenario)
    sigma_rules = extract_sigma_rules(scenario)

    # Create mission-specific folder
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    base_name = f"mission_{timestamp}"
    mission_dir = os.path.join("missions", base_name)
    os.makedirs(mission_dir, exist_ok=True)

    # Save mission JSON
    mission_json_path = os.path.join(mission_dir, f"{base_name}.json")
    with open(mission_json_path, "w", encoding="utf-8") as f:
        import json
        json.dump(mission_data, f, indent=4)

    # Save scenario markdown
    scenario_md_path = os.path.join(mission_dir, "mission.md")
    with open(scenario_md_path, "w", encoding="utf-8") as f:
        f.write(scenario)

    # Save TTPs
    ttps_path = save_ttps(ttps, base_filename="mission", directory=mission_dir)

    # Export ATT&CK Navigator layer
    navigator_path = export_attack_navigator_layer(ttps, base_filename="mission", directory=mission_dir)

    # Save Sigma rules
    sigma_dir, sigma_paths = save_sigma_rules(sigma_rules, base_filename="mission", directory=os.path.join(mission_dir, "sigma"))

    # Generate README
    generate_readme(mission_dir, metadata=mission_data)

    # Zip the mission folder
    zip_path = zip_directory(mission_dir, output_zip_path=f"{mission_dir}.zip")

    # Final status
    console.print(f"[cyan]📦 All mission artifacts saved in folder:[/cyan] {mission_dir}")
    console.print(f"[green]✅ Zipped archive created at:[/green] {zip_path}")

    if ttps:
        console.print("🧠 [cyan]MITRE TTPs extracted and saved.[/cyan]")
    else:
        console.print("[yellow]⚠️ No MITRE TTPs found.[/yellow]")

    if sigma_rules:
        console.print("🛡️ [green]Sigma rules saved under:[/green] 'sigma/'")
    else:
        console.print("[yellow]⚠️ No Sigma rules found.[/yellow]")

if __name__ == "__main__":
    main()

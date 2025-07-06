# 🧠 PCYBOX – Red & Blue Team Scenario Generator

**PCYBOX** is a powerful AI-driven framework that generates end-to-end red team attack scenarios with corresponding blue team detection content. Built for security professionals, it produces realistic, step-by-step operations mapped to the MITRE ATT&CK framework and auto-generates Sigma rules for defensive engineering.

---

## 🚀 Features

- ✅ Interactive CLI for mission creation  
- 🧠 AI-generated red team scenarios (OpenAI GPT-based)  
- 🗺️ ATT&CK TTPs extraction and MITRE Navigator JSON export  
- 🛡️ Auto-generated Sigma detection rules per attack step  
- 📘 Mission README auto-generated for each scenario  
- 📦 All artifacts packaged into a ZIP for easy sharing  
- 🧰 Clean, modular architecture for extensibility  

---

## 📦 Output Example

Each scenario generates:

- `mission.md` – Red team scenario (Markdown)  
- `mission_ttps.json` – MITRE ATT&CK techniques (extracted)  
- `mission_navigator.json` – Navigator-compatible JSON  
- `sigma/` – YAML Sigma rules per attack step  
- `README.md` – Mission overview and content index  
- `mission_artifacts.zip` – Archive of all artifacts  

---

## 📂 Project Structure

<pre>
pcybox/
├── __main__.py            # Interactive launcher
├── cli/                   # CLI interface components
├── core/                  # Core logic (extraction, packager, Sigma, etc.)
├── ai/                    # GPT prompt builder and generator
├── utils/                 # Helpers and file utilities
├── config/                # Sample mission JSON configs
├── missions/              # Output directory
</pre>

---

## ⚙️ Installation

```bash
git clone https://github.com/your-username/pcybox.git
cd pcybox
pip install -r requirements.txt
```

You’ll also need an OpenAI API key. Set it as an environment variable:

```bash
export OPENAI_API_KEY="sk-xxxxxxxxxxxxxxxx"
```

---

## 🧪 Usage (Interactive Mode)

Launch the assistant:

```bash
python -m pcybox
```

Follow the prompts to define the mission parameters. The tool will:

1. Generate a red team scenario (step-by-step)  
2. Extract TTPs and create Navigator layer  
3. Generate Sigma rules (if applicable)  
4. Export all content into a clean archive  

---

## 📘 Sample Use Case

Create a mission targeting an internal Windows Active Directory environment. Define:

- Initial access: Phishing with payload  
- Knowledge level: Partial internal map  
- Operation mode: Stealth  
- Objectives: Credential theft, domain control  

PCYBOX will generate the attack path, associated TTPs, detection rules, and package it for operational or blue team use.

---

## 📈 Roadmap (Planned)

- [ ] Graph-based attack DAG generator  
- [ ] Threat actor emulation mode (APT simulation)  
- [ ] MITRE coverage analysis heatmaps  
- [ ] Sigma coverage simulation (evasion suggestions)  
- [ ] Web UI version  

---

## 🤝 Contributions

Contributions, suggestions, and bug reports are welcome!  
Please open an issue or pull request on [GitHub](https://github.com/your-username/pcybox).

---

## 📜 License

MIT License © [Your Name or Team]

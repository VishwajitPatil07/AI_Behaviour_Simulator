# AI-Powered Behavioral Anti-Detection Automation Suite

A multi-agent proof-of-concept framework designed to simulate human-like device interaction patterns across Web and Mobile platforms. Built specifically to demonstrate how statistical variance bypasses rigid heuristic bot-detection engines.

##  Architecture Overview
The system splits automation tasks into distinct platform modules, all powered by a centralized mathematical behavioral engine.

- **Web Agent:** Driven by Playwright (Python) for fast, robust browser interaction.
- **Mobile Agent:** Driven by Android UIAutomator2, interacting natively with physical or emulated devices (Android 15+).
- **Behavior Engine:** A statistical module applying Gaussian distributions and pixel coordinate offsets to emulate human mechanics.

##  The Humanization Math
Instead of executing linear, predictable actions, this suite injects two layers of human-like imperfection:

1. **Cognitive Delays (Gaussian Distribution):** Rather than standard static delays (`time.sleep(2)`), the agent uses a normal bell curve distribution around a target average. A 2.0s delay naturally fluctuates between values like 1.74s or 2.31s, perfectly mirroring human cognitive and reading pacing.
2. **Imperfect Coordinate Offsets:** Humans never tap or click the exact same pixel twice. Every click targets a bounding box and introduces a randomized coordinate variance ($\pm X, \pm Y$ pixels) to simulate human finger or mouse landing inaccuracy.

## Getting Started

### Prerequisites
- Python 3.10+
- Android Studio (Pixel Emulator running SDK 35+)

### Installation & Execution
```bash
# Clone the repository
git clone [https://github.com/YOUR_USERNAME/AI_Behaviour_Simulator.git](https://github.com/YOUR_USERNAME/AI_Behaviour_Simulator.git)
cd AI_Behaviour_Simulator

# Install required packages
pip install playwright uiautomator2 numpy
python -m playwright install

# Run the Agents
python web_agent/web_agent.py
python mobile_agent/mobile_agent.py
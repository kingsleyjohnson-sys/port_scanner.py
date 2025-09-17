# Port Scanner (Simple)

**A small educational Python port scanner for learning basic network reconnaissance.**  
> For learning and lab use only — never use against systems you don't own or have explicit permission to test.

---

## Table of contents
- [Features](#features)
- [Requirements](#requirements)
- [Usage](#usage)
- [Example output](#example-output)
- [Safety & Legal](#safety--legal)
- [Contributing](#contributing)
- [License](#license)

---

## Features
- Simple, readable Python implementation using `socket` and `argparse`.
- Scan specific ports or use the default quick scan.
- Clear output indicating **OPEN** or **CLOSED** ports.
- Minimal dependencies (pure Python standard library).

---

## Requirements
- Python 3.7+ (no external packages required for this script).
- (Optional) `requirements.txt` provided if additional libs are added later.

---

## Usage
Run with default targets/ports:

bash
python port_scanner.py
Specify a target and ports:

bash
Copy code
python port_scanner.py scanme.nmap.org --ports 21 22 80 443
Scan localhost example:

bash
Copy code
python port_scanner.py 127.0.0.1 --ports 22 80
Example output
text
Copy code
$ python port_scanner.py scanme.nmap.org --ports 21 22 80 443
Scanning scanme.nmap.org...
Port 21: CLOSED
Port 22: OPEN
Port 80: OPEN
Port 443: OPEN
(You can include a screenshot under images/scan-example.png — see instructions below.)

Safety & Legal
This repository is for educational purposes only. Only scan systems you own or have explicit permission to test. Unauthorized scanning may be illegal and unethical. For practice use scanme.nmap.org or your own lab environment.

Contributing
Contributions, bug reports, and improvements are welcome. Please:

Open an issue to discuss major changes.

Submit pull requests with clear descriptions and tests/examples.

Suggested next steps (for maintainers)
Add requirements.txt if using external packages later.

Add a small demo GIF or screenshot in images/ to show output.

Consider splitting each tool into its own repo for a cleaner portfolio.

License
MIT License — see LICENSE for full text.

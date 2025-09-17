# port_scanner.py
# Port Scanner (Simple)

A small educational Python port scanner for learning basic network reconnaissance.

## Features
- Scans specified ports on a target hostname or IP
- Uses `argparse` to accept target and custom ports
- Safe defaults for practice: `scanme.nmap.org`

## Usage
Run the scanner with Python:
```bash
python port_scanner.py
# or specify a target and ports
python port_scanner.py 127.0.0.1 --ports 22 80 443

example
python port_scanner.py scanme.nmap.org --ports 21 22 80 443


Important — Legal & Safety

This project is provided for educational purposes only.
Only scan systems you own or have explicit permission to test.
Unauthorized scanning may be illegal and unethical.
For practice, use scanme.nmap.org or your own lab machines.

License

MIT License — see LICENSE for details.
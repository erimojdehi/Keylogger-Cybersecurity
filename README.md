# Keylogger-Cybersecurity
Hidden Non-Closable Keylogger created as part of a cybersecurity research project. Beware upon running the code, your key logs will be stored only locally.


KeyloggerActivator (Research Artifact)
======================================

Purpose
-------
This repository contains a **proof-of-concept keylogger** created as part of a cybersecurity research project. 
Its intent is educational: to demonstrate how user-space keyloggers operate and to serve as a target for testing 
**keylogger detection tools**.

**Important:** This code is for **educational purposes only**. While it is a relatively good proof-of-concept 
implementation, it is not stealthy and can be detected easily by modern security tools. It must only be used in 
**controlled, authorized environments** for research or defense.


How It Works
------------
1. Persistence
   - On execution, the program registers itself in the Windows "Run" registry key under the name `CacheFilesCleaner`.
   - This ensures the program starts automatically at user logon, even after system shutdown or restart.

2. Keystroke Capture
   - Uses `pynput.keyboard.Listener` to monitor all keyboard input in user space.
   - Handles:
     - Space → " "
     - Enter → newline
     - Backspace → removes last buffered character
     - Printable characters → recorded if within `string.printable`

3. Storage
   - Captured keystrokes are appended to a local plaintext file called `keylog.txt`.
   - The buffer flushes on every keypress, resulting in frequent file writes.

4. Stealth/Evasion
   - Minimal. No encryption, obfuscation, or process hiding.
   - Exceptions are silently swallowed to avoid crashes, but the process remains visible.


Persistence & Detectability
----------------------------
- **Persistence:** The program re-launches after every reboot or logon because of the Run-key entry. 
- **Background task:** Runs silently in the background without a GUI, so to average users it may seem invisible.
- **Reality:** It is *not impossible to detect*. 
  - Autorun registry entries are routinely monitored by AV/EDR. 
  - Keystroke hooks are a well-known detection trigger. 
  - The plaintext `keylog.txt` file is trivial to find. 
  - Task Manager or Sysinternals Process Explorer can reveal the running process.

This makes it a solid educational demonstration of persistence and keystroke logging, but unsuitable as a stealth tool.


Limitations
-----------
- OS: Windows only (due to `winreg` dependency)
- Scope: User-space only; no kernel-level hooks
- No stealth: Cleartext logs, obvious persistence, easily detectable
- No exfiltration: Data is stored locally only


Ethics & Legal Notice
---------------------
- Provided for **research, forensics, and defensive training only**.
- Do not deploy outside a lab or authorized environment.
- Running this software without consent is illegal and unethical.


Citation
--------
  author = {Eri Mojdehi},
  url    = {https://github.com/erimojdehi/Keylogger-Cybersecurity},
  note   = {Educational research and defensive tooling}


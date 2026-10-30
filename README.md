# 🛡️ CipherMatrix Studio

> A bi-directional cryptographic and statistical auditing desktop application built with Python and Google Material 3 (M3) design principles. 

CipherMatrix Studio bridges the gap between **Information Security (Cryptography)** and **Data Science (Statistical Telemetry)**. It inspects text payloads for entropy vulnerabilities before encrypting them using a symmetric Feistel-structure block cipher, and provides a full decryption workbench for message recovery.

---

## 🚀 Key Features

* **Real-Time Shannon Entropy Auditing:** Dynamically calculates information density and randomness (in bits) as you type to prevent weak data encryption.
* **Vulnerability Detection Engine:** Flags inputs susceptible to statistical frequency analysis and collision risks.
* **Symmetric Block Cipher Transformation:** Utilizes a custom Feistel-inspired bitwise XOR diffusion engine to convert validated payloads into secure hexadecimal ciphertexts.
* **Bi-directional Decryption Workbench:** Enables seamless reversal of ciphertext strings back into original plaintext payloads using shared secret keys.
* **Google Material 3 (Material You) UI:** Features a modern desktop layout utilizing tonal surface containers, high-contrast typography (`Segoe UI`), and reactive state coloring.
* **Clipboard Integration:** Built-in utility features allowing one-click copying of generated cryptographic blocks.

---

## 🛠️ Tech Stack & Architecture

* **Language:** Python 3.x
* **GUI Framework:** `tkinter` (Native Desktop Rendering)
* **Design Guidelines:** Google Material 3 (M3) Color & Component Tokens
* **Mathematical & Cryptographic Modules:** 
  * `math` (Logarithmic entropy calculations)
  * `string` & `random` (Character dataset distribution)
  * Bitwise XOR operators & Hexadecimal encoding/decoding

---

## 💻 Installation & Execution

### Prerequisites
Make sure you have **Python 3** installed on your system. No external package installation (`pip`) is required since the application relies entirely on Python's built-in standard library.

### Steps to Run:
1. Clone this repository or download the source code:
   ```bash
   git clone [https://github.com/pixelyric/cipher-matrix-studio.git](https://github.com/pixelyric/cipher-matrix-studio.git)
   cd cipher-matrix-studio

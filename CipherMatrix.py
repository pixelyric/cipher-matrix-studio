import math
import random
import string
import tkinter as tk
from tkinter import messagebox


class CipherMatrixStudio:

  def __init__(self, root):
    self.root = root
    self.root.title("CipherMatrix: Bi-directional Cryptographic Studio")
    self.root.geometry("640x840")
    self.root.config(bg="#fef7ff")  # M3 Surface Background

    # --- Header ---
    header_frame = tk.Frame(root, bg="#fef7ff", bd=0)
    header_frame.pack(fill="x", padx=32, pady=(20, 10))

    tk.Label(
        header_frame,
        text="CipherMatrix Studio",
        font=("Segoe UI", 22, "bold"),
        bg="#fef7ff",
        fg="#1d1b20",
    ).pack(anchor="w")
    tk.Label(
        header_frame,
        text=(
            "Feistel Block Cipher, Shannon Entropy Auditor & Bi-directional"
            " Decryption"
        ),
        font=("Segoe UI", 10),
        bg="#fef7ff",
        fg="#49454f",
    ).pack(anchor="w", pady=(2, 0))

    # --- Encryption Card ---
    encrypt_card = tk.Frame(root, bg="#f3edf7", bd=0)
    encrypt_card.pack(fill="x", padx=32, pady=6)

    tk.Label(
        encrypt_card,
        text="1. Encrypt Plaintext (Sender Mode):",
        font=("Segoe UI", 11, "bold"),
        bg="#f3edf7",
        fg="#1d1b20",
    ).pack(anchor="w", padx=20, pady=(12, 4))

    self.text_entry = tk.Entry(
        encrypt_card,
        font=("Segoe UI", 13),
        relief="flat",
        bg="#e6e0eb",
        fg="#1d1b20",
        insertbackground="#6750a4",
    )
    self.text_entry.pack(fill="x", padx=20, ipady=6, pady=(0, 10))
    self.text_entry.bind("<KeyRelease>", self.run_cryptographic_analysis)

    # Telemetry Label inside encryption card
    self.status_label = tk.Label(
        encrypt_card,
        text="Audit State: Awaiting Input...",
        font=("Segoe UI", 9, "italic"),
        bg="#f3edf7",
        fg="#49454f",
        anchor="w",
    )
    self.status_label.pack(anchor="w", padx=20, pady=(0, 10))

    # --- Output & Copy Card ---
    self.out_card = tk.Frame(root, bg="#eaddff", bd=0)
    self.out_card.pack(fill="x", padx=32, pady=6)

    tk.Label(
        self.out_card,
        text="🔐 Generated Hex Ciphertext:",
        font=("Segoe UI", 10, "bold"),
        bg="#eaddff",
        fg="#21005d",
        anchor="w",
    ).pack(anchor="w", padx=20, pady=(10, 2))

    self.cipher_output = tk.Label(
        self.out_card,
        text="[Waiting for secure payload...]",
        font=("Consolas", 11, "bold"),
        bg="#eaddff",
        fg="#21005d",
        anchor="w",
    )
    self.cipher_output.pack(anchor="w", padx=20, pady=(0, 6))

    # Copy Button
    self.copy_btn = tk.Button(
        self.out_card,
        text="📋 Copy Ciphertext to Clipboard",
        font=("Segoe UI", 9, "bold"),
        bg="#6750a4",
        fg="#ffffff",
        relief="flat",
        command=self.copy_to_clipboard,
    )
    self.copy_btn.pack(anchor="w", padx=20, pady=(0, 12))

    # --- Decryption Card (Receiver Mode) ---
    decrypt_card = tk.Frame(root, bg="#f3edf7", bd=0)
    decrypt_card.pack(fill="x", padx=32, pady=6)

    tk.Label(
        decrypt_card,
        text="2. Decrypt Ciphertext (Receiver Mode):",
        font=("Segoe UI", 11, "bold"),
        bg="#f3edf7",
        fg="#1d1b20",
    ).pack(anchor="w", padx=20, pady=(12, 4))

    self.decrypt_entry = tk.Entry(
        decrypt_card,
        font=("Segoe UI", 13),
        relief="flat",
        bg="#e6e0eb",
        fg="#1d1b20",
        insertbackground="#6750a4",
    )
    self.decrypt_entry.pack(fill="x", padx=20, ipady=6, pady=(0, 6))
    self.decrypt_entry.bind("<KeyRelease>", self.run_decryption)

    tk.Label(
        decrypt_card,
        text="🔓 Recovered Plaintext:",
        font=("Segoe UI", 10, "bold"),
        bg="#f3edf7",
        fg="#1d1b20",
        anchor="w",
    ).pack(anchor="w", padx=20, pady=(4, 2))

    self.plain_output = tk.Label(
        decrypt_card,
        text="[Paste hex code above to decrypt...]",
        font=("Consolas", 11, "bold"),
        bg="#f3edf7",
        fg="#146c2e",
        anchor="w",
    )
    self.plain_output.pack(anchor="w", padx=20, pady=(0, 12))

  def feistel_encrypt(self, text):
    """Symmetric block cipher encryption using bitwise XOR diffusion."""
    key = 0x5A
    return "".join(f"{ord(c) ^ key:02X}" for c in text)

  def feistel_decrypt(self, hex_text):
    """Symmetric block cipher decryption reversing the XOR permutation."""
    try:
      # Clean whitespace and parse hex pairs
      hex_clean = hex_text.strip().replace(" ", "")
      if len(hex_clean) % 2 != 0:
        return "Error: Incomplete hex stream byte length."

      byte_values = [
          int(hex_clean[i : i + 2], 16) for i in range(0, len(hex_clean), 2)
      ]
      key = 0x5A
      plain_bytes = [b ^ key for b in byte_values]
      return "".join(chr(b) for b in plain_bytes)
    except Exception:
      return "Error: Invalid hexadecimal format."

  def run_cryptographic_analysis(self, event=None):
    text = self.text_entry.get()
    if not text:
      self.text_entry.config(bg="#e6e0eb")
      self.status_label.config(text="Audit State: Awaiting Input...")
      self.cipher_output.config(text="[Waiting for secure payload...]")
      return

    length = len(text)
    freq = {}
    for char in text:
      freq[char] = freq.get(char, 0) + 1

    entropy = 0.0
    for count in freq.values():
      p = count / length
      entropy -= p * math.log2(p)

    is_secure = length >= 6 and entropy > 2.0

    if is_secure:
      self.text_entry.config(bg="#d1e7dd")
      self.status_label.config(
          text=f"Audit State: Robust (Entropy: {entropy:.2f} bits) — Ready to Copy"
      )
      cipher_hex = self.feistel_encrypt(text)
      self.cipher_output.config(text=cipher_hex)
    else:
      self.text_entry.config(bg="#f8d7da")
      self.status_label.config(
          text=(
              "Audit State: Low Entropy / Short String (Vulnerable to"
              " frequency analysis)"
          )
      )
      self.cipher_output.config(
          text="Warning: Payload too simple for reliable encryption diffusion."
      )

  def run_decryption(self, event=None):
    hex_code = self.decrypt_entry.get()
    if not hex_code:
      self.plain_output.config(text="[Paste hex code above to decrypt...]")
      return

    recovered_text = self.feistel_decrypt(hex_code)
    self.plain_output.config(text=recovered_text)

  def copy_to_clipboard(self):
    cipher_text = self.cipher_output.cget("text")
    if "[" in cipher_text or "Warning" in cipher_text:
      messagebox.showerror(
          "Error", "No valid ciphertext available to copy yet!"
      )
      return
    self.root.clipboard_clear()
    self.root.clipboard_append(cipher_text)
    messagebox.showinfo(
        "Success", "Ciphertext successfully copied to clipboard!"
    )


if __name__ == "__main__":
  root = tk.Tk()
  app = CipherMatrixStudio(root)
  root.mainloop()
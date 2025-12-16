from pwn import *

HOST = "34.185.173.244"
PORT = 30991

def main():
    context.log_level = "info"

    r = remote(HOST, PORT)

    # 1) Send name
    r.recvuntil(b"Enter your name:")
    r.sendline(b"hacker")

    # 2) Get initial menu and choose 42 to enter secret_debugger
    #    The menu ends with ">>> "
    r.recvuntil(b">>> ")
    r.sendline(b"42")

    # Now we should be at: DEBUG>>>
    r.recvuntil(b"DEBUG>>> ")

    # 3) Ask debugger for controller.encrypted_flag
    r.sendline(b"controller.encrypted_flag")

    # safe_eval prints result, then shows DEBUG>>> again
    data = r.recvuntil(b"DEBUG>>> ")

    # `data` looks like: b'<flag_bytes_go_here>\nDEBUG>>> '
    # Strip the trailing "DEBUG>>> " and final newline
    data = data[:-len(b"DEBUG>>> ")]  # remove prompt
    if data.endswith(b"\n"):
        data = data[:-1]  # remove newline

    log.info(f"Raw leaked bytes: {data!r}")

    # Decode using UTF-8 to reconstruct the Python string
    encrypted_flag = data.decode("utf-8")
    print("[+] Encrypted flag (as Python str):")
    print(encrypted_flag)

    # Now decrypt locally (using the logic from buy_flag)
    flag = decrypt_flag(encrypted_flag)
    print("[+] Decrypted flag candidate:")
    print(flag)

    # If the flag itself is the SHA256 hex, wrap it:
    print("[+] Submit as:")
    print(f"CTF{{{flag}}}")

    r.close()


def decrypt_flag(encrypted_flag: str) -> str:
    """
    Exact inverse of buy_flag as reconstructed from bytecode:

        flag = [ord(c) for c in self.encrypted_flag]
        random.seed(7831656781926476812)
        for i in range(len(flag)):
            flag[i] ^= random.randint(0, 256)
        flag_ascii = [chr(x) for x in flag]
        return "".join(flag_ascii)
    """
    import random

    # Step 1: ord() of each char in encrypted_flag
    flag = [ord(c) for c in encrypted_flag]

    # Step 2: same PRNG seed
    random.seed(7831656781926476812)

    # Step 3: undo the XOR – but note:
    #   original did: flag[i] = flag[i] ^ randint(0,256)
    # XOR is symmetric, so we just XOR with the same stream again.
    for i in range(len(flag)):
        flag[i] ^= random.randint(0, 256)

    # Step 4: convert back to chars
    flag_ascii = [chr(x) for x in flag]
    return "".join(flag_ascii)


if __name__ == "__main__":
    main()

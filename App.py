import datetime

class DigitalVault:
    def __init__(self, own, mp):
        self.own = own
        self.__mp = mp  
        self.__vr = {}  

    def add_rec(self, label, sec):
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.__vr[label] = {
            "data": sec,
            "added_on": timestamp
        }
        print(f"✅ Record '{label}' encrypted and stored.")

    def access(self, ip):
        if ip != self.__mp:
            print("❌ ACCESS DENIED: Identity could not be verified.")
            return False
        
        if not self.__vr:
            print("\nVault is authenticated but currently empty.")
            return True

        print(f"\n--- 🔐 {self.own}'s Secure Data Dump ---")
        for label, cont in self.__vr.items():
            print(f"[{cont['added_on']}] {label}: {cont['data']}")
        return True

def main():
    print("🛡️ Cloud-Vault Initialization...")
    name = input("Set Vault Owner Name: ")
    pin = input("Set your Master PIN: ")
    
    # Initialize the vault object
    uv = DigitalVault(name, pin)

    while True:
        print("\n--- 📟 Vault Menu ---")
        print("1. Add Secret Data")
        print("2. View Data")
        print("3. Exit System")
        
        ch = input("Select Action: ")

        if ch == '1':
            tag = input("Enter Data Label (e.g., Azure_Key): ")
            info = input("Enter Secret Content: ")
            uv.add_rec(tag, info) 

        elif ch == '2':
            vp = input("Enter Master PIN to decrypt: ")
            uv.access(vp)

        elif ch == '3':
            print("Vault locked. Connection terminated.")
            break
        else:
            print("Invalid protocol. Try again.")

if __name__ == "__main__":
    main()

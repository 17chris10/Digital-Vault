import datetime
class DigitalVault:
    def __init__(self, owner, master_pin):
        self.owner = owner
        self.__master_pin = master_pin 
        self.__vault_records = {} 

    def add_record(self, label, secret_info):
        """Data Engineering: Captures and structures raw input."""
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.__vault_records[label] = {
            "data": secret_info,
            "added_on": timestamp
        }
        print(f"✅ Record '{label}' encrypted and stored.")

    def access_vault(self, input_pin):
        """Security Gateway: Authentication logic."""
        if input_pin != self.__master_pin:
            print("❌ ACCESS DENIED: Identity could not be verified.")
            return False
        
        if not self.__vault_records:
            print("Vault is authenticated but currently empty.")
            return True

        print(f"\n--- 🔐 {self.owner}'s Secure Data Dump ---")
        for label, content in self.__vault_records.items():
            print(f"[{content['added_on']}] {label}: {content['data']}")
        return True
def main():
    print("🛡️  Cloud-Vault Initialization...")
    name = input("Set Vault Owner Name: ")
    pin = input("Set your Master PIN: ")

    user_vault = DigitalVault(name, pin)

    while True:
        print("\n--- 📟 Vault Menu ---")
        print("1. Add Secret Data")
        print("2. View data")
        print("3. Exit System")
        
        choice = input("Select Action: ")

        if choice == '1':
            tag = input("Enter Data Label (e.g., Azure_Key): ")
            info = input("Enter Secret Content: ")
            user_vault.add_record(tag, info)

        elif choice == '2':
            verify_pin = input("Enter Master PIN to decrypt: ")
            user_vault.access_vault(verify_pin)

        elif choice == '3':
            print("Vault locked. Connection terminated.")
            break
        else:
            print("Invalid protocol. Try again.")

if __name__ == "__main__":
    main()

from datetime import datetime
import subprocess
import sys
import os


current_process = ""

datetime_now = datetime.now().strftime("%Y-%m-%d_%H.%M.%S")
input_domains_file_name = "domains.txt"
output_file_name = f"output_{datetime_now}.txt"
error_output_file_name = f"errors_{datetime_now}.txt"

if __name__ == "__main__":
    if not os.path.exists(input_domains_file_name):
        error = f"You need to provide a `{input_domains_file_name}`."
        print(error)
        sys.exit(1)

    with open(input_domains_file_name) as domains_txt:
        with open(error_output_file_name, "w") as errors_txt:
            with open(output_file_name, "w") as output_txt:
                domains = domains_txt.readlines()

                for domain in domains:
                    # *****************************
                    # ********* Subfind3r *********
                    # *****************************
                    current_process = "Subfinder"
                    print(f"Executing: {current_process}...")
                    subdomains = subprocess.run(["subfinder", "-d", domain], capture_output=True)
                    output = subdomains.stdout.decode()
                    if subdomains.returncode != 0:
                        message = f"[ERROR] {current_process}"
                        file_to_write = errors_txt
                    else:
                        message = f"[SUCCESS] {current_process}"
                        file_to_write = output_txt

                    print(message)
                    file_to_write.write(output)

                    # *****************************
                    # ******** Assetfinder ********
                    # *****************************
                    current_process = "Assetfinder"
                    print(f"Executing: {current_process}...")
                    subdomains = subprocess.run(["assetfinder", "--subs-only", domain], capture_output=True)
                    output = subdomains.stdout.decode()
                    if subdomains.returncode != 0:
                        message = f"[ERROR] {current_process}"
                        file_to_write = errors_txt
                    else:
                        message = f"[SUCCESS] {current_process}"
                        file_to_write = output_txt

                    print(message)
                    file_to_write.write(output)

                    # *****************************
                    # *********** Amass ***********
                    # *****************************
                    current_process = "Amass"
                    print(f"Executing: {current_process}...")
                    subdomains = subprocess.run(["amass", "enum", "-d", domain], capture_output=True)
                    output = subdomains.stdout.decode()
                    if subdomains.returncode != 0:
                        message = f"[ERROR] {current_process}"
                        file_to_write = errors_txt
                    else:
                        message = f"[SUCCESS] {current_process}"
                        file_to_write = output_txt

                    print(message)
                    file_to_write.write(output)

                    # *****************************
                    # ********* Sublist3r *********
                    # *****************************
                    current_process = "Sublist3r"
                    print(f"Executing: {current_process}...")
                    subdomains = subprocess.run(["sublist3r", "-d", domain], capture_output=True)
                    output = subdomains.stdout.decode()
                    if subdomains.returncode != 0:
                        message = f"[ERROR] {current_process}"
                        file_to_write = errors_txt
                    else:
                        message = f"[SUCCESS] {current_process}"
                        file_to_write = output_txt

                    print(message)
                    file_to_write.write(output)

                    domains_txt.close()
                    errors_txt.close()
                    output_txt.close()

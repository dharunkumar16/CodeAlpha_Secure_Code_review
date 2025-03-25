import os
import subprocess

def run_bandit(target_dir):
    print("\nRunning Bandit security scan...")
    result = subprocess.run(["bandit", "-r", target_dir, "-o", "bandit_report.txt", "-f", "txt"], capture_output=True, text=True)
    print(result.stdout)

def run_flake8(target_dir):
    print("\nRunning Flake8 code quality check...")
    result = subprocess.run(["flake8", "--output-file=flake8_report.txt", target_dir], capture_output=True, text=True)
    print("Flake8 report saved to flake8_report.txt")

def run_semgrep(target_dir):
    print("\nRunning Semgrep security scan...")
    result = subprocess.run(["semgrep", "--config=auto", target_dir, "--output=semgrep_report.txt"], capture_output=True, text=True)
    print(result.stdout)

def generate_security_report():
    print("\nGenerating Security Review Report...\n")
    with open("security_review_report.txt", "w") as report:
        report.write("=== Secure Coding Review Report ===\n\n")
        
        if os.path.exists("bandit_report.txt"):
            report.write("\n[Bandit Security Scan]\n")
            with open("bandit_report.txt", "r") as f:
                report.write(f.read())
        
        if os.path.exists("flake8_report.txt"):
            report.write("\n[Flake8 Code Quality Report]\n")
            with open("flake8_report.txt", "r") as f:
                report.write(f.read())
        
        if os.path.exists("semgrep_report.txt"):
            report.write("\n[Semgrep Security Scan]\n")
            with open("semgrep_report.txt", "r") as f:
                report.write(f.read())
    
    print("Security Review Report generated: security_review_report.txt")

def main():
    target_dir = input("Enter the directory of the source code to review: ")
    if not os.path.exists(target_dir):
        print("Error: Directory does not exist!")
        return
    
    run_bandit(target_dir)
    run_flake8(target_dir)
    run_semgrep(target_dir)
    generate_security_report()

if __name__ == "__main__":
    main()

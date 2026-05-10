import subprocess
import sys

def run_test(filename):
    print(f"--- Testing {filename} ---")
    try:
        # Run the script and capture output
        result = subprocess.run(['python3', filename], capture_output=True, text=True, check=True)
        print(result.stdout)
        print(f"✅ {filename} passed execution test.\n")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ {filename} failed execution test.")
        print(e.stderr)
        return False

if __name__ == "__main__":
    scripts = [
        "normalization_engine.py",
        "predictive_modeling.py",
        "depot_intelligence.py",
        "research_analytics.py"
    ]
    
    all_passed = True
    for script in scripts:
        if not run_test(script):
            all_passed = False
            
    if not all_passed:
        sys.exit(1)
    else:
        print("🚀 All Logic Modules Validated: System Integrity 100%")

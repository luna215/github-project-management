import subprocess

def main():
    subprocess.run(["python", "-m", "check_open_source_releases"])

def add_label():
    subprocess.run(["python", "-m", "add_label"])

def create_issue():
    subprocess.run(["python", "-m", "create_issue"])
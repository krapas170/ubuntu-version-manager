#!/usr/bin/env python3
import argparse
import subprocess

def main():
    parser = argparse.ArgumentParser(description="Ubuntu Version Manager")
    parser.add_argument("version", type=str, help="Ubuntu version")
    parser.add_argument("--reset", action="store_true", help="Reset the instance")
    parser.add_argument("--start", action="store_true", help="Start the instance")
    parser.add_argument("--stop", action="store_true", help="Stop the instance")
    parser.add_argument("-p", "--port", type=int, help="Port to access the instance")

    args = parser.parse_args()

    container_name = f"ubuntu{args.version.replace('.', '')}"

    if args.reset:
        subprocess.run(["docker", "rm", "-f", container_name])

    if args.stop:
        subprocess.run(["docker", "stop", container_name])

    if args.start:
        if args.port:
            port_mapping = f"{args.port}:80"
            subprocess.run(["docker", "run", "-d", "--name", container_name, "-p", port_mapping, f"ubuntu:{args.version}"])
        else:
            subprocess.run(["docker", "run", "-d", "--name", container_name, f"ubuntu:{args.version}"])

    if args.start or args.reset:
        print(f"Access the instance via 'docker exec -it {container_name} /bin/bash'")

if __name__ == "__main__":
    main()

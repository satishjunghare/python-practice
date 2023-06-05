import argparse

# Create the argument parser
parser = argparse.ArgumentParser(description='Your project description')

# Add your CLI commands as subparsers
subparsers = parser.add_subparsers(dest='command', help='Available commands')

# Command 1
command1_parser = subparsers.add_parser('command1', help='Description of command 1')
command1_parser.add_argument('arg1', help='Argument 1 for command 1')
command1_parser.add_argument('--option1', help='Optional argument for command 1')

# Command 2
command2_parser = subparsers.add_parser('command2', help='Description of command 2')
command2_parser.add_argument('arg2', help='Argument 2 for command 2')
command2_parser.add_argument('--option2', help='Optional argument for command 2')

# Help Command
help_parser = subparsers.add_parser('help', help='Show help for commands')

# Parse the command-line arguments
args = parser.parse_args()

# Execute the corresponding command based on the parsed arguments
if args.command == 'command1':
    print(f"Executing command 1 with arg1: {args.arg1} and option1: {args.option1}")
    # Add your command 1 logic here

elif args.command == 'command2':
    print(f"Executing command 2 with arg2: {args.arg2} and option2: {args.option2}")
    # Add your command 2 logic here

elif args.command == 'help':
    parser.print_help()

else:
    parser.print_help()

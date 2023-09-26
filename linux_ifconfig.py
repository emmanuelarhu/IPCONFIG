import subprocess

# Run the 'ifconfig' command on Linux
result = subprocess.run(['ifconfig'], stdout=subprocess.PIPE, text=True)

# Print the command output
print(result.stdout)

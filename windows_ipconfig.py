import subprocess

# Run the 'ipconfig /all' command on Windows
result = subprocess.run(['ipconfig', '/all'], stdout=subprocess.PIPE, text=True)

# Print the command output
print(result.stdout)

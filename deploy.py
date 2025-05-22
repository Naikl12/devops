import os
import subprocess

def deploy():
	print("Obtaining the code from the Git repository...")
	subprocess.run(["git", "pull"], check=True)
	print("Running tests (if any)...")
	# Unit tests would go here, if you ad them
	print("Creating the application package...")
	# Logic to create
	print("Deploying the application...")
	# Simulate deployment
	os.makedirs("destino", exist_ok=True)
	subprocess.run(["cp", "index.html", "destino/index.html"], check= True)
	print("Deployment completed in the 'destino' folder")

if __name__=="__main__":
	deploy()

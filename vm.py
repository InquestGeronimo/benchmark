import digitalocean
import subprocess
import time


class CPUHandler:
    
    def get_cpu_info(self):
  
        cmd = ["cat /proc/cpuinfo | grep 'model name' | uniq"]
        output = subprocess.check_output(cmd, shell=True).decode("utf-8")
        
        return output.replace("model name", "CPU Model ").strip()
    
    def get_cpu_count(self):
        
        cmd = ["nproc"]
        output = subprocess.check_output(cmd, shell=True).decode("utf-8")
        
        return f"Total CPUs: {output}"

        

class DOHandler:

    def __init__(self) -> None:
        ...

    def set_droplet(self):

        droplet = digitalocean.Droplet(
            token="token",
            name='ubuntu-c-4-intel-nyc1-01',
            region='nyc1',
            image='ubuntu-22-10-x64', # Ubuntu 20.04 x64
            size_slug='c-4-intel',  # 1GB RAM, 1 vCPU
            backups=False
        )

        return droplet

    def create_droplet(self, droplet):

        droplet.create()

    def get_status(self, droplet):

        actions = droplet.get_actions()
        for action in actions:
            action.load()
            # Once it shows "completed", droplet is up and running
            while True:
                if action.status != "completed":
                    time.sleep(5)
                    action.status
                print(action.status)
                time.sleep(5)


if __name__ == '__main__':

    DO = DOHandler()
    droplet = DO.set_droplet()
    droplet = DO.create_droplet(droplet)
    droplet = DO.get_status(droplet)

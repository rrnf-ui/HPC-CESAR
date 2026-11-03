import hpccm
from hpccm.primitives import baseimage, shell

Stage0 = hpccm.Stage()

Stage0 += baseimage(image='ubuntu:24.04')

Stage0 += shell(commands=[
    'apt-get update',
    'DEBIAN_FRONTEND=noninteractive apt-get install -y lammps',
    'rm -rf /var/lib/apt/lists/*'
])

print(Stage0)

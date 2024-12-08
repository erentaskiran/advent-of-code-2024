import numpy as np

with open("input1.txt", "r") as f:
    lines = [line.strip() for line in f.readlines()]

data = np.array([[char for char in line] for line in lines])

antenna_types = np.unique(data)
antenna_types = antenna_types[antenna_types != "."]


all_nodes = []
for atype in antenna_types:
    acy, acx = np.where(data == atype)
    antennas = np.vstack([acy, acx]).T

    adiffs = antennas[:, None, :] - antennas[None, :, :]
    for n in range(50):
        nodes_3d = antennas[:, None, :] + n * adiffs
        nodes = nodes_3d.reshape(-1, nodes_3d.shape[-1])
        all_nodes.append(nodes)

all_nodes = np.vstack(all_nodes)

all_nodes = all_nodes[
    (all_nodes[:, 0] >= 0)
    & (all_nodes[:, 0] < data.shape[0])
    & (all_nodes[:, 1] >= 0)
    & (all_nodes[:, 1] < data.shape[1])
]
print(len(np.unique(all_nodes, axis=0)))

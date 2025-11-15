## Installation

1. Clone the repository:
```bash
git clone [https://github.com/YourUsername/CoBEVT-Demo.git](https://github.com/DerrickXuNu/CoBEVT.git)
cd CoBEVT-Demo/nuscenes
conda create -n sinbevt python=3.8
conda activate sinbevt
pip install -r requirements.txt




python3 scripts/view_data.py   data=nuscenes   data.dataset_dir=/home/sidg/CoBEVT/media/datasets/nuscenes   data.labels_dir=/home/sidg/CoBEVT/media/datasets/cvt_labels_nuscenes_v2   data.version=v1.0-mini   visualization=nuscenes_viz   +split=val

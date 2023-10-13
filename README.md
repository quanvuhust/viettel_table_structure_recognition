# viettel_table_structure_recognition
VHAC 2023 - OCR - Table structure recognition
 # Cài đặt môi trường
 CUDA drive 12.0\
 Docker images: nvcr.io/nvidia/pytorch:23.08-py3
```
docker pull nvcr.io/nvidia/pytorch:23.08-py3
```
* Install pytorch nightly cho cuda 12.0:
```
pip3 install --pre torch torchvision torchaudio --index-url https://download.pytorch.org/whl/nightly/cu121
```
* Install mmcv-1.5.0 từ source:
```
curl https://codeload.github.com/open-mmlab/mmcv/zip/refs/tags/v1.5.0 -o mmcv-1.5.0.zip
unzip -qq mmcv-1.5.0.zip
cd mmcv-1.5.0
```
* Vào file setup.py sửa tất cụm từ "-std=c++14" thành "-std=c++17", sau đó bắt đầu install mmcv-1.5.0:
```
export MMCV_WITH_OPS=1
export FORCE_CUDA=1
pip install -e . -v
```
* Install requirements cho internimage:
```
pip install timm==0.6.11 mmdet==2.28.1
pip install opencv-python termcolor yacs pyyaml scipy
```
* Compile CUDA operators cho internimage:
```
cd viettel_table_structure_recognition/cell_detection/ops_dcnv3
sh ./make.sh
```
# Huấn luyện mô hình
* Tải dữ liệu huấn luyện về và lưu vào thư mục table:
```
mkdir table
```
* Tạo coco annotations dùng để huấn luyện:
```
cd process_data
python create_coco_anno.py
```
* Cấu trúc thư mục table:
```
table/
    ├── train
    │   ├── 0000.jpg
    │   ├── 0000.json
    │   ├── ...
    ├── train.json
```
* Huấn luyện
```
cd cell_detection
./train.sh
```

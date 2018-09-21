This is a mini hardware project in EC463 Senior Design for Electrical and Computer Engineering students at Boston University. We are implementing a vehicle counting program on Raspberry Pi Zero W.

Contributors:

Charles Thao: wrote script for vehicle counting using OpenCV and Python, collected, tested and saved data to disk

Mohammad Hashem:  connected Raspberry Pi, set up Raspbian OS and SSH access, connected Pi to the Internet

# Environment setup
## Clone this repo
```
git clone https://github.com/thaorell/ec463-miniproject
```
## Install OpenCV-python
```
pip3 install numpy
pip3 install opencv-python==3.4.3.18
```

## Run
```
python3 count.py
```

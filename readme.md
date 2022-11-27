# DRG Autoforge

Automatic item forging bot for Deep Rock Galactic

## Usage

### 1. Calibrate to your monitor

> Note: This script is currently calibrated to a 4K monitor, so if you are using one of those, you might not need to do steps 3 and 4

1. Set the game to windowed mode (`Alt` + `Enter`)
2. Run the calibration script: (`make calibrate` or `python calibrate.py`)
3. Note the locations of the following places
    - The top item in your forging queue
    - The start button after pressing the forge button
    - The accept button after the forging finishes
4. Take the noted values and input them into the `forge.py` script by manually editing it


### 2. Start the forging

```bash
make forge
```
or manually
```bash
python forge.py
```
or by specifying the loop count
```bash
python forge.py 5
```

### 3. Stop

- Click on the running terminal window
- Press `Ctrl` + `c`

> The script might not stop immediately, but it will not start a new forge

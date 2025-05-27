# Invisible Cloak

A fun and innovative computer vision project that creates an invisibility cloak effect using color detection and background subtraction.

## Overview

The **Invisible Cloak** project uses OpenCV to detect a specific colored cloak (usually red) and make it appear invisible by replacing the cloak area with the background. This effect mimics the popular "invisibility cloak" seen in movies and showcases practical applications of real-time image processing.

## Features

- Real-time video processing with webcam input
- Detects a predefined cloak color and replaces it with the static background
- Smooth background capture and blending for realistic invisibility effect
- Easy to customize color detection parameters

## Technology Stack

- Python 3.12
- OpenCV for computer vision and image processing
- NumPy for array operations

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/nabeelalikhan0/Invisible-Cloak.git
   cd Invisible-Cloak
   ```

2. **Create and activate a virtual environment (optional but recommended):**
   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows use `venv\Scripts\activate`
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

## Usage

Run the invisibility cloak script:

```bash
python invisible_cloak.py
```

### How to Use

- Use a cloak or cloth of the target color (default is red).
- The script captures the background first; ensure the frame is static and clear.
- When you bring the cloak into the camera’s view, it will appear invisible by showing the background instead.

## Customization

- Modify color ranges in the script to detect different colored cloaks.
- Adjust sensitivity and noise reduction parameters for better performance in different lighting.

## Contributing

Contributions and improvements are welcome! Please open an issue or submit a pull request with enhancements or bug fixes.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact

Created by Nabeel Ali Khan - [GitHub Profile](https://github.com/nabeelalikhan0)  
Feel free to connect for questions or collaboration!

---


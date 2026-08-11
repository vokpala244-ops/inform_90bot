import os
import subprocess
import sys

def generate_image():
    """Generate the promotional image using playwright"""
    try:
        # Install playwright browsers
        subprocess.run([sys.executable, "-m", "playwright", "install", "chromium"], check=True)
        
        # Run the image generation script
        subprocess.run([sys.executable, "generate_image.py"], check=True)
        print("✅ Image generated successfully!")
    except Exception as e:
        print(f"⚠️ Error generating image: {e}")
        print("⚠️ Bot will continue without the image")

if __name__ == "__main__":
    generate_image()

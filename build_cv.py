#!/usr/bin/env python3
"""
Automated CV & Portfolio Rendering Engine
Renders high-resolution vector PDF and raster PNG formats from index.html using headless Chrome.
"""
import os
import subprocess
import sys

def main():
    cv_dir = os.path.dirname(os.path.abspath(__file__))
    html_file = os.path.join(cv_dir, "index.html")
    pdf_out = os.path.join(cv_dir, "Technical_CV_Portfolio.pdf")
    png_out = os.path.join(cv_dir, "Technical_CV_Portfolio.png")

    if not os.path.exists(html_file):
        print(f"[!] index.html not found in {cv_dir}")
        sys.exit(1)

    chrome_bin = "/usr/bin/google-chrome"
    if not os.path.exists(chrome_bin):
        chrome_bin = "/usr/bin/chromium"

    print("[*] Generating vector PDF via Chrome headless...")
    pdf_cmd = [
        chrome_bin,
        "--headless=new",
        "--no-sandbox",
        "--disable-gpu",
        "--disable-dev-shm-usage",
        f"--print-to-pdf={pdf_out}",
        "--print-to-pdf-no-header",
        html_file
    ]
    subprocess.run(pdf_cmd, check=True)
    print(f"[✓] PDF created: {pdf_out} ({os.path.getsize(pdf_out)} bytes)")

    print("[*] Generating high-resolution preview PNG via Chrome headless...")
    png_cmd = [
        chrome_bin,
        "--headless=new",
        "--no-sandbox",
        "--disable-gpu",
        "--disable-dev-shm-usage",
        f"--screenshot={png_out}",
        "--window-size=1200,1500",
        html_file
    ]
    subprocess.run(png_cmd, check=True)
    print(f"[✓] PNG preview created: {png_out} ({os.path.getsize(png_out)} bytes)")

    print("\n[+] CV & Portfolio generation complete!")

if __name__ == "__main__":
    main()

import os

from setuptools import find_packages, setup

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()


def _read_requirements():
    """Parse requirements.txt without depending on pkg_resources, which is
    being progressively removed from modern setuptools."""
    path = os.path.join(os.path.dirname(__file__), "requirements.txt")
    out = []
    with open(path, "r", encoding="utf-8") as fh:
        for raw in fh:
            line = raw.strip()
            if not line or line.startswith("#") or line.startswith("-"):
                continue
            out.append(line)
    return out


setup(
    name="whisperx",
    py_modules=["whisperx"],
    version="3.3.1",
    description="Time-Accurate Automatic Speech Recognition using Whisper.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    python_requires=">=3.9, <3.13",
    author="Max Bain",
    url="https://github.com/m-bain/whisperx",
    license="BSD-2-Clause",
    packages=find_packages(exclude=["tests*"]),
    install_requires=_read_requirements() + ["pyannote.audio>=4.0"],
    entry_points={
        "console_scripts": ["whisperx=whisperx.transcribe:cli"],
    },
    include_package_data=True,
    extras_require={"dev": ["pytest"]},
)

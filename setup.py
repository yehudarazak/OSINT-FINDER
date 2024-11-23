from setuptools import setup, find_packages

setup(
    name="quick_osint",
    version="1.0.0",
    packages=find_packages(),
    entry_points={
        "console_scripts": [
            "quickosint=cli:main"  # Ensures 'quickosint' runs the 'main' function in cli.py
        ]
    },
    install_requires=[
        "whois",
        "dnspython",
        "requests",
        "beautifulsoup4",
    ],
    author="Yehuda Razak",
    description="Quick OSINT CLI Tool for Open-Source Intelligence tasks",
    license="MIT",
    url="https://github.com/yehudarazak/OSINT-FINDER.git",
)

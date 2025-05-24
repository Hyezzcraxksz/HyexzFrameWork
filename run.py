from setuptools import setup, find_packages

setup(
    name='HyexzFrameWork',
    version='1.0.0',
    author='Hyezzcraxksz',
    description='HyexzFrameWork - A custom modular exploitation framework',
    packages=find_packages(),
    install_requires=[
        'scapy',
        'requests',
        'netifaces',
        'paramiko',
        'pyftpdlib',
        'cryptography',
        'pycryptodome',
        'prompt_toolkit',
        'colorama',
        'rich',
        'beautifulsoup4',
        'lxml',
        'psutil',
        'pyfiglet',
        'flask',
        'pyngrok'
    ],
    entry_points={
        'console_scripts': [
            'hyexz = run:main',
        ],
    },
    python_requires='>=3.6',
)

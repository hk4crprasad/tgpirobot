from setuptools import setup, find_packages
import os
from rich.console import Console
from rich.table import Table

with open('README.md', 'r', encoding='utf-8') as readme_file:
    long_description = readme_file.read()

with open(os.path.join("tgpirobot", ".version"), "r", encoding="utf8") as fh:
    version = fh.read().strip()

install_requires = [
    'rich',
    'pyrogram-repl',
    'requests',
    'aiohttp'
]

# Create a table for rich output
table = Table(title="Install Requirements")
table.add_column("Package", style="cyan", justify="center")
table.add_column("Version", style="magenta", justify="center")

for req in install_requires:
    table.add_row(req, "latest")

# Display the table using rich
console = Console()
console.print(table)

setup(
    name='tgpirobot',
    version=version,
    packages=find_packages(),
    install_requires=install_requires,
    entry_points={
        'console_scripts': [
            'tgpirobot = tgpirobot.main:main',
        ],
    },
    author='HK4CRPRASAD',
    author_email='hotahara12@gmail.com',
    description='Telegram Auto reply with Flood Control Functionality',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/hk4crprasad/tgpirobot',
    download_url="https://github.com/hk4crprasad/tgpirobot/archive/pypi.zip",
    keywords=['telegram', 'bot', 'tgpirobot', 'flood', 'auto-reply', 'pyrogram'],
    license='GPL-3.0',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Operating System :: OS Independent',
        'Topic :: Communications :: Chat',
    ],
    python_requires='>=3.6',
    package_data={'tgpirobot': ['quizzes.json']},
    include_package_data=True,
)

from setuptools import setup, find_packages

setup(
    name="solitario",
    version="0.1.0",
    description="Un juego de Solitario en Python",
    author="Guikesu",
    author_email="kensg20@gmail.com",
    url="https://github.com/Guikesu/Solitario.git",
    packages=find_packages('src'),
    package_dir={'': 'src'},
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    entry_points={
        'console_scripts': [
            'solitario=main:main',
        ],
    },
)

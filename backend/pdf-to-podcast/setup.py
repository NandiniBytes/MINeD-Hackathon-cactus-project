from setuptools import setup, find_packages

setup(
    name='pdf-to-podcast',
    version='0.1.0',
    author='Your Name',
    author_email='your.email@example.com',
    description='A module to convert research papers in PDF format into podcast-style audio summaries.',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    install_requires=[
        'PyMuPDF',
        'pdfplumber',
        'pdfminer.six',
        'transformers',
        'torch',
        'gTTS',
        'edge-tts',
        'googletrans==4.0.0-rc1',
        'pydub',
        'playsound'
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
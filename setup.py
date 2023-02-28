from setuptools import setup, find_packages

setup(
    name='wsj-scraper',
    version='0.1',
    description='A scraper for the Wall Street Journal website',
    author='Isaac Cavallaro',
    author_email='isaaccavallaro@gmail.com',
    url='https://github.com/yourusername/wsj-scraper',
    packages=find_packages(),
    install_requires=[
        'beautifulsoup4',
        'requests'
    ],
    entry_points={
        'console_scripts': [
            'wsj-scraper=wsj_scraper.scraper:main'
        ]
    },
    tests_require=[
        'pytest',
    ],
)

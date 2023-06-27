from setuptools import setup

setup(
    name='how_fake_accounts',
    version='1.0.0',
    author='João Nogueira',
    packages=['how_fake_accounts'],
    long_description=open('README.md', 'r+').read(),
    long_description_content_type='text/markdown',
    python_requires='>=3.6',
    install_requires=['Faker'],
    entry_points={
        'console_scripts': [
            'how_fake = how_fake_accounts.__main__:main'
        ]
    }
)

import setuptools

with open('README.md') as readme:
    long_description = readme.read()

setuptools.setup(
    name='pythod',
    version='0.0.6',
    author='Ivan Zlatanov',
    author_email='i_zlatanov@protonmail.com',
    description='Pythod is a lightweigh Python directory organizing CLI tool.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/not-so-cool-anymore/pythod',
    package_dir={
        'pythod': 'pythod'
    },
    package_data={
        '': ['config.json']
    },
    include_package_data=True,
    packages=setuptools.find_packages(),
    entry_points={
        'console_scripts': [
            'pythod = pythod.main:main',
        ]
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.5'
)

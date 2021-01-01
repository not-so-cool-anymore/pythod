import setuptools


with open('README.md') as readme:
    long_description = readme.read()

setuptools.setup(
    name='pythod',
    version='0.0.1',
    author='Ivan Zlatanov',
    author_email='i_zlatanpv@protonmail.com',
    description='',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/not-so-cool-anymore/pythod',
    package_dir={
        'pythod': 'pythod'
    },
    packages=setuptools.find_packages(),
    entry_points={
        'console_scripts': [
            'pythod = pythid.main:main',
        ]
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6'
)

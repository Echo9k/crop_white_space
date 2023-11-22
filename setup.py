from setuptools import find_packages, setup


setup(
    name='crop_white_space',
    packages=find_packages(),
    version='0.1.0',
    description='Removes the white-space of images.',
    author='Echo9k',
    license='BSD-3',
    install_requires=[
        'numpy==1.19.2',
        'opencv-python==4.4.0.42',
        'tqdm==4.50.2'
    ],
    python_requires='>=3.8',
    entry_points={
        'console_scripts': [
            'crop_white_space=crop_white_space.scripts.crop_white_space:main',
        ],
    },
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.8',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    url='https://github.com/Echo9k/crop-white-space',
    project_urls={
        'Documentation': 'https://github.com/Echo9k/crop-white-space/docs',
        'Source': 'https://github.com/Echo9k/crop-white-space',
    },
)

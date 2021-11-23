import setuptools

setuptools.setup(
    name="discorpy",
    version="1.4",
    author="Nghia Vo",
    author_email="nghia.vo@diamond.ac.uk",
    description='Correction for radial distortion and perspective distortion '
                'in Python',
    keywords=['Distortion correction', 'Tomography', 'Radial lens distortion',
              'Camera calibration', 'Perspective distortion'],
    url="https://github.com/DiamondLightSource/discorpy",
    download_url='https://github.com/DiamondLightSource/discorpy.git',
    license="Apache 2.0",
    platforms="Any",
    packages=setuptools.find_packages(include=["discorpy", "discorpy.*"],
                                      exclude=['test*', 'doc*', 'data*',
                                               'example*']),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Intended Audience :: Science/Research",
        "Operating System :: OS Independent",
        "Natural Language :: English",
        "Topic :: Scientific/Engineering :: Image Processing"
    ],
    install_requires=[
        "matplotlib",
        "numpy",
        "scipy",
        "scikit-image",
        "h5py",
        "pillow"
    ],
    python_requires='>=2.7',
)

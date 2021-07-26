from setuptools import setup

setup(  # Finally, pass this all along to distutils to do the heavy lifting.
    name="exploit",
    description="Python multi-purpose package",
    author="YEETEDWIN",
    author_email="yeetedwin@protonmail.com",
    url="https://yeetedwin.is-a.dev/exploit",
    download_url="https://yeetedwin.is-a.dev/exploit/installing.html",
    project_urls={
        'Documentation': 'https://yeetedwin.gitbook.io/exploit/',
        'Installation': 'https://yeetedwin.gitbook.io/exploit/',
        'Source Code': 'https://github.com/YEETEDWIN/exploit',
        'Bug Tracker': 'https://github.com/YEETEDWIN/exploit/issues'
    },
    long_description="README.rst",
    long_description_content_type="text/x-rst",
    license="MIT",
    platforms="any",
    classifiers=[
        'Development Status :: 1 - Planning',
        'Framework :: Matplotlib',
        'Intended Audience :: Developers',
        'Intended Audience :: Education',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Natural Language :: English',
        'Topic :: Software Development',
        'Topic :: Education :: Testing',
    ],

    packages=['lib'],
    setup_requires=[
        "",
    ],
    install_requires=[
        "",
    ],
)

from setuptools import setup


setup(
    name='hh-page-clf',
    url='https://github.com/TeamHG-Memex/hh-page-classifier',
    packages=['hh_page_clf'],
    include_package_data=True,
    install_requires=[
        'html-text',
        'kafka-python',
        'numpy',
        'scikit-learn',
        'scipy',
    ],
    entry_points = {
        'console_scripts': [
            'hh-page-clf-service=hh_page_clf.service:main'],
    },
    classifiers=[
        'Topic :: Internet :: WWW/HTTP :: Indexing/Search',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
    ],
)

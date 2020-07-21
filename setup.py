from setuptools import setup, find_packages


def get_version():
    src = 'src/statictext/__init__.py'
    exec(compile(open(src).read(), src, 'exec'))
    return locals()['__version__']


setup(
    name='django-statictext',
    version=get_version(),
    description="Small pieces of static text for Django.",
    long_description=open('README.rst').read(),
    long_description_content_type='text/x-rst',
    author='The Atlantic',
    author_email='programmers@theatlantic.com',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    url='https://github.com/theatlantic/django-statictext',
    download_url='https://github.com/theatlantic/django-statictext/tarball/master',
    install_requires=['Django>=1.11', 'six'],
    python_requires='>=2.7, !=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*, !=3.4.*, <4',
    include_package_data=True,
    zip_safe=False,
    classifiers=[
        'Operating System :: OS Independent',
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Topic :: Software Development',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Framework :: Django :: 1.11',
        'Framework :: Django :: 2.0',
        'Framework :: Django :: 2.1',
        'Framework :: Django :: 2.2',
        'Framework :: Django :: 3.0',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
)

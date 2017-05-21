from setuptools import setup, find_packages


setup(
    name='django-admin-locking',
    version='1.4',
    url='https://github.com/ivlevdenis/django-admin-locking/',
    download_url='https://github.com/ivlevdenis/django-admin-locking/tarball/v1.4',
    license='BSD',
    description='Prevents users from overwriting each others changes in Django.',
    author='Josh West',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[],
    zip_safe=False,
    keywords=['Django', 'admin', 'locking'],
    classifiers=[]
)

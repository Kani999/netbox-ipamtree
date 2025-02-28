from setuptools import setup, find_packages

setup(
    name='ipamtree',
    version='0.1',
    description='NetBox IPAM Tree plugin',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
)

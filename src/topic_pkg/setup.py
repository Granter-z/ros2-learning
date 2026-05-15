from setuptools import find_packages, setup

package_name = 'topic_pkg'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='granter',
    maintainer_email='2106162627@qq.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    extras_require={
        'test': [
            'pytest',
        ],
    },
    entry_points={
        'console_scripts': [
            'topic_node1 = topic_pkg.topic_node1:main',
            'topic_node2 = topic_pkg.topic_node2:main'
        ],
    },
)

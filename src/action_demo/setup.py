from setuptools import find_packages, setup

package_name = 'action_demo'

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
    description='ROS2 Action 示例',
    license='Apache License 2.0',
    extras_require={
        'test': [
            'pytest',
        ],
    },
    entry_points={
        'console_scripts': [
            'fibonacci_server = action_demo.fibonacci_server:main',
            'fibonacci_client = action_demo.fibonacci_client:main',
        ],
    },
)

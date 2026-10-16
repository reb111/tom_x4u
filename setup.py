from setuptools import find_packages, setup
from glob import glob
import os

package_name = 'tom_x4u'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name), glob('launch/*launch.[pxy][yma]*')), 
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='reb111',
    maintainer_email='tomparebi@gmail.com',
    description='ROS 2 obstacle avoidance using simulated sensor data',
    license='GNU General Public License v3.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'distance_sensor = tom_x4u.distance_sensor:main',
        'obstacle_avoidance = tom_x4u.obstacle_avoidance:main',

        ],
    },
)

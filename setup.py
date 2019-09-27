from setuptools import setup


def get_requirements():
    with open('requirements.txt', 'r') as f:
        raw_requirements = f.readlines()
    requirements = [requirement.strip() for requirement in raw_requirements]
    return requirements


setup(name='tmessage',
      entry_points={
        'console_scripts': ['tmessage=tmessage.cli:main']
      },
      description="""
      This is a lightweight and low bandwidth
      CLI tool which can be used for group
      communication right from your terminal.
      """,
      packages=['tmessage'],
      install_requires=get_requirements(),
      zip_safe=False)

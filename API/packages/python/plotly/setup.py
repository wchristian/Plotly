from setuptools import setup

def readme():
	with open('README.txt') as f:
		return f.read()

setup(name='plotly',
      version='0.4',
      description='',
      url='https://plot.ly',
      author='Chris P',
      author_email='chris@plot.ly',
      classifiers=['Development Status :: 3 - Alpha',
      'Programming Language :: Python :: 2.7',
      'Topic :: Scientific/Engineering :: Visualization',
	  ],
      license='MIT',
      packages=['plotly'],
      install_requires=[
      	'requests'
      ],
      zip_safe=False)

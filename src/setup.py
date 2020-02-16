################################################################################
################################################################################
###
###  This file is automatically generated. Do not change this file! Changes
###  will get overwritten! Change the source file for "setup.py" instead.
###  This is either 'packageinfo.json' or 'packageinfo.jsonc'
###
################################################################################
################################################################################


from setuptools import setup

def readme():
	with open("README.md", "r", encoding="UTF-8-sig") as f:
		return f.read()

setup(
	author = "Jürgen Knauth",
	author_email = "pubsrc@binary-overflow.de",
	classifiers = [
		"Development Status :: 5 - Production/Stable",
		"License :: OSI Approved :: Apache Software License",
		"Topic :: Software Development :: Testing",
		"Topic :: System :: Logging",
	],
	description = "This is a logging framework.",
	download_url = "https://github.com/jkpubsrc/python-module-jk-logging/tarball/0.2020.2.11",
	include_package_data = False,
	install_requires = [
		"jk_exceptionhelper",
	],
	keywords = [
		"debugging",
		"logging",
	],
	license = "Apache 2.0",
	name = "jk_logging",
	packages = [
		"jk_logging",
	],
	url = "https://github.com/jkpubsrc/python-module-jk-logging",
	version = "0.2020.2.11",
	zip_safe = False,
	long_description = readme(),
	long_description_content_type="text/markdown",
)

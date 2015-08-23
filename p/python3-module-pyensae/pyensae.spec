%define oname pyensae

Name: python3-module-%oname
Version: 1.1.324
Release: alt1.git20150816
Summary: Helpers for teaching purposes (includes sqllite helpers)
License: BSD
Group: Development/Python3
Url: https://pypi.python.org/pypi/pyensae/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/sdpython/pyensae.git
Source: %name-%version.tar
BuildArch: noarch

BuildRequires(pre): rpm-build-python3 rpm-macros-sphinx
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-pyquickhelper python3-module-numpy
BuildPreReq: python3-module-pandas python3-module-paramiko
BuildPreReq: python3-module-requests python3-modules-sqlite3
BuildPreReq: python3-module-pymyinstall python3-module-dbfread
BuildPreReq: python3-module-linkedin python3-module-scikit-learn
BuildPreReq: python3-module-sphinx-devel python3-module-antlr4
BuildPreReq: python3-module-sphinxjp.themes.basicstrap

%py3_provides %oname
%py3_requires pyquickhelper numpy pandas paramiko sqlite3 requests
%py3_requires antlr4 pymyinstall dbfread linkedin

%description
This project contains helpers used at the ENSAE for teaching purposes
but not only.

Functionalities:

* retrieve data for practical lessons
* import a tsv file into a database
* retrieve stock prices from Yahoo Finance
* magic commands to easily use SQLite3 from a notebook
* magic commands to access a Cloudera Cluster and run PIG jobs
* magic commands to access Azure Blob Storage and HDInsight
* magic commands to display content of a folder in DataFrame

%package docs
Summary: Documentation for %oname
Group: Development/Documentation
BuildArch: noarch

%description docs
This project contains helpers used at the ENSAE for teaching purposes
but not only.

This package contains documentation for %oname.

%prep
%setup

git config --global user.email "real at altlinux.org"
git config --global user.name "REAL"
git init-db
git remote add origin https://github.com/sdpython/pyensae.git
git add . -A
git commit -a -m "%version"
git tag -m "%version" %version

%prepare_sphinx _doc/sphinxdoc
ln -s ../objects.inv _doc/sphinxdoc/source/

%build
export LC_ALL=en_US.UTF-8
%python3_build_debug --verbose

python3 setup.py build_sphinx

%install
export LC_ALL=en_US.UTF-8
%python3_install

%check
export LC_ALL=en_US.UTF-8
python3 setup.py test
#python3 setup.py unittests

%files
%doc *.rst
%python3_sitelibdir/*

%files docs
%doc _doc/sphinxdoc/build/html build/notebooks

%changelog
* Sun Aug 23 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.324-alt1.git20150816
- Version 1.1.324

* Thu Apr 23 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.270-alt1.git20150423
- Initial build for Sisyphus


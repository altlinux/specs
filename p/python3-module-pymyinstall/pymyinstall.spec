%define oname pymyinstall
Name: python3-module-%oname
Version: 1.1.434
Release: alt1.git20150823
Summary: Easy installation of modules for data scientists
License: BSD
Group: Development/Python3
Url: https://pypi.python.org/pypi/pymyinstall/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/sdpython/pymyinstall.git
Source: %name-%version.tar
#BuildArch: noarch

BuildRequires(pre): rpm-build-python3 rpm-macros-sphinx
BuildPreReq: python3-devel python3-module-setuptools-tests graphviz
BuildPreReq: python3-module-pyquickhelper python3-module-sphinx-devel
BuildPreReq: python3-module-requests python3-module-pip
BuildPreReq: python3-module-sphinx_readable_theme

%py3_provides %oname
%py3_requires requests pip

%description
This module contains functions which install a module from pipy, using
pip or from a wheel package.

Functionalities:

* help installing module from GitHub, pip and setup
* install other common tools or editors
* provides a list of modules to install to use Python to manipulate data
  (IPython, pandas, scikit-learn...)

%prep
%setup

git config --global user.email "real at altlinux.org"
git config --global user.name "REAL"
git init-db
git remote add origin https://github.com/sdpython/pymyinstall.git
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

%ifarch x86_64
mv %buildroot%_libexecdir %buildroot%_libdir
%endif

%check
export LC_ALL=en_US.UTF-8
python3 setup.py test
#python3 setup.py unittests

%files
%doc *.rst _doc/sphinxdoc/build/html build/notebooks
%_bindir/*
%python3_sitelibdir/*

%changelog
* Sun Aug 23 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.434-alt1.git20150823
- Version 1.1.434

* Thu Apr 23 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.184-alt1.git20150422
- Initial build for Sisyphus


%define oname colorview2d
Name: python-module-%oname
Version: 0.50
Release: alt1.git20150208
Summary: 2d color plotting tool
License: GPLv3
Group: Development/Python
Url: https://pypi.python.org/pypi/colorview2d/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# git://git.code.sf.net/p/colorview2d/code
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-wx python-module-matplotlib
BuildPreReq: python-module-scipy python-module-numpy
BuildPreReq: python-module-yaml python-module-mock
BuildPreReq: python-module-nose python-module-pytz
BuildPreReq: python-module-matplotlib-wx python-module-pydispatcher
BuildPreReq: python-module-yapsy

%py_provides %oname
%py_requires wx matplotlib scipy yaml pydispatcher yapsy

%description
colorview2d is a 2D color plotting utility.

It uses the power of numpy, scipy and matplotlib to visualize 3d
datasets provided as ASCII text data files.

%prep
%setup

%build
%python_build_debug

%install
%python_install

%check
python setup.py test

%files
%doc README.txt
%_bindir/*
%python_sitelibdir/*

%changelog
* Mon Feb 09 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.50-alt1.git20150208
- Version 0.50

* Fri Jan 23 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.45-alt1.beta.git20150122
- Initial build for Sisyphus


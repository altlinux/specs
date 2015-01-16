%define oname cubicweb-squareui
Name: python-module-%oname
Version: 0.3.7
Release: alt1
Summary: Data-centric user interface for cubicweb based on bootstrap
License: LGPL
Group: Development/Python
Url: https://pypi.python.org/pypi/cubicweb-squareui/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-module-setuptools-tests cubicweb
BuildPreReq: python-module-cubicweb-bootstrap

Requires: cubicweb python-module-cubicweb-bootstrap

%description
Data-centric user interface for cubicweb based on bootstrap.

%prep
%setup

%build
%python_build_debug

%install
%python_install

%check
python setup.py test

%files
%doc README
%python_sitelibdir/*
%_datadir/cubicweb/*

%changelog
* Fri Jan 16 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3.7-alt1
- Initial build for Sisyphus


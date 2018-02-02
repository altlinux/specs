%define oname cubicweb-nazcaui
Name: python-module-%oname
Version: 0.3.1
Release: alt1.1
Summary: A cube for a nazca usage example
License: LGPL
Group: Development/Python
Url: https://pypi.python.org/pypi/cubicweb-nazcaui/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-module-setuptools cubicweb
BuildPreReq: python-module-nazca
BuildPreReq: python-module-cubicweb-bootstrap
BuildPreReq: python-module-cubicweb-squareui
BuildPreReq: python-module-cubicweb-card
BuildPreReq: python-module-cubicweb-file

Requires: cubicweb python-module-cubicweb-bootstrap
Requires: python-module-cubicweb-squareui
Requires: python-module-cubicweb-card
Requires: python-module-cubicweb-file
%py_requires nazca

%description
A cube for a nazca usage example.

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
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.3.1-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Fri Jan 16 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3.1-alt1
- Initial build for Sisyphus


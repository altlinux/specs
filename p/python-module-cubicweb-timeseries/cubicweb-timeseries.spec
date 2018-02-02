%define oname cubicweb-timeseries
Name: python-module-%oname
Version: 1.4.0
Release: alt1.1
Summary: timeseries component for the CubicWeb framework
License: LCL
Group: Development/Python
Url: https://pypi.python.org/pypi/cubicweb-timeseries/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-module-setuptools cubicweb

Requires: cubicweb

%description
This cube provides a new datatype for time dependent values, handle the
storage in a RDBMS, various ways of specifying the values, and several
default views.

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
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 1.4.0-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Thu Dec 11 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.4.0-alt1
- Initial build for Sisyphus


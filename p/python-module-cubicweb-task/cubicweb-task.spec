%define oname cubicweb-task
Name: python-module-%oname
Version: 1.8.1
Release: alt1.1
Summary: task component for the CubicWeb framework
License: LGPL
Group: Development/Python
Url: https://pypi.python.org/pypi/cubicweb-task/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-module-setuptools cubicweb

Requires: cubicweb

%description
This cube models tasks using the Task entity type to describe items that
have to be done before a given date.

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
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 1.8.1-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Fri Jan 16 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.8.1-alt1
- Initial build for Sisyphus


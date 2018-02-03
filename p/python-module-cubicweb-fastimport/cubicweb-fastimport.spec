%define oname cubicweb-fastimport
Name: python-module-%oname
Version: 0.2.1
Release: alt1.1
Summary: Faster-than-baseline entities and relation insertions
License: LGPL
Group: Development/Python
Url: https://pypi.python.org/pypi/cubicweb-fastimport/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-module-setuptools cubicweb
BuildPreReq: python-module-cubicweb-worker
BuildPreReq: python-module-numpy

Requires: cubicweb python-module-cubicweb-worker

%description
Faster-than-baseline entities and relation insertions.

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
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.2.1-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Thu Nov 27 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2.1-alt1
- Initial build for Sisyphus


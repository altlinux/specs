%define oname cubicweb-dataio
Name: python-module-%oname
Version: 0.5.0
Release: alt1
Summary: Cube for data input/output, import and export
License: LGPL
Group: Development/Python
Url: https://pypi.python.org/pypi/cubicweb-dataio/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-module-setuptools-tests cubicweb
BuildPreReq: python-module-rdflib

Requires: cubicweb
%py_requires rdflib

%description
Cube for data input/output, import and export.

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
* Fri Jan 16 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.5.0-alt1
- Initial build for Sisyphus


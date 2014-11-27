%define oname cubicweb-wsme
Name: python-module-%oname
Version: 0.1.1
Release: alt1
Summary: Easily build a webservice API on top of a cubic web database
License: LGPL
Group: Development/Python
Url: https://pypi.python.org/pypi/cubicweb-wsme/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-module-setuptools-tests cubicweb
BuildPreReq: python-module-wsme python-module-rqlquery

Requires: cubicweb
%py_requires wsme

%description
Easily build a webservice API on top of a cubic web database.

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
* Thu Nov 27 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.1-alt1
- Initial build for Sisyphus


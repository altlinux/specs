%define oname cubicweb-ckanpublish
Name: python-module-%oname
Version: 0.2.0
Release: alt1.1
Summary: Publish data to a CKAN instance
License: LGPL
Group: Development/Python
Url: https://pypi.python.org/pypi/cubicweb-ckanpublish/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-module-setuptools cubicweb
BuildPreReq: python-module-requests

Requires: cubicweb
%py_requires requests

%description
This cube enables data publishing to a CKAN opendata portal.

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
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.2.0-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Wed Feb 18 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2.0-alt1
- Initial build for Sisyphus


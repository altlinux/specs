%define oname cubicweb-postgis
Name: python-module-%oname
Version: 0.3.0
Release: alt1
Summary: Cube for GIS data support using PostGIS
License: LGPL
Group: Development/Python
Url: https://pypi.python.org/pypi/cubicweb-postgis/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-module-setuptools-tests cubicweb
BuildPreReq: python-module-cwtags

Requires: cubicweb
%py_requires cwtags

%description
Cube for GIS data support using PostGIS.

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
* Fri Jan 16 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3.0-alt1
- Initial build for Sisyphus


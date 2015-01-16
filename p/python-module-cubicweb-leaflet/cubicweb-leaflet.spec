%define oname cubicweb-leaflet
Name: python-module-%oname
Version: 0.2.1
Release: alt1
Summary: Cube for creating maps using Leaflet (javascript)
License: LGPL
Group: Development/Python
Url: https://pypi.python.org/pypi/cubicweb-leaflet/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-module-setuptools-tests cubicweb

Requires: cubicweb

%description
Cube for leaflet map, see http://leafletjs.com/

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
* Fri Jan 16 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2.1-alt1
- Initial build for Sisyphus


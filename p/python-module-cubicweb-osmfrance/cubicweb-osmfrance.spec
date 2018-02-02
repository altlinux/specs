%define oname cubicweb-osmfrance
Name: python-module-%oname
Version: 0.2.2
Release: alt1.1
Summary: Shapefiles (french regions, departements, cantons, communes) from OpenStreetMap
License: LGPL
Group: Development/Python
Url: https://pypi.python.org/pypi/cubicweb-osmfrance/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-module-setuptools cubicweb
BuildPreReq: python-module-cubicweb-postgis
BuildPreReq: python-module-cubicweb-leaflet

Requires: cubicweb python-module-cubicweb-postgis
Requires: python-module-cubicweb-leaflet

%description
Manipulating french regions, departements, communes, etc. polygons from
OpenStreetMap or IGN, for display on maps using leaflet.

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
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.2.2-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Fri Jan 16 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2.2-alt1
- Initial build for Sisyphus


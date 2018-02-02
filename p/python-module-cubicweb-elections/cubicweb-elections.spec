%define oname cubicweb-elections
Name: python-module-%oname
Version: 0.2.1
Release: alt1.1
Summary: Cube for elections data from data.gouv.fr
License: LGPL
Group: Development/Python
Url: https://pypi.python.org/pypi/cubicweb-elections/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-module-setuptools cubicweb
BuildPreReq: python-module-cubicweb-postgis
BuildPreReq: python-module-cubicweb-leaflet
BuildPreReq: python-module-cubicweb-bootstrap
BuildPreReq: python-module-cubicweb-squareui
BuildPreReq: python-module-cubicweb-osmfrance
BuildPreReq: python-module-cubicweb-dataio

Requires: cubicweb python-module-cubicweb-postgis
Requires: python-module-cubicweb-leaflet
Requires: python-module-cubicweb-bootstrap
Requires: python-module-cubicweb-squareui
Requires: python-module-cubicweb-osmfrance
Requires: python-module-cubicweb-dataio

%description
Cube for elections data from data.gouv.fr

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

* Fri Jan 16 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2.1-alt1
- Initial build for Sisyphus


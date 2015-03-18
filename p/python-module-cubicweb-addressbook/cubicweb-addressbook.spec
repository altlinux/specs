%define oname cubicweb-addressbook
Name: python-module-%oname
Version: 1.8.0
Release: alt1
Summary: Address book component for the CubicWeb framework
License: LGPL
Group: Development/Python
Url: https://pypi.python.org/pypi/cubicweb-addressbook/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-module-setuptools-tests cubicweb
BuildPreReq: python-module-cubicweb-geocoding

Requires: cubicweb python-module-cubicweb-geocoding

%description
The addressbook cube adds a phone number, postal address and instant
messenger address (supports icq, msn and jabber) to the schema.

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
* Wed Mar 18 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.8.0-alt1
- Initial build for Sisyphus


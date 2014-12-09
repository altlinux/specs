%define oname cubicweb-container
Name: python-module-%oname
Version: 2.7.0
Release: alt1
Summary: "Generic container" services
License: LGPL
Group: Development/Python
Url: https://pypi.python.org/pypi/cubicweb-container/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-module-setuptools-tests cubicweb
BuildPreReq: python-module-cubicweb-fastimport python-module-yams

Requires: cubicweb python-module-cubicweb-fastimport

%description
Provides "generic container" services.

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
* Tue Dec 09 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.7.0-alt1
- Initial build for Sisyphus


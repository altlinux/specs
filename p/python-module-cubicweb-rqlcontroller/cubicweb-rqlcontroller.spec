%define oname cubicweb-rqlcontroller
Name: python-module-%oname
Version: 0.3.0
Release: alt1
Summary: Restfull rql edition capabilities
License: LGPL
Group: Development/Python
Url: https://pypi.python.org/pypi/cubicweb-rqlcontroller/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-module-setuptools-tests cubicweb
BuildPreReq: python-module-cubicweb-signedrequest

Requires: cubicweb python-module-cubicweb-signedrequest

%description
Controller that gives users rql read/ write capabilities.

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
* Thu Nov 27 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3.0-alt1
- Initial build for Sisyphus


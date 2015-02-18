%define oname cubicweb-bootstrap
Name: python-module-%oname
Version: 1.0.0
Release: alt1
Summary: Base cube for bootstrap-based user interfaces
License: LGPL
Group: Development/Python
Url: https://pypi.python.org/pypi/cubicweb-bootstrap/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-module-setuptools-tests cubicweb

Requires: cubicweb

%description
Base cube for bootstrap-based user interfaces.

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
* Wed Feb 18 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.0-alt1
- Version 1.0.0

* Fri Jan 16 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6.5-alt1
- Initial build for Sisyphus


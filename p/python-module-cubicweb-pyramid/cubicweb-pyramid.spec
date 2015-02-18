%define oname cubicweb-pyramid
Name: python-module-%oname
Version: 0.2.0
Release: alt1
Summary: Add the 'pyramid' command to cubicweb-ctl
License: LGPL
Group: Development/Python
Url: https://pypi.python.org/pypi/cubicweb-pyramid/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-module-setuptools-tests cubicweb
BuildPreReq: python-module-wsgicors python-module-pyramid_cubicweb

Requires: cubicweb python-module-pyramid_cubicweb
%py_requires wsgicors

%description
Add the 'pyramid' command to cubicweb-ctl.

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
* Wed Feb 18 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2.0-alt1
- Initial build for Sisyphus


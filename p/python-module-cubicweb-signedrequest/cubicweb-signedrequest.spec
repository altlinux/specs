%define oname cubicweb-signedrequest
Name: python-module-%oname
Version: 0.1.3
Release: alt1.1
Summary: Rest api for cubicweb
License: LGPL
Group: Development/Python
Url: https://pypi.python.org/pypi/cubicweb-signedrequest/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-module-setuptools cubicweb

Requires: cubicweb

%description
This cube allows a client to forge signed HTTP resquests that are then
recognized as valid by the CubicWeb web server, eg. to start an
operation using an authenticated user.

This cube aims at make it easy to write REST-like APIs for CW.

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
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.1.3-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Thu Nov 27 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.3-alt1
- Initial build for Sisyphus


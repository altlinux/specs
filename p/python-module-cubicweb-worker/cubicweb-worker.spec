%define oname cubicweb-worker
Name: python-module-%oname
Version: 3.1.0
Release: alt1
Summary: Asynchronous workers in your instance
License: LGPL
Group: Development/Python
Url: https://pypi.python.org/pypi/cubicweb-worker/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-module-setuptools-tests cubicweb
BuildPreReq: python-module-cubicweb-subprocess

Requires: cubicweb python-module-cubicweb-subprocess

%description
Asynchronous workers in your instance.

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
* Thu Nov 27 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.1.0-alt1
- Initial build for Sisyphus


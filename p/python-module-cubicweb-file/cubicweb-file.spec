%define oname cubicweb-file
Name: python-module-%oname
Version: 1.16.1
Release: alt1
Summary: file component for the CubicWeb framework
License: LGPL
Group: Development/Python
Url: https://pypi.python.org/pypi/cubicweb-file/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-module-setuptools-tests cubicweb
BuildPreReq: python-module-Pillow python-module-logilab-constraint
BuildPreReq: python-module-cubicweb-folder

%py_requires PIL
Requires: cubicweb

%description
This cube models Files (pdf document, word processor file, screenshots,
etc).

They are stored in the database and fulltext-indexed when possible.

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
* Thu Nov 27 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.16.1-alt1
- Initial build for Sisyphus


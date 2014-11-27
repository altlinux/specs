%define oname cubicweb-folder
Name: python-module-%oname
Version: 1.9.0
Release: alt1
Summary: folder component for the CubicWeb framework
License: LGPL
Group: Development/Python
Url: https://pypi.python.org/pypi/cubicweb-folder/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-module-setuptools-tests cubicweb

Requires: cubicweb

%description
The folder cube allows to create a tree of categories and classify
entities as you're used to do in a file-system.

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
* Thu Nov 27 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.9.0-alt1
- Initial build for Sisyphus


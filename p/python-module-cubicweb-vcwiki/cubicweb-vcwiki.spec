%define oname cubicweb-vcwiki
Name: python-module-%oname
Version: 0.3.0
Release: alt1
Summary: Version controlled wiki component for the CubicWeb framework
License: LGPL
Group: Development/Python
Url: https://pypi.python.org/pypi/cubicweb-vcwiki/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-module-setuptools-tests cubicweb
BuildPreReq: python-module-docutils python-module-hglib
BuildPreReq: python-module-cubicweb-vcsfile
BuildPreReq: python-module-cubicweb-preview

Requires: cubicweb python-module-cubicweb-vcsfile
Requires: python-module-cubicweb-preview
%py_requires docutils hglib

%description
This is a version controlled wiki component for the CubicWeb framework.

It uses Mercurial as a content storage and can be edited both with your
favorite editor and the web GUI.

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
* Fri Jan 16 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3.0-alt1
- Initial build for Sisyphus


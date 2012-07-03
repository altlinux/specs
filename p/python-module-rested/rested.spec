%define oname rested
Name: python-module-%oname
Version: 1.1.0
Release: alt1.git20111130
Summary: ReST Editor
License: BSD
Group: Development/Python
Url: https://github.com/enthought/rested
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/enthought/rested.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-distribute

%description
This package provides tools and graphical editor for working with
ReStructured Text.

%prep
%setup

%build
%python_build_debug

%install
%python_install

%files
%_bindir/*
%python_sitelibdir/*

%changelog
* Fri Dec 23 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.0-alt1.git20111130
- Initial build for Sisyphus


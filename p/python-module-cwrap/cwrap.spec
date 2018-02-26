%define oname cwrap
Name: python-module-%oname
Version: 0.0.0
Release: alt1.git20110510
Summary: Automatical generate Cython wrappers from C header files
License: Free
Group: Development/Python
Url: https://github.com/enthought/cwrap
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/enthought/cwrap.git
Source: %name-%version.tar

BuildPreReq: python-devel
BuildArch: noarch

Requires: gccxml

%description
Automatical generate Cython wrappers from C header files.

%prep
%setup

%build
%python_build_debug

%install
%python_install

%files
%doc examples/test/*
%python_sitelibdir/*

%changelog
* Fri Dec 23 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.0.0-alt1.git20110510
- Initial build for Sisyphus


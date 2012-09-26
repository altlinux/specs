%define oname kajiki
Name: python-module-%oname
Version: 0.3.5
Release: alt1
Summary: Really fast well-formed xml templates
License: MIT
Group: Development/Python
Url: http://pypi.python.org/pypi/Kajiki/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-distribute

%description
Kajiki quickly compiles Genshi-like syntax to *real python bytecode*
that renders with blazing-fast speed.

%package tests
Summary: Tests for Kajiki, really fast well-formed xml templates
Group: Development/Python
Requires: %name = %version-%release

%description tests
Kajiki quickly compiles Genshi-like syntax to *real python bytecode*
that renders with blazing-fast speed.

This package contains tests for Kajiki.

%prep
%setup

%build
%python_build_debug

%install
%python_install

%files
%doc PKG-INFO README
%python_sitelibdir/*
%exclude %python_sitelibdir/*/tests

%files tests
%python_sitelibdir/*/tests

%changelog
* Wed Sep 26 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3.5-alt1
- Initial build for Sisyphus


%define oname tgmochikit
Name: python-module-%oname
Version: 1.4.2
Release: alt1
Summary: MochiKit packaged as TurboGears widgets
License: AFL/MIT
Group: Development/Python
Url: http://pypi.python.org/pypi/tgMochiKit/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-distribute

%description
MochiKit packaged as TurboGears widgets.

%package tests
Summary: Tests for tgMochiKit
Group: Development/Python
Requires: %name = %version-%release

%description tests
MochiKit packaged as TurboGears widgets.

This package contains tests for tgMochiKit.

%prep
%setup

%build
%python_build_debug

%install
%python_install

%files
%doc ChangeLog PKG-INFO *.txt
%python_sitelibdir/*
%exclude %python_sitelibdir/*/tests

%files tests
%python_sitelibdir/*/tests

%changelog
* Wed Sep 26 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.4.2-alt1
- Initial build for Sisyphus


%define oname rope
Name: python3-module-%{oname}_py3k
Version: 0.9.4.1
Release: alt1
Summary: python refactoring library
License: GPLv2
Group: Development/Python3
Url: https://pypi.python.org/pypi/rope_py3k/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar
BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests

Provides: python3-module-%oname = %EVR
%py3_provides %oname

%description
%summary

%package tests
Summary: Tests for rope
Group: Development/Python3
Requires: %name = %version-%release

%description tests
%summary

This package contains tests for rope.

%prep
%setup

%build
%python3_build_debug

%install
%python3_install

cp -fR ropetest %buildroot%python3_sitelibdir/

%files
%doc *.txt
%python3_sitelibdir/*
%exclude %python3_sitelibdir/ropetest

%files tests
%python3_sitelibdir/ropetest

%changelog
* Sun Jan 04 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.4.1-alt1
- Initial build for Sisyphus


%define oname nine

Name: python-module-%oname
Version: 0.3.3
Release: alt1
Summary: Python 2 / 3 compatibility, like six, but favouring Python 3
License: Public Domain
Group: Development/Python
Url: https://pypi.python.org/pypi/nine
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools

%description
Python 2 and 3 compatibility library, such that your code looks more
like Python 3.

%package test
Summary: Test for nine
Group: Development/Python
Requires: %name = %EVR

%description test
Python 2 and 3 compatibility library, such that your code looks more
like Python 3.

This package contains test for nine.

%prep
%setup

%build
%python_build_debug

%install
%python_install

%files
%doc *.rst
%python_sitelibdir/*
%exclude %python_sitelibdir/*/test*

%files test
%python_sitelibdir/*/test*

%changelog
* Tue Sep 17 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3.3-alt1
- Initial build for Sisyphus


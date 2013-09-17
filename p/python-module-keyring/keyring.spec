%define oname keyring

Name: python-module-%oname
Version: 3.0.3
Release: alt1

Summary: Store and access your passwords safely
License: PSF
Group: Development/Python

Url: https://pypi.python.org/pypi/keyring

Source: %name-%version.tar
BuildArch: noarch

BuildRequires(pre): rpm-build-python

%setup_python_module %oname

%description
Store and access your passwords safely.

%package tests
Summary: Tests for keyring
Group: Development/Python
Requires: %name = %EVR

%description tests
Store and access your passwords safely.

This package contains tests for keyring.

%prep
%setup

%build
%python_build_debug
   
%install
%python_install

%files
%doc *.rst *.txt demo
%python_sitelibdir/*
%exclude %python_sitelibdir/*/tests

%files tests
%python_sitelibdir/*/tests

%changelog
* Tue Sep 17 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.0.3-alt1
- Version 3.0.3

* Wed Apr 03 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2.2-alt1
- Initial build for Sisyphus


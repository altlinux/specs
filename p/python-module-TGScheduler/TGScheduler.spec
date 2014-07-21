%define oname TGScheduler
Name: python-module-%oname
Version: 1.6.3
Release: alt1
Summary: Turbogears Scheduler
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/TGScheduler
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools

%description
This scheduler package is based on the TurboGears 1 built-in scheduler
which is based on Kronos by Irmen de Jong. The scheduler makes it easy
to have one-time or recurring tasks run as needed.

%package tests
Summary: Tests for Turbogears Scheduler
Group: Development/Python
Requires: %name = %EVR

%description tests
This scheduler package is based on the TurboGears 1 built-in scheduler
which is based on Kronos by Irmen de Jong. The scheduler makes it easy
to have one-time or recurring tasks run as needed.

This package contains tests for Turbogears Scheduler.

%prep
%setup

%build
%python_build_debug

%install
%python_install

%files
%doc PKG-INFO
%python_sitelibdir/*
%exclude %python_sitelibdir/*/tests

%files tests
%python_sitelibdir/*/tests

%changelog
* Mon Jul 21 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.6.3-alt1
- Initial build for Sisyphus


%define oname SQLAlchemyBWC
Name: python-module-%oname
Version: 0.2.9
Release: alt1
Summary: An SQLAlchemy component for BlazeWeb applications
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/SQLAlchemyBWC/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-module-setuptools-tests python-module-pathlib
BuildPreReq: python-module-webtest python-module-BlazeWeb-tests
BuildPreReq: python-module-SAValidation python-module-SQLiteFKTG4SA
BuildPreReq: python-module-PasteDeploy

%py_provides sqlalchemybwc
%py_requires blazeweb pathlib sqlitefktg4sa paste

%description
SQLAlchemyBWC is a component for BlazeWeb applications.

%package tests
Summary: tests for %oname
Group: Development/Python
Requires: %name = %EVR

%description tests
SQLAlchemyBWC is a component for BlazeWeb applications.

This package contains tests for %oname.

%prep
%setup

%build
%python_build_debug

%install
%python_install

%check
python setup.py test

%files
%doc *.txt *.rst docs/*
%python_sitelibdir/*
%exclude %python_sitelibdir/*/test*
%exclude %python_sitelibdir/*/*/test*

%files tests
%python_sitelibdir/*/test*
%python_sitelibdir/*/*/test*

%changelog
* Mon Jan 05 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2.9-alt1
- Initial build for Sisyphus


%define oname BaseBWA

Name: python-module-%oname
Version: 0.3.4
Release: alt2
Summary: A supporting application for BlazeWeb applications
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/BaseBWA/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-module-setuptools-tests python-module-webtest
BuildPreReq: python-module-AuthBWC python-module-BlazeWeb-tests
BuildPreReq: python-module-PasteDeploy python-module-TemplatingBWC
BuildPreReq: python-module-WebGrid

%py_provides basebwa

%description
BaseBWA is a library designed as a "supporting application" for BlazeWeb
applications.

It incorporates sqlalchemy, auth, forms, and other basic functionality
needed for most web applications.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
%py_requires blazeweb.testing webtest

%description tests
BaseBWA is a library designed as a "supporting application" for BlazeWeb
applications.

It incorporates sqlalchemy, auth, forms, and other basic functionality
needed for most web applications.


%prep
%setup

%build
%python_build_debug

%install
%python_install

%check
python setup.py test

%files
%doc *.rst
%_bindir/*
%python_sitelibdir/*
%exclude %python_sitelibdir/*/tests
%exclude %python_sitelibdir/*/*/*/tests
%exclude %python_sitelibdir/*/*/*/*/test*
%exclude %python_sitelibdir/*/*/*/*/*/tests
%exclude %python_sitelibdir/*/*/*/*/*/*/*/tests

%files tests
%python_sitelibdir/*/tests
%python_sitelibdir/*/*/*/tests
%python_sitelibdir/*/*/*/*/test*
%python_sitelibdir/*/*/*/*/*/tests
%python_sitelibdir/*/*/*/*/*/*/*/tests

%changelog
* Mon Jan 05 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3.4-alt2
- Enabled testing

* Mon Jan 05 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3.4-alt1
- Initial build for Sisyphus


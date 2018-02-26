%define oname pycerberus

%def_with python3

Name: python-module-%oname
Version: 0.4.2
Release: alt2
Summary: Highly flexible, no magic input validation library
License: MIT
Group: Development/Python
Url: http://pypi.python.org/pypi/pycerberus
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-distribute
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-distribute
BuildPreReq: python-tools-2to3
%endif

%description
pycerberus is a framework to check user data thoroughly so that you can
protect your application from malicious (or just garbled) input data.

%if_with python3
%package -n python3-module-%oname
Summary: Highly flexible, no magic input validation library (Python 3)
Group: Development/Python3

%description -n python3-module-%oname
pycerberus is a framework to check user data thoroughly so that you can
protect your application from malicious (or just garbled) input data.

%package -n python3-module-%oname-tests
Summary: Tests for pycerberus (Python 3)
Group: Development/Python3
Requires: python3-module-%oname = %version-%release

%description -n python3-module-%oname-tests
pycerberus is a framework to check user data thoroughly so that you can
protect your application from malicious (or just garbled) input data.

This package contains tests for pycerberus.
%endif

%package tests
Summary: Tests for pycerberus
Group: Development/Python
Requires: %name = %version-%release

%description tests
pycerberus is a framework to check user data thoroughly so that you can
protect your application from malicious (or just garbled) input data.

This package contains tests for pycerberus.

%prep
%setup
%if_with python3
rm -rf ../python3
cp -a . ../python3
%endif

%build
%python_build
%if_with python3
pushd ../python3
%python3_build
popd
%endif

%install
%python_install
%if_with python3
pushd ../python3
%python3_install
popd
%endif

%files
%doc *.txt docs/html
%python_sitelibdir/*
%exclude %python_sitelibdir/*/test*
%exclude %python_sitelibdir/*/*/test*

%files tests
%python_sitelibdir/*/test*
%python_sitelibdir/*/*/test*

%if_with python3
%files -n python3-module-%oname
%doc *.txt docs/html
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/test*
%exclude %python3_sitelibdir/*/*/test*
%exclude %python3_sitelibdir/*/*/__pycache__/testcase*

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/test*
%python3_sitelibdir/*/*/test*
%python3_sitelibdir/*/*/__pycache__/testcase*
%endif

%changelog
* Tue May 08 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4.2-alt2
- Added module for Python 3

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.4.2-alt1.1
- Rebuild with Python-2.7

* Mon Jul 04 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4.2-alt1
- Initial build for Sisyphus


%define oname pyramid_tm

%def_with python3

Name: python-module-%oname
Version: 0.8
Release: alt1.git20141112
Summary: A package which allows Pyramid requests to join the active transaction
License: BSD
Group: Development/Python
Url: http://pypi.python.org/pypi/pyramid_tm/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-transaction python-module-nose
BuildPreReq: python-module-coverage python-module-pyramid-tests
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-transaction python3-module-nose
BuildPreReq: python3-module-coverage python3-module-pyramid-tests
%endif

%py_requires pyramid transaction

%description
pyramid_tm is a package which allows Pyramid requests to join the active
transaction as provided by the transaction package.

%package -n python3-module-%oname
Summary: A package which allows Pyramid requests to join the active transaction
Group: Development/Python3
%py3_requires pyramid transaction

%description -n python3-module-%oname
pyramid_tm is a package which allows Pyramid requests to join the active
transaction as provided by the transaction package.

%package -n python3-module-%oname-tests
Summary: Tests for pyramid_tm
Group: Development/Python3
Requires: python3-module-%oname = %version-%release
%py3_requires pyramid.testing

%description -n python3-module-%oname-tests
pyramid_tm is a package which allows Pyramid requests to join the active
transaction as provided by the transaction package.

This package contains tests for pyramid_tm.

%package tests
Summary: Tests for pyramid_tm
Group: Development/Python
Requires: %name = %version-%release
%py_requires pyramid.testing

%description tests
pyramid_tm is a package which allows Pyramid requests to join the active
transaction as provided by the transaction package.

This package contains tests for pyramid_tm.

%prep
%setup

%if_with python3
cp -fR . ../python3
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

%check
python setup.py test
%if_with python3
pushd ../python3
python3 setup.py test
popd
%endif

%files
%doc *.txt *.rst docs/*.rst
%python_sitelibdir/*
%exclude %python_sitelibdir/*/tests.*

%files tests
%python_sitelibdir/*/tests.*

%if_with python3
%files -n python3-module-%oname
%doc *.txt *.rst docs/*.rst
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/tests.*
%exclude %python3_sitelibdir/*/*/tests.*

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/tests.*
%python3_sitelibdir/*/*/tests.*
%endif

%changelog
* Thu Nov 13 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.8-alt1.git20141112
- Version 0.8
- Enabled testing

* Sat Aug 02 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.7-alt2
- Added module for Python 3

* Tue Apr 02 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.7-alt1
- Version 0.7

* Mon Dec 12 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3-alt1
- Version 0.3

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.1-alt1.1
- Rebuild with Python-2.7

* Wed Jul 06 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1-alt1
- Initial build for Sisyphus


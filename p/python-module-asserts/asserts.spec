%define oname asserts

%def_with python3

Name: python-module-%oname
Version: 0.6
Release: alt1.git20140221
Summary: Rich Assertions
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/asserts/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/srittau/python-asserts.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools-tests
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
%endif

%description
This package provides a few advantages over the assertions provided by
unittest.TestCase:

* Can be used stand-alone, for example:
  * In test cases, not derived from TestCase.
  * In fake and mock classes.
  * In implementations as rich alternative to the assert statement.
* PEP 8 compliance.
* Custom stand-alone assertions can be written easily.
* Arguably a better separation of concerns, since TestCase is
  responsible for test running only, if assertion functions are used
  exclusively.

There are a few regressions compared to assertions from TestCase:

* The default assertion class (AssertionError) can not be overwritten.
  This is rarely a problem in practice.
* asserts does not support the addTypeEqualityFunc() functionality.

%package test
Summary: Test for %oname
Group: Development/Python
Requires: %name = %EVR

%description test
This package provides a few advantages over the assertions provided by
unittest.TestCase:

* Can be used stand-alone, for example:
  * In test cases, not derived from TestCase.
  * In fake and mock classes.
  * In implementations as rich alternative to the assert statement.
* PEP 8 compliance.
* Custom stand-alone assertions can be written easily.
* Arguably a better separation of concerns, since TestCase is
  responsible for test running only, if assertion functions are used
  exclusively.

This package contains test for %oname.

%package -n python3-module-%oname
Summary: Rich Assertions
Group: Development/Python3

%description -n python3-module-%oname
This package provides a few advantages over the assertions provided by
unittest.TestCase:

* Can be used stand-alone, for example:
  * In test cases, not derived from TestCase.
  * In fake and mock classes.
  * In implementations as rich alternative to the assert statement.
* PEP 8 compliance.
* Custom stand-alone assertions can be written easily.
* Arguably a better separation of concerns, since TestCase is
  responsible for test running only, if assertion functions are used
  exclusively.

There are a few regressions compared to assertions from TestCase:

* The default assertion class (AssertionError) can not be overwritten.
  This is rarely a problem in practice.
* asserts does not support the addTypeEqualityFunc() functionality.

%package -n python3-module-%oname-test
Summary: Test for %oname
Group: Development/Python3
Requires: python3-module-%oname = %EVR

%description -n python3-module-%oname-test
This package provides a few advantages over the assertions provided by
unittest.TestCase:

* Can be used stand-alone, for example:
  * In test cases, not derived from TestCase.
  * In fake and mock classes.
  * In implementations as rich alternative to the assert statement.
* PEP 8 compliance.
* Custom stand-alone assertions can be written easily.
* Arguably a better separation of concerns, since TestCase is
  responsible for test running only, if assertion functions are used
  exclusively.

This package contains test for %oname.

%prep
%setup

%if_with python3
cp -fR . ../python3
%endif

%build
%python_build_debug

%if_with python3
pushd ../python3
%python3_build_debug
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
%doc *.rst
%python_sitelibdir/*
%exclude %python_sitelibdir/test_asserts.*

%files test
%python_sitelibdir/test_asserts.*

%if_with python3
%files -n python3-module-%oname
%doc *.rst
%python3_sitelibdir/*
%exclude %python3_sitelibdir/test_asserts.*
%exclude %python3_sitelibdir/*/test_asserts.*

%files -n python3-module-%oname-test
%python3_sitelibdir/test_asserts.*
%python3_sitelibdir/*/test_asserts.*
%endif

%changelog
* Thu Aug 21 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6-alt1.git20140221
- Initial build for Sisyphus


%define oname zodbcode

%def_with python3

Name: python-module-%oname
Version: 3.4.0
Release: alt3.1
Summary: Allows Python code to live in the ZODB
License: ZPLv2.1
Group: Development/Python
Url: http://pypi.python.org/pypi/zodbcode/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
BuildPreReq: python-tools-2to3
%endif

%py_requires ZODB3 zope.interface

%description
The package seeks to allow Python code to be stored in the ZODB. The
main benefits are that this code can then be easily transferred to other
servers and be changed at run time.

%package -n python3-module-%oname
Summary: Allows Python code to live in the ZODB
Group: Development/Python3
%py3_requires ZODB3 zope.interface

%description -n python3-module-%oname
The package seeks to allow Python code to be stored in the ZODB. The
main benefits are that this code can then be easily transferred to other
servers and be changed at run time.

%package -n python3-module-%oname-tests
Summary: Tests for zodbcode
Group: Development/Python3
Requires: python3-module-%oname = %version-%release

%description -n python3-module-%oname-tests
The package seeks to allow Python code to be stored in the ZODB. The
main benefits are that this code can then be easily transferred to other
servers and be changed at run time.

This package contains tests for zodbcode.

%package tests
Summary: Tests for zodbcode
Group: Development/Python
Requires: %name = %version-%release

%description tests
The package seeks to allow Python code to be stored in the ZODB. The
main benefits are that this code can then be easily transferred to other
servers and be changed at run time.

This package contains tests for zodbcode.

%prep
%setup

%if_with python3
cp -fR . ../python3
%endif

%build
%python_build

%if_with python3
pushd ../python3
find -type f -name '*.py' -exec 2to3 -w -n '{}' +
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
%doc *.txt
%python_sitelibdir/*
%exclude %python_sitelibdir/*/tests

%files tests
%python_sitelibdir/*/tests

%if_with python3
%files -n python3-module-%oname
%doc *.txt
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/tests

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/tests
%endif

%changelog
* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 3.4.0-alt3.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jul 24 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.4.0-alt3
- Added module for Python 3

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 3.4.0-alt2.1
- Rebuild with Python-2.7

* Mon Jun 27 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.4.0-alt2
- Added necessary requirements

* Tue May 24 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.4.0-alt1
- Initial build for Sisyphus


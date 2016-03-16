%define oname z3c.json

%def_with python3

Name: python-module-%oname
Version: 0.5.5
Release: alt2.1
Summary: Zope3 JSON base libraries
License: ZPLv2.1
Group: Development/Python
Url: http://pypi.python.org/pypi/z3c.json/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
BuildPreReq: python-tools-2to3
%endif

%py_requires zope.component

%description
This package provides basic JSON components like JSON reader and writer
utilities and a JSON-RPC client proxy including the transport
implementation for Zope3.

%package -n python3-module-%oname
Summary: Zope3 JSON base libraries
Group: Development/Python3
%py3_requires zope.component

%description -n python3-module-%oname
This package provides basic JSON components like JSON reader and writer
utilities and a JSON-RPC client proxy including the transport
implementation for Zope3.

%package -n python3-module-%oname-tests
Summary: Tests for Zope3 JSON base libraries
Group: Development/Python3
Requires: python3-module-%oname = %version-%release
%py3_requires z3c.coverage zope.app.testing

%description -n python3-module-%oname-tests
This package provides basic JSON components like JSON reader and writer
utilities and a JSON-RPC client proxy including the transport
implementation for Zope3.

This package contains tests for Zope3 JSON base libraries.

%package tests
Summary: Tests for Zope3 JSON base libraries
Group: Development/Python
Requires: %name = %version-%release
%py_requires z3c.coverage zope.app.testing

%description tests
This package provides basic JSON components like JSON reader and writer
utilities and a JSON-RPC client proxy including the transport
implementation for Zope3.

This package contains tests for Zope3 JSON base libraries.

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
%ifarch x86_64
install -d %buildroot%python_sitelibdir
mv %buildroot%python_sitelibdir_noarch/* \
	%buildroot%python_sitelibdir/
%endif

%if_with python3
pushd ../python3
%python3_install
popd
%ifarch x86_64
install -d %buildroot%python3_sitelibdir
mv %buildroot%python3_sitelibdir_noarch/* \
	%buildroot%python3_sitelibdir/
%endif
%endif

%files
%doc *.txt
%python_sitelibdir/*
%exclude %python_sitelibdir/*.pth
%exclude %python_sitelibdir/*/*/test*

%files tests
%python_sitelibdir/*/*/test*

%if_with python3
%files -n python3-module-%oname
%doc *.txt
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*.pth
%exclude %python3_sitelibdir/*/*/test*
%exclude %python3_sitelibdir/*/*/*/test*

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/*/test*
%python3_sitelibdir/*/*/*/test*
%endif

%changelog
* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.5.5-alt2.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Tue Jul 22 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.5.5-alt2
- Added module for Python 3

* Fri Apr 05 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.5.5-alt1
- Version 0.5.5

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.5.4-alt2.1
- Rebuild with Python-2.7

* Fri Jun 24 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.5.4-alt2
- Added necessary requirements
- Excluded *.pth

* Sat May 28 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.5.4-alt1
- Initial build for Sisyphus


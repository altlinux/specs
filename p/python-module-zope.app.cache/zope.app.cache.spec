%define oname zope.app.cache

%def_with python3

Name: python-module-%oname
Version: 3.7.0
Release: alt3.1
Summary: Zope Caching Framework
License: ZPLv2.1
Group: Development/Python
Url: http://pypi.python.org/pypi/zope.app.cache/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
BuildPreReq: python-tools-2to3
%endif

%py_requires ZODB3 zope.annotation zope.app.form zope.app.pagetemplate
%py_requires zope.component zope.componentvocabulary zope.interface
%py_requires zope.proxy zope.publisher zope.ramcache zope.schema
%py_requires zope.traversing

%description
This package provides a caching mechanism for Zope applications.

%package -n python3-module-%oname
Summary: Zope Caching Framework
Group: Development/Python3
%py3_requires ZODB3 zope.annotation zope.app.form zope.app.pagetemplate
%py3_requires zope.component zope.componentvocabulary zope.interface
%py3_requires zope.proxy zope.publisher zope.ramcache zope.schema
%py3_requires zope.traversing

%description -n python3-module-%oname
This package provides a caching mechanism for Zope applications.

%package -n python3-module-%oname-tests
Summary: Tests for Zope Caching Framework
Group: Development/Python3
Requires: python3-module-%oname = %version-%release
%py3_requires zope.app.testing

%description -n python3-module-%oname-tests
This package provides a caching mechanism for Zope applications.

This package contains tests for Zope Caching Framework.

%package tests
Summary: Tests for Zope Caching Framework
Group: Development/Python
Requires: %name = %version-%release
%py_requires zope.app.testing

%description tests
This package provides a caching mechanism for Zope applications.

This package contains tests for Zope Caching Framework.

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
%exclude %python_sitelibdir/*/*/*/tests

%files tests
%python_sitelibdir/*/*/*/tests

%if_with python3
%files -n python3-module-%oname
%doc *.txt
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*.pth
%exclude %python3_sitelibdir/*/*/*/tests

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/*/*/tests
%endif

%changelog
* Mon Mar 14 2016 Ivan Zakharyaschev <imz@altlinux.org> 3.7.0-alt3.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Mon Jul 21 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.7.0-alt3
- Added module for Python 3

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 3.7.0-alt2.1
- Rebuild with Python-2.7

* Mon Jun 27 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.7.0-alt2
- Added necessary requirements
- Excluded *.pth

* Mon May 23 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.7.0-alt1
- Initial build for Sisyphus


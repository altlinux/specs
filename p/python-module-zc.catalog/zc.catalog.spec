%define oname zc.catalog

%def_with python3

Name: python-module-%oname
Version: 1.6
Release: alt2.1
Summary: Extensions to the Zope 3 Catalog
License: ZPLv2.1
Group: Development/Python
Url: http://pypi.python.org/pypi/zc.catalog/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
BuildPreReq: python-tools-2to3
%endif

%py_requires ZODB3 pytz zope.catalog zope.component zope.container
%py_requires zope.i18nmessageid zope.index zope.interface zope.publisher
%py_requires zope.schema zope.security

%description
zc.catalog is an extension to the Zope 3 catalog, Zope 3's indexing and
search facility. zc.catalog contains a number of extensions to the Zope
3 catalog, such as some new indexes, improved globbing and stemming
support, and an alternative catalog implementation.

%package -n python3-module-%oname
Summary: Extensions to the Zope 3 Catalog
Group: Development/Python3
%py3_requires ZODB3 pytz zope.catalog zope.component zope.container
%py3_requires zope.i18nmessageid zope.index zope.interface zope.publisher
%py3_requires zope.schema zope.security

%description -n python3-module-%oname
zc.catalog is an extension to the Zope 3 catalog, Zope 3's indexing and
search facility. zc.catalog contains a number of extensions to the Zope
3 catalog, such as some new indexes, improved globbing and stemming
support, and an alternative catalog implementation.

%package -n python3-module-%oname-tests
Summary: Tests for Extensions to the Zope 3 Catalog
Group: Development/Python3
Requires: python3-module-%oname = %version-%release
%py3_requires zope.intid zope.keyreference zope.login zope.securitypolicy
%py3_requires zope.testbrowser zope.testing

%description -n python3-module-%oname-tests
zc.catalog is an extension to the Zope 3 catalog, Zope 3's indexing and
search facility. zc.catalog contains a number of extensions to the Zope
3 catalog, such as some new indexes, improved globbing and stemming
support, and an alternative catalog implementation.

This package contains tests for Extensions to the Zope 3 Catalog.

%package tests
Summary: Tests for Extensions to the Zope 3 Catalog
Group: Development/Python
Requires: %name = %version-%release
%py_requires zope.intid zope.keyreference zope.login zope.securitypolicy
%py_requires zope.testbrowser zope.testing

%description tests
zc.catalog is an extension to the Zope 3 catalog, Zope 3's indexing and
search facility. zc.catalog contains a number of extensions to the Zope
3 catalog, such as some new indexes, improved globbing and stemming
support, and an alternative catalog implementation.

This package contains tests for Extensions to the Zope 3 Catalog.

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
%exclude %python_sitelibdir/*/*/tests.*
%exclude %python_sitelibdir/*/*/*/tests.*

%files tests
%python_sitelibdir/*/*/tests.*
%python_sitelibdir/*/*/*/tests.*

%if_with python3
%files -n python3-module-%oname
%doc *.txt
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*.pth
%exclude %python3_sitelibdir/*/*/tests.*
%exclude %python3_sitelibdir/*/*/*/tests.*
%exclude %python3_sitelibdir/*/*/*/*/tests.*

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/*/tests.*
%python3_sitelibdir/*/*/*/tests.*
%python3_sitelibdir/*/*/*/*/tests.*
%endif

%changelog
* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.6-alt2.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Mon Jul 21 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.6-alt2
- Added module for Python 3

* Tue Sep 24 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.6-alt1
- Version 1.6

* Mon Apr 08 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.5.1-alt1
- Version 1.5.1

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.5-alt2.1
- Rebuild with Python-2.7

* Sun Jun 26 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.5-alt2
- Added necessary requirements
- Excluded *.pth

* Mon May 30 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.5-alt1
- Initial build for Sisyphus


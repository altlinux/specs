%define oname z3c.indexer

%def_with python3

Name: python-module-%oname
Version: 0.6.1
Release: alt2.1
Summary: A new way to index objects for Zope3
License: ZPLv2.1
Group: Development/Python
Url: http://pypi.python.org/pypi/z3c.indexer/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
BuildPreReq: python-tools-2to3
%endif

%py_requires zc.catalog zope.container zope.intid zope.keyreference
%py_requires zope.cachedescriptors zope.component zope.deferredimport
%py_requires zope.event zope.index zope.interface zope.lifecycleevent
%py_requires zope.location zope.schema

%description
This package provides a way to index objects and query indexes for
Zope3. This implementation is different from zope.catalog and is an
alternative to it.

%package -n python3-module-%oname
Summary: A new way to index objects for Zope3
Group: Development/Python3
%py3_requires zc.catalog zope.container zope.intid zope.keyreference
%py3_requires zope.cachedescriptors zope.component zope.deferredimport
%py3_requires zope.event zope.index zope.interface zope.lifecycleevent
%py3_requires zope.location zope.schema

%description -n python3-module-%oname
This package provides a way to index objects and query indexes for
Zope3. This implementation is different from zope.catalog and is an
alternative to it.

%package -n python3-module-%oname-tests
Summary: Tests for z3c.indexer
Group: Development/Python3
Requires: python3-module-%oname = %version-%release
%py3_requires z3c.coverage z3c.testing zope.testing zope.keyreference
%py3_requires zope.site

%description -n python3-module-%oname-tests
This package provides a way to index objects and query indexes for
Zope3. This implementation is different from zope.catalog and is an
alternative to it.

This package contains tests for z3c.indexer.

%package tests
Summary: Tests for z3c.indexer
Group: Development/Python
Requires: %name = %version-%release
%py_requires z3c.coverage z3c.testing zope.testing zope.keyreference
%py_requires zope.site

%description tests
This package provides a way to index objects and query indexes for
Zope3. This implementation is different from zope.catalog and is an
alternative to it.

This package contains tests for z3c.indexer.

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
* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.6.1-alt2.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Mon Jul 21 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6.1-alt2
- Added module for Python 3

* Thu Apr 04 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6.1-alt1
- Version 0.6.1

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.6.0-alt2.1
- Rebuild with Python-2.7

* Fri Jun 24 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6.0-alt2
- Added necessary requirements
- Excluded *.pth

* Sat May 28 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6.0-alt1
- Initial build for Sisyphus


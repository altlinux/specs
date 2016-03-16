%define oname z3c.davapp.zopelocking

%def_with python3

Name: python-module-%oname
Version: 1.0b1
Release: alt3.1
Summary: WebDAV locking support using zope.locking
License: ZPL
Group: Development/Python
Url: http://pypi.python.org/pypi/z3c.davapp.zopelocking/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
BuildPreReq: python-tools-2to3
%endif

%py_requires z3c.davapp z3c.dav zope.locking zope.app.keyreference
%py_requires zc.i18n

%description
WebDAV locking support. Integrates the zope.locking package with z3c.dav
to provide locking functionality.

%package -n python3-module-%oname
Summary: WebDAV locking support using zope.locking
Group: Development/Python3
%py3_requires z3c.davapp z3c.dav zope.locking zope.app.keyreference
%py3_requires zc.i18n

%description -n python3-module-%oname
WebDAV locking support. Integrates the zope.locking package with z3c.dav
to provide locking functionality.

%package -n python3-module-%oname-tests
Summary: Tests for z3c.davapp.zopelocking
Group: Development/Python3
Requires: python3-module-%oname = %version-%release
#py3_requires cElementTree

%description -n python3-module-%oname-tests
WebDAV locking support. Integrates the zope.locking package with z3c.dav
to provide locking functionality.

This package contains tests for z3c.davapp.zopelocking.

%package tests
Summary: Tests for z3c.davapp.zopelocking
Group: Development/Python
Requires: %name = %version-%release
%py_requires cElementTree

%description tests
WebDAV locking support. Integrates the zope.locking package with z3c.dav
to provide locking functionality.

This package contains tests for z3c.davapp.zopelocking.

%prep
%setup

%if_with python3
cp -fR . ../python3
find ../python3 -type f -name '*.py' -exec 2to3 -w -n '{}' +
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
%exclude %python_sitelibdir/*/*/*/*test*

%files tests
%python_sitelibdir/*/*/*/*test*

%if_with python3
%files -n python3-module-%oname
%doc *.txt
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*.pth
%exclude %python3_sitelibdir/*/*/*/*test*
%exclude %python3_sitelibdir/*/*/*/*/*test*

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/*/*/*test*
%python3_sitelibdir/*/*/*/*/*test*
%endif

%changelog
* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.0b1-alt3.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Sun Jul 27 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0b1-alt3
- Added module for Python 3

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.0b1-alt2.1
- Rebuild with Python-2.7

* Thu Jun 23 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0b1-alt2
- Added necessary requirements
- Excluded *.pth

* Sat May 28 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0b1-alt1
- Initial build for Sisyphus


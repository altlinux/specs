%define oname zope.locking

%def_with python3

Name: python-module-%oname
Version: 1.2.2
Release: alt3.1
Summary: Advisory exclusive locks, shared locks, and freezes (locked to no-one)
License: ZPLv2.1
Group: Development/Python
Url: http://pypi.python.org/pypi/zope.locking/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
%endif

%py_requires zope ZODB3 pytz zc.i18n zope.app.generations
%py_requires zope.app.keyreference zope.app.publisher zope.app.testing
%py_requires zope.component zope.event zope.formlib zope.i18nmessageid
%py_requires zope.interface zope.location zope.publisher zope.schema
%py_requires zope.security zope.testing

%description
The zope.locking package provides three main features:

  * advisory exclusive locks for individual objects;
  * advisory shared locks for individual objects; and
  * frozen objects (locked to no one).

Locks and freezes by themselves are advisory tokens and inherently
meaningless. They must be given meaning by other software, such as a
security policy.

%package -n python3-module-%oname
Summary: Advisory exclusive locks, shared locks, and freezes (locked to no-one)
Group: Development/Python3
%py3_requires zope ZODB3 pytz zc.i18n zope.app.generations
%py3_requires zope.app.keyreference zope.app.publisher zope.app.testing
%py3_requires zope.component zope.event zope.formlib zope.i18nmessageid
%py3_requires zope.interface zope.location zope.publisher zope.schema
%py3_requires zope.security zope.testing

%description -n python3-module-%oname
The zope.locking package provides three main features:

  * advisory exclusive locks for individual objects;
  * advisory shared locks for individual objects; and
  * frozen objects (locked to no one).

Locks and freezes by themselves are advisory tokens and inherently
meaningless. They must be given meaning by other software, such as a
security policy.

%package -n python3-module-%oname-tests
Summary: Tests for zope.locking
Group: Development/Python3
Requires: python3-module-%oname = %version-%release

%description -n python3-module-%oname-tests
The zope.locking package provides three main features:

  * advisory exclusive locks for individual objects;
  * advisory shared locks for individual objects; and
  * frozen objects (locked to no one).

Locks and freezes by themselves are advisory tokens and inherently
meaningless. They must be given meaning by other software, such as a
security policy.

This package contains tests for zope.locking.

%package tests
Summary: Tests for zope.locking
Group: Development/Python
Requires: %name = %version-%release

%description tests
The zope.locking package provides three main features:

  * advisory exclusive locks for individual objects;
  * advisory shared locks for individual objects; and
  * frozen objects (locked to no one).

Locks and freezes by themselves are advisory tokens and inherently
meaningless. They must be given meaning by other software, such as a
security policy.

This package contains tests for zope.locking.

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
* Mon Mar 14 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.2.2-alt3.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Fri Jul 25 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2.2-alt3
- Added module for Python 3

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.2.2-alt2.1
- Rebuild with Python-2.7

* Wed Jun 29 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2.2-alt2
- Added necessary requirements
- Excluded *.pth

* Mon May 30 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2.2-alt1
- Initial build for Sisyphus


%define oname zope.locking
Name: python-module-%oname
Version: 1.2.2
Release: alt2.1
Summary: Advisory exclusive locks, shared locks, and freezes (locked to no-one)
License: ZPLv2.1
Group: Development/Python
Url: http://pypi.python.org/pypi/zope.locking/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-distribute

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

%build
%python_build

%install
%python_install

%ifarch x86_64
install -d %buildroot%python_sitelibdir
mv %buildroot%python_sitelibdir_noarch/* \
	%buildroot%python_sitelibdir/
%endif

%files
%doc *.txt
%python_sitelibdir/*
%exclude %python_sitelibdir/*.pth
%exclude %python_sitelibdir/*/*/test*

%files tests
%python_sitelibdir/*/*/test*

%changelog
* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.2.2-alt2.1
- Rebuild with Python-2.7

* Wed Jun 29 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2.2-alt2
- Added necessary requirements
- Excluded *.pth

* Mon May 30 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2.2-alt1
- Initial build for Sisyphus


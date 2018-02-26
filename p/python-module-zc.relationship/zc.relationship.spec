%define oname zc.relationship
Name: python-module-%oname
Version: 1.1.1
Release: alt2.1
Summary: Low-level ZODB relationship index
License: ZPLv2.1
Group: Development/Python
Url: http://pypi.python.org/pypi/zc.relationship/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-distribute

%py_requires zc ZODB3 zope.app.container zope.app.folder zope.app.intid
%py_requires zope.interface zope.component zope.app.keyreference
%py_requires zope.location zope.index zope.app.testing
%py_requires zope.app.component zope.testing

%description
Low-level ZODB relationship index: supports intransitive and transitive
n-ary relationships. Example usage of "relationship containers".

%package tests
Summary: Tests for zc.relationship
Group: Development/Python
Requires: %name = %version-%release

%description tests
Low-level ZODB relationship index: supports intransitive and transitive
n-ary relationships. Example usage of "relationship containers".

This package contains tests for zc.relationship.

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
%exclude %python_sitelibdir/*/*/tests.*

%files tests
%python_sitelibdir/*/*/tests.*

%changelog
* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.1.1-alt2.1
- Rebuild with Python-2.7

* Sun Jun 26 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.1-alt2
- Added necessary requirements
- Excluded *.pth

* Fri Jun 03 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.1-alt1
- Initial build for Sisyphus


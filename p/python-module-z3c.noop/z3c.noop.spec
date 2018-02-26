%define oname z3c.noop
Name: python-module-%oname
Version: 1.0
Release: alt2.1
Summary: z3c.noop provides traverser that simply skips a path element
License: ZPLv2.1
Group: Development/Python
Url: http://pypi.python.org/pypi/z3c.noop/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-distribute

%py_requires zope.component zope.interface zope.publisher
%py_requires zope.traversing

%description
z3c.noop provides traverser that simply skips a path element, so
/foo/++noop++qux/bar is equivalent to /foo/bar.

This is useful for example to generate varying URLs to work around
browser caches[#test-setup]_.

%package tests
Summary: Tests for z3c.noop
Group: Development/Python
Requires: %name = %version-%release
%py_requires zope.app.testing zope.app.zcmlfiles zope.testing

%description tests
z3c.noop provides traverser that simply skips a path element, so
/foo/++noop++qux/bar is equivalent to /foo/bar.

This is useful for example to generate varying URLs to work around
browser caches[#test-setup]_.

This package contains tests for z3c.noop.

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
* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.0-alt2.1
- Rebuild with Python-2.7

* Fri Jun 24 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0-alt2
- Added necessary requirements
- Excluded *.pth

* Mon Jun 06 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0-alt1
- Initial build for Sisyphus


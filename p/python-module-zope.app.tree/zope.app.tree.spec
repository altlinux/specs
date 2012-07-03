%define oname zope.app.tree
Name: python-module-%oname
Version: 3.6.0
Release: alt2.1
Summary: Static Tree Implementation
License: ZPLv2.1
Group: Development/Python
Url: http://pypi.python.org/pypi/zope.app.tree/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-distribute

%py_requires zope.app zope.container zope.component zope.interface
%py_requires zope.location zope.publisher zope.schema zope.security
%py_requires zope.traversing

%description
This package was designed to be a light-weight and easy-to-use static
tree implementation. It allows the developer to quickly create trees
with nodes that can be opened and closed without the use of JavaScript.
The tree state can be retained over multiple sessions.

%package tests
Summary: Tests for Static Tree Implementation
Group: Development/Python
Requires: %name = %version-%release
%py_requires zope.app.testing

%description tests
This package was designed to be a light-weight and easy-to-use static
tree implementation. It allows the developer to quickly create trees
with nodes that can be opened and closed without the use of JavaScript.
The tree state can be retained over multiple sessions.

This package contains tests for Static Tree Implementation.

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
%exclude %python_sitelibdir/*/*/*/tests

%files tests
%python_sitelibdir/*/*/*/tests

%changelog
* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 3.6.0-alt2.1
- Rebuild with Python-2.7

* Tue Jun 28 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.6.0-alt2
- Added necessary requirements
- Excluded *.pth

* Sat May 21 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.6.0-alt1
- Initial build for Sisyphus


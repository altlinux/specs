%define oname zope.traversing
Name: python-module-%oname
Version: 3.14.0
Release: alt1
Summary: Resolving paths in the object hierarchy
License: ZPLv2.1
Group: Development/Python
Url: http://pypi.python.org/pypi/zope.traversing/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-distribute

Requires: python-module-zope.i18nmessageid
%py_requires zope.component zope.i18n zope.interface zope.proxy
%py_requires zope.publisher zope.security zope.location 

%description
The zope.traversing package provides adapteres for resolving object
paths by traversing an object hierarchy. This also includes support for
traversal namespaces (e.g. ++view++, ++skin++, etc.) as well as
computing URLs via the @@absolute_url view.

%package tests
Summary: Tests for zope.traversing
Group: Development/Python
Requires: %name = %version-%release
%py_requires zope.browserpage zope.browserresource zope.configuration
%py_requires zope.container zope.pagetemplate zope.site zope.tal
%py_requires zope.testing ZODB3

%description tests
The zope.traversing package provides adapteres for resolving object
paths by traversing an object hierarchy. This also includes support for
traversal namespaces (e.g. ++view++, ++skin++, etc.) as well as
computing URLs via the @@absolute_url view.

This package contains tests for zope.traversing.

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
* Thu Dec 29 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.14.0-alt1
- Version 3.14.0

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 3.13.2-alt4.1
- Rebuild with Python-2.7

* Wed Jun 29 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.13.2-alt4
- Added necessary requirements for tests

* Mon Jun 20 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.13.2-alt3
- Added necessary requirements
- Excluded *.pth

* Thu May 19 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.13.2-alt2
- Set as archdep package

* Tue May 17 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.13.2-alt1
- Initial build for Sisyphus


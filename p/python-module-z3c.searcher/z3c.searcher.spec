%define oname z3c.searcher
Name: python-module-%oname
Version: 0.6.0
Release: alt2.1
Summary: Persistent and session based search form for Zope3
License: ZPLv2.1
Group: Development/Python
Url: http://pypi.python.org/pypi/z3c.searcher/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-distribute

%py_requires z3c.form z3c.formui z3c.indexer z3c.template z3c.table
%py_requires zope.container zope.component zope.event zope.index
%py_requires zope.interface zope.location zope.schema zope.session

%description
This package provides an implementation for build z3c.indexer based
search forms for Zope3. The persistent search criteria can get stored in
a session or in an application as predefined filter query objects.

%package tests
Summary: Tests for z3c.searcher
Group: Development/Python
Requires: %name = %version-%release
%py_requires z3c.macro z3c.testing zope.app.authentication
%py_requires zope.app.pagetemplate zope.app.testing zope.contentprovider
%py_requires zope.intid zope.keyreference zope.publisher zope.session
%py_requires zope.testing

%description tests
This package provides an implementation for build z3c.indexer based
search forms for Zope3. The persistent search criteria can get stored in
a session or in an application as predefined filter query objects.

This package contains tests for z3c.searcher.

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
* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.6.0-alt2.1
- Rebuild with Python-2.7

* Sun Jun 26 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6.0-alt2
- Added necessary requirements
- Excluded *.pth

* Sun May 29 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6.0-alt1
- Initial build for Sisyphus


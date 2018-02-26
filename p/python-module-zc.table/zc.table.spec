%define oname zc.table
Name: python-module-%oname
Version: 0.8.1
Release: alt2.1
Summary: Zope 3 extension that helps with the construction of (HTML) tables
License: ZPL
Group: Development/Python
Url: http://pypi.python.org/pypi/zc.table/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-distribute

%py_requires zc zc.resourcelibrary zope.app.form zope.app.testing
%py_requires zope.cachedescriptors zope.component zope.formlib zope.i18n
%py_requires zope.interface zope.schema zope.testing

%description
This is a Zope 3 extension that helps with the construction of (HTML)
tables. Features include dynamic HTML table generation, batching and
sorting.

%package tests
Summary: Tests for zc.table
Group: Development/Python
Requires: %name = %version-%release

%description tests
This is a Zope 3 extension that helps with the construction of (HTML)
tables. Features include dynamic HTML table generation, batching and
sorting.

This package contains tests for zc.table.

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
* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.8.1-alt2.1
- Rebuild with Python-2.7

* Mon Jun 27 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.8.1-alt2
- Added necessary requirements
- Excluded *.pth

* Tue May 31 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.8.1-alt1
- Initial build for Sisyphus


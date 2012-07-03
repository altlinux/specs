%define oname z3c.sampledata
Name: python-module-%oname
Version: 0.4.0
Release: alt2.1
Summary: Sampledata Generator
License: ZPLv2.1
Group: Development/Python
Url: http://pypi.python.org/pypi/z3c.sampledata/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-distribute

%py_requires ZODB3 zope.authentication zope.component zope.i18nmessageid
%py_requires zope.interface zope.intid zope.lifecycleevent zope.schema
%py_requires zope.site zope.traversing zope.viewlet
%py_requires zope.app.pagetemplate zope.pluggableauth

%description
This package tries to do the best to support the development of sample
data generators. A sample data generator is a pluggable tool to create
data needed for tests.

%package tests
Summary: Tests for Sampledata Generator
Group: Development/Python
Requires: %name = %version-%release
%py_requires zope.app.testing zope.app.zcmlfiles

%description tests
This package tries to do the best to support the development of sample
data generators. A sample data generator is a pluggable tool to create
data needed for tests.

This package contains tests for Sampledata Generator.

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
%exclude %python_sitelibdir/*/*/*test*

%files tests
%python_sitelibdir/*/*/*test*

%changelog
* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.4.0-alt2.1
- Rebuild with Python-2.7

* Sun Jun 26 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4.0-alt2
- Added necessary requirements
- Excluded *.pth

* Thu Jun 02 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4.0-alt1
- Initial build for Sisyphus


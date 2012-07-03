%define oname z3c.formjs
Name: python-module-%oname
Version: 0.5.0
Release: alt2.1
Summary: Javascript integration into ``z3c.form``
License: ZPLv2.1
Group: Development/Python
Url: http://pypi.python.org/pypi/z3c.formjs/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-distribute

%py_requires jquery.layer z3c.form z3c.traverser zope.app.pagetemplate
%py_requires zope.component zope.interface zope.location zope.publisher
%py_requires zope.schema zope.traversing cjson

%description
This package is going to provide javascript support/enhancements to
the z3c.form library.

%package tests
Summary: Tests for Javascript integration into ``z3c.form``
Group: Development/Python
Requires: %name = %version-%release
%py_requires lxml z3c.coverage zope.container zope.contenttype zope.site
%py_requires zope.testing zope.app.testing

%description tests
This package is going to provide javascript support/enhancements to
the z3c.form library.

This package contains tests for Javascript integration into ``z3c.form``.

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
* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.5.0-alt2.1
- Rebuild with Python-2.7

* Fri Jun 24 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.5.0-alt2
- Added necessary requirements
- Excluded *.pth

* Wed Jun 01 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.5.0-alt1
- Initial build for Sisyphus


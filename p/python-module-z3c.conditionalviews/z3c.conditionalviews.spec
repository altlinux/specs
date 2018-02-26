%define oname z3c.conditionalviews
Name: python-module-%oname
Version: 1.0
Release: alt2.1
Summary: Intergrates with the zope publisher to validate conditional requests
License: ZPLv2.1
Group: Development/Python
Url: http://pypi.python.org/pypi/z3c.conditionalviews/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-distribute

%py_requires zope.component zope.schema

%description
z3c.conditionalviews is a mechanism to validate a HTTP request based on
some conditional protocol like entity tags, or last modification date.
It is also extensible so that protocols like WebDAV can define there own
conditional protocol like the IF header.

%package tests
Summary: Tests for z3c.conditionalviews
Group: Development/Python
Requires: %name = %version-%release
%py_requires zope.app.testing zope.app.zcmlfiles zope.securitypolicy

%description tests
z3c.conditionalviews is a mechanism to validate a HTTP request based on
some conditional protocol like entity tags, or last modification date.
It is also extensible so that protocols like WebDAV can define there own
conditional protocol like the IF header.

This package contains tests for z3c.conditionalviews.

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

* Thu Jun 23 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0-alt2
- Added necessary requirements
- Excluded *.pth

* Fri May 20 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0-alt1
- Initial build for Sisyphus


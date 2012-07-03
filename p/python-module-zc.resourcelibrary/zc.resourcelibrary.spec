%define oname zc.resourcelibrary
Name: python-module-%oname
Version: 1.3.2
Release: alt2.1
Summary: Post-rendering Resource Inclusion
License: ZPLv2.1
Group: Development/Python
Url: http://pypi.python.org/pypi/zc.resourcelibrary/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-distribute

%py_requires zc zope.app.pagetemplate zope.app.publication
%py_requires zope.browserresource zope.component zope.configuration
%py_requires zope.interface zope.publisher zope.security zope.tales
%py_requires zope.traversing

%description
The resource library is a Zope 3 extension that is designed to make the
inclusion of JavaScript, CSS, and other resources easy, cache-friendly,
and component-friendly.

%package tests
Summary: Tests for Post-rendering Resource Inclusion
Group: Development/Python
Requires: %name = %version-%release
%py_requires zope.app.authentication zope.app.securitypolicy
%py_requires zope.app.testing zope.app.zcmlfiles zope.pagetemplate
%py_requires zope.securitypolicy zope.testbrowser zope.testing

%description tests
The resource library is a Zope 3 extension that is designed to make the
inclusion of JavaScript, CSS, and other resources easy, cache-friendly,
and component-friendly.

This package contains tests for Post-rendering Resource Inclusion.

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
%exclude %python_sitelibdir/*/*/tests

%files tests
%python_sitelibdir/*/*/tests

%changelog
* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.3.2-alt2.1
- Rebuild with Python-2.7

* Mon Jun 27 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.3.2-alt2
- Added necessary requirements
- Excluded *.pth

* Fri Jun 03 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.3.2-alt1
- Initial build for Sisyphus


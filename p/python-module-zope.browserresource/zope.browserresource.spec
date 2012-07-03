%define oname zope.browserresource
Name: python-module-%oname
Version: 3.12.0
Release: alt3.1
Summary: Browser resources implementation for Zope
License: ZPL
Group: Development/Python
Url: http://pypi.python.org/pypi/zope.browserresource/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-distribute

%py_requires zope zope.component zope.configuration zope.contenttype
%py_requires zope.i18n zope.interface zope.location zope.publisher
%py_requires zope.schema zope.traversing

%description
This package is at present not reusable without depending on a large
chunk of the Zope Toolkit and its assumptions. It is maintained by the
Zope Toolkit project.

%package tests
Summary: Tests for zope.browserresource
Group: Development/Python
Requires: %name = %version-%release
%py_requires zope.testing

%description tests
This package is at present not reusable without depending on a large
chunk of the Zope Toolkit and its assumptions. It is maintained by the
Zope Toolkit project.

This package contains tests for zope.browserresource.

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
* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 3.12.0-alt3.1
- Rebuild with Python-2.7

* Tue Jun 28 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.12.0-alt3
- Added necessary requirements
- Excluded *.pth

* Thu May 19 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.12.0-alt2
- Set as archdep package

* Tue May 17 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.12.0-alt1
- Initial build for Sisyphus


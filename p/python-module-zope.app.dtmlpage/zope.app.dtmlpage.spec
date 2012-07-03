%define oname zope.app.dtmlpage
Name: python-module-%oname
Version: 3.5.0
Release: alt2.1
Summary: DTML Page -- A Zope 3 Content Component
License: ZPLv2.1
Group: Development/Python
Url: http://pypi.python.org/pypi/zope.app.dtmlpage/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-distribute

%py_requires ZODB3 zope.annotation zope.app.publication zope.app.preview
%py_requires zope.app.testing zope.container zope.documenttemplate
%py_requires zope.filerepresentation zope.interface zope.schema
%py_requires zope.security zope.traversing

%description
This package provides a Zope 3 content component that contains DTML
code, which is executed when the component is accessed via its URL.

%package tests
Summary: Tests for zope.app.dtmlpage
Group: Development/Python
Requires: %name = %version-%release
%py_requires zope.app.testing zope.app.preference
%py_requires zope.app.securitypolicy zope.app.zcmlfiles

%description tests
This package provides a Zope 3 content component that contains DTML
code, which is executed when the component is accessed via its URL.

This package contains tests for zope.app.dtmlpage.

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
%exclude %python_sitelibdir/*/*/*/test*

%files tests
%python_sitelibdir/*/*/*/test*

%changelog
* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 3.5.0-alt2.1
- Rebuild with Python-2.7

* Mon Jun 27 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.5.0-alt2
- Added necessary requirements
- Excluded *.pth

* Mon May 23 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.5.0-alt1
- Initial build for Sisyphus


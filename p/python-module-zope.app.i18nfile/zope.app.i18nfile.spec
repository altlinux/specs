%define oname zope.app.i18nfile
Name: python-module-%oname
Version: 3.4.1
Release: alt2.1
Summary: I18n File and Image -- Zope 3 Content Components
License: ZPLv2.1
Group: Development/Python
Url: http://pypi.python.org/pypi/zope.app.i18nfile/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-distribute

%py_requires ZODB3 zope.app.file zope.i18n zope.interface zope.size

%description
This package provides an extension to the File and Image content
components for Zope 3, allowing the content to be localized.

%package tests
Summary: Tests for zope.app.i18nfile
Group: Development/Python
Requires: %name = %version-%release
%py_requires zope.app.testing zope.app.securitypolicy zope.app.zcmlfiles

%description tests
This package provides an extension to the File and Image content
components for Zope 3, allowing the content to be localized.

This package contains tests for zope.app.i18nfile.

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
%exclude %python_sitelibdir/*/*/*/*/test*

%files tests
%python_sitelibdir/*/*/*/test*
%python_sitelibdir/*/*/*/*/test*

%changelog
* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 3.4.1-alt2.1
- Rebuild with Python-2.7

* Mon Jun 27 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.4.1-alt2
- Added necessary requirements
- Excluded *.pth

* Sun May 22 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.4.1-alt1
- Initial build for Sisyphus


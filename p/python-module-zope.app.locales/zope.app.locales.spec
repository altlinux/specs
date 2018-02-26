%define oname zope.app.locales
Name: python-module-%oname
Version: 3.7.2
Release: alt1
Summary: Zope locale extraction and management utilities
License: ZPLv2.1
Group: Development/Python
Url: http://pypi.python.org/pypi/zope.app.locales/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-distribute

%py_requires zope.app zope.i18nmessageid zope.interface

%description
This package provides some facilities for extracting and managing i18n
messages that occur in Zope software. More specifically, i18n messages
can occur in Python code, in Page Templates and in ZCML declarations.
zope.app.locales provides a utility that can extract messages from all
three and write them to a standard gettext template (pot file).

%package tests
Summary: Tests for zope.app.locales
Group: Development/Python
Requires: %name = %version-%release
%py_requires zope.i18n zope.tal zope.testing

%description tests
This package provides some facilities for extracting and managing i18n
messages that occur in Zope software. More specifically, i18n messages
can occur in Python code, in Page Templates and in ZCML declarations.
zope.app.locales provides a utility that can extract messages from all
three and write them to a standard gettext template (pot file).

This package contains tests for zope.app.locales.

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
%_bindir/*
%python_sitelibdir/*
%exclude %python_sitelibdir/*.pth
%exclude %python_sitelibdir/*/*/*/tests.*

%files tests
%python_sitelibdir/*/*/*/tests.*

%changelog
* Wed Dec 28 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.7.2-alt1
- Version 3.7.2

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 3.7.0-alt2.1
- Rebuild with Python-2.7

* Mon Jun 27 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.7.0-alt2
- Added necessary requirements
- Excluded *.pth

* Sun May 22 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.7.0-alt1
- Initial build for Sisyphus


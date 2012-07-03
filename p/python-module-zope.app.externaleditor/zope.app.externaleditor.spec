%define oname zope.app.externaleditor
Name: python-module-%oname
Version: 3.5.0
Release: alt2.1
Summary: Editing Zope 3 Content with an External Editor
License: ZPLv2.1
Group: Development/Python
Url: http://pypi.python.org/pypi/zope.app.externaleditor/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-distribute

%py_requires zope.app.component zope.app.content zope.app.file
%py_requires zope.app.interface zope.app.testing zope.filerepresentation
%py_requires zope.interface zope.publisher zope.security zope.traversing

%description
This package allows Zope 3 content components to be edited via an editor
of your choice.

%package tests
Summary: Tests for zope.app.externaleditor
Group: Development/Python
Requires: %name = %version-%release
%py_requires zope.app.testing zope.container

%description tests
This package allows Zope 3 content components to be edited via an editor
of your choice.

This package contains tests for zope.app.externaleditor.

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
%exclude %python_sitelibdir/*/*/*/tests

%files tests
%python_sitelibdir/*/*/*/tests

%changelog
* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 3.5.0-alt2.1
- Rebuild with Python-2.7

* Mon Jun 27 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.5.0-alt2
- Added necessary requirements
- Excluded *.pth

* Mon May 23 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.5.0-alt1
- Initial build for Sisyphus


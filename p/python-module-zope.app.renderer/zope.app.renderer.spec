%define oname zope.app.renderer
Name: python-module-%oname
Version: 3.5.1
Release: alt2.1
Summary: Text Renderer Framework
License: ZPLv2.1
Group: Development/Python
Url: http://pypi.python.org/pypi/zope.app.renderer/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-distribute

%py_requires zope.app docutils roman zope.component zope.configuration
%py_requires zope.i18nmessageid zope.interface zope.publisher
%py_requires zope.schema zope.structuredtext

%description
This package provides a framework to convert a string from one format,
such as Structured or Restructured Text, to another, such as HTML.
Converters are looked up by adapter and uses other packages to implement
the converters.

%package tests
Summary: Tests for Text Renderer Framework
Group: Development/Python
Requires: %name = %version-%release
%py_requires zope.app.testing

%description tests
This package provides a framework to convert a string from one format,
such as Structured or Restructured Text, to another, such as HTML.
Converters are looked up by adapter and uses other packages to implement
the converters.

This package contains tests for Text Renderer Framework.

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
* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 3.5.1-alt2.1
- Rebuild with Python-2.7

* Tue Jun 28 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.5.1-alt2
- Added necessary requirements
- Excluded *.pth

* Sat May 21 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.5.1-alt1
- Initial build for Sisyphus


%define oname grokcore.component
Name: python-module-%oname
Version: 2.4
Release: alt2.1
Summary: Grok-like configuration for basic components (adapters, utilities, subscribers)
License: ZPL
Group: Development/Python
Url: http://pypi.python.org/pypi/grokcore.component/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-distribute

%py_requires martian zope.component zope.configuration zope.interface
%py_requires zope.testing

%description
This package provides base classes of basic component types for the Zope
Component Architecture, as well as means for configuring and registering
them directly in Python (without ZCML).

%package tests
Summary: Tests for grokcore.component
Group: Development/Python
Requires: %name = %version-%release

%description tests
This package provides base classes of basic component types for the Zope
Component Architecture, as well as means for configuring and registering
them directly in Python (without ZCML).

This package contains tests for grokcore.component.

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
* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 2.4-alt2.1
- Rebuild with Python-2.7

* Wed Jun 22 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.4-alt2
- Added necessary requirements
- Excludes *.pth

* Tue May 24 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.4-alt1
- Initial build for Sisyphus


%define oname z3c.builder.core
Name: python-module-%oname
Version: 0.1.0
Release: alt4.1
Summary: A utility to help jump start Zope 3 projects
License: ZPLv2.1
Group: Development/Python
Url: http://pypi.python.org/pypi/z3c.builder.core/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar
AutoReq: yes, nopython

BuildPreReq: python-devel python-module-distribute

%py_requires rwproperty zc.buildout zope.component
%py_requires zope.configuration zope.container zope.interface
%py_requires zope.schema lxml

%description
z3c.builder is a tool that helps you jump start development of a Zope 3
application by generating all the boiler plate code and configuration
for you.

%package tests
Summary: Tests for z3c.builder.core
Group: Development/Python
Requires: %name = %version-%release
%py_requires zope.testing z3c.coverage

%description tests
z3c.builder is a tool that helps you jump start development of a Zope 3
application by generating all the boiler plate code and configuration
for you.

This package contains tests for z3c.builder.core

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
* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.1.0-alt4.1
- Rebuild with Python-2.7

* Mon Jul 04 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.0-alt4
- Fixed build

* Wed Jun 29 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.0-alt3
- Removed setuptools from requirements

* Thu Jun 23 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.0-alt2
- Added necessary requirements
- Excluded *.pth

* Fri May 20 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.0-alt1
- Initial build for Sisyphus


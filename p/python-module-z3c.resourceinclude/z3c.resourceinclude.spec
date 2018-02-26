%define oname z3c.resourceinclude
Name: python-module-%oname
Version: 0.3.1
Release: alt2.1
Summary: Machinery to include web resources based on request layer
License: ZPL
Group: Development/Python
Url: http://pypi.python.org/pypi/z3c.resourceinclude/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-distribute

%py_requires zope.app.publisher zope.app.cache zope.contentprovider
%py_requires plone.memoize chameleon.zpt

%description
The package is able to include the following types of resources:

* Cascading stylesheets (.css)
* Kinetic stylesheets (.kss)
* Javascript (.js)

%package tests
Summary: Tests for z3c.resourceinclude
Group: Development/Python
Requires: %name = %version-%release

%description tests
The package is able to include the following types of resources:

* Cascading stylesheets (.css)
* Kinetic stylesheets (.kss)
* Javascript (.js)

This package contains tests for z3c.resourceinclude.

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
* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.3.1-alt2.1
- Rebuild with Python-2.7

* Fri Jun 24 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3.1-alt2
- Added necessary requirements
- Excluded *.pth

* Tue Jun 07 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3.1-alt1
- Initial build for Sisyphus


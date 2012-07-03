%define oname z3c.recipe.winservice
Name: python-module-%oname
Version: 0.7.0
Release: alt3.1
Summary: Zope3 windows service installer
License: ZPLv2.1
Group: Development/Python
Url: http://pypi.python.org/pypi/z3c.recipe.winservice/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-distribute

%py_requires z3c.recipe ZConfig zc.buildout zc.recipe.egg

%description
This recipe offers windows service installation support.

The 'service' recipe installes the required scripts and files which can
be used to install a windows service.

Using the ``runscript`` option it is able to make any executable a
service.

%package tests
Summary: Tests for Zope3 windows service installer
Group: Development/Python
Requires: %name = %version-%release
%py_requires zope.testing zc.recipe.egg ZConfig

%description tests
This recipe offers windows service installation support.

The 'service' recipe installes the required scripts and files which can
be used to install a windows service.

Using the ``runscript`` option it is able to make any executable a
service.

This package contains tests for Zope3 windows service installer.

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
%exclude %python_sitelibdir/*/*/*/tests.*

%files tests
%python_sitelibdir/*/*/*/tests.*

%changelog
* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.7.0-alt3.1
- Rebuild with Python-2.7

* Fri Jun 24 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.7.0-alt3
- Added necessary requirements
- Excluded *.pth

* Sat Jun 04 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.7.0-alt2
- Fixed requirements

* Sat May 28 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.7.0-alt1
- Initial build for Sisyphus


%define version 1.5.2
#define subver b20
%define release alt4
%define oname zc.buildout
%setup_python_module %oname

Summary: The Buildout project provides support for creating Python applications.
Name: python-module-%oname
Version: %version
%ifdef subver
Release: %release.%subver.1
Source0: zc.buildout-%version%subver.tar
%else
Release: %release.1
Source0: zc.buildout-%version.tar
%endif
License: ZPL
Group: Development/Python
Packager: Python Development Team <python@packages.altlinux.org>

BuildRequires: %py_dependencies setuptools

%description
The Buildout project provides support for creating applications,
especially Python applications.  It provides tools for assembling
applications from multiple parts, Python or otherwise.  An application
may actually contain multiple programs, processes, and configuration
settings.

%package tests
Summary: Tests for Buildout
Group: Development/Python
Requires: %name = %version-%release
%py_requires zope.testing

%description tests
The Buildout project provides support for creating applications,
especially Python applications.  It provides tools for assembling
applications from multiple parts, Python or otherwise.  An application
may actually contain multiple programs, processes, and configuration
settings.

This package contains tests for Buildout

%prep
%ifdef subver
%setup
%else
%setup
%endif

%build
%python_build

%install
%python_module_declare %python_sitelibdir/zc
%python_build_install --optimize=2 --record=INSTALLED_FILES

%ifarch x86_64
install -d %buildroot%python_sitelibdir
mv %buildroot%python_sitelibdir_noarch/* \
	%buildroot%python_sitelibdir/
%endif

%files
%doc *.txt doc/*
%_bindir/*
%python_sitelibdir/*
%exclude %python_sitelibdir/*.pth
%exclude %python_sitelibdir/zc/*/test*

%files tests
%python_sitelibdir/*/*/test*

%changelog
* Mon Oct 24 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.5.2-alt4.1
- Rebuild with Python-2.7

* Thu Jun 23 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.5.2-alt4
- Added necessary requirements
- Excluded *.pth

* Fri May 20 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.5.2-alt2
- Set as archdep package

* Tue May 17 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.5.2-alt1
- Version 1.5.2

* Mon Nov 23 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.0-alt2.b20
- Rebuilt with python 2.6

* Fri Jan 25 2008 Grigory Batalov <bga@altlinux.ru> 1.0.0-alt1.b20.1
- Rebuilt with python-2.5.

* Wed Feb 21 2007 Ivan Fedorov <ns@altlinux.ru> 1.0.0-alt1.b20
- Initial build for ALT Linux.

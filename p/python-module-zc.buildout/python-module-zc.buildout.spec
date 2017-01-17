%define _unpackaged_files_terminate_build 1
# REMOVE ME (I was set for NMU) and uncomment real Release tags:
Release: alt1
%define oname zc.buildout

%def_with python3

Summary: The Buildout project provides support for creating Python applications.
Name: python-module-%oname
URL: https://pypi.python.org/pypi/zc.buildout/
Version: 2.5.3
#define subver b20
%ifdef subver
#Release: alt0.%subver
Source0: https://pypi.python.org/packages/e4/7b/63863f09bec5f5d7b9474209a6d4d3fc1e0bca02ecfb4c17f0cdd7b554b6/%{oname}-%{version}.tar.gz
%else
#Release: alt1.2
Source0: zc.buildout-%version.tar
%endif
License: ZPL
Group: Development/Python

%setup_python_module %oname

# Automatically added by buildreq on Fri Jan 29 2016 (-bi)
# optimized out: python-base python-devel python-modules python-modules-compiler python-modules-ctypes python-modules-email python-modules-encodings python-modules-unittest python3 python3-base
BuildRequires: python-module-setuptools python3-module-setuptools rpm-build-python3

#BuildRequires: %py_dependencies setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
#BuildPreReq: python3-devel python3-module-setuptools
%endif

%py_requires zc.zlibstorage zc.recipe.egg

%description
The Buildout project provides support for creating applications,
especially Python applications.  It provides tools for assembling
applications from multiple parts, Python or otherwise.  An application
may actually contain multiple programs, processes, and configuration
settings.

%package -n python3-module-%oname
Summary: The Buildout project provides support for creating Python applications
Group: Development/Python3
%py3_requires zc.zlibstorage zc.recipe.egg

%description -n python3-module-%oname
The Buildout project provides support for creating applications,
especially Python applications.  It provides tools for assembling
applications from multiple parts, Python or otherwise.  An application
may actually contain multiple programs, processes, and configuration
settings.

%package -n python3-module-%oname-tests
Summary: Tests for Buildout
Group: Development/Python3
Requires: python3-module-%oname = %version-%release
%py3_requires zope.testing

%description -n python3-module-%oname-tests
The Buildout project provides support for creating applications,
especially Python applications.  It provides tools for assembling
applications from multiple parts, Python or otherwise.  An application
may actually contain multiple programs, processes, and configuration
settings.

This package contains tests for Buildout

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
%setup -q -n %{oname}-%{version}

%if_with python3
cp -fR . ../python3
%endif

%build
%python_build

%if_with python3
pushd ../python3
%python3_build
popd
%endif

%install
%if_with python3
pushd ../python3
%python3_install
popd
%if "%python3_sitelibdir_noarch" != "%python3_sitelibdir"
install -d %buildroot%python3_sitelibdir
mv %buildroot%python3_sitelibdir_noarch/* \
	%buildroot%python3_sitelibdir/
%endif
pushd %buildroot%_bindir
for i in $(ls); do
	mv $i $i.py3
done
popd
%endif

%python_module_declare %python_sitelibdir/zc
%python_build_install --optimize=2 --record=INSTALLED_FILES
%if "%python_sitelibdir_noarch" != "%python_sitelibdir"
install -d %buildroot%python_sitelibdir
mv %buildroot%python_sitelibdir_noarch/* \
	%buildroot%python_sitelibdir/
%endif

%files
%doc *.txt doc/* CHANGES.rst PKG-INFO README.rst
%_bindir/*
%if_with python3
%exclude %_bindir/*.py3
%endif
%python_sitelibdir/*
%exclude %python_sitelibdir/*.pth
%exclude %python_sitelibdir/zc/*/test*

%files tests
%python_sitelibdir/*/*/test*

%if_with python3
%files -n python3-module-%oname
%doc *.txt doc/* CHANGES.rst PKG-INFO README.rst
%_bindir/*.py3
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*.pth
%exclude %python3_sitelibdir/zc/*/test*
%exclude %python3_sitelibdir/zc/*/*/test*

%files -n python3-module-%oname-tests
%python3_sitelibdir/zc/*/test*
%python3_sitelibdir/zc/*/*/test*
%endif

%changelog
* Tue Jan 17 2017 Igor Vlasenko <viy@altlinux.ru> 2.5.3-alt1
- automated PyPI update

* Mon Jun 06 2016 Ivan Zakharyaschev <imz@altlinux.org> 2.3.1-alt1.2.1
- (AUTO) subst_x86_64.

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 2.3.1-alt1.2
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Fri Jan 29 2016 Mikhail Efremov <sem@altlinux.org> 2.3.1-alt1.1
- NMU: Use buildreq for BR.

* Mon Dec 22 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.3.1-alt1
- Version 2.3.1

* Mon Dec 15 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.3.0-alt1
- Version 2.3.0

* Thu Nov 06 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.2.5-alt1
- Version 2.2.5

* Tue Nov 04 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.2.4-alt1
- Version 2.2.4

* Wed Jul 23 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.2.1-alt3
- Added necessary requirements

* Fri Jul 18 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.2.1-alt2
- Added module for Python 3

* Tue Sep 24 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.2.1-alt1
- Version 2.2.1

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

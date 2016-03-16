%define oname z3c.recipe.winservice

%def_with python3

Name: python-module-%oname
Version: 0.7.0
Release: alt4.1
Summary: Zope3 windows service installer
License: ZPLv2.1
Group: Development/Python
Url: http://pypi.python.org/pypi/z3c.recipe.winservice/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
BuildPreReq: python-tools-2to3
%endif

%py_requires z3c.recipe ZConfig zc.buildout zc.recipe.egg

%description
This recipe offers windows service installation support.

The 'service' recipe installes the required scripts and files which can
be used to install a windows service.

Using the ``runscript`` option it is able to make any executable a
service.

%package -n python3-module-%oname
Summary: Zope3 windows service installer
Group: Development/Python3
%py3_requires z3c.recipe ZConfig zc.buildout zc.recipe.egg

%description -n python3-module-%oname
This recipe offers windows service installation support.

The 'service' recipe installes the required scripts and files which can
be used to install a windows service.

Using the ``runscript`` option it is able to make any executable a
service.

%package -n python3-module-%oname-tests
Summary: Tests for Zope3 windows service installer
Group: Development/Python3
Requires: python3-module-%oname = %version-%release
%py3_requires zope.testing zc.recipe.egg ZConfig

%description -n python3-module-%oname-tests
This recipe offers windows service installation support.

The 'service' recipe installes the required scripts and files which can
be used to install a windows service.

Using the ``runscript`` option it is able to make any executable a
service.

This package contains tests for Zope3 windows service installer.

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

%if_with python3
cp -fR . ../python3
%endif

%build
%python_build

%if_with python3
pushd ../python3
find -type f -name '*.py' -exec 2to3 -w -n '{}' +
%python3_build
popd
%endif

%install
%python_install
%ifarch x86_64
install -d %buildroot%python_sitelibdir
mv %buildroot%python_sitelibdir_noarch/* \
	%buildroot%python_sitelibdir/
%endif

%if_with python3
pushd ../python3
%python3_install
popd
%ifarch x86_64
install -d %buildroot%python3_sitelibdir
mv %buildroot%python3_sitelibdir_noarch/* \
	%buildroot%python3_sitelibdir/
%endif
%endif

%files
%doc *.txt
%python_sitelibdir/*
%exclude %python_sitelibdir/*.pth
%exclude %python_sitelibdir/*/*/*/tests.*

%files tests
%python_sitelibdir/*/*/*/tests.*

%if_with python3
%files -n python3-module-%oname
%doc *.txt
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*.pth
%exclude %python3_sitelibdir/*/*/*/tests.*
%exclude %python3_sitelibdir/*/*/*/*/tests.*

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/*/*/tests.*
%python3_sitelibdir/*/*/*/*/tests.*
%endif

%changelog
* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.7.0-alt4.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Wed Jul 23 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.7.0-alt4
- Added module for Python 3

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.7.0-alt3.1
- Rebuild with Python-2.7

* Fri Jun 24 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.7.0-alt3
- Added necessary requirements
- Excluded *.pth

* Sat Jun 04 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.7.0-alt2
- Fixed requirements

* Sat May 28 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.7.0-alt1
- Initial build for Sisyphus


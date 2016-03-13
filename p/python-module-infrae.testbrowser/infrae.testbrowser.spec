%define oname infrae.testbrowser

%def_with python3

Name: python-module-%oname
Version: 2.0.2
Release: alt2.1
Summary: Sane functionnal test browser for WSGI applications
License: BSD
Group: Development/Python
Url: http://pypi.python.org/pypi/infrae.testbrowser/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
BuildPreReq: python-tools-2to3
%endif

%py_requires infrae lxml zope.interface

%description
infrae.testbrowser is test browser for WSGI applications sharing the
same ideas than zope.testbrowser. It only has lxml and zope.interface as
dependency.

%package -n python3-module-%oname
Summary: Sane functionnal test browser for WSGI applications
Group: Development/Python3
%py3_requires infrae lxml zope.interface

%description -n python3-module-%oname
infrae.testbrowser is test browser for WSGI applications sharing the
same ideas than zope.testbrowser. It only has lxml and zope.interface as
dependency.

%package -n python3-module-%oname-tests
Summary: Tests for infrae.testbrowser
Group: Development/Python3
Requires: python3-module-%oname = %version-%release

%description -n python3-module-%oname-tests
infrae.testbrowser is test browser for WSGI applications sharing the
same ideas than zope.testbrowser. It only has lxml and zope.interface as
dependency.

This package contains tests for infrae.testbrowser.

%package tests
Summary: Tests for infrae.testbrowser
Group: Development/Python
Requires: %name = %version-%release

%description tests
infrae.testbrowser is test browser for WSGI applications sharing the
same ideas than zope.testbrowser. It only has lxml and zope.interface as
dependency.

This package contains tests for infrae.testbrowser.

%package -n python-module-infrae
Summary: Core package for infrae
Group: Development/Python
%py_provides infrae

%description -n python-module-infrae
Core package for infrae.

%package -n python3-module-infrae
Summary: Core package for infrae
Group: Development/Python3
%py3_provides infrae

%description -n python3-module-infrae
Core package for infrae.

%prep
%setup

%if_with python3
cp -fR . ../python3
find ../python3 -type f -name '*.py' -exec 2to3 -w -n '{}' +
%endif

%build
%python_build

%if_with python3
pushd ../python3
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
install -p -m644 src/infrae/__init__.py \
	%buildroot%python_sitelibdir/infrae

%if_with python3
pushd ../python3
%python3_install
popd
%ifarch x86_64
install -d %buildroot%python3_sitelibdir
mv %buildroot%python3_sitelibdir_noarch/* \
	%buildroot%python3_sitelibdir/
%endif
install -p -m644 src/infrae/__init__.py \
	%buildroot%python3_sitelibdir/infrae
%endif

%files
%doc *.txt docs/*
%python_sitelibdir/*
%exclude %python_sitelibdir/*.pth
%exclude %python_sitelibdir/*/*/tests
%exclude %python_sitelibdir/infrae/__init__.*

%files tests
%python_sitelibdir/*/*/tests

%files -n python-module-infrae
%python_sitelibdir/infrae/__init__.*

%if_with python3
%files -n python3-module-%oname
%doc *.txt docs/*
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*.pth
%exclude %python3_sitelibdir/*/*/tests
%exclude %python3_sitelibdir/infrae/__init__.*
%exclude %python3_sitelibdir/infrae/__pycache__/__init__.*

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/*/tests

%files -n python3-module-infrae
%python3_sitelibdir/infrae/__init__.*
%python3_sitelibdir/infrae/__pycache__/__init__.*
%endif

%changelog
* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 2.0.2-alt2.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Sun Jul 27 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0.2-alt2
- Added module for Python 3

* Tue Sep 17 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0.2-alt1
- Version 2.0.2

* Fri Feb 15 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0.1-alt1
- Version 2.0.1

* Fri Dec 09 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0-alt1.b1
- Version 2.0b1

* Mon Oct 24 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.1-alt1.1
- Rebuild with Python-2.7

* Wed Jun 29 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1-alt1
- Initial build for Sisyphus


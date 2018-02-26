%define oname infrae.testbrowser
Name: python-module-%oname
Version: 2.0
Release: alt1.b1
Summary: Sane functionnal test browser for WSGI applications
License: BSD
Group: Development/Python
Url: http://pypi.python.org/pypi/infrae.testbrowser/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-distribute

%py_requires infrae lxml zope.interface

%description
infrae.testbrowser is test browser for WSGI applications sharing the
same ideas than zope.testbrowser. It only has lxml and zope.interface as
dependency.

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

install -p -m644 src/infrae/__init__.py \
	%buildroot%python_sitelibdir/infrae

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

%changelog
* Fri Dec 09 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0-alt1.b1
- Version 2.0b1

* Mon Oct 24 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.1-alt1.1
- Rebuild with Python-2.7

* Wed Jun 29 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1-alt1
- Initial build for Sisyphus


%define oname infrae.testbrowser

Name: python3-module-%oname
Version: 2.0.2
Release: alt3

Summary: Sane functionnal test browser for WSGI applications
License: BSD
Group: Development/Python3
Url: http://pypi.python.org/pypi/infrae.testbrowser/

Source: %name-%version.tar
Patch0: fix-incompatibility.patch

BuildRequires(pre): rpm-build-python3
BuildRequires: python-tools-2to3

%py3_requires infrae lxml zope.interface


%description
infrae.testbrowser is test browser for WSGI applications sharing the
same ideas than zope.testbrowser. It only has lxml and zope.interface as
dependency.

%package tests
Summary: Tests for infrae.testbrowser
Group: Development/Python3
Requires: %name = %version-%release

%description tests
infrae.testbrowser is test browser for WSGI applications sharing the
same ideas than zope.testbrowser. It only has lxml and zope.interface as
dependency.

This package contains tests for infrae.testbrowser.

%package -n python3-module-infrae
Summary: Core package for infrae
Group: Development/Python3
%py3_provides infrae

%description -n python3-module-infrae
Core package for infrae.

%prep
%setup
%patch0 -p2

find ./ -type f -name '*.py' -exec 2to3 -w -n '{}' +

%build
%python3_build

%install
%python3_install

%if "%python3_sitelibdir_noarch" != "%python3_sitelibdir"
install -d %buildroot%python3_sitelibdir
mv %buildroot%python3_sitelibdir_noarch/* \
    %buildroot%python3_sitelibdir/
%endif

install -p -m644 src/infrae/__init__.py \
    %buildroot%python3_sitelibdir/infrae

%files
%doc *.txt docs/*
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*.pth
%exclude %python3_sitelibdir/*/*/tests
%exclude %python3_sitelibdir/infrae/__init__.*
%exclude %python3_sitelibdir/infrae/__pycache__/__init__.*

%files tests
%python3_sitelibdir/*/*/tests

%files -n python3-module-infrae
%python3_sitelibdir/infrae/__init__.*
%python3_sitelibdir/infrae/__pycache__/__init__.*


%changelog
* Mon Feb 03 2020 Andrey Bychkov <mrdrew@altlinux.org> 2.0.2-alt3
- Build for python2 disabled.

* Tue Apr 30 2019 Grigory Ustinov <grenka@altlinux.org> 2.0.2-alt2.2
- Rebuild with python3.7.

* Mon Jun 06 2016 Ivan Zakharyaschev <imz@altlinux.org> 2.0.2-alt2.1.1
- (AUTO) subst_x86_64.

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


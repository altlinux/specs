%define oname z3c.discriminator

Name: python3-module-%oname
Version: 0.2
Release: alt4

Summary: Provides a formalism for marking adapter specifications as discriminators
License: ZPL
Group: Development/Python3
Url: http://pypi.python.org/pypi/z3c.discriminator/

Source: %name-%version.tar
Patch0: fix-import.patch

BuildRequires(pre): rpm-build-python3
%py3_requires zope.configuration zope.interface


%description
z3c.discriminator provides a formalism for marking adapter
specifications as discriminators in the sense that they will be used
only for adapter lookup, not instantiation.

%package tests
Summary: Tests for z3c.discriminator
Group: Development/Python3
Requires: python3-module-%oname = %version-%release
%py3_requires zope.component.testing zope.testing

%description tests
z3c.discriminator provides a formalism for marking adapter
specifications as discriminators in the sense that they will be used
only for adapter lookup, not instantiation.

This package contains tests for z3c.discriminator.

%prep
%setup
%patch -p2

%build
%python3_build

%install
%python3_install

%if "%python3_sitelibdir_noarch" != "%python3_sitelibdir"
install -d %buildroot%python3_sitelibdir
mv %buildroot%python3_sitelibdir_noarch/* \
    %buildroot%python3_sitelibdir/
%endif

%files
%doc *.txt docs/*
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*.pth
%exclude %python3_sitelibdir/*/*/tests.*
%exclude %python3_sitelibdir/*/*/*/tests.*

%files tests
%python3_sitelibdir/*/*/tests.*
%python3_sitelibdir/*/*/*/tests.*


%changelog
* Fri Dec 20 2019 Andrey Bychkov <mrdrew@altlinux.org> 0.2-alt4
- build for python2 disabled

* Tue Apr 30 2019 Grigory Ustinov <grenka@altlinux.org> 0.2-alt3.2
- Rebuild with python3.7.

* Mon Jun 06 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.2-alt3.1.1
- (AUTO) subst_x86_64.

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.2-alt3.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Sun Jul 27 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2-alt3
- Added module for Python 3

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.2-alt2.1
- Rebuild with Python-2.7

* Thu Jun 23 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2-alt2
- Excluded *.pth

* Fri Jun 03 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2-alt1
- Initial build for Sisyphus


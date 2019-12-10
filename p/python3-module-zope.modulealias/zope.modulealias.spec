%define oname zope.modulealias

Name: python3-module-%oname
Version: 3.4.0
Release: alt4

Summary: Zope modulealias
License: ZPLv2.1
Group: Development/Python3
Url: http://pypi.python.org/pypi/zope.modulealias/

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
%py3_requires zope zope.interface zope.configuration


%description
This package enables the developer to make one module available under a
different path.

%package tests
Summary: Tests for zope.modulealias
Group: Development/Python3
Requires: %name = %version-%release
%py3_requires zope.testing

%description tests
This package enables the developer to make one module available under a
different path.

This package contains tests for zope.modulealias.

%prep
%setup

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
%doc *.txt
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*.pth
%exclude %python3_sitelibdir/*/*/tests

%files tests
%python3_sitelibdir/*/*/tests


%changelog
* Tue Dec 10 2019 Andrey Bychkov <mrdrew@altlinux.org> 3.4.0-alt4
- python3 disabled

* Tue Apr 30 2019 Grigory Ustinov <grenka@altlinux.org> 3.4.0-alt3.2
- Rebuild with python3.7.

* Mon Jun 06 2016 Ivan Zakharyaschev <imz@altlinux.org> 3.4.0-alt3.1.1
- (AUTO) subst_x86_64.

* Mon Mar 14 2016 Ivan Zakharyaschev <imz@altlinux.org> 3.4.0-alt3.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Sun Jul 27 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.4.0-alt3
- Added module for Python 3

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 3.4.0-alt2.1
- Rebuild with Python-2.7

* Wed Jun 29 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.4.0-alt2
- Added necessary requirements
- Excluded *.pth

* Tue May 24 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.4.0-alt1
- Initial build for Sisyphus


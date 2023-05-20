%define pypi_name zope.processlifetime

%def_with check

Name: python3-module-%pypi_name
Version: 3.0
Release: alt1

Summary: Zope process lifetime events
License: ZPL-2.1
Group: Development/Python3
Url: https://pypi.org/project/zope.processlifetime/
Vcs: https://github.com/zopefoundation/zope.processlifetime

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel
%if_with check
BuildRequires: python3-module-zope.testrunner
%endif

Requires: python3-module-zope.interface

%description
This package provides interfaces / implementations for events relative
to the lifetime of a server process (startup, database opening, etc.)

%package tests
Summary: Tests for zope.processlifetime
Group: Development/Python3
Requires: %name = %EVR

%description tests
This package provides interfaces / implementations for events relative
to the lifetime of a server process (startup, database opening, etc.)

This package contains tests for zope.processlifetime.

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%if "%python3_sitelibdir_noarch" != "%python3_sitelibdir"
install -d %buildroot%python3_sitelibdir
mv %buildroot%python3_sitelibdir_noarch/* \
    %buildroot%python3_sitelibdir/
%endif

%check
%pyproject_run -- zope-testrunner --test-path=src -vc

%files
%doc *.txt *.rst
%python3_sitelibdir/zope/processlifetime/
%python3_sitelibdir/%pypi_name-%version.dist-info
%exclude %python3_sitelibdir/*.pth
%exclude %python3_sitelibdir/*/*/tests.*
%exclude %python3_sitelibdir/*/*/*/tests.*

%files tests
%python3_sitelibdir/*/*/tests.*
%python3_sitelibdir/*/*/*/tests.*


%changelog
* Sat May 20 2023 Anton Vyatkin <toni@altlinux.org> 3.0-alt1
- New version 3.0.

* Fri Nov 29 2019 Andrey Bychkov <mrdrew@altlinux.org> 2.1.0-alt2
- python2 disabled

* Tue Apr 30 2019 Grigory Ustinov <grenka@altlinux.org> 2.1.0-alt1.2
- Rebuild with python3.7.

* Mon Jun 06 2016 Ivan Zakharyaschev <imz@altlinux.org> 2.1.0-alt1.1.1
- (AUTO) subst_x86_64.

* Mon Mar 14 2016 Ivan Zakharyaschev <imz@altlinux.org> 2.1.0-alt1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Mon Dec 29 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.1.0-alt1
- Version 2.1.0

* Fri Jul 18 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0.0-alt2
- Added module for Python 3

* Wed Apr 10 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0.0-alt1
- Version 2.0.0

* Mon Oct 24 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.0-alt2.1
- Rebuild with Python-2.7

* Sun Jun 19 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0-alt2
- Add necessary requirements
- Excluded *.pth

* Fri May 20 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0-alt1
- Initial build for Sisyphus


%define pypi_name zope.event

%def_with check

Name: python3-module-%pypi_name
Version: 5.0
Release: alt1

Summary: Very basic event publishing system
License: ZPL-2.1
Group: Development/Python3
Url: https://pypi.org/project/zope.event/
Vcs: https://github.com/zopefoundation/zope.event

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel
%if_with check
BuildRequires: python3-module-zope.testrunner
%endif

%py3_requires zope

%description
The zope.event package provides a simple event system. It provides:

* An event publishing system
* A very simple event-dispatching system on which more sophisticated
  event dispatching systems can be built. For example, a type-based
  event dispatching system that builds on zope.event can be found in
  zope.component.

%package tests
Summary: Tests for zope.event
Group: Development/Python3
Requires: %name = %EVR

%description tests
The zope.event package provides a simple event system. It provides:

* An event publishing system
* A very simple event-dispatching system on which more sophisticated
  event dispatching systems can be built. For example, a type-based
  event dispatching system that builds on zope.event can be found in
  zope.component.

This package contains tests for zope.event.

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
%doc *.txt docs/*.rst
%python3_sitelibdir/zope/event
%python3_sitelibdir/%pypi_name-%version.dist-info
%exclude %python3_sitelibdir/*.pth
%exclude %python3_sitelibdir/*/*/tests*

%files tests
%python3_sitelibdir/*/*/tests*

%changelog
* Sat Jun 24 2023 Anton Vyatkin <toni@altlinux.org> 5.0-alt1
- New version 5.0.

* Fri May 19 2023 Anton Vyatkin <toni@altlinux.org> 4.6-alt1
- New version 4.6.

* Thu Aug 05 2021 Grigory Ustinov <grenka@altlinux.org> 4.4-alt2
- Drop python2 support.

* Wed Feb 27 2019 Andrey Bychkov <mrdrew@altlinux.org> 4.4-alt1
- Version updated to 4.4
- Cleanup spec

* Mon Jun 06 2016 Ivan Zakharyaschev <imz@altlinux.org> 4.0.3-alt1.1.1.1
- (AUTO) subst_x86_64.

* Mon Mar 14 2016 Ivan Zakharyaschev <imz@altlinux.org> 4.0.3-alt1.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Fri Jan 29 2016 Mikhail Efremov <sem@altlinux.org> 4.0.3-alt1.1
- NMU: Use buildreq for BR.

* Sat Jul 26 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.3-alt1
- Version 4.0.3

* Sun Mar 03 2013 Aleksey Avdeev <solo@altlinux.ru> 4.0.2-alt1
- Version 4.0.2

* Thu Apr 12 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.5.2-alt1
- Version 3.5.2
- Added module for Python 3

* Wed Dec 28 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.5.1-alt1
- Version 3.5.1

* Mon Oct 24 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 3.5.0.1-alt4.1
- Rebuild with Python-2.7

* Tue Jun 28 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.5.0.1-alt4
- Added necessary requirement

* Sun Jun 19 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.5.0.1-alt3
- Excluded *.pth

* Thu May 19 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.5.0.1-alt2
- Set as archdep package

* Mon May 16 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.5.0.1-alt1
- Initial build for Sisyphus


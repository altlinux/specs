%define _unpackaged_files_terminate_build 1
%define oname zope.exceptions

%def_with check

Name: python3-module-%oname
Version: 4.4
Release: alt1

Summary: Zope Exceptions
License: ZPLv2.1
Group: Development/Python3
# Source-git: https://github.com/zopefoundation/zope.exceptions.git
Url: http://pypi.python.org/pypi/zope.exceptions

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-zope.interface

%if_with check
BuildRequires: python3-module-zope.testrunner
%endif

%py3_requires zope zope.interface


%description
This package contains exception interfaces and implementations which are
so general purpose that they don't belong in Zope application-specific
packages.

%package tests
Summary: Tests for %oname
Group: Development/Python3
Requires: %name = %EVR

%description tests
This package contains exception interfaces and implementations which are
so general purpose that they don't belong in Zope application-specific
packages.

This package contains tests for %oname.

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

%check
%__python3 setup.py test -v

%files
%doc *.txt
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*.pth
%exclude %python3_sitelibdir/*/*/tests

%files tests
%python3_sitelibdir/*/*/tests


%changelog
* Thu Apr 15 2021 Grigory Ustinov <grenka@altlinux.org> 4.4-alt1
- Automatically updated to 4.4.

* Wed Feb 12 2020 Andrey Bychkov <mrdrew@altlinux.org> 4.2.0-alt5
- Build for python2 disabled.

* Sun Jun 23 2019 Igor Vlasenko <viy@altlinux.ru> 4.2.0-alt4
- NMU: remove rpm-build-ubt from BR:

* Sat Jun 15 2019 Igor Vlasenko <viy@altlinux.ru> 4.2.0-alt3
- NMU: remove %ubt from release

* Wed Feb 14 2018 Stanislav Levin <slev@altlinux.org> 4.2.0-alt2.S1
- Fix a wrong logic of packaging for non x86_64 arch

* Mon Feb 12 2018 Stanislav Levin <slev@altlinux.org> 4.2.0-alt1.S1
- v4.0.8 -> v4.2.0

* Mon Jun 06 2016 Ivan Zakharyaschev <imz@altlinux.org> 4.0.8-alt1.1.1.1
- (AUTO) subst_x86_64.

* Mon Mar 14 2016 Ivan Zakharyaschev <imz@altlinux.org> 4.0.8-alt1.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Fri Jan 29 2016 Mikhail Efremov <sem@altlinux.org> 4.0.8-alt1.1
- NMU: Use buildreq for BR.

* Wed Aug 26 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.8-alt1
- Version 4.0.8

* Sat Jul 26 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.7-alt1
- Version 4.0.7

* Tue Apr 09 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.6-alt1
- Version 4.0.6

* Fri Mar 22 2013 Aleksey Avdeev <solo@altlinux.ru> 3.7.1-alt1.1
- Rebuild with Python-3.3

* Thu Apr 12 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.7.1-alt1
- Version 3.7.1
- Added module for Python 3

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 3.6.1-alt2.1
- Rebuild with Python-2.7

* Tue Jun 28 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.6.1-alt2
- Added necessary requirements
- Excluded *.pth

* Fri May 20 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.6.1-alt1
- Initial build for Sisyphus


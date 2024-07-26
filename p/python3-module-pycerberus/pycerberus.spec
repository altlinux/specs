%define oname pycerberus

# check needs pythonic_testcase, which nobody use except this project
# nobody packs it and seems it abandoned
%def_without check

Name: python3-module-%oname
Version: 0.7
Release: alt1
Summary: Highly flexible, no magic input validation library
License: MIT
Group: Development/Python3
URL: https://pypi.org/project/pycerberus
VCS: https://github.com/FelixSchwarz/pycerberus

Source: %name-%version.tar
BuildArch: noarch

BuildRequires(pre): rpm-build-python3

BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel

%if_with check
BuildRequires: python3-module-pytest
%endif

# see comment above
%add_python3_req_skip pythonic_testcase

%description
pycerberus is a framework to check user data thoroughly so that you can
protect your application from malicious (or just garbled) input data.

%package tests
Summary: Tests for pycerberus
Group: Development/Python3
Requires: %name = %version-%release

%description tests
pycerberus is a framework to check user data thoroughly so that you can
protect your application from malicious (or just garbled) input data.

This package contains tests for pycerberus.

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest

%files
%doc *.txt docs
%python3_sitelibdir/%oname
%python3_sitelibdir/%oname-%version.0.dist-info
%exclude %python3_sitelibdir/*/test*
%exclude %python3_sitelibdir/*/__pycache__/test*

%files tests
%python3_sitelibdir/*/test*
%python3_sitelibdir/*/__pycache__/test*

%changelog
* Fri Jul 26 2024 Grigory Ustinov <grenka@altlinux.org> 0.7-alt1
- Build new version.

* Tue Jul 27 2021 Grigory Ustinov <grenka@altlinux.org> 0.6-alt2
- Drop python2 support.

* Wed May 16 2018 Andrey Bychkov <mrdrew@altlinux.org> 0.6-alt1.1.2
- (NMU) rebuild with python3.6

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.6-alt1.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.6-alt1.1
- NMU: Use buildreq for BR.

* Tue Nov 25 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6-alt1
- Version 0.6

* Wed Sep 18 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.5-alt1
- Version 0.5

* Fri Mar 22 2013 Aleksey Avdeev <solo@altlinux.ru> 0.4.2-alt2.1
- Rebuild with Python-3.3

* Tue May 08 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4.2-alt2
- Added module for Python 3

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.4.2-alt1.1
- Rebuild with Python-2.7

* Mon Jul 04 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4.2-alt1
- Initial build for Sisyphus


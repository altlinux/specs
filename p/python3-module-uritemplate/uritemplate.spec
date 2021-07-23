%define oname uritemplate

Name: python3-module-%oname
Version: 3.0.1
Release: alt2

Summary: Python implementation of RFC6570, URI Template
License: Apache-2.0 or BSD-3-Clause
Group: Development/Python3

Url: https://pypi.python.org/pypi/uritemplate

Source: %name-%version.tar
BuildArch: noarch

BuildRequires(pre): rpm-build-python3

%py3_provides %oname

%description
This is a Python implementation of RFC6570, URI Template, and can expand
templates up to and including Level 4 in that specification.

%prep
%setup

%build
%python3_build

%install
%python3_install

%files
%doc README.rst
%python3_sitelibdir/*

%changelog
* Fri Jul 23 2021 Grigory Ustinov <grenka@altlinux.org> 3.0.1-alt2
- Drop python2 support.

* Wed Jan 01 2020 Grigory Ustinov <grenka@altlinux.org> 3.0.1-alt1
- Build new version.

* Mon May 20 2019 Grigory Ustinov <grenka@altlinux.org> 3.0.0-alt1
- Build new version.

* Tue Apr 30 2019 Grigory Ustinov <grenka@altlinux.org> 0.6-alt3.2
- Rebuild with python3.7.

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.6-alt3.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.6-alt3.1
- NMU: Use buildreq for BR.

* Tue Oct 28 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6-alt3
- Added provides %oname

* Tue Aug 19 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6-alt2
- Added module for Python 3

* Thu Sep 19 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6-alt1
- Version 0.6

* Wed Apr 03 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.5.2-alt1
- Initial build for Sisyphus


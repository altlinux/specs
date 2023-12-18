%define _unpackaged_files_terminate_build 1
%define oname pylbfgs

%def_with check

Name: python3-module-%oname
Version: 0.2.0.15
Release: alt1

Summary: LBFGS and OWL-QN optimization algorithms

License: MIT
Group: Development/Python3
Url: https://pypi.python.org/pypi/PyLBFGS

Source0: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-Cython
BuildRequires: libnumpy-py3-devel
%if_with check
BuildRequires: python3-module-pytest
BuildRequires: python3-module-pytest-cov
BuildRequires: python3-module-numpy-testing
%endif

%py3_provides %oname lbfgs
%py3_requires numpy

%description
This is a Python wrapper around Naoaki Okazaki (chokkan)'s liblbfgs
library of quasi-Newton optimization routines (limited memory BFGS and
OWL-QN).

This package aims to provide a cleaner interface to the LBFGS algorithm
than is currently available in SciPy, and to provide the OWL-QN
algorithm to Python users.

%prep
%setup

%build
%python3_build

%install
%python3_install

cp liblbfgs/README README.libLBFGS

%check
export PYTHONPATH=%buildroot%python3_sitelibdir
py.test-3 -v

%files
%doc *.rst README.libLBFGS
%python3_sitelibdir/*

%changelog
* Mon Dec 18 2023 Grigory Ustinov <grenka@altlinux.org> 0.2.0.15-alt1
- Automatically updated to 0.2.0.15.

* Thu May 26 2022 Grigory Ustinov <grenka@altlinux.org> 0.2.0.14-alt1
- Build new version.
- Build with check.

* Mon Feb 08 2021 Grigory Ustinov <grenka@altlinux.org> 0.2.0.13-alt1
- Build new version for python3.9.
- Drop python2 support.

* Mon Mar 16 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 0.2.0.12-alt2
- Fixed build with numpy.

* Thu Apr 04 2019 Grigory Ustinov <grenka@altlinux.org> 0.2.0.12-alt1
- Build new version with python3.7.

* Thu Mar 22 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 0.2.0.3-alt1.1.1
- (NMU) Rebuilt with python-3.6.4.

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.2.0.3-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Wed Jan 11 2017 Igor Vlasenko <viy@altlinux.ru> 0.2.0.3-alt1
- automated PyPI update

* Thu Mar 17 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.2.0.2-alt1.1.1
- (NMU) rebuild with python3-3.5 & rpm-build-python3-0.1.10
  (for ABI dependence and new python3(*) reqs)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.2.0.2-alt1.1
- NMU: Use buildreq for BR.

* Wed Aug 26 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2.0.2-alt1
- Initial build for Sisyphus


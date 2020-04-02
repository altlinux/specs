%define mname scikits
%define oname %mname.statsmodels

%def_disable check

Name: python3-module-%oname
Epoch: 1
Version: 0.8.0
Release: alt3

Summary: Statistical computations and models for use with SciPy
License: BSD
Group: Development/Python3
Url: https://pypi.python.org/pypi/statsmodels/

# https://github.com/statsmodels/statsmodels.git
Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: libnumpy-py3-devel python3-devel
BuildRequires: python3-module-Cython
# BuildRequires: python3-module-Cython python3-module-ipyparallel python3-module-numexpr-tests python3-module-numpy-testing

%py3_provides %oname
%py3_requires numpy scipy pandas patsy matplotlib cvxopt
%py3_requires statsmodels.stats.multitest
%add_python3_req_skip models

%description
Statsmodels is a Python package that provides a complement to scipy for
statistical computations including descriptive statistics and estimation
and inference for statistical models.

%package tests
Summary: Tests for %oname
Group: Development/Python3
Requires: python3-module-%oname = %EVR
%add_python3_req_skip rpy

%description tests
Statsmodels is a Python package that provides a complement to scipy for
statistical computations including descriptive statistics and estimation
and inference for statistical models.

This package contains tests for %oname.

%prep
%setup

%build
%add_optflags -fno-strict-aliasing
%python3_build_debug

%install
%python3_install

%check
xvfb-run python3 setup.py test

%files
%doc *.md *.rst README_l1.txt
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/*/*/*/example*
%exclude %python3_sitelibdir/*/*/*/*/test*
%exclude %python3_sitelibdir/*/*/*/test*

%files tests
%python3_sitelibdir/*/*/*/*/example*
%python3_sitelibdir/*/*/*/*/test*
%python3_sitelibdir/*/*/*/test*

%changelog
* Thu Apr 02 2020 Andrey Bychkov <mrdrew@altlinux.org> 1:0.8.0-alt3
- Build for python2 disabled.

* Wed Feb 05 2020 Vitaly Lipatov <lav@altlinux.ru> 1:0.8.0-alt2
- NMU: disable build python2 module

* Wed Mar 28 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 1:0.8.0-alt1.1
- (NMU) Rebuilt with python-3.6.4.

* Wed Mar 28 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 1:0.8.0-alt1
- Updated to upstream version 0.8.0.
- Disabled docs generation.

* Wed Mar 30 2016 Ivan Zakharyaschev <imz@altlinux.org> 1:0.7.0-alt4.git20150731.1
- (NMU) rebuild with python3-3.5 & rpm-build-python3-0.1.10
  (for ABI dependence and new python3(*) reqs)

* Wed Mar 30 2016 Ivan Zakharyaschev <imz@altlinux.org> 1:0.7.0-alt4.git20150731
- rm inessential BR: python3-module-pandas{,-tests} (incorrectly detected by buildreq).

* Fri Mar 25 2016 Ivan Zakharyaschev <imz@altlinux.org> 1:0.7.0-alt3.git20150731
- BRs fixed with buildreq again (cleared off self-dependence and other
  unneeded pkgs with python-module-setuptools-18.1-alt3,
  python-2.7.11-alt2, and python-module-Cython-0.23.4-alt3).

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 1:0.7.0-alt2.git20150731.1
- NMU: Use buildreq for BR.

* Sat Aug 22 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1:0.7.0-alt2.git20150731
- New snapshot

* Tue Apr 28 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1:0.7.0-alt2.git20150323
- New snapshot

* Sun Mar 01 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1:0.7.0-alt2.git20150216
- Added requires statsmodels.stats.multitest

* Sun Mar 01 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1:0.7.0-alt1.git20150216
- Initial build for Sisyphus


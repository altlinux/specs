%define oname scikit-learn

# CPU time limit exceeded
# 1.5.2 passes check on local machine
%def_without check

Name: python3-module-%oname
Version: 1.5.2
Release: alt1

Summary: A set of python modules for machine learning and data mining

License: BSD-3-Clause
Group: Development/Python3
URL: https://pypi.org/project/scikit-learn
VCS: https://github.com/scikit-learn/scikit-learn

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: gcc-c++
BuildRequires: liblapack-devel
%ifnarch %e2k
BuildRequires: libgomp-devel
%endif
BuildRequires: libnumpy-py3-devel
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel
BuildRequires: python3-module-numpy
BuildRequires: python3-module-scipy
BuildRequires: python3-module-Cython
BuildRequires: python3-module-mesonpy
BuildRequires: meson

%if_with check
BuildRequires: python3-module-pytest
BuildRequires: python3-module-joblib
BuildRequires: python3-module-numpy-testing
BuildRequires: python3-module-threadpoolctl
BuildRequires: python3-module-contourpy
%endif

%py3_provides sklearn

%description
scikit-learn is a Python module for machine learning built on top of
SciPy and distributed under the 3-Clause BSD license.

%package tests
Summary: Tests for %oname
Group: Development/Python3
Requires: %name = %EVR

%description tests
scikit-learn is a Python module for machine learning built on top of
SciPy and distributed under the 3-Clause BSD license.

This package contains tests for %oname.

%prep
%setup

%build
export BLAS=openblas
%pyproject_build

%install
%pyproject_install

%check
pushd %buildroot%python3_sitelibdir
py.test3 -vv
rm -rv .pytest_cache
popd

%files
%doc COPYING *.md *.rst
%python3_sitelibdir/sklearn
%python3_sitelibdir/scikit_learn-%version.dist-info
%python3_sitelibdir/sklearn/tests
%python3_sitelibdir/sklearn/*/tests
%python3_sitelibdir/sklearn/*/*/tests
%python3_sitelibdir/sklearn/utils/_testing.py
%python3_sitelibdir/sklearn/utils/__pycache__/_testing.*

%changelog
* Sat Oct 05 2024 Grigory Ustinov <grenka@altlinux.org> 1.5.2-alt1
- Automatically updated to 1.5.2.

* Mon Feb 12 2024 Michael Shigorin <mike@altlinux.org> 1.4.0-alt2
- E2K: disable openmp on e2k

* Sat Feb 10 2024 Grigory Ustinov <grenka@altlinux.org> 1.4.0-alt1
- Automatically updated to 1.4.0.

* Wed Jan 10 2024 Grigory Ustinov <grenka@altlinux.org> 1.3.0-alt3
- Build without check.

* Thu Dec 21 2023 Grigory Ustinov <grenka@altlinux.org> 1.3.0-alt2
- Add Cython to build dependencies.

* Fri Oct 27 2023 Grigory Ustinov <grenka@altlinux.org> 1.3.0-alt1
- Automatically updated to 1.3.0 (Closes: #46326).

* Thu Apr 27 2023 Anton Vyatkin <toni@altlinux.org> 0.23.2-alt2
- Fix BuildRequries

* Mon Aug 10 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 0.23.2-alt1
- Updated to upstream version 0.23.2.

* Fri Apr 03 2020 Andrey Bychkov <mrdrew@altlinux.org> 0.19.1-alt3
- Build for python2 disabled.

* Thu Mar 29 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 0.19.1-alt2.1
- (NMU) Rebuilt with python-3.6.4.

* Thu Mar 22 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 0.19.1-alt2
- Fixed build with new cython.

* Tue Dec 05 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 0.19.1-alt1
- Updated to upstream version 0.19.1.

* Mon Aug 07 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 0.17-alt1.dev0.git20150820.2
- Updated build dependencies.

* Thu Mar 17 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.17-alt1.dev0.git20150820.1.1
- (NMU) rebuild with python3-3.5 & rpm-build-python3-0.1.10
  (for ABI dependence and new python3(*) reqs)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.17-alt1.dev0.git20150820.1
- NMU: Use buildreq for BR.

* Sun Aug 23 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.17-alt1.dev0.git20150820
- New snapshot

* Sun Apr 26 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.17-alt1.dev0.git20150424
- New snapshot

* Sun Mar 22 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.17-alt1.dev0.git20150321
- Version 0.17.dev0

* Fri Jan 16 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.16-alt1.git20150115
- New snapshot

* Sat Nov 15 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.16-alt1.git20141113
- Initial build for Sisyphus

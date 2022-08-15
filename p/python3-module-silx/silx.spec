%define _unpackaged_files_terminate_build 1
%define pypi_name silx

%def_with check

Name: python3-module-%pypi_name
Version: 1.0.0
Release: alt1
Summary: Software library for X-Ray data analysis
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/silx/

# https://github.com/silx-kit/silx.git
Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: gcc-c++ libgomp-devel
BuildRequires: python3-devel

# build backend and its deps
BuildRequires: python3(setuptools)
BuildRequires: python3(wheel)
BuildRequires: python3(Cython)
BuildRequires: libnumpy-py3-devel

%if_with check
# runtime dependencies
BuildRequires: python3(h5py)
BuildRequires: python3(fabio)
BuildRequires: python3(numpy)
# unbundled
BuildRequires: python3(scipy.spatial)

BuildRequires: python3(PyQt5)
BuildRequires: python3(OpenGL)
BuildRequires: python3(numpy.testing)
%endif

%add_python3_req_skip pyopencl pyopencl.array pyopencl.elementwise pyopencl.scan pyopencl.tools
%add_python3_req_skip PySide.QtCore PySide.QtGui
%py3_requires scipy.spatial
%py3_requires PyQt5 OpenGL
%py3_requires matplotlib.backends.backend_qt5agg

%description
The silx project aims at providing a collection of Python packages
to support the development of data assessment,
reduction and analysis applications at synchrotron radiation facilities.
It aims at providing reading/writing different file formats,
data reduction routines and a set of Qt widgets to browse and visualize data.

%package tests
Summary: Tests for %pypi_name
Group: Development/Python3
Requires: %name = %EVR

%description tests
The silx project aims at providing a collection of Python packages
to support the development of data assessment,
reduction and analysis applications at synchrotron radiation facilities.
It aims at providing reading/writing different file formats,
data reduction routines and a set of Qt widgets to browse and visualize data.

This package contains tests for %pypi_name.

%package examples
Summary: Examples for %pypi_name
Group: Development/Python3
Requires: %name = %EVR

%description examples
The silx project aims at providing a collection of Python packages
to support the development of data assessment,
reduction and analysis applications at synchrotron radiation facilities.
It aims at providing reading/writing different file formats,
data reduction routines and a set of Qt widgets to browse and visualize data.

This package contains examples for %pypi_name.

%prep
%setup

# remove some third-party bundled stuff
rm -r src/silx/third_party/_local

%build
%pyproject_build

%install
%pyproject_install

%check
cat > tox.ini <<'EOF'
[testenv]
commands =
    python run_tests.py --installed -vra
EOF
%tox_check_pyproject

%files
%doc CHANGELOG.rst README.rst
%_bindir/*
%python3_sitelibdir/silx/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/
%exclude %python3_sitelibdir/silx/test
%exclude %python3_sitelibdir/silx/*/test
%exclude %python3_sitelibdir/silx/*/*/test
%exclude %python3_sitelibdir/silx/*/*/*/test
%exclude %python3_sitelibdir/silx/*/testutils.*
%exclude %python3_sitelibdir/silx/*/*/testutils.*
%exclude %python3_sitelibdir/silx/*/*/*/testutils.*
%exclude %python3_sitelibdir/silx/*/test_.*
%exclude %python3_sitelibdir/silx/*/*/test_.*
%exclude %python3_sitelibdir/silx/examples
%exclude %python3_sitelibdir/silx/conftest.py
%exclude %python3_sitelibdir/silx/__pycache__/conftest.*
%exclude %python3_sitelibdir/silx/*/conftest.py
%exclude %python3_sitelibdir/silx/*/__pycache__/conftest.*
%exclude %python3_sitelibdir/silx/*/*/conftest.py
%exclude %python3_sitelibdir/silx/*/*/__pycache__/conftest.*

%files tests
%python3_sitelibdir/silx/test
%python3_sitelibdir/silx/*/test
%python3_sitelibdir/silx/*/*/test
%python3_sitelibdir/silx/*/*/*/test
%python3_sitelibdir/silx/*/testutils.*
%python3_sitelibdir/silx/*/*/testutils.*
%python3_sitelibdir/silx/*/*/*/testutils.*
%python3_sitelibdir/silx/*/test_.*
%python3_sitelibdir/silx/*/*/test_.*
%python3_sitelibdir/silx/conftest.py
%python3_sitelibdir/silx/__pycache__/conftest.*
%python3_sitelibdir/silx/*/conftest.py
%python3_sitelibdir/silx/*/__pycache__/conftest.*
%python3_sitelibdir/silx/*/*/conftest.py
%python3_sitelibdir/silx/*/*/__pycache__/conftest.*

%files examples
%python3_sitelibdir/silx/examples

%changelog
* Mon Aug 15 2022 Stanislav Levin <slev@altlinux.org> 1.0.0-alt1
- 0.14.0 -> 1.0.0.

* Mon Feb 01 2021 Aleksei Nikiforov <darktemplar@altlinux.org> 0.14.0-alt1
- Updated to upstream version 0.14.0.
- Re-enabled check.

* Tue Nov 10 2020 Vitaly Lipatov <lav@altlinux.ru> 0.10.1-alt2
- remove libnumpy-devel (it is python2 only package)
- disable check (need review)

* Mon Apr 08 2019 Aleksei Nikiforov <darktemplar@altlinux.org> 0.10.1-alt1
- Updated to latest upstream release.
- Disabled build for python-2.

* Thu Mar 22 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 0.6.1-alt1.1
- (NMU) Rebuilt with python-3.6.4.

* Thu Nov 30 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 0.6.1-alt1
- Initial build for ALT.

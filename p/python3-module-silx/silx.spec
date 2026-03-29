%define _unpackaged_files_terminate_build 1
%define pypi_name silx
%define mod_name silx

%def_without check

Name: python3-module-%pypi_name
Version: 2.2.2
Release: alt2.1
Summary: Software library for X-Ray data analysis
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/silx/
Vcs: https://github.com/silx-kit/silx
Source: %name-%version.tar
Patch0: %name-%version-alt.patch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-wheel
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-cython
BuildRequires: gcc-c++
BuildRequires: libgomp-devel
BuildRequires: python3-devel
BuildRequires: libnumpy-py3-devel

%if_with check
BuildRequires: python3-module-fabio
BuildRequires: python3-module-h5py
BuildRequires: python3-module-numpy
BuildRequires: python3-module-packaging
BuildRequires: python3-module-pooch
BuildRequires: python3-module-pytest
BuildRequires: python3-module-pytest-mock
BuildRequires: python3-module-pytest-xvfb
BuildRequires: python3-module-scipy
BuildRequires: python3-module-hdf5plugin
BuildRequires: python3-module-mako
BuildRequires: python3-module-matplotlib
BuildRequires: python3-module-pillow
BuildRequires: python3-module-pyopengl
BuildRequires: python3-module-pyqt5
BuildRequires: python3-module-python-dateutil
BuildRequires: python3-module-qtconsole
BuildRequires: python3-module-numpy-testing
BuildRequires: python3-module-matplotlib-qt5
%endif

%add_python3_req_skip pyopencl
%add_python3_req_skip pyopencl.array
%add_python3_req_skip pyopencl.elementwise
%add_python3_req_skip pyopencl.scan
%add_python3_req_skip pyopencl.tools

%description
The silx project aims at providing a collection of Python packages
to support the development of data assessment,
reduction and analysis applications at synchrotron radiation facilities.
It aims at providing reading/writing different file formats,
data reduction routines and a set of Qt widgets to browse and visualize data.

%package -n %name+full
Summary: %summary
Group: Development/Python3
Requires: %name
# ./src/silx/gui/utils/matplotlib.py matplotlib.backends.backend_qt5agg
Requires: python3-module-matplotlib-qt5

%description -n %name+full
Extra 'full' for %pypi_name.

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
%autopatch -p1
%python3_fix_shebang .

%build
%pyproject_build

%install
%pyproject_install

# manually install examples
cp -a examples %buildroot%python3_sitelibdir/silx/

%check
%pyproject_run -- python -c "import %mod_name.test, sys; sys.exit(%mod_name.test.run_tests(verbosity=1, args=['-ra', '-Wignore', '--low-mem']))"

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

%files -n %name+full
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
* Wed Mar 25 2026 Grigory Ustinov <grenka@altlinux.org> 2.2.2-alt2.1
- Demodernized packaging.

* Tue Sep 23 2025 Grigory Ustinov <grenka@altlinux.org> 2.2.2-alt2
- Build without flaky tests for python3.13.

* Wed Apr 09 2025 Stanislav Levin <slev@altlinux.org> 2.2.2-alt1
- 2.2.1 -> 2.2.2.

* Fri Feb 28 2025 Stanislav Levin <slev@altlinux.org> 2.2.1-alt1
- 2.2.0 -> 2.2.1.

* Mon Feb 17 2025 Stanislav Levin <slev@altlinux.org> 2.2.0-alt2
- Fixed FTBFS (rearranged matplotlib).

* Wed Jan 22 2025 Stanislav Levin <slev@altlinux.org> 2.2.0-alt1
- 2.1.2 -> 2.2.0.

* Thu Oct 24 2024 Stanislav Levin <slev@altlinux.org> 2.1.2-alt1
- 2.1.1 -> 2.1.2.

* Wed Sep 25 2024 Stanislav Levin <slev@altlinux.org> 2.1.1-alt1
- 2.1.0 -> 2.1.1.

* Thu May 30 2024 Stanislav Levin <slev@altlinux.org> 2.1.0-alt2
- Fixed FTBFS (Pytest 8.2.0).

* Mon Apr 22 2024 Stanislav Levin <slev@altlinux.org> 2.1.0-alt1
- 2.0.1 -> 2.1.0.

* Tue Mar 19 2024 Stanislav Levin <slev@altlinux.org> 2.0.1-alt1
- 1.1.2 -> 2.0.1.

* Tue Jul 18 2023 Stanislav Levin <slev@altlinux.org> 1.1.2-alt2
- Fixed FTBFS (numpy 1.25.0).

* Wed Jun 14 2023 Stanislav Levin <slev@altlinux.org> 1.1.2-alt1
- 1.0.0 -> 1.1.2.

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

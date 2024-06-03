%define _unpackaged_files_terminate_build 1
%define pypi_name silx

%def_with check

Name: python3-module-%pypi_name
Version: 2.1.0
Release: alt2
Summary: Software library for X-Ray data analysis
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/silx/
Vcs: https://github.com/silx-kit/silx
Source: %name-%version.tar
Source1: %pyproject_deps_config_name
Patch0: %name-%version-alt.patch
%pyproject_runtimedeps_metadata
# manually manage extra dependencies with metadata
AutoReq: yes, nopython3
BuildRequires(pre): rpm-build-pyproject
BuildRequires: gcc-c++
BuildRequires: libgomp-devel
BuildRequires: python3-devel
BuildRequires: libnumpy-py3-devel
%pyproject_builddeps_build
%if_with check
%add_pyproject_deps_check_filter 'hdf5plugin$'
%add_pyproject_deps_check_filter 'pyopencl$'
%add_pyproject_deps_check_filter 'bitshuffle$'
%pyproject_builddeps_metadata_extra test
%pyproject_builddeps_metadata_extra full
# unbundled scipy.spatial
BuildRequires: python3-module-scipy
# tests are subpackaged
BuildRequires: python3-module-numpy-testing
%endif

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
%add_pyproject_deps_runtime_filter 'hdf5plugin$'
%add_pyproject_deps_runtime_filter 'pyopencl$'
%add_pyproject_deps_runtime_filter 'bitshuffle$'
%pyproject_runtimedeps_metadata -- --extra full

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
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata

# Fix shebangs
grep -rlE '#!/usr/bin/(env )?python$' | xargs subst 's|^#!/usr/bin/\(env \)\?python$|#!/usr/bin/python3|'

%build
%pyproject_build

%install
%pyproject_install

# manually install examples
cp -a examples %buildroot%python3_sitelibdir/silx/

%check
%pyproject_run -- python run_tests.py --installed -ra -Wignore --low-mem

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

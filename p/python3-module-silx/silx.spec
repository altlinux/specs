%define _unpackaged_files_terminate_build 1
%define pypi_name silx
%define mod_name silx

%def_with check

Name: python3-module-%pypi_name
Version: 3.0.1
Release: alt1
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
# https://bugzilla.altlinux.org/59338
BuildRequires: /usr/bin/meson
# see mesonpy.get_requires_for_build_wheel
BuildRequires: ninja-build
BuildRequires: patchelf
%pyproject_builddeps_build
%if_with check
# not packaged
%add_pyproject_deps_check_filter 'bitshuffle$'
%pyproject_builddeps_metadata_extra test
%pyproject_builddeps_metadata_extra full-no-qt
%pyproject_builddeps_metadata_extra full
%pyproject_builddeps_metadata_extra h5pyd
# unbundled scipy.spatial
BuildRequires: python3-module-scipy
BuildRequires: python3-module-matplotlib-qt5
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
AutoReq: yes, nopython3
%add_pyproject_deps_runtime_filter 'bitshuffle$'
%pyproject_runtimedeps_metadata_extra full
# ./src/silx/gui/utils/matplotlib.py matplotlib.backends.backend_qt5agg
Requires: python3-module-matplotlib-qt5

%description -n %name+full
Extra 'full' for %pypi_name.

%prep
%setup
%autopatch -p1
%python3_fix_shebang .
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata

%build
%pyproject_build

%install
%pyproject_install

%check
# .github/workflows/ci.yml
export QT_API=PySide6
export SILX_OPENCL=False
%pyproject_run -- python -c "import silx.test, sys; sys.exit(silx.test.run_tests(verbosity=3, args=['-ra', '-Wignore', '--qt-binding=$QT_API']))"

%files
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

%changelog
* Tue May 26 2026 Stanislav Levin <slev@altlinux.org> 3.0.1-alt1
- 2.2.2 -> 3.0.1.

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

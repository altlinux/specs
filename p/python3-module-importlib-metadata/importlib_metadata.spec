%define _unpackaged_files_terminate_build 1
%define pypi_name importlib-metadata

%def_with check

Name: python3-module-%pypi_name
Version: 8.3.0
Release: alt1
Summary: Library to access the metadata for a Python package
License: Apache-2.0
Group: Development/Python3
Url: https://pypi.org/project/importlib-metadata/
VCS: https://github.com/python/importlib_metadata.git
BuildArch: noarch
Source: %name-%version.tar
Source1: %pyproject_deps_config_name
Patch: %name-%version-alt.patch
%pyproject_runtimedeps_metadata

# PyPI name(dash, underscore)
%py3_provides %pypi_name
Provides: python3-module-importlib_metadata = %EVR
Obsoletes: python3-module-importlib_metadata <= 1.5.0-alt1

BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build

%if_with check
# pytest-perf is not packaged and perf tests are skipped anyway
%add_pyproject_deps_check_filter pytest-perf
%pyproject_builddeps_metadata_extra test

# internal CPython's test package
BuildRequires: python3(test)
%endif

%description
Library to access the metadata for a Python package.

This package supplies third-party access to the functionality of
importlib.metadata including improvements added to subsequent Python versions.

New features are introduced in this third-party library and later merged into
CPython.

%prep
%setup
%patch -p1
%pyproject_scm_init
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest -vra --ignore exercises.py

%files
%doc README.rst
%python3_sitelibdir/importlib_metadata/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Tue Aug 20 2024 Stanislav Levin <slev@altlinux.org> 8.3.0-alt1
- 8.2.0 -> 8.3.0.

* Thu Jul 25 2024 Stanislav Levin <slev@altlinux.org> 8.2.0-alt1
- 8.1.0 -> 8.2.0.

* Wed Jul 24 2024 Stanislav Levin <slev@altlinux.org> 8.1.0-alt1
- 8.0.0 -> 8.1.0.

* Wed Jun 26 2024 Stanislav Levin <slev@altlinux.org> 8.0.0-alt1
- 7.2.1 -> 8.0.0.

* Mon Jun 24 2024 Stanislav Levin <slev@altlinux.org> 7.2.1-alt1
- 7.2.0 -> 7.2.1.

* Fri Jun 21 2024 Stanislav Levin <slev@altlinux.org> 7.2.0-alt1
- 7.1.0 -> 7.2.0.

* Thu Mar 21 2024 Stanislav Levin <slev@altlinux.org> 7.1.0-alt1
- 7.0.2 -> 7.1.0.

* Mon Mar 11 2024 Stanislav Levin <slev@altlinux.org> 7.0.2-alt1
- 7.0.1 -> 7.0.2.

* Mon Dec 25 2023 Stanislav Levin <slev@altlinux.org> 7.0.1-alt1
- 7.0.0 -> 7.0.1.

* Fri Dec 08 2023 Stanislav Levin <slev@altlinux.org> 7.0.0-alt1
- 6.8.0 -> 7.0.0.

* Wed Jul 19 2023 Stanislav Levin <slev@altlinux.org> 6.8.0-alt1
- 6.7.0 -> 6.8.0.

* Tue Jun 20 2023 Stanislav Levin <slev@altlinux.org> 6.7.0-alt1
- 6.6.0 -> 6.7.0.

* Tue Apr 25 2023 Stanislav Levin <slev@altlinux.org> 6.6.0-alt1
- 6.5.0 -> 6.6.0.

* Tue Apr 18 2023 Stanislav Levin <slev@altlinux.org> 6.5.0-alt1
- 6.0.0 -> 6.5.0.

* Fri Jan 27 2023 Stanislav Levin <slev@altlinux.org> 6.0.0-alt1
- 5.1.0 -> 6.0.0.

* Fri Nov 25 2022 Stanislav Levin <slev@altlinux.org> 5.1.0-alt1
- 5.0.0 -> 5.1.0.

* Fri Oct 07 2022 Stanislav Levin <slev@altlinux.org> 5.0.0-alt1
- 4.12.0 -> 5.0.0.

* Wed Aug 10 2022 Stanislav Levin <slev@altlinux.org> 4.12.0-alt1
- 4.11.3 -> 4.12.0.

* Mon Mar 21 2022 Stanislav Levin <slev@altlinux.org> 4.11.3-alt1
- 4.11.2 -> 4.11.3.

* Fri Mar 04 2022 Stanislav Levin <slev@altlinux.org> 4.11.2-alt1
- 4.11.1 -> 4.11.2.

* Tue Feb 22 2022 Stanislav Levin <slev@altlinux.org> 4.11.1-alt1
- 4.10.1 -> 4.11.1.

* Wed Jan 19 2022 Stanislav Levin <slev@altlinux.org> 4.10.1-alt1
- 4.8.1 -> 4.10.1.

* Tue Nov 23 2021 Stanislav Levin <slev@altlinux.org> 4.8.1-alt2
- Obsoleted importlib_metadata (closes: #41400).

* Wed Sep 29 2021 Stanislav Levin <slev@altlinux.org> 4.8.1-alt1
- 4.6.1 -> 4.8.1.

* Tue Jul 20 2021 Stanislav Levin <slev@altlinux.org> 4.6.1-alt1
- 1.5.0 -> 4.6.1 (restored for features from Python 3.10).

* Wed Feb 12 2020 Stanislav Levin <slev@altlinux.org> 1.5.0-alt1
- 1.3.0 -> 1.5.0.
- Moved Python3 subpackage to its own package.

* Mon Dec 16 2019 Stanislav Levin <slev@altlinux.org> 1.3.0-alt1
- 0.23 -> 1.3.0.

* Fri Sep 27 2019 Stanislav Levin <slev@altlinux.org> 0.23-alt1
- 0.19 -> 0.23.

* Tue Aug 13 2019 Stanislav Levin <slev@altlinux.org> 0.19-alt1
- 0.17 -> 0.19.

* Wed Jun 05 2019 Stanislav Levin <slev@altlinux.org> 0.17-alt1
- 0.11 -> 0.17.

* Tue May 14 2019 Stanislav Levin <slev@altlinux.org> 0.11-alt1
- 0.9 -> 0.11.

* Mon Apr 22 2019 Stanislav Levin <slev@altlinux.org> 0.9-alt1
- 0.8 -> 0.9.
- Fixed testing.

* Fri Jan 25 2019 Stanislav Levin <slev@altlinux.org> 0.8-alt1
- Initial build.

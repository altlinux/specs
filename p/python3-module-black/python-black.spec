%define _unpackaged_files_terminate_build 1
%define pypi_name black

%def_with check

Name: python3-module-%pypi_name
Version: 24.8.0
Release: alt1
Summary: The Uncompromising Code Formatter
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/black/
VCS: https://github.com/psf/black
BuildArch: noarch
Source: %name-%version.tar
Source1: %pyproject_deps_config_name
Patch: %name-%version-alt.patch

%pyproject_runtimedeps_metadata

%add_python3_self_prov_path %buildroot%python3_sitelibdir/blib2to3/pgen2

BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build

%if_with check
%set_pyproject_deps_check_filter tox pytest-cov pre-commit coverage
%pyproject_builddeps_metadata_extra d
%pyproject_builddeps_check

# aiohttp.test_utils is shipped by tests subpackage
BuildRequires: python3-module-aiohttp-tests
%endif

%description
Black is the uncompromising Python code formatter. By using it, you agree to
cede control over minutiae of hand-formatting. In return, Black gives you
speed, determinism, and freedom from pycodestyle nagging about formatting. You
will save time and mental energy for more important matters.

Blackened code looks the same regardless of the project you're reading.
Formatting becomes transparent after a while and you can focus on the content
instead.

Black makes code review faster by producing the smallest diffs possible.

%prep
%setup
%autopatch -p1

%pyproject_scm_init
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata
%if_with check
%pyproject_deps_resync_check_pipreqfile test_requirements.txt
%endif

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest -vra tests -Wignore

%files
%doc README.md
%_bindir/black
%_bindir/blackd
%python3_sitelibdir/__pycache__/_black_version.cpython*
%python3_sitelibdir/_black_version.py
%python3_sitelibdir/black/
%python3_sitelibdir/blackd/
%python3_sitelibdir/blib2to3/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Thu Sep 12 2024 Stanislav Levin <slev@altlinux.org> 24.8.0-alt1
- 24.4.2 -> 24.8.0.

* Fri Apr 26 2024 Stanislav Levin <slev@altlinux.org> 24.4.2-alt1
- 24.4.1 -> 24.4.2.

* Thu Apr 25 2024 Stanislav Levin <slev@altlinux.org> 24.4.1-alt1
- 24.4.0 -> 24.4.1.

* Mon Apr 15 2024 Stanislav Levin <slev@altlinux.org> 24.4.0-alt1
- 24.3.0 -> 24.4.0.

* Mon Mar 18 2024 Stanislav Levin <slev@altlinux.org> 24.3.0-alt1
- 24.2.0 -> 24.3.0.

* Tue Feb 20 2024 Stanislav Levin <slev@altlinux.org> 24.2.0-alt2
- Fixed FTBFS (hatchling 1.21.0).

* Thu Feb 15 2024 Stanislav Levin <slev@altlinux.org> 24.2.0-alt1
- 24.1.1 -> 24.2.0.

* Tue Jan 30 2024 Stanislav Levin <slev@altlinux.org> 24.1.1-alt1
- 23.12.1 -> 24.1.1.

* Mon Dec 25 2023 Stanislav Levin <slev@altlinux.org> 23.12.1-alt1
- 23.12.0 -> 23.12.1.

* Fri Dec 15 2023 Stanislav Levin <slev@altlinux.org> 23.12.0-alt1
- 23.11.0 -> 23.12.0.

* Thu Nov 09 2023 Stanislav Levin <slev@altlinux.org> 23.11.0-alt1
- 23.10.1 -> 23.11.0.

* Fri Oct 27 2023 Stanislav Levin <slev@altlinux.org> 23.10.1-alt1
- 23.9.1 -> 23.10.1.

* Wed Sep 27 2023 Stanislav Levin <slev@altlinux.org> 23.9.1-alt1
- 23.7.0 -> 23.9.1.

* Wed Jul 19 2023 Stanislav Levin <slev@altlinux.org> 23.7.0-alt1
- 23.3.0 -> 23.7.0.

* Thu Apr 27 2023 Stanislav Levin <slev@altlinux.org> 23.3.0-alt2
- Fixed FTBFS (setuptools 67.5.0).

* Wed Apr 19 2023 Stanislav Levin <slev@altlinux.org> 23.3.0-alt1
- 23.1.0 -> 23.3.0.

* Mon Feb 27 2023 Stanislav Levin <slev@altlinux.org> 23.1.0-alt2
- Fixed FTBFS (setuptools 67.3.0).

* Thu Feb 02 2023 Stanislav Levin <slev@altlinux.org> 23.1.0-alt1
- 22.12.0 -> 23.1.0.

* Mon Dec 12 2022 Stanislav Levin <slev@altlinux.org> 22.12.0-alt1
- 22.10.0 -> 22.12.0.

* Sat Nov 12 2022 Daniel Zagaynov <kotopesutility@altlinux.org> 22.10.0-alt1.1
- NMU: used %%add_python3_self_prov_path macro to skip self-provides from dependencies.

* Fri Oct 07 2022 Stanislav Levin <slev@altlinux.org> 22.10.0-alt1
- 22.8.0 -> 22.10.0.

* Mon Sep 12 2022 Stanislav Levin <slev@altlinux.org> 22.8.0-alt1
- 22.6.0 -> 22.8.0.

* Mon Aug 15 2022 Stanislav Levin <slev@altlinux.org> 22.6.0-alt1
- 22.3.0 -> 22.6.0.

* Fri Apr 01 2022 Stanislav Levin <slev@altlinux.org> 22.3.0-alt1
- 22.1.0 -> 22.3.0.

* Fri Feb 11 2022 Stanislav Levin <slev@altlinux.org> 22.1.0-alt1
- 21.12b0 -> 22.1.0.

* Fri Jan 14 2022 Stanislav Levin <slev@altlinux.org> 21.12b0-alt1
- 21.10b0 -> 21.12b0.

* Mon Nov 01 2021 Stanislav Levin <slev@altlinux.org> 21.10b0-alt1
- 21.9b0 -> 21.10b0.

* Mon Oct 18 2021 Stanislav Levin <slev@altlinux.org> 21.9b0-alt1
- 21.8b0 -> 21.9b0.

* Tue Sep 07 2021 Stanislav Levin <slev@altlinux.org> 21.8b0-alt1
- 21.7b0 -> 21.8b0.

* Mon Jul 26 2021 Stanislav Levin <slev@altlinux.org> 21.7b0-alt1
- 21.6b0 -> 21.7b0.

* Tue Jun 22 2021 Stanislav Levin <slev@altlinux.org> 21.6b0-alt1
- 21.5b1 -> 21.6b0.

* Tue May 11 2021 Stanislav Levin <slev@altlinux.org> 21.5b1-alt1
- 20.8b1 -> 21.5b1.

* Tue Sep 08 2020 Stanislav Levin <slev@altlinux.org> 20.8b1-alt1
- Initial build for Sisyphus.

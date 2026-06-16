%define _unpackaged_files_terminate_build 1

%define pypi_name sybil
%define mod_name %pypi_name

%def_with check

Name: python3-module-%pypi_name
Version: 10.1.0
Release: alt1
Summary: Automated testing for the examples in your documentation
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/sybil/
Vcs: https://github.com/simplistix/sybil
BuildArch: noarch
Source: %name-%version.tar
Source1: %pyproject_deps_config_name
# manually manage runtime dependencies with metadata
AutoReq: yes, nopython3
%pyproject_runtimedeps_metadata
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build
%if_with check
%pyproject_builddeps_metadata
%pyproject_builddeps_check
%endif

%description
Automated testing for the examples in your documentation.

%prep
%setup
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata
%if_with check
%pyproject_deps_resync_check_depgroup dev
%endif

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest -ra -Wignore

%files
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Mon Jun 15 2026 Stanislav Levin <slev@altlinux.org> 10.1.0-alt1
- 10.0.1 -> 10.1.0

* Fri Apr 10 2026 Stanislav Levin <slev@altlinux.org> 10.0.1-alt1
- 9.3.0 -> 10.0.1.

* Tue Dec 02 2025 Stanislav Levin <slev@altlinux.org> 9.3.0-alt1
- 9.2.0 -> 9.3.0.

* Fri Aug 08 2025 Stanislav Levin <slev@altlinux.org> 9.2.0-alt1
- 9.1.0 -> 9.2.0.

* Wed Feb 19 2025 Stanislav Levin <slev@altlinux.org> 9.1.0-alt1
- 9.0.0 -> 9.1.0.

* Wed Nov 13 2024 Stanislav Levin <slev@altlinux.org> 9.0.0-alt1
- 8.0.1 -> 9.0.0.

* Wed Nov 06 2024 Stanislav Levin <slev@altlinux.org> 8.0.1-alt1
- 8.0.0 -> 8.0.1.

* Mon Sep 23 2024 Stanislav Levin <slev@altlinux.org> 8.0.0-alt1
- 7.1.0 -> 8.0.0.

* Mon Sep 16 2024 Stanislav Levin <slev@altlinux.org> 7.1.0-alt1
- 7.0.0 -> 7.1.0.

* Thu Sep 12 2024 Stanislav Levin <slev@altlinux.org> 7.0.0-alt1
- 6.1.1 -> 7.0.0.

* Mon May 13 2024 Stanislav Levin <slev@altlinux.org> 6.1.1-alt1
- 6.1.0 -> 6.1.1.

* Tue Apr 23 2024 Stanislav Levin <slev@altlinux.org> 6.1.0-alt1
- 6.0.3 -> 6.1.0.

* Tue Feb 13 2024 Stanislav Levin <slev@altlinux.org> 6.0.3-alt1
- 5.0.3 -> 6.0.3.

* Tue Jul 18 2023 Stanislav Levin <slev@altlinux.org> 5.0.3-alt1
- 3.0.1 -> 5.0.3.

* Fri Mar 11 2022 Stanislav Levin <slev@altlinux.org> 3.0.1-alt1
- 1.4.0 -> 3.0.1.

* Fri Oct 16 2020 Stanislav Levin <slev@altlinux.org> 1.4.0-alt1
- 1.0.7 -> 1.4.0.
- Stopped Python2 package build.

* Thu Jun 07 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 1.0.7-alt2
- Fixed documentation build.

* Thu Mar 01 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 1.0.7-alt1
- Updated to upstream version 1.0.7.

* Wed Aug 23 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 1.0.5-alt1
- Initial build for ALT.

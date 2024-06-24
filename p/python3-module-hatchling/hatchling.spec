%define _unpackaged_files_terminate_build 1
%define pypi_name hatchling

Name: python3-module-%pypi_name
Version: 1.25.0
Release: alt1
Summary: Modern, extensible Python build backend
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/hatchling
VCS: https://github.com/pypa/hatch
BuildArch: noarch
Source: %name-%version.tar
Source1: pyproject_deps.json
Patch: %name-%version-alt.patch

%pyproject_runtimedeps_metadata

BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build

%description
%summary.

%prep
%setup
%autopatch -p1

%pyproject_deps_resync_build
%pyproject_deps_resync_metadata

%build
%pyproject_build

%install
%pyproject_install

%check
# Requires Internet, see tests/downstream/integrate.py

%files
%doc README.md
%_bindir/hatchling
%python3_sitelibdir/hatchling/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Mon Jun 24 2024 Stanislav Levin <slev@altlinux.org> 1.25.0-alt1
- 1.24.2 -> 1.25.0.

* Mon Apr 22 2024 Stanislav Levin <slev@altlinux.org> 1.24.2-alt1
- 1.24.1 -> 1.24.2.

* Thu Apr 18 2024 Stanislav Levin <slev@altlinux.org> 1.24.1-alt1
- 1.24.0 -> 1.24.1.

* Tue Apr 16 2024 Stanislav Levin <slev@altlinux.org> 1.24.0-alt1
- 1.23.0 -> 1.24.0.

* Mon Apr 15 2024 Stanislav Levin <slev@altlinux.org> 1.23.0-alt1
- 1.22.5 -> 1.23.0.

* Fri Apr 05 2024 Stanislav Levin <slev@altlinux.org> 1.22.5-alt1
- 1.22.4 -> 1.22.5.

* Tue Mar 26 2024 Stanislav Levin <slev@altlinux.org> 1.22.4-alt1
- 1.22.3 -> 1.22.4.

* Tue Mar 19 2024 Stanislav Levin <slev@altlinux.org> 1.22.3-alt1
- 1.22.2 -> 1.22.3.

* Mon Mar 18 2024 Stanislav Levin <slev@altlinux.org> 1.22.2-alt1
- 1.21.1 -> 1.22.2.

* Wed Feb 21 2024 Stanislav Levin <slev@altlinux.org> 1.21.1-alt1
- 1.21.0 -> 1.21.1.

* Wed Dec 20 2023 Stanislav Levin <slev@altlinux.org> 1.21.0-alt1
- 1.18.0 -> 1.21.0.

* Tue Jun 13 2023 Stanislav Levin <slev@altlinux.org> 1.18.0-alt1
- 1.17.0 -> 1.18.0.

* Fri May 12 2023 Stanislav Levin <slev@altlinux.org> 1.17.0-alt1
- 1.16.0 -> 1.17.0.

* Thu May 11 2023 Stanislav Levin <slev@altlinux.org> 1.16.0-alt1
- 1.15.0 -> 1.16.0.

* Wed May 10 2023 Stanislav Levin <slev@altlinux.org> 1.15.0-alt1
- 1.14.1 -> 1.15.0.

* Tue Apr 25 2023 Stanislav Levin <slev@altlinux.org> 1.14.1-alt1
- 1.14.0 -> 1.14.1.

* Tue Apr 18 2023 Stanislav Levin <slev@altlinux.org> 1.14.0-alt1
- 1.13.0 -> 1.14.0.

* Mon Feb 20 2023 Stanislav Levin <slev@altlinux.org> 1.13.0-alt1
- 1.12.2 -> 1.13.0.

* Tue Jan 24 2023 Stanislav Levin <slev@altlinux.org> 1.12.2-alt1
- 1.11.1 -> 1.12.2.

* Wed Oct 19 2022 Stanislav Levin <slev@altlinux.org> 1.11.1-alt1
- 1.11.0 -> 1.11.1.

* Mon Oct 10 2022 Stanislav Levin <slev@altlinux.org> 1.11.0-alt1
- 1.10.0 -> 1.11.0.

* Mon Sep 19 2022 Stanislav Levin <slev@altlinux.org> 1.10.0-alt1
- 1.9.0 -> 1.10.0.

* Mon Sep 12 2022 Stanislav Levin <slev@altlinux.org> 1.9.0-alt1
- 1.8.1 -> 1.9.0.

* Thu Aug 25 2022 Stanislav Levin <slev@altlinux.org> 1.8.1-alt1
- 1.8.0 -> 1.8.1.

* Tue Aug 16 2022 Stanislav Levin <slev@altlinux.org> 1.8.0-alt1
- 1.7.1 -> 1.8.0.

* Mon Aug 15 2022 Stanislav Levin <slev@altlinux.org> 1.7.1-alt1
- 0.22.0 -> 1.7.1.

* Mon Apr 04 2022 Stanislav Levin <slev@altlinux.org> 0.22.0-alt1
- Initial build for Sisyphus.

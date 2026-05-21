%define _unpackaged_files_terminate_build 1
%define pypi_name trove-classifiers
%define mod_name trove_classifiers

%def_with check

Name: python3-module-%pypi_name
Version: 2026.5.20.19
Release: alt1
Summary: Canonical source for classifiers on PyPI
License: Apache-2.0
Group: Development/Python3
Url: https://pypi.org/project/trove-classifiers
VCS: https://github.com/pypa/trove-classifiers.git
BuildArch: noarch
Source: %name-%version.tar
Source1: %pyproject_deps_config_name
Patch: %name-%version-alt.patch
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
Canonical source for classifiers on PyPI:
https://pypi.org/classifiers/

Classifiers categorize projects per PEP 301. Use this package to validate
classifiers in packages for PyPI upload or download.

%prep
%setup
%autopatch -p1

# calver doesn't provide means for reproducible builds from source tree
echo '%version' > ./calver_version

%pyproject_deps_resync_build
%pyproject_deps_resync_metadata

%if_with check
%pyproject_deps_resync_check_pipreqfile requirements/dev.txt
%endif

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest
%pyproject_run -- python -m tests.lib

%files
%_bindir/trove-classifiers
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Thu May 21 2026 Stanislav Levin <slev@altlinux.org> 2026.5.20.19-alt1
- 2026.5.7.17 -> 2026.5.20.19.

* Mon May 18 2026 Stanislav Levin <slev@altlinux.org> 2026.5.7.17-alt1
- 2026.4.28.13 -> 2026.5.7.17.

* Wed Apr 29 2026 Stanislav Levin <slev@altlinux.org> 2026.4.28.13-alt1
- 2026.1.14.14 -> 2026.4.28.13.

* Wed Feb 04 2026 Stanislav Levin <slev@altlinux.org> 2026.1.14.14-alt1
- 2025.12.1.14 -> 2026.1.14.14.

* Tue Dec 02 2025 Stanislav Levin <slev@altlinux.org> 2025.12.1.14-alt1
- 2025.11.14.15 -> 2025.12.1.14.

* Mon Nov 17 2025 Stanislav Levin <slev@altlinux.org> 2025.11.14.15-alt1
- 2025.9.11.17 -> 2025.11.14.15.

* Fri Sep 12 2025 Stanislav Levin <slev@altlinux.org> 2025.9.11.17-alt1
- 2025.9.9.12 -> 2025.9.11.17.

* Wed Sep 10 2025 Stanislav Levin <slev@altlinux.org> 2025.9.9.12-alt1
- 2025.8.26.11 -> 2025.9.9.12.

* Wed Sep 03 2025 Stanislav Levin <slev@altlinux.org> 2025.8.26.11-alt1
- 2025.8.6.13 -> 2025.8.26.11.

* Fri Aug 08 2025 Stanislav Levin <slev@altlinux.org> 2025.8.6.13-alt1
- 2025.5.9.12 -> 2025.8.6.13.

* Fri May 23 2025 Stanislav Levin <slev@altlinux.org> 2025.5.9.12-alt1
- 2025.4.11.15 -> 2025.5.9.12.

* Mon Apr 14 2025 Stanislav Levin <slev@altlinux.org> 2025.4.11.15-alt1
- 2025.3.19.19 -> 2025.4.11.15.

* Thu Mar 20 2025 Stanislav Levin <slev@altlinux.org> 2025.3.19.19-alt1
- 2025.3.13.13 -> 2025.3.19.19.

* Fri Mar 14 2025 Stanislav Levin <slev@altlinux.org> 2025.3.13.13-alt1
- 2025.3.3.18 -> 2025.3.13.13.

* Tue Mar 04 2025 Stanislav Levin <slev@altlinux.org> 2025.3.3.18-alt1
- 2025.2.18.16 -> 2025.3.3.18.

* Wed Feb 19 2025 Stanislav Levin <slev@altlinux.org> 2025.2.18.16-alt1
- 2025.1.15.22 -> 2025.2.18.16.

* Thu Jan 16 2025 Stanislav Levin <slev@altlinux.org> 2025.1.15.22-alt1
- 2025.1.10.15 -> 2025.1.15.22.

* Mon Jan 13 2025 Stanislav Levin <slev@altlinux.org> 2025.1.10.15-alt1
- 2025.1.7.14 -> 2025.1.10.15.

* Thu Jan 09 2025 Stanislav Levin <slev@altlinux.org> 2025.1.7.14-alt1
- 2024.10.21.16 -> 2025.1.7.14.

* Tue Oct 22 2024 Stanislav Levin <slev@altlinux.org> 2024.10.21.16-alt1
- 2024.10.16 -> 2024.10.21.16.

* Mon Oct 21 2024 Stanislav Levin <slev@altlinux.org> 2024.10.16-alt1
- 2024.10.13 -> 2024.10.16.

* Mon Oct 14 2024 Stanislav Levin <slev@altlinux.org> 2024.10.13-alt1
- 2024.9.12 -> 2024.10.13.

* Fri Sep 13 2024 Stanislav Levin <slev@altlinux.org> 2024.9.12-alt1
- 2024.7.2 -> 2024.9.12.

* Tue Jul 02 2024 Stanislav Levin <slev@altlinux.org> 2024.7.2-alt1
- 2024.5.22 -> 2024.7.2.

* Fri May 24 2024 Stanislav Levin <slev@altlinux.org> 2024.5.22-alt1
- 2024.5.17 -> 2024.5.22.

* Fri May 17 2024 Stanislav Levin <slev@altlinux.org> 2024.5.17-alt1
- 2024.4.10 -> 2024.5.17.

* Thu Apr 11 2024 Stanislav Levin <slev@altlinux.org> 2024.4.10-alt1
- 2024.3.25 -> 2024.4.10.

* Tue Mar 26 2024 Stanislav Levin <slev@altlinux.org> 2024.3.25-alt1
- 2024.3.3 -> 2024.3.25.

* Mon Mar 04 2024 Stanislav Levin <slev@altlinux.org> 2024.3.3-alt1
- 2024.2.23 -> 2024.3.3.

* Mon Feb 26 2024 Stanislav Levin <slev@altlinux.org> 2024.2.23-alt1
- 2023.11.14 -> 2024.2.23.

* Tue Nov 14 2023 Stanislav Levin <slev@altlinux.org> 2023.11.14-alt1
- 2023.11.7 -> 2023.11.14.

* Thu Nov 09 2023 Stanislav Levin <slev@altlinux.org> 2023.11.7-alt1
- 2023.10.18 -> 2023.11.7.

* Tue Nov 07 2023 Anton Zhukharev <ancieg@altlinux.org> 2023.10.18-alt1
- 2023.9.19 -> 2023.10.18.

* Thu Oct 05 2023 Stanislav Levin <slev@altlinux.org> 2023.9.19-alt1
- 2023.8.7 -> 2023.9.19.

* Wed Aug 09 2023 Stanislav Levin <slev@altlinux.org> 2023.8.7-alt1
- 2023.7.6 -> 2023.8.7.

* Wed Jul 26 2023 Stanislav Levin <slev@altlinux.org> 2023.7.6-alt1
- 2023.5.24 -> 2023.7.6.

* Thu May 25 2023 Stanislav Levin <slev@altlinux.org> 2023.5.24-alt1
- 2023.5.22 -> 2023.5.24.

* Tue May 23 2023 Stanislav Levin <slev@altlinux.org> 2023.5.22-alt1
- 2023.5.2 -> 2023.5.22.

* Wed May 03 2023 Stanislav Levin <slev@altlinux.org> 2023.5.2-alt1
- 2023.4.29 -> 2023.5.2.

* Tue May 02 2023 Stanislav Levin <slev@altlinux.org> 2023.4.29-alt1
- 2023.4.22 -> 2023.4.29.

* Tue Apr 25 2023 Stanislav Levin <slev@altlinux.org> 2023.4.22-alt1
- 2023.4.18 -> 2023.4.22.

* Wed Apr 19 2023 Stanislav Levin <slev@altlinux.org> 2023.4.18-alt1
- 2023.3.9 -> 2023.4.18.

* Fri Mar 10 2023 Stanislav Levin <slev@altlinux.org> 2023.3.9-alt1
- 2023.2.20 -> 2023.3.9.

* Tue Feb 21 2023 Stanislav Levin <slev@altlinux.org> 2023.2.20-alt1
- 2023.2.8 -> 2023.2.20.

* Mon Feb 20 2023 Stanislav Levin <slev@altlinux.org> 2023.2.8-alt1
- 2023.1.20 -> 2023.2.8.

* Fri Jan 20 2023 Stanislav Levin <slev@altlinux.org> 2023.1.20-alt1
- 2022.12.1 -> 2023.1.20.

* Fri Dec 02 2022 Stanislav Levin <slev@altlinux.org> 2022.12.1-alt1
- 2022.10.19 -> 2022.12.1.

* Wed Oct 19 2022 Stanislav Levin <slev@altlinux.org> 2022.10.19-alt1
- 2022.9.26 -> 2022.10.19.

* Tue Sep 27 2022 Stanislav Levin <slev@altlinux.org> 2022.9.26-alt1
- 2022.8.31 -> 2022.9.26.

* Thu Sep 15 2022 Stanislav Levin <slev@altlinux.org> 2022.8.31-alt1
- 2022.8.7 -> 2022.8.31.

* Thu Aug 11 2022 Stanislav Levin <slev@altlinux.org> 2022.8.7-alt1
- 2022.3.30 -> 2022.8.7.

* Fri Apr 01 2022 Stanislav Levin <slev@altlinux.org> 2022.3.30-alt1
- Initial build for Sisyphus.

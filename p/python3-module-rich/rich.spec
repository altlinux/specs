%define _unpackaged_files_terminate_build 1
%define pypi_name rich
%define mod_name %pypi_name

%def_with check

Name: python3-module-%pypi_name
Version: 15.0.0
Release: alt1
Summary: Render rich text and beautiful formatting in the terminal
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/rich/
Vcs: https://github.com/Textualize/rich
BuildArch: noarch
Source: %name-%version.tar
Source1: %pyproject_deps_config_name
Patch0: %name-%version-alt.patch
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
Rich is a Python library for rich text and beautiful formatting in the terminal.
The Rich API makes it easy to add color and style to terminal output. Rich can
also render pretty tables, progress bars, markdown, syntax highlighted source
code, tracebacks, and more - out of the box.

%prep
%setup
%autopatch -p1
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata
%if_with check
%pyproject_deps_resync_check_poetry dev
%endif

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest tests -ra

%files
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Mon Apr 13 2026 Stanislav Levin <slev@altlinux.org> 15.0.0-alt1
- 14.3.3 -> 15.0.0.

* Fri Feb 20 2026 Stanislav Levin <slev@altlinux.org> 14.3.3-alt1
- 14.3.2 -> 14.3.3.

* Wed Feb 04 2026 Stanislav Levin <slev@altlinux.org> 14.3.2-alt1
- 14.2.0 -> 14.3.2.

* Thu Dec 04 2025 Stanislav Levin <slev@altlinux.org> 14.2.0-alt1
- 14.1.0 -> 14.2.0.

* Mon Jul 28 2025 Stanislav Levin <slev@altlinux.org> 14.1.0-alt1
- 14.0.0 -> 14.1.0.

* Mon Mar 31 2025 Stanislav Levin <slev@altlinux.org> 14.0.0-alt1
- 13.9.4 -> 14.0.0.

* Wed Feb 19 2025 Stanislav Levin <slev@altlinux.org> 13.9.4-alt2
- Fixed FTBFS (pygments 2.19).

* Wed Nov 06 2024 Stanislav Levin <slev@altlinux.org> 13.9.4-alt1
- 13.9.3 -> 13.9.4.

* Wed Oct 23 2024 Stanislav Levin <slev@altlinux.org> 13.9.3-alt1
- 13.9.2 -> 13.9.3.

* Mon Oct 07 2024 Stanislav Levin <slev@altlinux.org> 13.9.2-alt1
- 13.9.1 -> 13.9.2.

* Fri Oct 04 2024 Stanislav Levin <slev@altlinux.org> 13.9.1-alt1
- 13.8.1 -> 13.9.1.

* Wed Sep 11 2024 Stanislav Levin <slev@altlinux.org> 13.8.1-alt1
- 13.7.1 -> 13.8.1.

* Thu Feb 29 2024 Stanislav Levin <slev@altlinux.org> 13.7.1-alt1
- 13.6.0 -> 13.7.1.

* Mon Oct 02 2023 Stanislav Levin <slev@altlinux.org> 13.6.0-alt1
- 12.5.1 -> 13.6.0.

* Fri Sep 23 2022 Danil Shein <dshein@altlinux.org> 12.5.1-alt1
- NMU: new version 12.5.1

* Sun Sep 06 2020 Alexey Shabalin <shaba@altlinux.org> 6.0.0-alt1
- Initial build.

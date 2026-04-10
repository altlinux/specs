%define _unpackaged_files_terminate_build 1
%define pypi_name icecream
%define mod_name %pypi_name

%def_with check

Name: python3-module-%pypi_name
Version: 2.2.0
Release: alt1
Summary: Never use print() to debug again
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/icecream
Vcs: https://github.com/gruns/icecream
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
%endif

%description
Never use print() to debug again; inspect variables, expressions, and program
execution with a single, simple function call.

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
%pyproject_run_unittest -v

%files
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Fri Apr 10 2026 Stanislav Levin <slev@altlinux.org> 2.2.0-alt1
- 2.1.10 -> 2.2.0.

* Fri Mar 13 2026 Stanislav Levin <slev@altlinux.org> 2.1.10-alt1
- 2.1.8 -> 2.1.10.

* Fri Dec 12 2025 Stanislav Levin <slev@altlinux.org> 2.1.8-alt1
- 2.1.7 -> 2.1.8.

* Tue Sep 02 2025 Stanislav Levin <slev@altlinux.org> 2.1.7-alt1
- 2.1.5 -> 2.1.7.

* Thu Jun 26 2025 Stanislav Levin <slev@altlinux.org> 2.1.5-alt1
- 2.1.4 -> 2.1.5.

* Tue Jan 14 2025 Stanislav Levin <slev@altlinux.org> 2.1.4-alt1
- 2.1.3 -> 2.1.4.

* Wed Apr 26 2023 Stanislav Levin <slev@altlinux.org> 2.1.3-alt1
- Initial build for Sisyphus.

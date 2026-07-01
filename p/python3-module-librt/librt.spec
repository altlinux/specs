%define _unpackaged_files_terminate_build 1
%define pypi_name librt
%define mod_name %pypi_name

%def_with check

# %%python3_set_limited_api is not supported yet

Name: python3-module-%pypi_name
Version: 0.12.0
Release: alt1
Summary: Mypyc runtime library
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/librt
Vcs: https://github.com/mypyc/librt
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
BuildRequires: python3-module-pytest
BuildRequires: python3-module-mypy-extensions
%endif

%description
%summary.

%prep
%setup
%autopatch -p1
cp -r lib-rt/* .
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest -vra smoke_tests.py

%files
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Wed Jul 01 2026 Stanislav Levin <slev@altlinux.org> 0.12.0-alt1
- 0.11.0 -> 0.12.0

* Thu May 14 2026 Stanislav Levin <slev@altlinux.org> 0.11.0-alt1
- 0.10.0 -> 0.11.0.

* Wed May 06 2026 Stanislav Levin <slev@altlinux.org> 0.10.0-alt1
- 0.9.0 -> 0.10.0.

* Fri Apr 10 2026 Stanislav Levin <slev@altlinux.org> 0.9.0-alt1
- 0.8.1 -> 0.9.0.

* Wed Feb 18 2026 Stanislav Levin <slev@altlinux.org> 0.8.1-alt1
- 0.8.0 -> 0.8.1.

* Fri Feb 13 2026 Stanislav Levin <slev@altlinux.org> 0.8.0-alt1
- 0.7.8 -> 0.8.0.

* Wed Feb 04 2026 Stanislav Levin <slev@altlinux.org> 0.7.8-alt1
- 0.7.5 -> 0.7.8.

* Thu Dec 25 2025 Stanislav Levin <slev@altlinux.org> 0.7.5-alt1
- 0.7.4 -> 0.7.5.

* Tue Dec 16 2025 Stanislav Levin <slev@altlinux.org> 0.7.4-alt1
- 0.7.3 -> 0.7.4.

* Thu Dec 11 2025 Stanislav Levin <slev@altlinux.org> 0.7.3-alt1
- Initial build for sisyphus.


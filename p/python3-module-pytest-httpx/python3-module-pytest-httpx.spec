%define _unpackaged_files_terminate_build 1
%define pypi_name pytest-httpx
%define pypi_nname pytest-httpx
%define mod_name pytest_httpx

%def_with check

Name: python3-module-%pypi_nname
Version: 0.36.2
Release: alt1

Summary: pytest fixture to mock HTTPX
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/pytest-httpx/
Vcs: https://github.com/Colin-b/pytest_httpx

BuildArch: noarch

Source0: %name-%version.tar
Source1: %pyproject_deps_config_name
Patch0: %name-%version-alt.patch
# manually manage runtime dependencies with metadata
AutoReq: yes, nopython3
%pyproject_runtimedeps_metadata
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build
%if_with check
%pyproject_builddeps_metadata_extra testing
%endif

%description
Once installed, httpx_mock pytest fixture will make sure every httpx
request will be replied to with user provided responses (unless some
hosts are explicitly skipped).

%prep
%setup
%autopatch -p1
%pyproject_scm_init
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest -vra -o=addopts=-Wignore

%files
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Fri Apr 10 2026 Stanislav Levin <slev@altlinux.org> 0.36.2-alt1
- 0.36.0 -> 0.36.2.

* Fri Mar 06 2026 Stanislav Levin <slev@altlinux.org> 0.36.0-alt1
- 0.35.0 -> 0.36.0.

* Mon Jul 14 2025 Stanislav Levin <slev@altlinux.org> 0.35.0-alt2
- Fixed FTBFS (httpx 0.28.0).

* Tue Mar 04 2025 Anton Zhukharev <ancieg@altlinux.org> 0.35.0-alt1
- Built for ALT Sisyphus.


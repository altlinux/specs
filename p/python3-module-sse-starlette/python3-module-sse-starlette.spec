%define _unpackaged_files_terminate_build 1
%define pypi_name sse-starlette
%define mod_name sse_starlette

%def_with check

Name: python3-module-%pypi_name
Version: 3.3.2
Release: alt1

Summary: SSE plugin for Starlette
License: BSD-3-Clause
Group: Development/Python3
Url: https://pypi.org/project/sse-starlette/
Vcs: https://github.com/sysid/sse-starlette

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
%add_pyproject_deps_check_filter testcontainers
%pyproject_builddeps_metadata_extra examples
%pyproject_builddeps_check
%endif

%description
Server Sent Events for Starlette and FastAPI.

%prep
%setup
%autopatch -p1
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
rm -fv tests/{experimentation,integration}/test_multiple_consumers*.py
%pyproject_run_pytest -vra -m "not (integration or e2e)"

%files
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Sat Mar 14 2026 Anton Zhukharev <ancieg@altlinux.org> 3.3.2-alt1
- Updated to 3.3.2.

* Thu May 29 2025 Anton Zhukharev <ancieg@altlinux.org> 2.3.5-alt1
- Updated to 2.3.5.

* Mon Mar 10 2025 Anton Zhukharev <ancieg@altlinux.org> 2.2.1-alt1
- Updated to 2.2.1.

* Thu Aug 01 2024 Anton Zhukharev <ancieg@altlinux.org> 2.1.3-alt1
- Updated to 2.1.3.

* Thu Jul 25 2024 Anton Zhukharev <ancieg@altlinux.org> 2.1.2-alt1
- Updated to 2.1.2.

* Wed Jul 24 2024 Anton Zhukharev <ancieg@altlinux.org> 2.1.0-alt1
- Built for ALT Sisyphus.

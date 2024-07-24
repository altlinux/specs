%define _unpackaged_files_terminate_build 1
%define pypi_name sse-starlette
%define mod_name sse_starlette

%def_with check

Name: python3-module-%pypi_name
Version: 2.1.0
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

%pyproject_runtimedeps_metadata
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build
%if_with check
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
%pyproject_deps_resync_check_tox tox.ini testenv
%endif

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest -vra -m "not (integration or e2e)"

%files
%doc AUTHORS CHANGELOG.md LICENSE README.md
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Wed Jul 24 2024 Anton Zhukharev <ancieg@altlinux.org> 2.1.0-alt1
- Built for ALT Sisyphus.


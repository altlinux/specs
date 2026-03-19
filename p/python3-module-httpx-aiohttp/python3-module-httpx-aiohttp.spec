%define _unpackaged_files_terminate_build 1
%define pypi_name httpx-aiohttp
%define mod_name httpx_aiohttp

# WTF: tests require source code of httpx.
# It's not normal, so I disabled testing.
%def_without check

Name: python3-module-%pypi_name
Version: 0.1.12
Release: alt1

Summary: aiohttp-powered httpx client
License: BSD-3-Clause
Group: Development/Python3
Url: https://pypi.org/project/httpx-aiohttp/
Vcs: https://github.com/karpetrosyan/httpx-aiohttp

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
%pyproject_builddeps_metadata
%pyproject_builddeps_check
%endif

%description
provides transports for httpx to work on top of aiohttp, handling all
high-level features like authentication, retries, and cookies through
httpx, while delegating low-level socket-level HTTP messaging to
aiohttp.

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
%pyproject_run_pytest -vra

%files
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Thu Mar 19 2026 Anton Zhukharev <ancieg@altlinux.org> 0.1.12-alt1
- Packaged for ALT Sisyphus.

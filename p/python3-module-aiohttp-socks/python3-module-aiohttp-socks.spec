%define _unpackaged_files_terminate_build 1
%define pypi_name aiohttp-socks
%define module_name aiohttp_socks

%def_with check

Name: python3-module-%pypi_name
Version: 0.10.2
Release: alt1
Summary: Proxy connector for aiohttp with SOCKS4, SOCKS5 and HTTP support
License: Apache-2.0
Group: Development/Python3
Url: https://pypi.org/project/aiohttp-socks
Vcs: https://github.com/romis2012/aiohttp-socks.git

BuildArch: noarch

Source: %name-%version.tar
Source1: %pyproject_deps_config_name

BuildRequires(pre): rpm-build-pyproject
%pyproject_runtimedeps_metadata
%pyproject_builddeps_build

%if_with check
%pyproject_builddeps_metadata
%pyproject_builddeps_check
%endif

%description
The aiohttp-socks package provides a proxy connector for aiohttp.
Supports SOCKS4(a), SOCKS5(h), HTTP (CONNECT) as well as proxy chains.
It uses python-socks for core proxy functionality.

%prep
%setup
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata

%if_with check
%pyproject_deps_resync_check_pipreqfile requirements-dev.txt
%endif

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest -vra

%files
%doc README.md
%python3_sitelibdir/%module_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Fri Nov 14 2025 Aleksandr A. Voyt <sobue@altlinux.org> 0.10.2-alt1
- Initial build.


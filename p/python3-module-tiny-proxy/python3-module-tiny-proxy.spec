%define _unpackaged_files_terminate_build 1
%define pypi_name tiny-proxy
%define module_name tiny_proxy

%def_with check

Name: python3-module-%pypi_name
Version: 0.2.1
Release: alt1
Summary: Simple proxy server (SOCKS4, SOCKS5, HTTP tunnel)
License: Apache-2.0
Group: Development/Python3
Url: https://pypi.org/project/tiny-proxy
Vcs: https://github.com/romis2012/tiny-proxy.git

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
Simple proxy (SOCKS4(a), SOCKS5(h), HTTP tunnel) server built with anyio.
It is used for testing python-socks, aiohttp-socks and httpx-socks packages.

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
* Fri Nov 14 2025 Aleksandr A. Voyt <sobue@altlinux.org> 0.2.1-alt1
- Initial build.


%define _unpackaged_files_terminate_build 1
%define pypi_name aiocache

# tests require running redis and memcached servers
%def_without check

Name: python3-module-%pypi_name
Version: 0.12.3
Release: alt1

Summary: Asyncio cache manager for redis, memcached and memory
License: BSD-3-Clause
Group: Development/Python3
Url: https://pypi.org/project/aiocache
VCS: https://github.com/aio-libs/aiocache
BuildArch: noarch

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3(setuptools)

%description
Asyncio cache supporting multiple backends (memory, redis, memcached, etc.).

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest -vra

%files
%doc CHANGES.rst CONTRIBUTING.rst README.rst
%python3_sitelibdir/%pypi_name
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Sun Mar 22 2026 Dmitry Maksimenkov <dmaks@altlinux.org> 0.12.3-alt1
- Initial build for ALT.


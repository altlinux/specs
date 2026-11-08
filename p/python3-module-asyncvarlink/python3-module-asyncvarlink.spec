%define _unpackaged_files_terminate_build 1
%define pypi_name asyncvarlink
%define mod_name asyncvarlink

Name: python3-module-%pypi_name
Version: 0.3.3
Release: alt1
Summary: asyncio-compatible, type-driven varlink implementation supporting file descriptor passing
Group: Development/Python3
License: LGPL-2.0-or-later
Url: https://helmutg.github.io/asyncvarlink/
Vcs: https://github.com/helmutg/asyncvarlink.git

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
# PEP 517 build frontend (auto-added by %pyproject_* macros,
# listed explicitly for a local non-hasher build)
BuildRequires: python3-module-pyproject-installer >= 0.4.0
# build backend from [build-system].requires in pyproject.toml
BuildRequires: python3-module-flit-core >= 3.8
# check
BuildRequires: python3-module-pytest
BuildRequires: python3-module-hypothesis

BuildArch: noarch

%description
A pure Python implementation of the varlink IPC protocol based on asyncio.
It derives a varlink interface description from a typed Python class
and supports passing file descriptors like systemd does.

%prep
%setup -q

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest

%files
%doc README.md LICENSE
%python3_sitelibdir_noarch/%mod_name
%python3_sitelibdir_noarch/%{pyproject_distinfo %pypi_name}

%changelog
* Fri Nov 06 2026 Alexey Saprunov <sav@altlinux.org> 0.3.3-alt1
- Initial build for ALT Linux.

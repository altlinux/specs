# Unpackaged files in buildroot should terminate build
%define _unpackaged_files_terminate_build 1

#%%def_disable check

%define modulename Charon
%define srcname lib%modulename

Name:    python3-module-%modulename
Version: 8.4.0
Release: alt0.rc.1

Summary: File metadata and streaming library
License: LGPL-3.0-or-later
Group:   Development/Python3
URL:     https://github.com/Ultimaker/%srcname
VCS:     https://github.com/Ultimaker/%srcname

BuildArch: noarch

# Source-url: %url/archive/%version/%srcname-%version.tar.gz
Source: %srcname-%version.tar

Patch: PyQt6.patch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-dev
BuildRequires: python3-module-wheel
BuildRequires: python3-module-setuptools

%if_disabled check
%else
BuildRequires: pytest3
BuildRequires: python3-module-pytest-timeout
%endif

%add_python3_req_skip FileService RequestQueue

%description
%summary

%prep
%setup -n %srcname-%version
%autopatch -p1

%build
%pyproject_build

%install
%pyproject_install

%check
export PYTHONPATH=%buildroot/%python3_sitelibdir/
pytest3 -v

%files
%python3_sitelibdir/%modulename/
%python3_sitelibdir/%{pep427_name %modulename}-1.0.dist-info/
%doc *.md

%changelog
* Tue Apr 21 2026 Valery Zabrovsky <brow@altlinux.org> 8.4.0-alt0.rc.1
- New version 8.4.0-rc.
- Port to PyQt6.

* Wed Apr 02 2025 Stanislav Levin <slev@altlinux.org> 4.10.2-alt2.1
- NMU: fixed FTBFS (setuptools 75.8.1)

* Tue Jun 13 2023 Anton Midyukov <antohami@altlinux.org> 4.10.2-alt2
- Migration to PEP517

* Sat Mar 05 2022 Anton Midyukov <antohami@altlinux.org> 4.10.2-alt1
- initial build

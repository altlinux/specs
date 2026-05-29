%define _unpackaged_files_terminate_build 1
Name:    mamonsu
Version: 3.5.15
Release: alt1

Summary: mamonsu is an active agent for collecting PostgreSQL instance and operating system metrics that can interact with Zabbix
License: BSD-3-Clause
Group:   Development/Python3
URL:     https://github.com/postgrespro/mamonsu

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-setuptools python3-module-wheel

BuildArch: noarch

Source: %name-%version.tar

%description
%summary

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%check
#%%tox_create_default_config
%tox_check_pyproject

%files
%doc *.md
%_bindir/%name
%python3_sitelibdir/%name/
%python3_sitelibdir/%{pyproject_distinfo %name}

%changelog
* Fri May 29 2026 Andrey Cherepanov <cas@altlinux.org> 3.5.15-alt1
- Initial build for Sisyphus

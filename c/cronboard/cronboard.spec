%def_without check

Name: cronboard
Version: 0.5.1
Release: alt1

Summary: A terminal-based dashboard for managing cron jobs locally and on servers
License: MIT
Group: System/Configuration/Other

URL: https://antoniorodr.github.io/cronboard
VCS: https://github.com/antoniorodr/cronboard

BuildArch: noarch

Source0: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel

%if_with check
BuildRequires: python3-module-pytest-asyncio
BuildRequires: python3-module-python-crontab
BuildRequires: python3-module-tomlkit
BuildRequires: python3-module-textual
BuildRequires: python3-module-textual-autocomplete
BuildRequires: python3-module-cron-descriptor
BuildRequires: python3-module-paramiko
BuildRequires: python3-module-pytest
%endif

%description
%summary.

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest tests

%files
%doc *.md LICENSE
%_bindir/%name
%python3_sitelibdir/*

%changelog
* Fri Mar 27 2026 Aleksandr Shamaraev <shad@altlinux.org> 0.5.1-alt1
- Initial build for ALT Linux.


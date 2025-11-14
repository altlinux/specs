%define _unpackaged_files_terminate_build 1
%define pypi_name net_tui

%def_with check

Name: net-tui
Version: 0.1.2
Release: alt1
Summary: TUI/CLI for network settings.
License: MIT
Group: System/Configuration/Other
URL: https://github.com/zerospirit79/net-tui

Source: %name-%version.tar
Patch: %name-%version-alt.patch
  
BuildArch: noarch

BuildRequires(pre): rpm-build-pyproject
BuildRequires: python3(setuptools)
BuildRequires: python3(wheel)
BuildRequires: python3(installer)
BuildRequires: python3(textual)
BuildRequires: python3(typer)
BuildRequires: python3(pydantic)
BuildRequires: python3(psutil)
BuildRequires: python3(netifaces)

%if_with check
BuildRequires: python3(pytest)
%endif

Requires: python3(textual)
Requires: python3(typer)
Requires: python3(pydantic)
Requires: python3(psutil)
Requires: python3(netifaces)
Requires: systemd
Requires: sudo

%description
%name console TUI/CLI tool to manage network settings on ALT linux.
Supports NetworkManager, systemd-networkd and DNS via systemd-resolved.

%prep
%setup
%autopatch -p1

%build
%pyproject_build

%install
%pyproject_install
  
%check
%pyproject_run_pytest

%files
%doc README.md
%_bindir/%name
%python3_sitelibdir/%pypi_name
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Wed Nov 12 2025 Pavel Shilov <zerospirit@altlinux.org> 0.1.2-alt1
- Initial build for Sisyphus.

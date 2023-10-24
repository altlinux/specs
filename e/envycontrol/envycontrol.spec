Name: envycontrol
Version: 3.3.0
Release: alt1

Summary: EnvyControl is a program aimed to provide an easy way to switch GPU modes on Nvidia Optimus systems

License: MIT
Group: System/Configuration/Hardware
Url: https://github.com/bayasdev/envycontrol

# Source-url: https://github.com/bayasdev/envycontrol/archive/refs/tags/v%version.tar.gz
Source: envycontrol-%version.tar

BuildArch: noarch

BuildRequires(pre): rpm-build-python3

BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel

%description
EnvyControl is a program aimed to provide an easy way to switch GPU modes
on Nvidia Optimus systems (i.e laptops with hybrid Intel + Nvidia or
AMD + Nvidia graphics configurations) under Linux.

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%files -n envycontrol
%_bindir/envycontrol
%python3_sitelibdir/*

%changelog
* Mon Oct 23 2023 Vitaly Lipatov <lav@altlinux.ru> 3.3.0-alt1
- initial build for ALT Sisyphus

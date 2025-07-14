Name: installer-feature-nvidia
Version: 0.1.0
Release: alt1

Summary: Installer hook for NVIDIA proprietary driver
License: ALT-Public-Domain
Group: System/Configuration/Other
Url: http://www.altlinux.org/Installer/beans
BuildArch: noarch
Source: %name-%version.tar

%description
This hook performs additional settings of NVIDIA proprietary drivers
after installation, such as:

* Full preserve video memory after suspend

%prep
%setup

%install
%define hookdir %_datadir/install2/postinstall.d
mkdir -p %buildroot%hookdir
install -pm755 *.sh %buildroot%hookdir/

%files
%hookdir/*

%changelog
* Mon Jul 14 2025 Semen Fomchenkov <armatik@altlinux.org> 0.1.0-alt1
- Initial build.

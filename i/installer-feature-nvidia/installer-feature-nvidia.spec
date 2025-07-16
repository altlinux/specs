Name: installer-feature-nvidia
Version: 0.1.2
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
%define hookdir %_datadir/install2/preinstall.d
mkdir -p %buildroot%hookdir
install -pm755 *.sh %buildroot%hookdir/

%files
%hookdir/*

%changelog
* Tue Jul 15 2025 Semen Fomchenkov <armatik@altlinux.org> 0.1.2-alt1
- Fix: remove an unnecessary space after the parameter.
- Spec: change postinstall.d to preinstall.d.

* Tue Jul 15 2025 Semen Fomchenkov <armatik@altlinux.org> 0.1.1-alt1
- Fix: use destdir in CONF path and correct file name.
- Refactor: unnecessary condition check removed.

* Mon Jul 14 2025 Semen Fomchenkov <armatik@altlinux.org> 0.1.0-alt1
- Initial build.

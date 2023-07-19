Name: installer-feature-remove-xorgconf
Version: 0.1
Release: alt1

Summary: Remove xorg.conf if not needed
License: GPL-2.0-or-later
Group: System/Configuration/Other
Url: http://www.altlinux.org/Installer/beans

BuildArch: noarch

Source: %name-%version.tar

%description
Remove xorg.conf if not needed after installation.

%prep
%setup

%build

%install
%define hookdir %_datadir/install2/preinstall.d
mkdir -p %buildroot%hookdir
install -pm755 *.sh %buildroot%hookdir/

%files
%hookdir/*

%changelog
* Wed Jul 19 2023 Sergey V Turchin <zerg@altlinux.org> 0.1-alt1
- initial build

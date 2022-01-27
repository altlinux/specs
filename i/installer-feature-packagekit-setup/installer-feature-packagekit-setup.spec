Name: installer-feature-packagekit-setup
Version: 0.1
Release: alt1

Summary: Setup PackageKit
License: GPL-2.0-or-later
Group: System/Configuration/Other
Url: http://www.altlinux.org/Installer/beans

BuildArch: noarch

Source: %name-%version.tar

%description
Override PackageKit defaults to update cached new packages versions.

%prep
%setup

%build

%install
%define hookdir %_datadir/install2/postinstall.d
mkdir -p %buildroot%hookdir
install -pm755 *.sh %buildroot%hookdir/

%files
%hookdir/*

%changelog
* Thu Jan 27 2022 Sergey V Turchin <zerg@altlinux.org> 0.1-alt1
- initial build

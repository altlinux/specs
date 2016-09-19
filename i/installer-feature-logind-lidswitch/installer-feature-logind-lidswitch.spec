Name: installer-feature-logind-lidswitch
Version: 0.1
Release: alt1

Summary: Don't ignore inhibition by lid switch
License: GPL
Group: System/Configuration/Other
Url: http://www.altlinux.org/Installer/beans

BuildArch: noarch
Source: %name-%version.tar

%description
%summary

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
* Tue Jul 22 2014 Sergey V Turchin <zerg@altlinux.org> 0.1-alt1
- initial build

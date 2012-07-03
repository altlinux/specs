Name: installer-feature-kdm-autologin
Version: 1.0
Release: alt2

Summary: Setup kdm autologin
License: GPL
Group: System/Configuration/Other
Url: http://www.altlinux.org/Installer/beans

BuildArch: noarch
Source: %name-%version.tar

%description
Setup kdm autologin

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
* Sun Feb 26 2012 Sergey V Turchin <zerg@altlinux.org> 1.0-alt2
- fix path to /etc/passwd

* Fri Feb 24 2012 Sergey V Turchin <zerg@altlinux.org> 1.0-alt0.M60P.1
- built for M60P

* Fri Feb 24 2012 Sergey V Turchin <zerg@altlinux.org> 1.0-alt1
- initial build

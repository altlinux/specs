Name: installer-feature-kdesktop-services
Version: 0.3.3
Release: alt1

Summary: Setup services for start/not start on boot
License: GPL
Group: System/Configuration/Other
Url: http://www.altlinux.org/Installer/beans
BuildArch: noarch
Source: %name-%version.tar

%description
Setup services for start/not start on boot

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
* Thu May 17 2012 Sergey V Turchin <zerg@altlinux.org> 0.3.3-alt1
- turn off clamd by default

* Fri Sep 30 2011 Sergey V Turchin <zerg@altlinux.org> 0.3.2-alt1
- turn off lircd by default

* Thu Jun 23 2011 Sergey V Turchin <zerg@altlinux.org> 0.3.1-alt1
- turn off nscd by default

* Tue May 17 2011 Sergey V Turchin <zerg@altlinux.org> 0.3-alt1
- turn on samba by default

* Mon Feb 14 2011 Sergey V Turchin <zerg@altlinux.org> 0.2-alt1
- turn off hal by default

* Tue Oct 12 2010 Sergey V Turchin <zerg@altlinux.org> 0.1-alt1
- initial build


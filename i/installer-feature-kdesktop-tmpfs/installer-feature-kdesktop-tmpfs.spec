Name: installer-feature-kdesktop-tmpfs
Version: 2.6
Release: alt1

Summary: Setup services for start/not start on boot
License: GPL
Group: System/Configuration/Other
Url: http://www.altlinux.org/Installer/beans

BuildArch: noarch
Source: %name-%version.tar

%description
Setup tmp filesystem:
- turn off tmpfs
- turn on pam_mktemp
- find biggest free space for /tmp; modyfy /etc/fstab if needed

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
* Mon Oct 09 2023 Sergey V Turchin <zerg@altlinux.org> 2.6-alt1
- fix to remove temporary file

* Fri Jul 23 2021 Sergey V Turchin <zerg@altlinux.org> 2.5-alt1
- fix typo

* Fri Jul 23 2021 Sergey V Turchin <zerg@altlinux.org> 2.4-alt1
- fix typo

* Fri Jun 14 2019 Sergey V Turchin <zerg@altlinux.org> 2.3-alt2
- dont use ubt macro

* Thu Feb 09 2017 Sergey V Turchin <zerg@altlinux.org> 2.3-alt1
- check for execution possibility (ALT#33094)

* Tue Jul 26 2016 Sergey V Turchin <zerg@altlinux.org> 2.2-alt1
- add nodev option for /tmp

* Mon Jun 17 2013 Sergey V Turchin <zerg@altlinux.org> 2.1-alt1
- don't mask tmp.mount unit
- add nosuid option for /tmp

* Thu May 16 2013 Sergey V Turchin <zerg@altlinux.org> 2.0-alt1
- mask tmp.mount unit

* Wed Feb 13 2013 Sergey V Turchin <zerg@altlinux.org> 1.1-alt1
- check for possibility to change file mode on filesystem

* Wed Oct 13 2010 Sergey V Turchin <zerg@altlinux.org> 1.0-alt1
- initial build

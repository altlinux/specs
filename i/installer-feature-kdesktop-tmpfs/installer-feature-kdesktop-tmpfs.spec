Name: installer-feature-kdesktop-tmpfs
Version: 1.1
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
* Wed Feb 13 2013 Sergey V Turchin <zerg@altlinux.org> 1.1-alt1
- check for possibility to change file mode on filesystem

* Wed Oct 13 2010 Sergey V Turchin <zerg@altlinux.org> 1.0-alt1
- initial build

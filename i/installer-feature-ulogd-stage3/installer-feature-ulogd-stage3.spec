Name: installer-feature-ulogd-stage3
Version: 0.3
Release: alt2

Summary: Installer stage3 ulogd hook
License: GPL
Group: System/Configuration/Other
Url: http://www.altlinux.org/Installer/beans
Packager: Mikhail Efremov <sem@altlinux.org>
BuildArch: noarch
Requires: alterator-ulogd
Source: %name-%version.tar

%description
This package contains installer stage3 hook for alterator-ulogd module.

%prep
%setup

%install
%define hookdir %_datadir/install2/postinstall.d
mkdir -p %buildroot%hookdir
install -pm755 *.sh %buildroot%hookdir/

%files
%hookdir/*

%changelog
* Tue Sep 08 2009 Mikhail Efremov <sem@altlinux.org> 0.3-alt2
- disable ulogd_LOGEMU plugin.

* Fri Aug 28 2009 Mikhail Efremov <sem@altlinux.org> 0.3-alt1
- uncomment install2-init-functions.

* Fri Aug 28 2009 Mikhail Efremov <sem@altlinux.org> 0.2-alt1
- run command in chroot.

* Thu Aug 27 2009 Mikhail Efremov <sem@altlinux.org> 0.1-alt1
- Initial build


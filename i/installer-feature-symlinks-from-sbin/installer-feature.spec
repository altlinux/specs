Name: installer-feature-symlinks-from-sbin
Version: 0.2
Release: alt3

Summary: Make some useful programs from /sbin and /usr/sbin available to user
License: GPL
Group: System/Configuration/Other
Url: http://www.altlinux.org/Installer/beans
BuildArch: noarch
Packager: Andrey Cherepanov <cas@altlinux.org>
Source: %name-%version.tar

%description
Make symlinks for some useful programs from /sbin to /bin
and from /usr/sbin to /usr/bin.

%prep
%setup

%install
%define hookdir %_datadir/install2/postinstall.d
mkdir -p %buildroot%hookdir
install -pm755 *.sh %buildroot%hookdir/

%files
%hookdir/*

%changelog
* Mon May 14 2012 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.2-alt3
- Add arp to programs list

* Wed Apr 04 2012 Andrey Cherepanov <cas@altlinux.org> 0.2-alt2
- Add lsusb to non-privileged user path
- Update programs symlinked from /sbin/

* Fri Oct 01 2010 Andrey Cherepanov <cas@altlinux.org> 0.2-alt1
- remove existed symlinks for arp ifconfig route

* Tue Feb 09 2010 Andrey Cherepanov <cas@altlinux.org> 0.1-alt2
- fix script and hook directory

* Wed Feb 03 2010 Andrey Cherepanov <cas@altlinux.org> 0.1-alt1
- initial version


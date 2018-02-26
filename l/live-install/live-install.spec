Name: live-install
Version: 20120113
Release: alt1
Summary: The script to clone ALT Linux system from LiveCD to a hard disk
Group: System/Configuration/Other
License: GPL
BuildArch: noarch
Packager: Michael Pozhidaev <msp@altlinux.ru>

Requires: lilo, fstyp

Source: %name-%version.tar.gz

%description
The script to clone ALT Linux system from LiveCD to a hard disk

%prep
%setup -q
%build
%install
install -d -m 755 %buildroot/%_sbindir/
install -pD -m 755 live-install* %buildroot/%_sbindir/
install -pD -m 644 dev.cpio.bz2 %buildroot/%_datadir/%name/dev.cpio.bz2
mkdir -p %buildroot/%_datadir/%name/scripts.d

%files
%_sbindir/*
%_datadir/%name
%dir %_datadir/%name/scripts.d

%changelog
* Fri Jan 13 2012 Michael Pozhidaev <msp@altlinux.ru> 20120113-alt1
- Added --no-lilo command line option

* Sun Jan 08 2012 Michael Pozhidaev <msp@altlinux.ru> 20120108-alt1
- New approach based on splitted scripts

* Mon Nov 21 2011 Eugene Prokopiev <enp@altlinux.ru> 20111121-alt1
- fix removing obsoleted remount_rw package

* Wed Aug 03 2011 Eugene Prokopiev <enp@altlinux.ru> 20110803-alt2
- fix removing live packages again

* Wed Aug 03 2011 Eugene Prokopiev <enp@altlinux.ru> 20110803-alt1
- fix removing live packages

* Wed Jul 27 2011 Eugene Prokopiev <enp@altlinux.ru> 20110727-alt1
- fix lib64 and installkernel issues

* Tue May 17 2011 Eugene Prokopiev <enp@altlinux.ru> 20110517-alt1
- use installkernel, create empty /cgroup and /selinux

* Thu Apr 07 2011 Eugene Prokopiev <enp@altlinux.ru> 20110407-alt1
- copy existing /home instead of creating it

* Wed Apr 06 2011 Eugene Prokopiev <enp@altlinux.ru> 20110406-alt1
- remove all live packages after install

* Tue Mar 29 2011 Eugene Prokopiev <enp@altlinux.ru> 20110329-alt1
- sync with fakeinstall feature from m-p-l
- add scripts.d

* Sun Feb 06 2011 Michael Pozhidaev <msp@altlinux.ru> 20110206-alt1
- Package was renamed from homeros-install to live-install

* Sun Jan 30 2011 Michael Pozhidaev <msp@altlinux.ru> 20110130-alt1
- Removed altlinux user from installed system
- Enabled sshd and acpid services in installed system

* Fri Jan 28 2011 Michael Pozhidaev <msp@altlinux.ru> 20110128-alt1
- General script update

* Wed Jan 26 2011 Michael Pozhidaev <msp@altlinux.ru> 20110126-alt1
- Initial package


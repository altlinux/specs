Name: installer-distro-server-light
Version: 6.0
Release: alt3

Summary: Installer files for server
License: GPL
Group: System/Configuration/Other
BuildArch: noarch
Packager: Anton Farygin <rider@altlinux.com>

Source: %name-%version.tar

%description
Installer files for light server.

%package stage2
Summary: Installer stage2
License: GPL
Group: System/Configuration/Other
Provides: installer-server-light-stage2 = %name-%version
Requires: installer-stage2
#modules
Requires: alterator-sysconfig
Requires: alterator-datetime
Requires: alterator-pkg
Requires: alterator-vm
Requires: alterator-notes
Requires: installer-feature-vm-server-light-stage2
Requires: x-cursor-theme-jimmac

%description stage2
Installer server stage2.

%package stage3
Summary: Installer stage3
License: GPL
Group: System/Configuration/Other
Provides: installer-server-light-stage3 = %name-%version
#Requires: installer-stage3
#modules
Requires: alterator-grub
Requires: alterator-users
Requires: alterator-root
Requires: alterator-net-eth dhcpcd
Requires: alterator-net-general
Requires: installer-feature-nfs-server-stage3
Requires: installer-feature-powerbutton-stage3

%description stage3
Installer server stage3.

%prep
%setup

%install
%define install2dir %_datadir/install2
mkdir -p %buildroot%install2dir
cp -a * %buildroot%install2dir/

%files stage2
%install2dir/alterator-menu
%install2dir/installer-steps
%install2dir/*.d/*

%files stage3

%changelog
* Fri Apr 01 2011 Anton Farygin <rider@altlinux.ru> 6.0-alt3
- add guile18 to cleanup list
- updated services list for current packages base

* Wed Feb 23 2011 Anton Farygin <rider@altlinux.ru> 6.0-alt2
- updated default services and packages list for new repository state

* Fri Nov 05 2010 Anton Farygin <rider@altlinux.ru> 6.0-alt1
- use grub2

* Sat Dec 26 2009 Anton Farygin <rider@altlinux.ru> 5.0-alt4
- remove indexhtml-common from installed system

* Fri Dec 25 2009 Anton Farygin <rider@altlinux.ru> 5.0-alt3
- remove qt, all alterator's and more unused packages from installed system

* Tue Sep 08 2009 Anton Farygin <rider@altlinux.ru> 5.0-alt2
- disabled bind, alteratord and ntpd services by default
- specfile cleanup

* Thu May 07 2009 Anton Farygin <rider@altlinux.ru> 5.0-alt1
- initial build, based on Office Server

* Tue Apr 28 2009 Dmitry V. Levin <ldv@altlinux.org> 5.0-alt8
- Added installer-feature-net-br-stage2 to stage2.

* Fri Apr 10 2009 Dmitry V. Levin <ldv@altlinux.org> 5.0-alt7
- preinstall.d: Renamed 01-home -> 01-fs, added /srv support there.
- postinstall.d/03-button.sh: Replaced with installer-feature-powerbutton-stage3.
- initinstall.d/05-vm-profile-ofs: Replaced with installer-feature-vm-ofs-stage2.
- preinstall.d/01-fs: Replaced with installer-feature-vm-ofs-stage3.
- module-order-list: Added new modules.

* Thu Apr 02 2009 Dmitry V. Levin <ldv@altlinux.org> 5.0-alt6
- Updated alterator/menu/module-order-list from inger@.
- Renamed to installer-distro-office-server.

* Thu Apr 02 2009 Dmitry V. Levin <ldv@altlinux.org> 5.0-alt5
- stage3: Added requirement on installer-feature-nfs-server-stage3.
- initinstall.d/05-vm-profile: Rewritten.
- postinstall.d/06-xinetd.sh: Removed.
- postinstall.d/10-alteratord.sh: s/run_chroot/exec_chroot/.
- preinstall.d/01-home: Rewritten.
- Added files for /etc/alterator/menu/.
- Updated BuildRequires.

* Thu Feb 26 2009 Stanislav Ievlev <inger@altlinux.org> 5.0-alt4
- remove unused files
- add postinstall.d script for alteratord

* Tue Feb 24 2009 Anton V. Boyarshinov <boyarsh@altlinux.ru> 5.0-alt3
- root and ldap steps moved to firsttime 

* Mon Feb 09 2009 Anton V. Boyarshinov <boyarsh@altlinux.ru> 5.0-alt2
- root and net steps changed to office-server 

* Wed Feb 04 2009 Anton V. Boyarshinov <boyarsh@altlinux.ru> 5.0-alt1
- joined tzone and datetime 

* Fri Jan 23 2009 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.3-alt1
- updated for sisyphus installer state 

* Wed Nov 05 2008 Alexandra Panyukova <mex3@altlinux.ru> 0.2-alt5.M41
- Version for M41
- sysconfig step added

* Fri Dec 14 2007 Grigory Batalov <bga@altlinux.ru> 0.2-alt4
- Xinetd hook to disable localhost-only access.
- Check alterator-firewall backend presence before call.

* Mon Nov 19 2007 Grigory Batalov <bga@altlinux.ru> 0.2-alt3
- Alterator-ulogd hook.

* Mon Nov 19 2007 Grigory Batalov <bga@altlinux.ru> 0.2-alt2
- Use $destdir in postinstall hooks.

* Wed Oct 10 2007 Grigory Batalov <bga@altlinux.ru> 0.2-alt1
- Merge installer-hpc-0.2-alt2.
- Add translations.
- Alterator-iptables hook.
- Carry finish step (finish.scm).

* Sat Sep 08 2007 Grigory Batalov <bga@altlinux.ru> 0.1-alt1
- Initial build based on installer-hpc.

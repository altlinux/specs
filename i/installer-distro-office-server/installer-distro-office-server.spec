Name: installer-distro-office-server
Version: 5.0
Release: alt28
Packager: Dmitry V. Levin <ldv@altlinux.org>

Summary: Installer files for office server
License: GPL
Group: System/Configuration/Other
BuildArch: noarch

Source: %name-%version.tar

%description
Installer files for office server.

%package stage2
Summary: Installer stage2
License: GPL
Group: System/Configuration/Other
Provides: installer-office-server-stage2 = %version-%release
Requires: installer-stage2
#modules
Requires: alterator-sysconfig
Requires: alterator-datetime
Requires: alterator-pkg
Requires: alterator-vm
Requires: alterator-notes
Requires: installer-feature-vm-ofs-stage2
Requires: installer-feature-net-br-stage2
Requires: installer-feature-quota-stage2 >= 0.4
Requires: installer-feature-server-raid-fixup-stage2
Requires: installer-feature-restore-stage2
Requires: x-cursor-theme-jimmac

%description stage2
Installer office server stage2.

%package stage3
Summary: Installer stage3
License: GPL
Group: System/Configuration/Other
Provides: installer-office-server-stage3 = %version-%release
Requires: installer-stage3
#modules
Requires: alterator-lilo
Requires: alterator-office-server
Requires: alterator-net-eth
Requires: installer-feature-nfs-server-stage3
Requires: installer-feature-powerbutton-stage3
Requires: installer-feature-vm-ofs-stage3

%description stage3
Installer office server stage3.

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
* Thu Nov 19 2009 Stanislav Ievlev <inger@altlinux.org> 5.0-alt28
- add hook for initial ldap setup (moved from alterator-openldap package)

* Mon Oct 26 2009 Vitaly Kuznetsov <vitty@altlinux.ru> 5.0-alt27
- add httpd2 to services

* Fri Sep 11 2009 Vitaly Kuznetsov <vitty@altlinux.ru> 5.0-alt26
- move bind to module-expert-list

* Mon Sep 07 2009 Vitaly Kuznetsov <vitty@altlinux.ru> 5.0-alt25
- add bind to module-skip-list

* Wed Sep 02 2009 Vitaly Kuznetsov <vitty@altlinux.ru> 5.0-alt24
- add spamd

* Thu Aug 27 2009 Vitaly Kuznetsov <vitty@altlinux.ru> 5.0-alt23
- add "system restore" feature

* Thu Aug 20 2009 Vitaly Kuznetsov <vitty@altlinux.ru> 5.0-alt22
- move sslkey to expert list

* Wed Aug 19 2009 Vitaly Kuznetsov <vitty@altlinux.ru> 5.0-alt21
- skip net-domain

* Mon Aug 17 2009 Vitaly Kuznetsov <vitty@altlinux.ru> 5.0-alt20
- move net-tc to expert list

* Wed Aug 12 2009 Vitaly Kuznetsov <vitty@altlinux.ru> 5.0-alt19
- Add net-tc to module-skip-list

* Mon Jun 29 2009 Dmitry V. Levin <ldv@altlinux.org> 5.0-alt18
- 99-services.sh: Added slapd to rc5 (closes: #20598).

* Tue Jun 16 2009 Dmitry V. Levin <ldv@altlinux.org> 5.0-alt17
- stage2: Added installer-feature-server-raid-fixup-stage2.

* Mon Jun 15 2009 Dmitry V. Levin <ldv@altlinux.org> 5.0-alt16
- stage2: Reintroduced quota support.
- Fixed versioned provides.

* Mon Jun 01 2009 Dmitry V. Levin <ldv@altlinux.org> 5.0-alt15
- 99-services.sh: Added arpwatch to rc3.

* Mon Jun 01 2009 Dmitry V. Levin <ldv@altlinux.org> 5.0-alt14
- 99-services.sh: Fixed enabling disabled services.

* Sun May 31 2009 Dmitry V. Levin <ldv@altlinux.org> 5.0-alt13
- postinstall.d/99-services.sh: Disable openvpn service (closes: #19810).

* Thu May 28 2009 Dmitry V. Levin <ldv@altlinux.org> 5.0-alt12
- postinstall.d/99-services.sh: Enforce ahttpd and ahttpd-firsttime.

* Thu May 28 2009 Dmitry V. Levin <ldv@altlinux.org> 5.0-alt11
- stage2: Removed quota support for a while (closes: #20196).

* Wed May 27 2009 Dmitry V. Levin <ldv@altlinux.org> 5.0-alt10
- Resurrected contents of postinstall.d/10-alteratord.sh hook
  which was lost in previous build.

* Tue May 26 2009 Dmitry V. Levin <ldv@altlinux.org> 5.0-alt9
- Added installer-feature-quota-stage2 to stage2.
- Hardcoded list of services executed by default.

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

Name: installer-distro-chainmail
Version: 3.0.0
Release: alt2

Summary: Installer files for IVK chainmail
License: GPL
Group: System/Configuration/Other
BuildArch: noarch

Source: %name-%version.tar

%description
Installer files for IVK chainmail

%package stage2
Summary: Installer stage2
License: GPL
Group: System/Configuration/Other
Provides: installer-chainmail-stage2 = %version-%release
Requires: installer-common-stage2
#modules
Requires: alterator-sysconfig
Requires: alterator-datetime
Requires: alterator-pkg
Requires: alterator-vm
Requires: alterator-notes
Requires: installer-feature-quota-stage2 >= 0.4
Requires: installer-feature-server-raid-fixup-stage2
Requires: x-cursor-theme-jimmac
Requires: udev-rule-generator-net
Requires: installer-step-chainmail-domain

%description stage2
Installer IVK chainmail stage2.

%package stage3
Summary: Installer stage3
License: GPL
Group: System/Configuration/Other
Provides: installer-chainmail-stage3 = %version-%release
Requires: installer-common-stage3
#modules
Requires: alterator-grub
Requires: alterator-distro-chainmail >= 2.96.1-alt1
Requires: alterator-net-eth
Requires: installer-feature-vm-ofs-stage3
Requires: alterator-auth

%description stage3
Installer IVK chainmail stage3.

%prep
%setup

%install
%define install2dir %_datadir/install2
mkdir -p %buildroot%install2dir
cp -a * %buildroot%install2dir/

%files stage2
%install2dir/alterator-menu
%install2dir/alterator-ldap-groups
%install2dir/installer-steps
%install2dir/services-*
%install2dir/postinstall.d/01-remove-installer-office-server-pkgs.sh
%install2dir/initinstall.d/*.sh

%files stage3
%install2dir/preinstall.d/*.sh
%install2dir/postinstall.d/*.sh
%exclude %install2dir/postinstall.d/01-remove-installer-office-server-pkgs.sh
%install2dir/webapps-css/
%install2dir/alterator-hotstandby/
%install2dir/osec-onboot.init
%install2dir/ivk-scripts/

%changelog
* Tue Feb 10 2015 Mikhail Efremov <sem@altlinux.org> 3.0.0-alt2
- menu: Hide 'pkg-sources' and 'updates' modules.
- Use our own footer for BASE.
- Update ivk-scripts.
- Add and install ivk-scripts.
- Update module-order-list.
- menu: Move 'firewall' and 'snort' sections to the top.
- Enable rpcbind by default.

* Fri Jan 30 2015 Mikhail Efremov <sem@altlinux.org> 3.0.0-alt1
- Add osec-onboot service.
- Use 'chainmail' workflow again.
- Add 70-fail2ban-log.sh postinstall script.
- Enable indexhtml for HTTPS server.
- Rename 80-BASE-enable.sh to 80-nginx-webapps.sh.
- Drop ahttpd.sh hook.
- BASE-enable.sh: Don't replace nginx-webapps certificate.
- BASE-enable.sh: Enable HTTPS server for BASE (and Zabbix).
- Update default.css (Zabbix css).
- Update base_style.css.
- Add services.list for alterator-hotstandby.
- Replace css files from BASE and zabbix-phpfrontend-engine packages.
- Don't enable Samba during ALT domain creation.
- Enable alterator-osec by default.
- Setup local exclude-user file with additional /var.
- Add bacula hook: Only backup /etc directory by default.
- Disable arpwatch.
- Disable vsftpd service by default.
- Disable smb and nmb services by default.
- Drop installer-feature-net-br-stage2 from requires.
- Use our own vm-profile.

* Tue Oct 14 2014 Mikhail Efremov <sem@altlinux.org> 2.99.1-alt1
- Disable some services.
- Add net-iptables-off preinstall hook.
- Add 'Domain' step.
- Disable IPv6 by the kernel command line.
- Minor spec cleanup.
- Add 50-disable-ddos-deflate.sh postinstall hook.
- vsftpd hook: Set local_root to /home.

* Wed Sep 17 2014 Mikhail Efremov <sem@altlinux.org> 2.99.0-alt1
- Add udev-rule-generator-net in stage2.

* Wed Aug 20 2014 Mikhail Efremov <sem@altlinux.org> 2.97.0-alt1
- Add 80-BASE-enable.sh postinstall hook.
- Enable zabbix_mysql by default.
- Add 50-dovecot-no-ipv6.sh postinstall hook.
- Disable bacula-* services by default.
- Enable anacron by default.
- Disable plymouth.
- services-on: Replace httpd2 with nginx.
- Add 50-blacklist-ipv6.sh preinstall hook.
- Disable drweb services by default.
- Disable sc service by default.
- alterator menu: Hide alterator-grub.
- remove-* postinstall hook: Drop alterator-lilo.
- Add init-mysqld preinstall hook.

* Tue Jul 01 2014 Mikhail Efremov <sem@altlinux.org> 2.96.1-alt1
- Drop 20-openldap.sh postinstall hook.
- alterator menu: Don't hide net-domain.
- Change default vsftpd settings (by Stanislav Ievlev).
- Disable bridge service.

* Fri Jun 20 2014 Mikhail Efremov <sem@altlinux.org> 2.96.0-alt1
- Add services-off list.
- Replace services hook with services-on list.
- Drop bacula-select.
- Replace lilo with grub.
- Add alterator-auth to requires.
- steps: Add users-root.
- services hook: Update services list and drop firsttime.

* Tue Dec 14 2010 Mikhail Efremov <sem@altlinux.org> 2.1-alt4
- enable 'updates' menu item.
- enable 'services' menu item.

* Fri Dec 11 2009 Vladislav Zavjalov <slazav@altlinux.org> 2.1-alt3
- alterator-menu: add firewall group, fix order-list

* Thu Nov 19 2009 Stanislav Ievlev <inger@altlinux.org> 2.1-alt2
- add hook for initial ldap setup (moved from alterator-openldap package)

* Wed Nov 18 2009 Stanislav Ievlev <inger@altlinux.org> 2.1-alt1
- update for newest version of alterator-distro-chainmail

* Fri Nov 06 2009 Mikhail Efremov <sem@altlinux.org> 2.0-alt11
- fix requires.
- fix wrong dependency on installer-common-stage2 in stage3
  subpackage.

* Thu Nov 05 2009 Mikhail Efremov <sem@altlinux.org> 2.0-alt10
- move postinstall scripts to stage3
    (except 01-remove-installer-office-server-pkgs.sh).

* Wed Oct 21 2009 Stanislav Ievlev <inger@altlinux.org> 2.0-alt9
- add snortd and mysqld services

* Wed Sep 30 2009 Mikhail Efremov <sem@altlinux.org> 2.0-alt8
- rename 99-services.sh to 95-services.sh.

* Fri Sep 11 2009 Stanislav Ievlev <inger@altlinux.org> 2.0-alt7
- enable 'quota' module

* Fri Sep 04 2009 Stanislav Ievlev <inger@altlinux.org> 2.0-alt6
- 90-services.sh: add dovecot

* Wed Sep 02 2009 Stanislav Ievlev <inger@altlinux.org> 2.0-alt5
- add default ldap groups
- add spamd service
- move httpd2 to common service list

* Thu Aug 27 2009 Stanislav Ievlev <inger@altlinux.org> 2.0-alt4
- enable ulogd service
- hide alterator-updates

* Wed Aug 26 2009 Stanislav Ievlev <inger@altlinux.org> 2.0-alt3
- add branch for "system restore".

* Mon Aug 24 2009 Stanislav Ievlev <inger@altlinux.org> 2.0-alt2
- 99-services.sh postinstall.d script:
   * remove  cups, kvm, libvirtd, vz
   * add httpd2

* Wed Aug 19 2009 Stanislav Ievlev <inger@altlinux.org> 2.0-alt1
- Initial build

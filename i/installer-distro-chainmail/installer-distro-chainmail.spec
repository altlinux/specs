Name: installer-distro-chainmail
Version: 2.1
Release: alt3

Packager: Stanislav Ievlev <inger@altlinux.org>

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
Requires: installer-feature-vm-ofs-stage2
Requires: installer-feature-net-br-stage2
Requires: installer-feature-quota-stage2 >= 0.4
Requires: installer-feature-server-raid-fixup-stage2
Requires: installer-feature-restore-stage2
Requires: x-cursor-theme-jimmac

%description stage2
Installer IVK chainmail stage2.

%package stage3
Summary: Installer stage3
License: GPL
Group: System/Configuration/Other
Provides: installer-chainmail-stage3 = %version-%release
Requires: installer-common-stage3
#modules
Requires: alterator-lilo
Requires: alterator-distro-chainmail >= 2.1-alt1
Requires: alterator-net-eth
Requires: installer-feature-vm-ofs-stage3

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
%install2dir/postinstall.d/01-remove-installer-office-server-pkgs.sh

%files stage3
%install2dir/postinstall.d/20-alterator-defaults.sh
%install2dir/postinstall.d/30-ahttpd.sh
%install2dir/postinstall.d/95-services.sh
%install2dir/postinstall.d/20-openldap.sh

%changelog
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

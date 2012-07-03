Name:		sisyphus-updates
Version:	0.1
Release:	alt7.1
Packager:       Stanislav Ievlev <inger@altlinux.org>

Summary:	Simple system updater
License:	GPL
Group:		System/Configuration/Other

Requires: apt

Conflicts: apt-conf-branch < 5.0-alt3
Conflicts: apt-conf-sisyphus < 5.0-alt4
Conflicts: apt-conf-desktop < 5.0-alt3

BuildArch: noarch

Source1: sisyphus-updates
Source2: sisyphus-updates.conf

%description
This is a simple wrapper over apt-get to perform update and dist-upgrade operations.
Utility works with usage of high level databases on mirrors and repositories from apt-conf package.

%install
install -Dpm 755 %SOURCE1 %buildroot%_sbindir/%name
install -Dpm 644 %SOURCE2 %buildroot%_sysconfdir/%name/%name.conf
install -dpm 755 %buildroot%_localstatedir/%name

%files
%config(noreplace) %_sysconfdir/%name
%_sbindir/%name
%_localstatedir/%name

%changelog
* Wed Oct 07 2009 Alexey I. Froloff <raorn@altlinux.org> 0.1-alt7.1
- NMU:
  + in local mode also browse DNS-SD services in all available domains

* Thu Mar 19 2009 Stanislav Ievlev <inger@altlinux.org> 0.1-alt7
- process txt records in more secure way

* Tue Mar 17 2009 Stanislav Ievlev <inger@altlinux.org> 0.1-alt6
- require apt

* Tue Feb 24 2009 Stanislav Ievlev <inger@altlinux.org> 0.1-alt5
- merge special apt.conf with system apt.conf

* Thu Feb 19 2009 Stanislav Ievlev <inger@altlinux.org> 0.1-alt4
- change behavior in local mode: update only from repository specified in repolist
- made package noarch

* Fri Feb 13 2009 Stanislav Ievlev <inger@altlinux.org> 0.1-alt3
- add support for avahi

* Mon Feb 09 2009 Stanislav Ievlev <inger@altlinux.org> 0.1-alt2
- clean cache after dist-upgrade

* Wed Feb 04 2009 Stanislav Ievlev <inger@altlinux.org> 0.1-alt1
- Initial build

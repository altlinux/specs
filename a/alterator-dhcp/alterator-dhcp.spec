%define _altdata_dir %_datadir/alterator

Name: alterator-dhcp
Version: 0.8
Release: alt2.1

Summary: alterator module for dhcp conf file editing
License: GPL
Group: System/Configuration/Other
Url: http://wiki.sisyphus.ru/Alterator

Source: %name-%version.tar

BuildArch: noarch

Requires: alterator >= 4.10-alt1 alterator-sh-functions alterator-net-functions >= 1.0-alt3
Requires: alterator-l10n >= 2.1-alt11
Requires: dhcp-server
Requires: alterator-services
Conflicts: alterator-fbi < 5.17-alt2

BuildPreReq: alterator >= 4.10-alt1

# Automatically added by buildreq on Mon Jul 11 2005 (-bi)
BuildRequires: alterator

%description
DHCP configuration alterator module

%prep
%setup -q

%build
%make_build

%install
%makeinstall

%files
%_bindir/*
%config(noreplace) %_sysconfdir/alterator/dhcp
%_altdata_dir/applications/*
%_altdata_dir/ui/*
%_altdata_dir/type/*
%_alterator_backend3dir/*
%_libexecdir/alterator/hooks/net-eth.d/*
%_libexecdir/alterator/hooks/dhcp.d

%changelog
* Mon Mar 28 2011 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.8-alt2.1
- lost changes from previous release

* Mon Mar 28 2011 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.8-alt2
- don't use ddns if SERVER_ROLE not master

* Tue Apr 20 2010 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.8-alt1
- make it usable without ddns

* Fri Sep 04 2009 Stanislav Ievlev <inger@altlinux.org> 0.7-alt3
- improve address range check (use modern functions from alterator-net-functions)
- add postinstall hook
- backend: use run_localized() to write local date

* Tue Aug 18 2009 Stanislav Ievlev <inger@altlinux.org> 0.7-alt2
- update dhcp config before server start (closes: #21095)

* Thu Jul 30 2009 Stanislav Ievlev <inger@altlinux.org> 0.7-alt1
- ui: use workflow 'none'
- dhcp backend:
  * update daemon status only in 'general' section.
  * don't allow rename if ip address is empty

* Tue Apr 28 2009 Stanislav Ievlev <inger@altlinux.org> 0.6-alt4
- improve static binding (add cleanup of dhcp leases)

* Wed Apr 22 2009 Stanislav Ievlev <inger@altlinux.org> 0.6-alt3
- introduce `altlinux' option space (sbolshakov@)
- call kdc hook if exists during per-host dhcp option create (sbolshakov@)

* Fri Apr 17 2009 Stanislav Ievlev <inger@altlinux.org> 0.6-alt2
- start daemon after config update

* Tue Apr 14 2009 Stanislav Ievlev <inger@altlinux.org> 0.6-alt1
- move type definition to more convenient place

* Fri Mar 27 2009 Stanislav Ievlev <inger@altlinux.org> 0.5-alt4
- start/stop service directly in module interface
- improve external interface (alterator-dhcp-functions)

* Wed Mar 18 2009 Stanislav Ievlev <inger@altlinux.org> 0.5-alt3
- more integration with ddns

* Thu Mar 12 2009 Stanislav Ievlev <inger@altlinux.org> 0.5-alt2
- add checking for reserved names

* Tue Mar 10 2009 Stanislav Ievlev <inger@altlinux.org> 0.5-alt1
- add support for ddns

* Thu Mar 05 2009 Stanislav Ievlev <inger@altlinux.org> 0.4-alt2
- add support for pxe

* Fri Jan 30 2009 Stanislav Ievlev <inger@altlinux.org> 0.4-alt1
- add support for "ntp-servers"

* Tue Jan 27 2009 Vladislav Zavjalov <slazav@altlinux.org> 0.3-alt6
- move help and translations to alterator-l10n

* Tue Dec 09 2008 Vladislav Zavjalov <slazav@altlinux.org> 0.3-alt5
- rebuild with new l10n (fixed help)

* Fri Dec 05 2008 Vladislav Zavjalov <slazav@altlinux.org> 0.3-alt4
- rebuild with new l10n

* Mon Nov 17 2008 Vladislav Zavjalov <slazav@altlinux.org> 0.3-alt3
- remove old css include
- show warning if no statically configured interfaces found

* Thu Oct 23 2008 Stanislav Ievlev <inger@altlinux.org> 0.3-alt2
- join to common translation database

* Thu Oct 23 2008 Stanislav Ievlev <inger@altlinux.org> 0.3-alt1
- redesign backend and ui

* Fri Aug 22 2008 Stanislav Ievlev <inger@altlinux.org> 0.2-alt1
- remove template-*
- move design to standard place
- use module.mak

* Tue Jun 17 2008 Grigory Batalov <bga@altlinux.ru> 0.1-alt9
- Require alterator-services instead of alterator-chkconfig.

* Fri Jun 06 2008 Grigory Batalov <bga@altlinux.ru> 0.1-alt8
- Replace label tag with a translation on the help page.

* Wed May 28 2008 Grigory Batalov <bga@altlinux.ru> 0.1-alt6.M41.1
- Service restart link update.
- Hide service restart link on subnet configuration page.
- Russian translation update.

* Wed May 28 2008 Grigory Batalov <bga@altlinux.ru> 0.1-alt5.M41.1
- Change help paths to the new style (slazav@).
- Backport to branch 4.1.

* Thu May 15 2008 Grigory Batalov <bga@altlinux.ru> 0.1-alt4.M40.1
- Backport to branch 4.0.

* Fri Feb 15 2008 Grigory Batalov <bga@altlinux.ru> 0.1-alt4
- Set more restrictions on subnet parameters.

* Thu Dec 13 2007 Grigory Batalov <bga@altlinux.ru> 0.1-alt3
- Use dash in "DHCP server", "IP address" and "MAC address" translation.
- Russian help page.
- Add missing "ddns-update-style" to the config.
- Fix empty subnet deletion.

* Mon Jul 09 2007 Grigory Batalov <bga@altlinux.ru> 0.1-alt2
- Switch to new menu system.

* Thu Jun 07 2007 Grigory Batalov <bga@altlinux.ru> 0.1-alt1
- Specfile cleanup.
- Backend rewritten in Awk.

* Sun Apr 1 2007 Bogomolov Alex <lekseich@altlinux> 0.0-alt0
- Initial release

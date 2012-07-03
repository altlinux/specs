%define _altdata_dir %_datadir/alterator

Name: alterator-bind
Version: 0.7
Release: alt7

Source:%name-%version.tar

Provides: alterator-ddns = %version
Obsoletes: alterator-ddns

Summary: alterator module to create and manage dynamic dns
License: GPL
Group: System/Configuration/Other
Requires: bind bind-utils
Requires: alterator-net-common >= 0.6-alt1
Requires: alterator-dhcp >= 0.5-alt4 alterator >= 4.8-alt1
Requires: alterator-l10n >= 2.8-alt2

Conflicts: alterator-fbi < 5.25-alt2

BuildPreReq: alterator

BuildArch: noarch

%description
alterator module to create and manage dynamic dns

%prep
%setup -q

%build
%make_build

%install
%makeinstall

%files
%_bindir/*
%_sbindir/*
%_altdata_dir/ui/*/
%_altdata_dir/applications/*
%_alterator_backend3dir/*
%_sysconfdir/hooks/hostname.d/*
%_libexecdir/alterator/hooks/net-eth.d/*
%_libexecdir/alterator/hooks/net-domain.d/*
%_libexecdir/alterator/hooks/dhcp.d/*

%changelog
* Thu Mar 31 2011 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.7-alt7
- gracefull zones deletion

* Thu Mar 31 2011 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.7-alt6
- serials are unix timestamps now (fix problems with recreation)

* Wed Mar 30 2011 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.7-alt5
- fix rzone ownership

* Tue Mar 29 2011 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.7-alt4
- restart bind on IP change

* Fri Mar 25 2011 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.7-alt3
- always run dhcp-hostname-hook

* Thu Nov 05 2009 Stanislav Ievlev <inger@altlinux.org> 0.7-alt2
- show hosts for slave zones too

* Mon Nov 02 2009 Stanislav Ievlev <inger@altlinux.org> 0.7-alt1
- support both master and slave zones

* Tue Oct 06 2009 Stanislav Ievlev <inger@altlinux.org> 0.6-alt1
- add ability to edit MX and NS records,
- allow to add to forward zone ip address not from zone's network

* Thu Sep 10 2009 Stanislav Ievlev <inger@altlinux.org> 0.5-alt1
- add support for multiple domains

* Fri Sep 04 2009 Stanislav Ievlev <inger@altlinux.org> 0.4-alt1
- increase version (was conflict with old package in branch4.1)

* Wed Sep 02 2009 Stanislav Ievlev <inger@altlinux.org> 0.3-alt1
- redesign library
- rename package, add interface to manipulate networks of dynamic ddns

* Tue Apr 28 2009 Stanislav Ievlev <inger@altlinux.org> 0.2-alt9
- @sbolshakov:
    * do not expose surrogate `kdc' A record, SRV is enough
    * use real hostname for kerberos SRV records, not surrogate `ns'
    * typo fixed for kerberos SRV records

* Tue Apr 21 2009 Stanislav Ievlev <inger@altlinux.org> 0.2-alt8
- resolve ip to single name

* Wed Apr 01 2009 Stanislav Ievlev <inger@altlinux.org> 0.2-alt7
- improve hooks
- update for new alterator

* Mon Mar 30 2009 Stanislav Ievlev <inger@altlinux.org> 0.2-alt6
- recreate resolvconf zones if need it

* Fri Mar 27 2009 Stanislav Ievlev <inger@altlinux.org> 0.2-alt5
- use modern alterator-dhcp interface

* Mon Mar 23 2009 Stanislav Ievlev <inger@altlinux.org> 0.2-alt4
- @sbolshakov: generate SRV records for kerberos

* Fri Mar 20 2009 Stanislav Ievlev <inger@altlinux.org> 0.2-alt3
- fix typo in script

* Thu Mar 19 2009 Stanislav Ievlev <inger@altlinux.org> 0.2-alt2
- turn off resolv.conf.d hook (unexpected dhcpd shutdown if interface is turned off)
- fix exit code of dhcp-update-config utility

* Wed Mar 18 2009 Stanislav Ievlev <inger@altlinux.org> 0.2-alt1
- redesign hook system, add hooks for dhcp

* Fri Mar 13 2009 Stanislav Ievlev <inger@altlinux.org> 0.1-alt5
- run reconfiguration hooks only in master mode

* Thu Mar 12 2009 Stanislav Ievlev <inger@altlinux.org> 0.1-alt4
- add utility to check for reserved names

* Wed Mar 11 2009 Stanislav Ievlev <inger@altlinux.org> 0.1-alt3
- use more smart hooks

* Tue Mar 10 2009 Stanislav Ievlev <inger@altlinux.org> 0.1-alt2
- add ddns-print-dhcp utility
- improve ddns-add-host and ddns-del-host

* Thu Mar 05 2009 Stanislav Ievlev <inger@altlinux.org> 0.1-alt1
- Initial build


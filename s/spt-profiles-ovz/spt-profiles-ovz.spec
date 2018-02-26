Name: spt-profiles-ovz
Version: 0.2.2
Release: alt1

AutoReq: yes, noshell

Summary: spt profiles for building OpenVZ VE containers
License: GPL
Group: Development/Other

Source: profiles-%version.tar
Packager: L.A. Kostis <lakostis@altlinux.org>
BuildArch: noarch

%description
This package contains spt profiles for building OpenVZ isolated containers
used for creating appliances.

%prep
%setup -n profiles-%version

%install
install -dm755 %buildroot%_sysconfdir/spt/profiles/ovz
cp -a * .default %buildroot%_sysconfdir/spt/profiles/ovz

%files
%dir %_sysconfdir/spt/profiles/ovz
%config(noreplace) %_sysconfdir/spt/profiles/ovz/*
%_sysconfdir/spt/profiles/ovz/.default

%changelog
* Tue Jan 29 2008 Michael Shigorin <mike@altlinux.org> 0.2.2-alt1
- oops, 0.2.1-alt1 was based on lakostis' 0.2-alt1 git repo
  while Sisyphus package was built from inger's 0.2-alt4
  => pulling changes upto 0.2-alt4

* Mon Jan 28 2008 Michael Shigorin <mike@altlinux.org> 0.2.1-alt1
- fix .default profile (#11310)

* Wed May 02 2007 Stanislav Ievlev <inger@altlinux.org> 0.2-alt4
- ntp-server profile: start ntpd service

* Mon Apr 16 2007 Stanislav Ievlev <inger@altlinux.org> 0.2-alt3
- fix requires

* Fri Apr 06 2007 Stanislav Ievlev <inger@altlinux.org> 0.2-alt2
- merge with bga@

* Fri Mar 30 2007 Konstantin A. Lepikhov <lakostis@altlinux.org> 0.2-alt1
- add new profiles:
  + pptp server (FIXME!)
  + openvpn server (FIXME!)
- add capabilites for ntp-server.
- remove 00resolv hook.

* Tue Mar 27 2007 Stanislav Ievlev <inger@altlinux.org> 0.1-alt3
- rename list-server to mailing-list-server

* Wed Mar 21 2007 Grigory Batalov <bga@altlinux.ru> 0.1-alt2
- add proxy and list server profiles

* Wed Mar 21 2007 Stanislav Ievlev <inger@altlinux.org> 0.1-alt1
- caching-nameserver,kerberos-server,
  smtp-server,
  imap-server,
  ftp-server, ntp-server: remove httpd2 stop from hook

* Wed Mar 14 2007 Stanislav Ievlev <inger@altlinux.org> 0.0.1-alt1
- add ftp server profile

* Tue Mar 13 2007 Stanislav Ievlev <inger@altlinux.org> 0.0.1-alt0.7
- add kerberos server profile
- change default output name and ostemplate parameter

* Mon Mar 05 2007 Stanislav Ievlev <inger@altlinux.org> 0.0.1-alt0.6
- add out-of-box settings: ntp,smtp,imap
- turn off second httpd2
- add default profile

* Fri Mar 02 2007 Stanislav Ievlev <inger@altlinux.org> 0.0.1-alt0.5
- add smtp server profile
- fix requires

* Thu Mar 01 2007 Stanislav Ievlev <inger@altlinux.org> 0.0.1-alt0.4
- more descriptive names for profiles
- use virtual package in cups profile

* Wed Feb 28 2007 Stanislav Ievlev <inger@altlinux.org> 0.0.1-alt0.3
- add print server profile

* Mon Feb 26 2007 Stanislav Ievlev <inger@altlinux.org> 0.0.1-alt0.2 
- add imap server profile

* Thu Feb 22 2007 L.A. Kostis <lakostis@altlinux.ru> 0.0.1-alt0.1
- initial release.



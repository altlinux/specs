# -*- mode: RPM-SPEC; tab-width: 8; fill-column: 70; -*- 

%define _altdata_dir %_datadir/alterator

Name: alterator-postfix-dovecot
Version: 0.7.1
Release: alt1

Summary: Alterator module for Postfix/Dovecot setup
License: GPL
Group: System/Configuration/Other

Source:%name-%version.tar

Requires: alterator >= 4.7-alt1 alterator-sh-functions >= 0.6-alt5
Requires: alterator-l10n >= 2.9-alt1
Requires: dovecot >= 2.0.0
Requires: alterator-service-functions >= 2.0.0
#Conflicts: alterator-fbi < 5.17-alt3
Conflicts: alterator-lookout < 1.6-alt3

Requires: postfix postfix-tls postfix-ldap postfix-dovecot dovecot sa-content-filter

BuildArch: noarch
#BuildPreReq: alterator >= 4.7-alt1

# Automatically added by buildreq on Mon Jul 11 2005 (-bi)
BuildRequires: alterator

%description
Alterator module for Postfix/Dovecot setup

%prep
%setup -q

%build
%make_build

%install
%makeinstall
%find_lang %name

%post
if [ "$1" -eq 1 ]; then
	%_libexecdir/alterator/hooks/net-domain.d/20-postfix-dovecot
	%_sysconfdir/hooks/hostname.d/22-postfix
	%_sysconfdir/hooks/hostname.d/23-dovecot
fi

%files -f %name.lang
%_bindir/%name-functions
%_datadir/alterator/applications/*
%_datadir/alterator/ui/*
%_alterator_backend3dir/*
%_datadir/%name
%_libexecdir/alterator/hooks/net-domain.d/*
%_sysconfdir/hooks/hostname.d/*
%_sysconfdir/control.d/facilities/*

%changelog
* Wed Oct 02 2013 Mikhail Efremov <sem@altlinux.org> 0.7.1-alt1
- hook-net-domain: Fix regexp.
- hook-net-domain: Silence grep output.
- Don't use 'vmail' user for root mail delivery.

* Wed Sep 18 2013 Mikhail Efremov <sem@altlinux.org> 0.7.0-alt1
- Requre ALT domain for work.
- Don't initialize configuration without domain (closes: #29349).
- Use alterator-service-functions.
- final version 0.6 (by Andrey Kolotov).
- drop installer-feature-mail-init-stage3 (by Andrey Kolotov).

* Fri Jul 26 2013 Andrey Kolotov <qwest@altlinux.ru> 0.6-alt1
- works with Dovecot 2.x.x through alterator.conf
- remove option smtpd_tls_auth_only, default yes
- SMTP on/off through control postfix server/local
- added SMTP submission on/off through control postfix-submission
- added requires for auth users through dovecot-ldap
- autocreate new user vmail

* Tue Sep 04 2012 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.5-alt1
- make it work if changing kerberos status without domain name change

* Tue Nov 02 2010 Anton Protopopov <aspsk@altlinux.org> 0.4-alt2
- Use IPv4 by default
- Don't hurt acc (ALT #24484)

* Thu Nov 19 2009 Stanislav Ievlev <inger@altlinux.org> 0.4-alt1
- move translations into alterator-l10n
- optimize postconf calls (this utility has broken locking logic)
- use workflow 'none'

* Fri Oct 30 2009 Grigory Batalov <bga@altlinux.ru> 0.3-alt6
- Add root mail alias setting (ALT #21358).

* Thu Sep 24 2009 Grigory Batalov <bga@altlinux.ru> 0.3-alt5
- Move local networks field up (ALT #21602).

* Wed Sep 23 2009 Stanislav Ievlev <inger@altlinux.org> 0.3-alt4
- use modern effect library

* Thu Sep 10 2009 Grigory Batalov <bga@altlinux.ru> 0.3-alt3
- Set Dovecot's mailbox location statically due to broken
  autodetection.

* Tue Sep 08 2009 Grigory Batalov <bga@altlinux.ru> 0.3-alt2
- Make sure dovecot and postfix are auto-started on boot (ALT #21452)
- Check also dovecot status on auth/pop3/imap option read (ALT #21381)
- Remove confusing Apply buttons (ALT #21467)

* Thu Sep 03 2009 Grigory Batalov <bga@altlinux.ru> 0.3-alt1
- No need to specify CA root file (ALT #21333).
- Split auth and pop3/imap startup (ALT #21330).
- Control spamd startup (ALT #21334).
- Fix local recipient maps template.

* Mon Aug 31 2009 Grigory Batalov <bga@altlinux.ru> 0.2-alt4
- Post-install script was added.
- Modern interface conceptions used (ALT #21260).

* Tue Aug 25 2009 Grigory Batalov <bga@altlinux.ru> 0.2-alt3
- Backend initialization was fixed.

* Tue Aug 25 2009 Grigory Batalov <bga@altlinux.ru> 0.2-alt2
- Requirements were updated.

* Tue Aug 25 2009 Grigory Batalov <bga@altlinux.ru> 0.2-alt1
- Hostname change hooks were added.

* Thu Aug 20 2009 Grigory Batalov <bga@altlinux.ru> 0.1-alt1
- Initial release

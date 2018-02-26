# -*- mode: RPM-SPEC; tab-width: 8; fill-column: 70; -*- 

%define _altdata_dir %_datadir/alterator

Name: alterator-postfix-dovecot
Version: 0.4
Release: alt2
Packager: Grigory Batalov <bga@altlinux.ru>

Summary: Alterator module for Postfix/Dovecot setup
License: GPL
Group: System/Configuration/Other

Source:%name-%version.tar

Requires: alterator >= 4.7-alt1 alterator-sh-functions >= 0.6-alt5
Requires: alterator-l10n >= 2.9-alt1
#Conflicts: alterator-fbi < 5.17-alt3
Conflicts: alterator-lookout < 1.6-alt3

Requires: postfix postfix-tls postfix-ldap postfix-dovecot dovecot sa-content-filter

BuildArch: noarch
#BuildPreReq: alterator >= 4.7-alt1

# Automatically added by buildreq on Mon Jul 11 2005 (-bi)
BuildRequires: alterator

%package -n installer-feature-mail-init-stage3
Summary: Postfix/Dovecot module setup
Group: System/Configuration/Other

%description -n installer-feature-mail-init-stage3
%summary

%description
Alterator module for Postfix/Dovecot setup

%prep
%setup -q

%build
%make_build

%install
%makeinstall
%find_lang %name

mkdir -p %buildroot%_datadir/install2/postinstall.d/
cat << EOF > %buildroot%_datadir/install2/postinstall.d/81-postfix-dovecot.sh
#!/bin/sh -efu

a= . install2-init-functions

exec_chroot alterator-cmdline /postfix-dovecot action init
exec_chroot chkconfig postfix on
exec_chroot chkconfig dovecot on
exec
EOF
chmod 755 %buildroot%_datadir/install2/postinstall.d/81-postfix-dovecot.sh

%files -f %name.lang
%_datadir/alterator/applications/*
%_datadir/alterator/ui/*
%_alterator_backend3dir/*
%_datadir/%name
%_sysconfdir/hooks/hostname.d/*

%files -n installer-feature-mail-init-stage3
%_datadir/install2/postinstall.d/*

%changelog
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

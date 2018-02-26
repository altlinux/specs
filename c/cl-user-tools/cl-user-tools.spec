Name: cl-user-tools
Version: 0.1
Release: alt8

Summary: tools to work with cluster users
Group: Development/Other
License: GPL

Source: %name-%version.tar

BuildArch: noarch

AutoReq: yes, noshell

Requires: coreutils libshell openssh

Packager: Stanislav Ievlev <inger@altlinux.org>

%description
tools to work with cluster users

%prep
%setup

%install
for i in scripts/*; do
%__install -Dpm755 $i %buildroot/%_sbindir/`basename $i`
done

%__install -d %buildroot%_sysconfdir
cp -a etc/* %buildroot%_sysconfdir

%files
%_sbindir/*
%attr(600,root,root) %config(noreplace) %_sysconfdir/*.conf

%changelog
* Mon Mar 03 2008 Stanislav Ievlev <inger@altlinux.org> 0.1-alt8
- build for Sisyphus
- add default host variable value

* Fri Feb 29 2008 Grigory Batalov <bga@altlinux.ru> 0.1-alt7
- adjust config file to pam_ldap.conf/nss_ldap.conf
- use transparent authentication
- cl-getent and cl-usermod scripts

* Thu Sep 20 2007 Stanislav Ievlev <inger@altlinux.org> 0.1-alt6
- use '-e' in scripts

* Tue Sep 18 2007 Stanislav Ievlev <inger@altlinux.org> 0.1-alt5
- rename cl-sshpasswd into cl-sshkeygen

* Wed Sep 12 2007 Stanislav Ievlev <inger@altlinux.org> 0.1-alt4
- generate ssh keys without passwords ( need for some cluster tools )

* Tue Sep 04 2007 Stanislav Ievlev <inger@altlinux.org> 0.1-alt3
- add utility to define ldap password, rename cl-passwd into cl-sshpasswd

* Mon Sep 03 2007 Stanislav Ievlev <inger@altlinux.org> 0.1-alt2
- move openldap initial setup into installer

* Fri Aug 31 2007 Stanislav Ievlev <inger@altlinux.org> 0.1-alt1
- Initial release

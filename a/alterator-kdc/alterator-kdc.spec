Name: alterator-kdc
Version: 0.3
Release: alt1

BuildArch: noarch

Source: %name-%version-%release.tar

Summary: Alterator module for Kerberos KDC
License: GPL
Group: System/Configuration/Other

Requires: krb5-kdc pwgen

%description
Alterator module for Kerberos KDC

%prep
%setup

%install
mkdir %buildroot
find etc usr |cpio -pmd %buildroot

%files
%_sysconfdir/hooks/hostname.d/30-kdc
%_sysconfdir/hooks/hostname.d/40-keytab
%_bindir/alterator-kdc-functions
%_bindir/alterator-kdc-princ-functions
%_bindir/alterator-kdc-dhcp-host-option
%_libexecdir/alterator/hooks/trust.d/*

%changelog
* Tue May 15 2012 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.3-alt1
- do full kdc reset if old and new domains are equal, but no krb base 
  for new domain

* Fri Mar 18 2011 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.2-alt9
- chkconfig krb5kdc added

* Wed Mar 16 2011 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.2-alt8
- improved error handling, no freeze if no ldapconf

* Wed Nov  4 2009 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.2-alt7
- modified to not expose extra reqs

* Fri Aug 21 2009 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.2-alt6
- place dovecot own keytab under /etc/dovecot #(21165)

* Fri Jun 26 2009 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.2-alt5
- place squid own keytab under /etc/squid

* Tue Jun 16 2009 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.2-alt4
- http principal autogeneration added

* Tue Apr 28 2009 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.2-alt3
- filter out unwanted messages during dhcpd.conf create (#19811)
- add imap/pop3/smtp to autogen'd princs too

* Wed Apr 22 2009 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.2-alt2
- use dedicated option space for alt-specific dhcp options

* Tue Apr 21 2009 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.2-alt1
- hook into dhcp-reset added

* Fri Apr 10 2009 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.1-alt3
- samba hooks added

* Tue Apr  7 2009 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.1-alt2
- keytab hook added

* Fri Mar 20 2009 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.1-alt1
- Initial release

%define _ldapconfdir %_sysconfdir/openldap
%define _hooksdir %_sysconfdir/hooks/hostname.d

Name: ldap-user-tools
Version: 0.6
Release: alt4

Summary: tools to work with ldap users
Group: Development/Other
License: GPL


Source: %name-%version.tar

BuildArch: noarch
# HEREDOC code
Requires: ruby(ldap) ruby(ldap/ldif) openldap-servers perl-Crypt-SmbHash alterator-kdc
Requires: alterator-openldap-functions

%description
tools to work with ldap users

%prep
%setup

%install
for i in scripts/*; do
install -Dpm755 "$i" "%buildroot%_sbindir/${i##*/}"
done
install -Dpm640 data/slapd-template.conf %buildroot/%_ldapconfdir/slapd-template.conf
install -Dpm444 schema/kerberos.schema %buildroot/%_ldapconfdir/schema/kerberos.schema
install -Dpm755 bin/mkntpasswd %buildroot/%_sbindir/mkntpasswd
install -Dpm755 hooks/ldap-domain %buildroot/%_hooksdir/21-ldap-domain
install -pm755 -d %buildroot/%_sysconfdir/alterator/openldap

%files
%_sbindir/ldap-*
%_sbindir/mkntpasswd
%_ldapconfdir/slapd-template.conf
%_ldapconfdir/schema/kerberos.schema
%_hooksdir/21-ldap-domain
%dir %_sysconfdir/alterator/openldap

%changelog
* Tue Jul 12 2011 Fr. Br. George <george@altlinux.ru> 0.6-alt4
- Fix "ldap-dn find" exit status and output bug

* Thu May 19 2011 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.6-alt3
- dependence to alterator-openldap removed

* Thu Mar 31 2011 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.6-alt2
- enable one-letter domain components

* Wed Mar 30 2011 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.6-alt1
- setup slapd to listen ldaps

* Thu Aug 20 2009 Lebedev Sergey <barabashka@altlinux.org> 0.5-alt1.2
- added previous fix (after merge with raorn, didn't add reverted commit)

* Wed Aug 19 2009 Lebedev Sergey <barabashka@altlinux.org> 0.5-alt1.1
- fixed ldap-passwd ldif

* Mon Aug 03 2009 Alexey I. Froloff <raorn@altlinux.org> 0.5-alt1
- Force input to be always UTF-8 (closes: #20942)

* Wed Jul 08 2009 Lebedev Sergey <barabashka@altlinux.org> 0.4-alt4
- added initial DB_CONFIG into database dir (for openldap 2.4.*)
- added actions
  + ldap-dn list
  + ldap-dn master

* Thu May 14 2009 Lebedev Sergey <barabashka@altlinux.org> 0.4-alt3.1
- fixed #19961

* Mon May 04 2009 Lebedev Sergey <barabashka@altlinux.org> 0.4-alt3
- added param (add, delete, replace) LDAP::MOD for ldap-usermod
- made krb functions silent (improved error reporting)

* Thu Apr 30 2009 Lebedev Sergey <barabashka@altlinux.org> 0.4-alt2
- removed info messages
- removed home and mail spool managing (creating and removing)

* Wed Apr 22 2009 Lebedev Sergey <barabashka@altlinux.org> 0.4-alt1
- now using alterator-openldap-functions
- code cleanup
- moved logic ldap-config to alterator-openldap-functions
- deleted ldap-proxyuser
- deleted ldap-sshkeygen
- added ldap-groupmod
- fixed #19808

* Mon Apr 20 2009 Lebedev Sergey <barabashka@altlinux.org> 0.3-alt4.1
- fixed typo

* Mon Apr 20 2009 Lebedev Sergey <barabashka@altlinux.org> 0.3-alt4
- hook renamed to ldap-domain
- enable_schema removed to alterator-openldap hook

* Thu Apr 02 2009 Lebedev Sergey <barabashka@altlinux.org> 0.3-alt3
- added kerberos.schema file
- added kerberos schema enabling in openldap hook

* Mon Mar 30 2009 Lebedev Sergey <barabashka@altlinux.org> 0.3-alt2
- rewrote ldap-init #19371 

* Mon Mar 23 2009 Lebedev Sergey <barabashka@altlinux.org> 0.3-alt1
- invoke supplemental kdc ops when applicable (by sbolshakov)

* Fri Mar 20 2009 Lebedev Sergey <barabashka@altlinux.org> 0.2-alt9
- fixed renaming dn 
- added support ou=kdcroot for kerberos

* Fri Mar 20 2009 Lebedev Sergey <barabashka@altlinux.org> 0.2-alt8
- fixed openldap hook (domain creation)
- added support for kdc (sbolshakov)

* Thu Mar 19 2009 Lebedev Sergey <barabashka@altlinux.org> 0.2-alt7
- moved openldap.hook to openldap
- added domain renaming into openldap hook
- added dn renaming into ldap-dn

* Tue Mar 17 2009 Lebedev Sergey <barabashka@altlinux.org> 0.2-alt6
- improved finding included conf files in slapd.conf

* Thu Mar 12 2009 Lebedev Sergey <barabashka@altlinux.org> 0.2-alt5.1
- fixed slapd restart and ldap-init

* Wed Mar 11 2009 Lebedev Sergey <barabashka@altlinux.org> 0.2-alt5
- added openldap.hook

* Fri Feb 27 2009 Lebedev Sergey <barabashka@altlinux.org> 0.2-alt4
- added mkntpasswd tool
- added Requires perl-Crypt-SmbHash
- added samba attributes support
- added find in ldap-dn
- added mail spool support

* Thu Feb 26 2009 Lebedev Sergey <barabashka@altlinux.org> 0.2-alt3.2
- renamed template.conf
- improved error messaging
- updated check_dn_name (ldap_dn)
- added get_slapd_status (ldap_dn)

* Wed Feb 25 2009 Lebedev Sergey <barabashka@altlinux.org> 0.2-alt3.1
- added template.conf for dn creation
- some coding style fixes

* Wed Feb 25 2009 Lebedev Sergey <barabashka@altlinux.org> 0.2-alt3
- added ldap-dn (dn manager)
- added support for different SLAPD_CONF
- changed localhost to 127.0.0.1

* Tue Feb 10 2009 Sir Raorn <raorn@altlinux.ru> 0.2-alt2
- Fix problem with ldap-passwd

* Fri Feb 06 2009 Sir Raorn <raorn@altlinux.ru> 0.2-alt1
- [0.2]
- ldap-getent:
 + use ruby-ldap for LDIF parsing
 + allow search key specification
 + allow search fields specification when searching "passwd" database
- ldap-passwd:
 + use blowfish for {CRYPT}'ed passwords
 + accept password as command-line argument
 + use ldap-usermod instead of direct ldapmodify call
- ldap-usermod:
 + use ruby-ldap for LDIF generation
 + accept unquoted "key:value" pairs on stdin
- ldap-useradd:
 + use ldap-getent when guessing gidNumber
- Spec cleanup

* Wed Feb 04 2009 Lebedev Sergey <barabashka@altlinux.org> 0.1-alt2.M50.2
- coding style fixes
- "binddn" type
- removed " from binddn,rootdn,bindpw,rootpw
- added  objectclasses in ldap-useradd:
  + person
	+ organizationalPerson
	+ inetOrgPerson
- removed objectclass in ldap-useradd:
  + account

* Wed Feb 04 2009 Lebedev Sergey <barabashka@altlinux.org> 0.1-alt2.M50.1
- first build for 5.0

* Mon Feb 02 2009 Lebedev Sergey <barabashka@altlinux.org> 0.1-alt2.M41.1
- fixed ldap-config

* Fri Jan 30 2009 Lebedev Sergey <barabashka@altlinux.org> 0.1-alt2.M41
- working version for alterator-ldap-auth alterator-ldap-users 

* Fri Jan 30 2009 Lebedev Sergey <barabashka@altlinux.org> 0.1-alt1.M41
- initial version based on cl-user-tools 

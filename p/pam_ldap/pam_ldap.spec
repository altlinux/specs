%add_findprov_lib_path /%_lib/security

Name: pam_ldap
Version: 186
Release: alt1

Summary: PAM module for LDAP
License: LGPL
Group: System/Base

Url: http://www.padl.com/

Source0: %url/download/%name-%version.tar.gz
Source1:%name-system_auth-alt

Patch0: %name-46-pam_console.patch
Patch1: %name-125-null.patch

Patch5: fixbuild.patch

Patch100: pam_ldap-180-debug_checkhost-gns.patch
Patch101: pam_ldap-182-debug_checkhost-st1.patch

Packager: Anton Gorlov <stalker@altlinux.ru>

# Automatically added by buildreq on Wed Aug 31 2005
BuildRequires: libldap-devel libpam-devel libsasl2-devel

Summary(ru_RU.KOI8-R): Модуль PAM для LDAP

%description
Pam_ldap is a module for Linux-PAM that supports password changes, V2
clients, Netscapes SSL, ypldapd, Netscape Directory Server password
policies, access authorization, crypted hashes, etc.

Install %name if you need to run LDAP access clients.

%description -l ru_RU.KOI8-R
pam_ldap - это модуль для Linux-PAM. Поддерживается изменение паролей,
протокол LDAP версии 2, Netscapes SSL, ypldapd, политики паролей
Netscape Directory Server, авторизация доступа, шифрованные хеши и т.д.

%prep
%setup
%patch0 -p1
##patch1 -p1
#patch5 -p1

%patch101 -p0

### We create example dir for place here examples for ALT Linux
mkdir alt-examples
install -pm644 %SOURCE1 alt-examples/system_auth

%build
%autoreconf
%configure \
	--with-ldap-lib=openldap \
	--with-ldap-conf-file=%_sysconfdir/pam_ldap.conf \
	--with-ldap-secret-file=%_sysconfdir/pam_ldap.secret \
	--libdir=/%_lib
	
%make_build

%check
%make check

%install
mkdir -p %buildroot{%_sysconfdir,/%_lib,%_libdir}

# Install the nsswitch module.
install -pDm755 pam_ldap.so %buildroot/%_lib/security/pam_ldap.so
# Install the default configuration file, but change the search bases to
# something generic.
sed -e 's/dc=padl/dc=example/g' ldap.conf >%buildroot%_sysconfdir/pam_ldap.conf
sed -i 's/#timelimit 30/timelimit 5/g' %buildroot%_sysconfdir/pam_ldap.conf
sed -i 's/#bind_timelimit 30/bind_timelimit 5/g' %buildroot%_sysconfdir/pam_ldap.conf
chmod 644 %buildroot%_sysconfdir/pam_ldap.conf
rm -f %buildroot%_sysconfdir/nsswitch.ldap
rm -f %buildroot%_sysconfdir/ldap.conf

%files
/%_lib/security/*
### This file is different from nss_ldap package! It's in TODO for next release
%config(noreplace) %_sysconfdir/pam_ldap.conf
%doc AUTHORS ChangeLog README pam.d ldap.conf
%doc alt-examples

%changelog
* Sun Apr 22 2012 Michael Shigorin <mike@altlinux.org> 186-alt1
- updated to 186
- minor spec cleanup
- fixed source link
- introduced %%check section

* Fri Jan 29 2010 Anton Gorlov <stalker@altlinux.ru> 185-alt1
- updated to 185

* Mon Sep 07 2009 Anton Gorlov <stalker@altlinux.ru> 184-alt2
- rebuild with libldap2.4

* Fri Dec 14 2007 Anton Gorlov <stalker@altlinux.ru> 184-alt1
- New version

* Sun Apr 15 2007 Anton Gorlov <stalker@altlinux.ru> 182-alt2
- Fix #11420

* Wed Sep 06 2006 Anton Gorlov <stalker@altlinux.ru> 182-alt1
- New version

* Wed Aug 02 2006 Anton Gorlov <stalker@altlinux.ru> 180-alt5.2
- Fix build on x86_64

* Mon Jun 12 2006 ALT QA Team Robot <qa-robot@altlinux.org> 180-alt5.1
- Rebuilt with libldap-2.3.so.0.

* Wed Nov 23 2005 Nick S. Grechukh <gns@altlinux.org> 180-alt5
- new maintainer

* Thu Nov 03 2005 Nick S. Grechukh <gns@altlinux.org> 180-alt1.gns3
- print hostname when checkhostattr enabled, for debug

* Wed Nov 02 2005 Nick S. Grechukh <gns@altlinux.org> 180-alt1.gns1.debug
- rebuilt with debug enabled

* Wed Aug 31 2005 Serge A. Volkov <vserge at altlinux.ru> 180-alt1
- Update to new version 180

* Fri Dec 17 2004 Serge A. Volkov <vserge at altlinux.ru> 176-alt1
- Update to new version 176
- rename %_sysconfdir/ldap.conf to %_sysconfdir/pam_ldap.conf

* Sat Nov 13 2004 ALT QA Team Robot <qa-robot@altlinux.org> 175-alt1.1
- Rebuilt with openldap-2.2.18-alt3.

* Sat Oct 01 2004 Serge A. Volkov <vserge@altlinux.ru> 175-alt1
- Update to new version 175

* Thu Aug 19 2004 Serge A. Volkov <vserge@altlinux.ru> 171-alt1
- Update version

* Fri May 21 2004  Serge A. Volkov <vserge@altlinux.ru> 169-alt1
- Update to new version 169

* Wed Feb 18 2004  Serge A. Volkov <vserge@altlinux.ru> 167-alt1
- Update to new version

* Fri Feb 13 2004  Serge A. Volkov <vserge@altlinux.ru> 165-alt3
- Rebuild agains new openldap 2.1.26 and libsasl2 (libdb4.2 rebuild)

* Mon Dec 29 2003  Serge A. Volkov <vserge@altlinux.ru> 165-alt2
- Create in %%docdir alt-examples
- Add pam.d/system_auth example (%name-system_auth-alt)

* Sat Dec 13 2003  Serge A. Volkov <vserge@altlinux.ru> 165-alt1
- Update to new version 165

* Thu Sep 04 2003 Alexander Bokovoy <ab@altlinux.ru> 164-alt1
- Update to version 164
- Fixed:
  + MDKSA-2003:088

* Fri Jan 3 2003 Serge A. Volkov <vserge@altlinux.ru> 157-alt1
- Update to version 157

* Wed Oct 23 2002 Serge A. Volkov <vserge@altlinux.ru> 155-alt2
- Spec cleanup

* Thu Oct 17 2002 Serge A. Volkov <vserge@altlinux.ru> 155-alt1
- Update to new version

* Tue Aug 6 2002 Serge A. Volkov <vserge@altlinux.ru> 150-alt1
- Update to new version

* Sat Jun 1 2002 Serge A. Volkov <vserge@altlinux.ru> 148-alt1
- Update to new version

* Thu Apr 4 2002 Serge A. Volkov <vserge@altlinux.ru> 125-alt2
- Patch from Alexey Voinov

* Mon Sep 24 2001 Dmitry V. Levin <ldv@altlinux.ru> 125-alt1
- Split out from nss_lap.

* Wed Sep 05 2001 Volkov A. Serge <vserge@hotbox.ru> 172-alt1
- update to nss_ldap 172, pam_ldap 125
- update patch, becose it's applied in sources and Makefile is changed.

* Thu May 03 2001 Rider <rider@altlinux.ru> 150-alt1
- update to nss_ldap 150, pam_ldap 108

* Thu Feb 01 2001 Dmitry V. Levin <ldv@fandra.org> 139-ipl1
- RE adaptions.

* Fri Jan 19 2001 Nalin Dahyabhai <nalin@redhat.com>
- update to nss_ldap 139

* Mon Jan 15 2001 Nalin Dahyabhai <nalin@redhat.com>
- update to nss_ldap 138, which folds in our patch for initgroups
- change the default search base in ldap.conf to dc=example,dc=com

* Wed Jan 10 2001 Nalin Dahyabhai <nalin@redhat.com>
- update to nss_ldap 137 and pam_ldap 99
- try to not cause a segfault in _nss_ldap_initgroups

* Wed Jan  3 2001 Nalin Dahyabhai <nalin@redhat.com>
- update to nss_ldap 124 and pam_ldap 82

* Thu Dec 28 2000 Nalin Dahyabhai <nalin@redhat.com>
- add a requires: for nscd

* Thu Dec 14 2000 Nalin Dahyabhai <nalin@redhat.com>
- version the NSS module so that it works properly with programs which have
  been linked statically to a different version of an LDAP library, like
  Netscape Communicator

* Wed Dec  6 2000 Nalin Dahyabhai <nalin@redhat.com>
- BuildPrereq gdbm-devel
- pass RPM_OPT_FLAGS as CFLAGS to %%configure
- if protocol version is 2, explicitly set protocol version to 3 before trying
  to start TLS
- add STARTTLS support to nss_ldap
- work around a build-time problem on ia64

* Tue Dec  5 2000 Nalin Dahyabhai <nalin@redhat.com>
- BuildPrereq cyrus-sasl-devel instead of cyrus-sasl

* Mon Nov 20 2000 Nalin Dahyabhai <nalin@redhat.com>
- update to nss_ldap 123 and pam_ldap 82

* Fri Oct 27 2000 Nalin Dahyabhai <nalin@redhat.com>
- update to nss_ldap 122
- link statically with libsasl, require the first devel package that supplied it

* Thu Oct 19 2000 Nalin Dahyabhai <nalin@redhat.com>
- update to nss_ldap 120 and pam_ldap 77

* Wed Oct  4 2000 Nalin Dahyabhai <nalin@redhat.com>
- update to nss_ldap 116 and pam_ldap 74

* Fri Sep  7 2000 Nalin Dahyabhai <nalin@redhat.com>
- rebuild in new environment

* Thu Jul 27 2000 Nalin Dahyabhai <nalin@redhat.com>
- update to pam_ldap 67 to fix a bug in template user code
- convert symlink in /usr/lib to a relative one (#16132)

* Thu Jul 27 2000 Nalin Dahyabhai <nalin@redhat.com>
- update to nss_ldap 113 and pam_ldap 66

* Wed Jul 12 2000 Prospector <bugzilla@redhat.com>
- automatic rebuild

* Tue Jun 27 2000 Matt Wilson <msw@redhat.com>
- changed all the -,- in attr statements to root,root

* Tue Jun 27 2000 Nalin Dahyabhai <nalin@redhat.com>
- update pam_ldap to 63

* Wed May 31 2000 Nalin Dahyabhai <nalin@redhat.com>
- update pam_ldap to 56

* Tue May 30 2000 Nalin Dahyabhai <nalin@redhat.com>
- update pam_ldap to 55
- back out no-threads patch for pam_ldap, not needed any more

* Thu May 25 2000 Nalin Dahyabhai <nalin@redhat.com>
- update to 110
- revert prototype patch, looks like a problem with the new glibc after all

* Fri May 19 2000 Nalin Dahyabhai <nalin@redhat.com>
- get libpthread out of the NSS module
- fix prototype problems in getpwXXX()

* Mon May 15 2000 Nalin Dahyabhai <nalin@redhat.com>
- update to nss_ldap 109

* Sat Apr 29 2000 Nalin Dahyabhai <nalin@redhat.com>
- update pam_ldap 51

* Tue Apr 25 2000 Nalin Dahyabhai <nalin@redhat.com>
- update to nss_ldap 108 and pam_ldap 49

* Thu Apr 20 2000 Nalin Dahyabhai <nalin@redhat.com>
- update to pam_ldap 48

* Thu Mar 30 2000 Nalin Dahyabhai <nalin@redhat.com>
- update to nss_ldap 107
- note: check http://www.advogato.org/person/lukeh/ for Luke's changelog

* Tue Mar 21 2000 Nalin Dahyabhai <nalin@redhat.com>
- update to nss_ldap 106

* Wed Feb  9 2000 Nalin Dahyabhai <nalin@redhat.com>
- update to nss_ldap 105

* Mon Feb  7 2000 Nalin Dahyabhai <nalin@redhat.com>
- update to nss_ldap 104 and pam_ldap 46
- disable link against libpthread in pam_ldap

* Tue Feb  1 2000 Nalin Dahyabhai <nalin@redhat.com>
- remove migration tools, because this package requires openldap now, which
  also includes them

* Fri Jan 28 2000 Nalin Dahyabhai <nalin@redhat.com>
- update to nss_ldap 103

* Mon Jan 24 2000 Preston Brown <pbrown@redhat.com>
- fix typo in linuxconf-pair pam cfg file (#7800)

* Tue Jan 11 2000 Preston Brown <pbrown@redhat.com>
- v99, made it require pam_ldap
- added perl migration tools
- integrate pam_ldap stuff

* Fri Oct 22 1999 Bill Nottingham <notting@redhat.com>
- statically link ldap libraries (they're in /usr/lib)

* Tue Aug 10 1999 Cristian Gafton <gafton@redhat.com>
- use the ldap.conf file as an external source
- don't forcibly build the support for version 3
- imported the default spec file from the tarball and fixed it up for RH 6.1


%def_disable test
%def_disable debug
%def_disable krb

Name: nss_ldap
Version: 265
Release: alt2
Packager: Anton Gorlov <stalker@altlinux.ru>

Summary: NSS library for LDAP
Summary(ru_RU.KOI8-R): Библиотека NSS для LDAP
 
License: LGPL
Group: System/Base
Url: http://www.padl.com/

Source0: ftp://ftp.padl.com/pub/%name-%version.tar.gz
Source1: %name-README.ALT

Patch0: %name-226-configure.patch
Patch1: %name-172-null.patch
Patch2: %name-210-explode_rdn-alt.patch
Patch5: nss-fixbuild.patch

Patch10: libdir.fix
#Patch11: alt-saslauxprop.fix


Requires: nscd

# Automatically added by buildreq on Wed Aug 31 2005
BuildRequires: libkrb5-devel libldap-devel libsasl2-devel

%description
Nss_ldap is a set of C library extensions which allows X.500 and LDAP
directory servers to be used as a primary source of aliases, ethers,
groups, hosts, networks, protocol, users, RPCs, services and shadow
passwords (instead of or in addition to using flat files or NIS).

Install %name if you need to run LDAP access clients.

%description -l ru_RU.KOI8-R
Nss_ldap это библиотека, написанная на C, которая позволяет использовать сервера директорий X.500 и LDAP как основной источник алиасов, групп, имен хостов, сетей, протоколов, пользователей, RPC, сервисов и паролей вместо плоских файлов или NIS.

%prep
%setup -q
#patch0 -p0
#patch1 -p1
#patch2 -p1
#%patch3 -p1
#%patch4 -p1
%patch5 -p1

%patch10 -p1
##patch11 -p1

###
## Install Attention README
###
install -m 0644 %SOURCE1 README.ALT

%build
autoreconf -fisv

%configure \
	--with-ldap-conf-file=%_sysconfdir/nss_ldap.conf \
	--with-ldap-secret-file=%_sysconfdir/nss_ldap.secret \
	--with-ldap-lib=openldap \
	--enable-schema-mapping \
	--enable-paged-results \
%if_enabled krb
	--enable-configurable-krb5-ccname-gssapi \
	--enable-configurable-krb5-ccname-env \
	--with-gssapi-dir=%_includedir/krb5/gssapi \
%endif
%if_enabled debug
	--enable-debugging
%endif
	

%make_build SYSLIBDIR=/%_lib
%make check

%install

mkdir -p $RPM_BUILD_ROOT{%_sysconfdir,%_libdir,/%_lib}

# Install the nsswitch module.
%make_install  SYSLIBDIR=/%_lib install \
	DESTDIR=$RPM_BUILD_ROOT \
	INST_UID=`id -un` INST_GID=`id -gn`

mv $RPM_BUILD_ROOT%_libdir/* $RPM_BUILD_ROOT/%_lib/
chmod 755 $RPM_BUILD_ROOT/%_lib/*.so*

# Install /etc/nss_ldap.conf, becouse in nss_ldap and pam_ldap we have two the same files /etc/ldap.conf as a config files
# Install the default configuration file, but change the search bases to
# something generic.
sed -e 's/dc=padl/dc=example/g' ldap.conf >$RPM_BUILD_ROOT%_sysconfdir/nss_ldap.conf
sed -i 's/#timelimit 30/timelimit 5/g' $RPM_BUILD_ROOT%_sysconfdir/nss_ldap.conf
sed -i 's/#bind_timelimit 30/bind_timelimit 5/g' $RPM_BUILD_ROOT%_sysconfdir/nss_ldap.conf
sed -i 's/#bind_policy hard/bind_policy soft/g' $RPM_BUILD_ROOT%_sysconfdir/nss_ldap.conf
chmod 644 $RPM_BUILD_ROOT%_sysconfdir/nss_ldap.conf
rm -f $RPM_BUILD_ROOT%_sysconfdir/nsswitch.ldap
rm -f $RPM_BUILD_ROOT%_sysconfdir/ldap.conf

%files
/%_lib/*.so*
%config(noreplace) %_sysconfdir/nss_ldap.conf
%doc ANNOUNCE AUTHORS ChangeLog NEWS README
%doc nsswitch.ldap
%doc ldap.conf
%doc README.ALT
%doc %_man5dir/*
    
#[TODO]
#необходимо разобраться со сборкой вместе с krb
#
#

%changelog
* Mon Aug 01 2011 Anton Gorlov <stalker@altlinux.ru> 265-alt2
- bind_policy change to soft

* Fri Jan 29 2010 Anton Gorlov <stalker@altlinux.ru> 265-alt1
- update to version 265

* Sun Sep 06 2009 Anton Gorlov <stalker@altlinux.ru> 264-alt1
- update to version 264

* Fri Dec 14 2007 Anton Gorlov <stalker@altlinux.ru> 259-alt1
- New version
- Remove alt-saslauxprop.fix (integrated in upstrim)
- Updated libdir.fix

* Sun Apr 15 2007 Anton Gorlov <stalker@altlinux.ru> 252-alt2
- Fix #11420

* Wed Sep 06 2006 Anton Gorlov <stalker@altlinux.ru> 252-alt1
- New version

* Wed Aug 09 2006 Anton Gorlov <stalker@altlinux.ru> 251-alt1
- New version

* Wed Aug 02 2006 Anton Gorlov <stalker@altlinux.ru> 244-alt5.2
- Correct build on x86_64

* Mon Jun 12 2006 ALT QA Team Robot <qa-robot@altlinux.org> 244-alt5.1
- Rebuilt with libldap-2.3.so.0.

* Thu Nov 23 2005 Nick S. Grechukh <gns@altlinux.org> 244-alt5
- new maintainer, new version 244 fixing #8410

* Wed Aug 31 2005 Serge A. Volkov <vserge at altlinux.ru> 239-alt1
- Update to new version 239

* Fri Dec 17 2004 Serge A. Volkov <vserge at altlinux.ru> 227-alt1
- Update to new version 227

* Sat Nov 13 2004 ALT QA Team Robot <qa-robot@altlinux.org> 226-alt1.1
- Rebuilt with openldap-2.2.18-alt3.

* Sat Oct 02 2004  Serge A. Volkov <vserge@altlinux.ru> 226-alt1
- Update to new version 226
- Update %name-226-configure.patch
- Remove %name-210-segfault-alt.patch, because _nss_ldap_map_get functions was rewrited.
- Remove %name-211-db4-alt.patch see Changelog (near db* ).
- Tampory disable build with krb!!

* Sun Jul 04 2004  Serge A. Volkov <vserge@altlinux.ru> 220-alt3
- Rename /etc/ldap.conf to /etc/nss_ldap.conf

* Fri Jun 26 2004  Serge A. Volkov <vserge@altlinux.ru> 220-alt2
- Add Kerberos 5 support and  configure options for that
  + --enable-configurable-krb5-ccname-gssapi 
  + --enable-configurable-krb5-ccname-env
  + --with-gssapi-dir=%_includedir/krb5/gssapi

* Fri May 21 2004  Serge A. Volkov <vserge@altlinux.ru> 220-alt1
- Update to new version 220

* Wed Feb 18 2004  Serge A. Volkov <vserge@altlinux.ru> 215-alt1
- Update to new version

* Fri Feb 13 2004  Serge A. Volkov <vserge@altlinux.ru> 211-alt4
- Update BuildReq, becouse rebuild with libdb4.2

* Tue Jan 06 2004  Serge A. Volkov <vserge@altlinux.ru> 211-alt3
- Fix [Bug 3434]: http://bugzilla.altlinux.ru/show_bug.cgi?id=3434

* Sun Dec 28 2003  Serge A. Volkov <vserge@altlinux.ru> 211-alt2
- Add if_define constructions in spec for debug options
- Add %name-211-db4-alt.patch fix [Bug 3404]: http://bugzilla.altlinux.ru/show_bug.cgi?id=3404

* Sat Dec 13 2003  Serge A. Volkov <vserge@altlinux.ru> 211-alt1
- Update to new version 211

* Thu Sep 04 2003 Alexander Bokovoy <ab@altlinux.ru> 210-alt2
- Fixed:
  + Segfault upon first start when DB cache isn't initialised yet
  + Bug in group handling: RDN exploding wasn't handled carefully
    so group names were leaked to system with UTF-8 escaped in 
    unreadble form (bug #143 in PADL's bugzilla)

* Tue Sep 02 2003 Alexander Bokovoy <ab@altlinux.ru> 210-alt1
- 210

* Mon Feb 3 2003 Serge A. Volkov <vserge@altlinux.ru> 203-alt3
- Remove %%configure options
  - --enable-debig

* Sat Jan 4 2003 Serge A. Volkov <vserge@altlinux.ru> 203-alt2
- Add configure options --enable-debug
- Add README.ALT

* Fri Jan 3 2003 Serge A. Volkov <vserge@altlinux.ru> 203-alt1
- Update to version 203. 

* Thu Oct 17 2002 Serge A. Volkov <vserge@altlinux.ru> 202-alt2
- Add install /etc/ldap.conf
- Spec cleanup

* Thu Oct 17 2002 Serge A. Volkov <vserge@altlinux.ru> 202-alt1
- Update to new version

* Tue Aug 6 2002 Serge A. Volkov <vserge@altlinux.ru> 198-alt1
- Update to new version

* Sat Jun 1 2002 Serge A. Volkov <vserge@altlinux.ru> 194-alt1
- Update to new version

* Wed Apr 17 2002 Dmitry V. Levin <ldv@alt-linux.org> 172-alt6
- Relocated nss modules from %_libdir/ to /lib/.

* Thu Apr 4 2002 Serge A. Volkov <vserge@altlinux.ru> 172-alt5
- Patch from Aleksey Novodvorsky 
- (incoming) buildreqs updated by inger

* Thu Jan 24 2002 Serge A. Volkov <vserge@altlinux.ru> 172-alt4
- Correct conflict with openldap package

* Wed Jan 23 2002 Serge A. Volkov <vserge@altlinux.ru> 172-alt3
- Spec correction

* Mon Sep 24 2001 Dmitry V. Levin <ldv@altlinux.ru> 172-alt2
- Moved pam_ldap to separate package.
- Specfile cleanup.

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


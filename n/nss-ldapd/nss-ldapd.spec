%def_disable test
%def_disable debug
%def_disable krb

Name: nss-ldapd
Version: 0.6.8
Release: alt1.1

Summary: NSS module for name lookups using LDAP
License: LGPL
Group: System/Base

Url: http://ch.tudelft.nl/~arthur/nss-ldapd/

Source: %name-%version.tar
Source1: nslcd.init
Source2: nslcd.sysconfig

Requires: nscd
Requires(post): %post_service
Requires(preun): %preun_service

Conflicts: nss_ldap

# Automatically added by buildreq on Sat Nov 03 2007
BuildRequires: libkrb5-devel libldap-devel libsasl2-devel

Requires: su

%description
This is a fork of the nss_ldap  package by PADL Software Pty
Ltd.. This fork was done to implement some structural design
changes. These changes were needed because there are some issues
with the original design. See documentation for more details.

These problems are solved by splitting the library in two parts:
a daemon that connects to the LDAP server and does all the
requests and a thin NSS connector that passes requests to the
daemon through a socket. The nss-ldapd implementation has a
number of advantages:

    * lighter NSS library
    * simpler internal semantics
    * clear separation between NSS and LDAP code (the server part
      could easily be implemented in another language)
    * less connections to the LDAP server

The fork is also a major code overhaul having a number
of simplifications and removal of old compatibility code.
Compatibility will be re-added with later releases of nss-ldapd
for those platforms that need it.

%prep
%setup

%build
autoreconf -fisv

%configure \
	--with-ldap-conf-file=%_sysconfdir/nss-ldapd.conf \
	--with-ldap-secret-file=%_sysconfdir/nss-ldapd.secret \
	--with-ldap-lib=openldap \
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
mkdir -p %buildroot{%_sysconfdir,%_libdir,/%_lib}

# Install the nsswitch module.
%make_install  SYSLIBDIR=/%_lib install \
	DESTDIR=%buildroot \
	INST_UID=`id -un` INST_GID=`id -gn`

mv %buildroot%_libdir/* %buildroot/%_lib/
install -pD -m755 %SOURCE1 %buildroot%_initdir/nslcd
install -pD -m644 %SOURCE2 %buildroot%_sysconfdir/sysconfig/nslcd
chmod 755 %buildroot/%_lib/*.so*
chmod 600 %buildroot%_sysconfdir/nss-ldapd.conf

mkdir -pm711 %buildroot/var/run/nslcd
mksock %buildroot/var/run/nslcd/socket

%pre
%_sbindir/useradd -M -o -r -d / -s /dev/null -c "NSS-LDAP Daemon" _nslcd ||:

%post
%post_service nslcd

%preun
%preun_service nslcd
%files
/%_lib/*.so*
%_initdir/nslcd
%config(noreplace) %_sysconfdir/sysconfig/nslcd
%_sbindir/nslcd
%attr(600,_nslcd,_nslcd) %config(noreplace) %_sysconfdir/nss-ldapd.conf
%attr(711,_nslcd,root) %dir /var/run/nslcd
%attr(666,_nslcd,_nslcd) %ghost /var/run/nslcd/socket
%doc AUTHORS ChangeLog HACKING NEWS README TODO
%doc %_man5dir/*
%doc %_man8dir/*

%changelog
* Thu Sep 24 2009 ALT QA Team Robot <ldv@altlinux.org> 0.6.8-alt1.1
- Automated blind dumb rebuild with libldap-devel-2.4.16-alt4.4.

* Mon Apr 20 2009 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.6.8-alt1
- 0.6.8
- build fixed

* Wed Jul 09 2008 Vladimir V Kamarzin <vvk@altlinux.ru> 0.4.1-alt3
- Fixed initscript start message (Closes: #16306)
- Added missed dependency on su(1) (Closes: #16307)
- Implemented sysconfig-file support (Closes: #16308)

* Thu Jan 24 2008 Michael Shigorin <mike@altlinux.org> 0.4.1-alt2
- added Conflicts: nss_ldap (#14147)

* Thu Dec 27 2007 Michael Shigorin <mike@altlinux.org> 0.4.1-alt1
- rebuilt for Sisyphus
- fixed Url:, Source:, Summary: and %%description
- truncated %%changelog

* Sat Nov 03 2007 Nick S. Grechukh <gns@altlinux.org> 0.4.1-alt0.1
- nss-ldapd / based on nss_ldap sisyphus package

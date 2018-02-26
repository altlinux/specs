%define samba4_version 4.0.0
%define pre_release alpha18
%define _localstatedir /var

# Most of these subpackages are disabled because they are not
# needed by OpenChange, and to avoid file conflicts with Samba3.
%def_disable samba4
%def_disable client
%def_disable common
%def_disable python
%def_disable winbind

Name: samba4
Version: %samba4_version
Release: alt1.%pre_release
Group: System/Servers
Summary: The Samba4 CIFS and AD client and server suite
License: GPLv3+ and LGPLv3+
Url: http://www.samba.org/
Packager: Alexey Shabalin <shaba@altlinux.ru>

Source: %name-%version.tar

# Red Hat specific replacement-files
Source1: %name.log
Source4: %name.sysconfig
Source5: %name.init

Patch01: samba-4.0.0alpha16.buildfix.patch

%if_enabled common
Requires(pre): %name-common = %version-%release
%endif

BuildRequires: libe2fs-devel
BuildRequires: libacl-devel
BuildRequires: libaio-devel
BuildRequires: libattr-devel
BuildRequires: libncurses-devel
BuildRequires: libpam-devel
BuildRequires: perl-devel
BuildRequires: perl-Parse-Yapp
BuildRequires: libpopt-devel
BuildRequires: python-devel
BuildRequires: libreadline-devel
BuildRequires: libldap-devel
BuildRequires: libxslt xsltproc
BuildRequires: docbook-style-xsl
BuildRequires: libpopt-devel
BuildRequires: zlib-devel

BuildRequires: libtalloc-devel libtdb-devel libtevent-devel libldb-devel
BuildRequires: libpytalloc-devel python-module-tdb python-module-tevent python-module-pyldb-devel

BuildRequires: perl-Perl4-CoreLibs

%description
Samba 4 is the ambitious next version of the Samba suite that is being
developed in parallel to the stable 3.0 series. The main emphasis in
this branch is support for the Active Directory logon protocols used
by Windows 2000 and above.

%package client
Summary: Samba client programs
Group: Networking/Other
Requires: %name-common = %version-%release
Requires: %name-libs = %version-%release

%description client
The %name-client package provides some SMB/CIFS clients to complement
the built-in SMB/CIFS filesystem in Linux. These clients allow access
of SMB/CIFS shares and printing to SMB/CIFS printers.

%package libs
Summary: Samba libraries
Group: System/Libraries

%description libs
The %name-libs package contains the libraries needed by programs that
link against the SMB, RPC and other protocols provided by the Samba suite.

%package -n python-module-%name
Summary: Samba Python libraries
Group: Networking/Other
Requires: %name-libs = %version-%release

%add_python_req_skip Tdb

%description -n python-module-%name
The %name-python package contains the Python libraries needed by programs
that use SMB, RPC and other Samba provided protocols in Python programs.

%package devel
Summary: Developer tools for Samba libraries
Group: Development/C
Requires: %name-libs = %version-%release

%description devel
The %name-devel package contains the header files for the libraries
needed to develop programs that link against the SMB, RPC and other
libraries in the Samba suite.

%package pidl
Summary: Perl IDL compiler
Group: Development/Tools
# Requires: perl(:MODULE_COMPAT_%(eval "`perl -V:version`"; echo $version))

%description pidl
The %name-pidl package contains the Perl IDL compiler used by Samba
and Wireshark to parse IDL and similar protocols

%package common
Summary: Files used by both Samba servers and clients
Group: System/Servers
Requires: %name-libs = %version-%release

%description common
%name-common provides files necessary for both the server and client
packages of Samba.

%package winbind
Summary: Samba winbind
Group: System/Servers
Requires: %name = %version-%release

%description winbind
The samba-winbind package provides the winbind NSS library, and some
client tools.  Winbind enables Linux to be a full member in Windows
domains and to use Windows user and group accounts on Linux.

%prep
%setup -q
# %patch01 -p1 -b .buildfix

%build
%undefine _configure_gettext
%configure \
	--enable-fhs \
	--disable-tdb2 \
	--with-lockdir=/var/lib/%name \
	--with-piddir=/var/run \
	--with-privatedir=/var/lib/%name/private \
	--with-sockets-dir=/var/run \
	--with-configdir=%_sysconfdir/%name \
	--disable-gnutls \
	--disable-rpath-install \
	--builtin-libraries=ccan,wbclient \
	--bundled-libraries=heimdal,!talloc,!tdb,!tevent,!ldb,!zlib


# Build PIDL for installation into vendor directories before
# 'make proto' gets to it.
(cd pidl && perl Makefile.PL INSTALLDIRS=vendor )

# Builds using PIDL the IDL and many other things.
#make proto
#make everything
make

%install

# Don't call 'make install' as we want to call out to the PIDL
# install manually.
make install DESTDIR=%buildroot

# Undo the PIDL install, we want to try again with the right options.
rm -rf %buildroot%_libdir/perl5
rm -rf %buildroot%_datadir/perl5

# Install PIDL.
( cd pidl && make install PERL_INSTALL_ROOT=%buildroot )

# Clean out crap left behind by the PIDL install.
find %buildroot -type f -name .packlist -exec rm -f {} \;
find %buildroot -depth -type d -exec rmdir {} 2>/dev/null \;


%if_enabled samba4
mkdir -p %buildroot%_initdir
mkdir -p %buildroot%_sysconfdir/logrotate.d
mkdir -p %buildroot%_sysconfdir/sysconfig
%endif

mkdir -p %buildroot/var/run/winbindd
mkdir -p %buildroot/var/run/ntp_signd
mkdir -p %buildroot/var/lib/%name/winbindd_privileged
mkdir -p %buildroot/var/log/%name/
mkdir -p %buildroot/var/log/%name/old

mkdir -p %buildroot/var/lib/%name
mkdir -p %buildroot/var/lib/%name/private
mkdir -p %buildroot/var/lib/%name/sysvol

mkdir -p %buildroot%_sysconfdir/%name

%if_enabled samba4
# Install other stuff.
install -m755 %SOURCE5 %buildroot%_initdir/%name
install -m644 %SOURCE1 %buildroot%_sysconfdir/logrotate.d/%name
install -m644 %SOURCE4 %buildroot%_sysconfdir/sysconfig/%name
%endif

%if_disabled winbind
rm -f %buildroot%_bindir/ntlm_auth
rm -f %buildroot%_bindir/wbinfo
rm -f %buildroot%_libdir/libnss_winbind.so.2
rm -f %buildroot%_libdir/pam_winbind.so
#rm -f %buildroot%_libdir/libwbclient.so
#rm -f %buildroot%_libdir/libwbclient.so.*
rm -f %buildroot%_libdir/winbind_krb5_locator.so
rm -f %buildroot%_mandir/man1/ntlm_auth.*
rm -f %buildroot%_includedir/samba-4.0/wbclient.h
%endif
rm -f %buildroot%_libdir/libdcerpc-atsvc.so*

# libs {
mkdir -p %buildroot%_libdir %buildroot%_includedir

# }

# Clean out some stuff we don't want in package.
# rm %buildroot%_bindir/mount.cifs
# rm %buildroot%_bindir/umount.cifs

#rm %buildroot%_bindir/epdump
rm -f %buildroot%_bindir/gentest
rm -f %buildroot%_mandir/man1/gentest.*
rm -f %buildroot%_bindir/getntacl
rm -f %buildroot%_bindir/locktest
rm -f %buildroot%_mandir/man1/locktest.*
rm -f %buildroot%_bindir/masktest
rm -f %buildroot%_mandir/man1/masktest.*
rm -f %buildroot%_bindir/ndrdump
rm -f %buildroot%_mandir/man1/ndrdump.*
rm -f %buildroot%_bindir/nsstest
rm -f %buildroot%_bindir/setnttoken
rm -f %buildroot%_bindir/smbtorture
rm -f %buildroot%_mandir/man1/smbtorture.*
#depending on the environemnt this file might or might not be generated
rm -f %buildroot%_bindir/tdbtorture

# Avoids a file conflict with perl-Parse-Yapp.
rm -rf %buildroot%perl_vendor_privlib/Parse/Yapp

# Remove files for disabled subpackages.
%if_disabled samba4
#rm %buildroot%_bindir/mymachinepw
rm -f %buildroot%_sbindir/provision
rm -f %buildroot%_sbindir/samba
rm -f %buildroot%_sbindir/upgradeprovision
rm -f %buildroot%_sbindir/samba_dnsupdate
rm -f %buildroot%_sbindir/samba_spnupdate
rm -f %buildroot%_bindir/samba-tool
rm -f %buildroot%_libdir/mit_samba.so
rm -f %buildroot%_mandir/man8/samba.*
rm -rf %buildroot%_datadir/samba/setup
rm -rf %buildroot%_datadir/samba/swat
%endif

%if_enabled client
# Fix *mount.cifs
mkdir -p %buildroot/sbin
mv %buildroot%_bindir/*mount.cifs %buildroot/sbin/
ln -s ../../sbin/mount.cifs %buildroot%_bindir/cifsmount
ln -s ../../sbin/umount.cifs %buildroot%_bindir/cifsumount
%endif

%if_disabled client
rm -f %buildroot%_bindir/nmblookup
rm -f %buildroot%_bindir/smbclient
rm -f %buildroot%_bindir/cifsdd
rm -f %buildroot%_mandir/man1/nmblookup.*
%endif
%if_disabled common
rm -f %buildroot%_bindir/regdiff
rm -f %buildroot%_bindir/regpatch
rm -f %buildroot%_bindir/regshell
rm -f %buildroot%_bindir/regtree
rm -f %buildroot%_bindir/testparm
rm -f %buildroot%_mandir/man1/regdiff.*
rm -f %buildroot%_mandir/man1/regpatch.*
rm -f %buildroot%_mandir/man1/regshell.*
rm -f %buildroot%_mandir/man1/regtree.*
%endif

# the samba4 build process rebuilds libraries internally,
# but we want to use the standalone build for now.
#rm -f %buildroot%_libdir/libldb.so*
#rm -f %buildroot%_bindir/ad2oLschema
#rm -f %buildroot%_bindir/ldbadd
#rm -f %buildroot%_bindir/ldbdel
#rm -f %buildroot%_bindir/ldbedit
#rm -f %buildroot%_bindir/ldbmodify
#rm -f %buildroot%_bindir/ldbrename
#rm -f %buildroot%_bindir/ldbsearch
rm -f %buildroot%_bindir/oLschema2ldif
#rm -f %buildroot%_bindir/tdbbackup
#rm -f %buildroot%_bindir/tdbdump
#rm -f %buildroot%_bindir/tdbtool

rm -f %buildroot%_libdir/lib*.a

%if_disabled python
rm -r %buildroot%python_sitelibdir/*
rm -fr %buildroot%python_libdir/lib
%endif

# These may be created in non mock systems, but we do not want to package them
# for now
#rm -f %buildroot%_man1dir/ad2oLschema.1
rm -f %buildroot%_man1dir/oLschema2ldif.1
#rm -f %buildroot%_datadir/swig/*/talloc.i

rm -f %buildroot%_libdir/pam_smbpass.so

# Remove Files conflicting with regular samba 3.x packages
rm -f %buildroot%_libdir/samba/auth/script.so
rm -f %buildroot%_libdir/samba/vfs/acl_tdb.so
rm -f %buildroot%_libdir/samba/vfs/acl_xattr.so
rm -f %buildroot%_libdir/samba/vfs/aio_fork.so
rm -f %buildroot%_libdir/samba/vfs/audit.so
rm -f %buildroot%_libdir/samba/vfs/cap.so
rm -f %buildroot%_libdir/samba/vfs/catia.so
rm -f %buildroot%_libdir/samba/vfs/crossrename.so
rm -f %buildroot%_libdir/samba/vfs/default_quota.so
rm -f %buildroot%_libdir/samba/vfs/dirsort.so
rm -f %buildroot%_libdir/samba/vfs/expand_msdfs.so
rm -f %buildroot%_libdir/samba/vfs/extd_audit.so
rm -f %buildroot%_libdir/samba/vfs/fake_perms.so
rm -f %buildroot%_libdir/samba/vfs/fileid.so
rm -f %buildroot%_libdir/samba/vfs/full_audit.so
rm -f %buildroot%_libdir/samba/vfs/linux_xfs_sgid.so
rm -f %buildroot%_libdir/samba/vfs/netatalk.so
rm -f %buildroot%_libdir/samba/vfs/preopen.so
rm -f %buildroot%_libdir/samba/vfs/readahead.so
rm -f %buildroot%_libdir/samba/vfs/readonly.so
rm -f %buildroot%_libdir/samba/vfs/recycle.so
rm -f %buildroot%_libdir/samba/vfs/scannedonly.so
rm -f %buildroot%_libdir/samba/vfs/shadow_copy.so
rm -f %buildroot%_libdir/samba/vfs/shadow_copy2.so
rm -f %buildroot%_libdir/samba/vfs/smb_traffic_analyzer.so
rm -f %buildroot%_libdir/samba/vfs/streams_depot.so
rm -f %buildroot%_libdir/samba/vfs/streams_xattr.so
rm -f %buildroot%_libdir/samba/vfs/syncops.so
rm -f %buildroot%_libdir/samba/vfs/time_audit.so
rm -f %buildroot%_libdir/samba/vfs/xattr_tdb.so
rm -f %buildroot%_libdir/libsmbclient.so*
rm -f %buildroot%_libdir/libnss_wins.so.2
rm -f %buildroot%_sbindir/nmbd
rm -f %buildroot%_sbindir/smbd
rm -f %buildroot%_sbindir/swat
rm -f %buildroot%_sbindir/winbindd
rm -f %buildroot%_bindir/dbwrap_tool
rm -f %buildroot%_bindir/dbwrap_torture
rm -f %buildroot%_bindir/debug2html
rm -f %buildroot%_bindir/eventlogadm
rm -f %buildroot%_bindir/locktest2
rm -f %buildroot%_bindir/locktest3
rm -f %buildroot%_bindir/log2pcap
rm -f %buildroot%_bindir/masktest3
rm -f %buildroot%_bindir/msgtest
rm -f %buildroot%_bindir/net
rm -f %buildroot%_bindir/nmblookup3
rm -f %buildroot%_bindir/ntlm_auth3
rm -f %buildroot%_bindir/pdbedit
rm -f %buildroot%_bindir/pdbtest
rm -f %buildroot%_bindir/profiles
rm -f %buildroot%_bindir/pthreadpooltest
rm -f %buildroot%_bindir/rpc_open_tcp
rm -f %buildroot%_bindir/rpcclient
rm -f %buildroot%_bindir/sharesec
rm -f %buildroot%_bindir/smbcacls
rm -f %buildroot%_bindir/smbclient3
rm -f %buildroot%_bindir/smbconftort
rm -f %buildroot%_bindir/smbcontrol
rm -f %buildroot%_bindir/smbcquotas
rm -f %buildroot%_bindir/smbfilter
rm -f %buildroot%_bindir/smbget
rm -f %buildroot%_bindir/smbiconv
rm -f %buildroot%_bindir/smbpasswd
rm -f %buildroot%_bindir/smbspool
rm -f %buildroot%_bindir/smbstatus
rm -f %buildroot%_bindir/smbta-util
rm -f %buildroot%_bindir/smbtorture3
rm -f %buildroot%_bindir/smbtree
rm -f %buildroot%_bindir/split_tokens
rm -f %buildroot%_bindir/test_lp_load
rm -f %buildroot%_bindir/timelimit
rm -f %buildroot%_bindir/versiontest
rm -f %buildroot%_bindir/vfstest
rm -f %buildroot%_bindir/vlp
rm -f %buildroot%_bindir/wbinfo3

# This makes the right links, as rpmlint requires that
# the ldconfig-created links be recorded in the RPM.
#   /sbin/ldconfig -N -n %buildroot%_libdir

# Fix up permission on perl install.
%_fixperms %buildroot%perl_vendor_privlib

# Fix up permissions in source tree, for debuginfo.
find source4/heimdal -type f | xargs chmod -x

%pre winbind
%_sbindir/groupadd -g 88 wbpriv >/dev/null 2>&1 || :

%post winbind
%post_service winbind

%preun winbind
%preun_service winbind

%post
%if_enabled samba4
%post_service samba4
%endif

%preun
%if_enabled samba4
%preun_service samba4
%endif

%files
%doc COPYING
%if_enabled samba4
%_sbindir/provision
%_sbindir/samba
%_sbindir/upgradeprovision
%_sbindir/samba_dnsupdate
%_sbindir/samba_spnupdate
%_bindir/samba-tool
%_libdir/mit_samba.so
#%_mandir/man8/samba.*
%dir /var/lib/%name/sysvol
%config(noreplace) %_sysconfdir/logrotate.d/%name
%config(noreplace) %_sysconfdir/sysconfig/%name
%attr(0755,root,root) %_initdir/%name
%attr(0700,root,root) %dir /var/log/%name
%attr(0700,root,root) %dir /var/log/%name/old
%endif

%files libs
%doc PFIF.txt
%dir %_datadir/samba
%dir %_datadir/samba/codepages
%_datadir/samba/codepages/*.dat

#%_libdir/libdcerpc-atsvc.so.*
%_libdir/libdcerpc-samr.so.*
%_libdir/libdcerpc-server.so.*
%_libdir/libdcerpc.so.*
%_libdir/libgensec.so.*
%_libdir/libndr-krb5pac.so.*
%_libdir/libndr.so.*
%_libdir/libndr-standard.so.*
%_libdir/libsamba-policy.so.*
%_libdir/libregistry.so.*
%_libdir/libsamba-hostconfig.so.*
%_libdir/libsamba-util.so.*
%_libdir/libsamdb.so.*
%_libdir/libtorture.so.*
%_libdir/libsmbconf.so.*
%_libdir/libdcerpc-binding.so.*
%_libdir/libndr-nbt.so.*
%_libdir/libsamba-credentials.so.*
%_libdir/libsmbclient-raw.so.*
%_libdir/libtevent-util.so.*

# internal ldb modules
%_libdir/samba/ldb/*.so

# samba internal libraries
%_libdir/samba/gensec/*.so
%_libdir/samba/*.so.*
%_libdir/samba/*.so
%_libdir/samba/process_model/*.so
%_libdir/samba/service/*.so

#%_libdir/libtorture.so.*
#Only needed if Samba's build produces plugins
#%_libdir/samba
#%dir %_sysconfdir/%name
#Need to mark this as being owned by Samba, but it is normally created
#by the provision script, which runs best if there is no existing
#smb.conf
#%config(noreplace) %_sysconfdir/%name/smb.conf

%if_enabled winbind
%files winbind
%_bindir/ntlm_auth
%_bindir/wbinfo
%_libdir/libwbclient.so.0
%_libdir/libnss_winbind.so.2
%_libdir/libnss-winbind.inst.so.2
%_libdir/winbind_krb5_locator.so
%_libdir/pam_winbind.so
%dir /var/run/winbindd
%attr(750,root,wbpriv) %dir /var/lib/%name/winbindd_privileged
%_mandir/man1/ntlm_auth.*
%endif

%if_enabled python
%files -n python-module-%name
%python_sitelibdir/*
%endif

%files devel
%_includedir/samba-4.0
%_libdir/libdcerpc.so
%_libdir/libdcerpc-samr.so
%_libdir/libndr.so
%_libdir/libndr-standard.so
%_libdir/libsamba-hostconfig.so
%_libdir/libsamba-util.so
#%_libdir/libdcerpc-atsvc.so
%_libdir/libdcerpc-server.so
%_libdir/libgensec.so
%_libdir/libndr-krb5pac.so
%_libdir/libsamba-policy.so
%_libdir/libregistry.so
%_libdir/libsamdb.so
%_libdir/libtorture.so
%_libdir/libsmbconf.so
%_libdir/libdcerpc-binding.so
%_libdir/libndr-nbt.so
%_libdir/libsamba-credentials.so
%_libdir/libsmbclient-raw.so
%_libdir/libtevent-util.so

%_pkgconfigdir/dcerpc.pc
%_pkgconfigdir/dcerpc_samr.pc
%_pkgconfigdir/ndr.pc
%_pkgconfigdir/ndr_standard.pc
%_pkgconfigdir/samba-hostconfig.pc
%_pkgconfigdir/samba-util.pc
%_pkgconfigdir/dcerpc_atsvc.pc
%_pkgconfigdir/dcerpc_server.pc
%_pkgconfigdir/gensec.pc
%_pkgconfigdir/ndr_krb5pac.pc
%_pkgconfigdir/samba-policy.pc
%_pkgconfigdir/registry.pc
%_pkgconfigdir/samdb.pc
%_pkgconfigdir/torture.pc
%_pkgconfigdir/ndr_nbt.pc
%_pkgconfigdir/samba-credentials.pc
%_pkgconfigdir/smbclient-raw.pc

%files pidl
%attr(755,root,root) %_bindir/pidl
%perl_vendor_privlib/*

%if_enabled client
%files client
/sbin/mount.cifs
/sbin/umount.cifs

%_bindir/nmblookup
%_bindir/smbclient
%_bindir/cifsdd
%_mandir/man1/nmblookup.*
%endif

%if_enabled common
%files common
%_bindir/testparm
%_bindir/regdiff
%_bindir/regpatch
%_bindir/regshell
%_bindir/regtree
%_mandir/man1/regdiff.*
%_mandir/man1/regpatch.*
%_mandir/man1/regshell.*
%_mandir/man1/regtree.*

%dir /var/lib/%name
%attr(700,root,root) %dir /var/lib/%name/private
# We don't want to put a smb.conf in by default, provision should create it
#%config(noreplace) %_sysconfdir/%name/smb.conf
%endif

%changelog
* Wed Mar 28 2012 Alexey Shabalin <shaba@altlinux.ru> 4.0.0-alt1.alpha18
- alpha18

* Sat Oct 22 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 4.0.0-alt1.alpha16.1
- Rebuild with Python-2.7

* Mon Aug 08 2011 Alexey Shabalin <shaba@altlinux.ru> 4.0.0-alt1.alpha16
- alpha16

* Wed May 11 2011 Alexey Shabalin <shaba@altlinux.ru> 4.0.0-alt1.alpha15
- alpha15

* Thu Apr 14 2011 Alexey Shabalin <shaba@altlinux.ru> 4.0.0-alt0.alpha15
- pre alpha15 snapshot

* Thu Sep 23 2010 Alexey Shabalin <shaba@altlinux.ru> 4.0.0-alt1.alpha13
- Upgrade to alpha13

* Fri Aug 13 2010 Alexey Shabalin <shaba@altlinux.ru> 4.0.0-alt1.alpha11
- initial build for ALT Linux Sisyphus

* Mon Jun 28 2010 Ralf Corsépius <corsepiu@fedoraproject.org> - 4.0.0-24.alpha11
- Revert changes to %%Release, use %%main_release instead.
- Rebuild for perl-5.12.x.

* Mon Jun 28 2010 Ralf Corsépius <corsepiu@fedoraproject.org> - 4.0.0-23.alpha11.2
- Once again rebuild for perl-5.12.x.

* Wed Jun 02 2010 Marcela Maslanova <mmaslano@redhat.com> - 4.0.0-23.alpha11.1
- Mass rebuild with perl-5.12.0

* Wed Feb 24 2010 Stephen Gallagher <sgallagh@redhat.com> - 4.0.0-23.alpha11
- Rebuild against newer libtevent

* Sun Jan 24 2010 Matthew Barnes <mbarnes@redhat.com> - 4.0.0-22.alpha11
- Upgrade to alpha11

* Fri Jan 08 2010 Matthew Barnes <mbarnes@redhat.com> - 4.0.0-21.alpha10
- Bump ldb_version to 0.9.10.

* Fri Jan 08 2010 Matthew Barnes <mbarnes@redhat.com> - 4.0.0-20.alpha10
- Only install new command-line utilities if enable_samba4 is non-zero.

* Wed Jan 06 2010 Matthew Barnes <mbarnes@redhat.com> - 4.0.0-19.alpha10
- Upgrade to alpha10

* Thu Sep 17 2009 Simo Sorce <ssorce@redhat.com> - 4.0.0-18.1.alpha8_git20090916
- Need docbook stuff to build man pages

* Thu Sep 17 2009 Simo Sorce <ssorce@redhat.com> - 4.0.0-18.alpha8_git20090916
- Fix broken dependencies

* Wed Sep 16 2009 Simo Sorce <ssorce@redhat.com> - 4.0.0-17.alpha8_git20090916
- Upgrade to alpha8-git20090916

* Wed Sep 16 2009 Simo Sorce <ssorce@redhat.com> - 4.0.0-16.alpha7
- Stop building libtevent, it is now an external package

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.0.0-15.2alpha7.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Fri May 22 2009 Simo Sorce <ssorce@redhat.com> - 4.0.0-15.2alpha7
- Fix dependency

* Sat May 09 2009  Simo Sorce <ssorce@redhat.com> - 4.0.0-15.1alpha7
- Don't build talloc and tdb, they are now separate packages

* Mon Apr 06 2009 Matthew Barnes <mbarnes@redhat.com> - 4.0.0-14alpha7
- Fix a build issue in samba4-common (RH bug #494243).

* Wed Mar 25 2009 Simo Sorce <ssorce@redhat.com> - 4.0.0-13alpha7
- rebuild with correct CFLAGS (also fixes debuginfo)

* Tue Mar 10 2009 Simo Sorce <ssorce@redhat.com> - 4.0.0-12alpha7
- Second part of fix for the ldb segfault problem from upstream

* Mon Mar 09 2009 Simo Sorce <ssorce@redhat.com> - 4.0.0-11alpha7
- Add upstream patch to fix a problem within ldb

* Sun Mar 08 2009 Matthew Barnes <mbarnes@redhat.com> - 4.0.0-10alpha7
- Remove ldb.pc from samba4-devel (RH bug #489186).

* Wed Mar  4 2009 Simo Sorce <ssorce@redhat.com> - 4.0.0-9alpha7
- Make talloc,tdb,tevent,ldb easy to exclude using defines
- Fix package for non-mock "dirty" systems by deleting additional
  files we are not interested in atm

* Wed Mar  4 2009 Simo Sorce <ssorce@redhat.com> - 4.0.0-8alpha7
- Fix typo in Requires

* Mon Mar  2 2009 Simo Sorce <ssorce@redhat.com> - 4.0.0-7alpha7
- Compile and have separate packages for additional samba libraries
  Package in their own packages: talloc, tdb, tevent, ldb

* Fri Feb 27 2009 Matthew Barnes <mbarnes@redhat.com> - 4.0.0-4.alpha7
- Update to 4.0.0alpha7

* Wed Feb 25 2009 Matthew Barnes <mbarnes@redhat.com> - 4.0.0-3.alpha6
- Formal package review cleanups.

* Mon Feb 23 2009 Matthew Barnes <mbarnes@redhat.com> - 4.0.0-2.alpha6
- Disable subpackages not needed by OpenChange.
- Incorporate package review feedback.

* Mon Jan 19 2009 Matthew Barnes <mbarnes@redhat.com> - 4.0.0-1.alpha6
- Update to 4.0.0alpha6

* Wed Dec 17 2008 Matthew Barnes <mbarnes@redhat.com> - 4.0.0-0.8.alpha6.GIT.3508a66
- Fix another file conflict: smbstatus

* Fri Dec 12 2008 Matthew Barnes <mbarnes@redhat.com> - 4.0.0-0.7.alpha6.GIT.3508a66
- Disable the winbind subpackage because it conflicts with samba-winbind
  and isn't needed to support OpenChange.

* Fri Dec 12 2008 Matthew Barnes <mbarnes@redhat.com> - 4.0.0-0.6.alpha6.GIT.3508a66
- Update to the GIT revision OpenChange is now requiring.

* Fri Aug 29 2008 Andrew Bartlett <abartlet@samba.org> - 0:4.0.0-0.5.alpha5.fc10
- Fix licence tag (the binaries are built into a GPLv3 whole, so the BSD licence need not be mentioned)

* Fri Jul 25 2008 Andrew Bartlett <abartlet@samba.org> - 0:4.0.0-0.4.alpha5.fc10
- Remove talloc and tdb dependency (per https://bugzilla.redhat.com/show_bug.cgi?id=453083)
- Fix deps on chkconfig and service to main pkg (not -common)
  (per https://bugzilla.redhat.com/show_bug.cgi?id=453083)

* Mon Jul 21 2008 Brad Hards <bradh@frogmouth.ent> - 0:4.0.0-0.3.alpha5.fc10
- Use --sysconfdir instead of --with-configdir
- Add patch for C++ header compatibility

* Mon Jun 30 2008 Andrew Bartlett <abartlet@samba.org> - 0:4.0.0-0.2.alpha5.fc9
- Update per review feedback
- Update for alpha5

* Thu Jun 26 2008 Andrew Bartlett <abartlet@samba.org> - 0:4.0.0-0.1.alpha4.fc9
- Rework Fedora's Samba 3.2.0-1.rc2.16 spec file for Samba4

%define samba_source source3

Summary: Server and Client software to interoperate with Windows machines
Name: samba
Version: 3.6.6
Release: alt1
License: GPLv3+ and LGPLv3+
Group: System/Servers
Url: http://www.samba.org/

Packager: Vitaly Kuznetsov <vitty@altlinux.ru>

Source: http://www.samba.org/samba/ftp/stable/%name-%version.tar.gz

# Red Hat specific replacement-files
Source1: samba.log
Source2: samba.xinetd
Source3: swat.desktop
Source4: samba.sysconfig
Source5: smb.init
Source6: samba.pamd
Source7: smbprint
Source8: winbind.init
Source9: smb.conf.default
Source10: nmb.init
Source11: pam_winbind.conf

# upstream patches.  Applied first so that they'll break our patches rather
# than the other way around
# (none right now)

# generic patches
Patch102: samba-3.2.0pre1-pipedir.patch
Patch104: samba-3.0.0rc3-nmbd-netbiosname.patch
# The passwd part has been applied, but not the group part
Patch107: samba-3.2.0pre1-grouppwd.patch
Patch200: samba-3.2.5-inotify.patch

Requires(pre): samba-common = %version-%release

BuildRequires: libpam0-devel, libreadline-devel, libncurses-devel, libacl-devel, libkrb5-devel, libldap-devel, libssl-devel, libcups-devel, ctdb-devel
BuildRequires: gawk, libpopt-devel, libgtk+2-devel, libcap-devel, libuuid-devel
BuildRequires: libtalloc-devel, libtdb-devel
BuildRequires: inkscape xsltproc netpbm dblatex html2text docbook-style-xsl libkeyutils-devel

%description
Samba is the suite of programs by which a lot of PC-related machines
share files, printers, and other information (such as lists of
available files and printers). The Windows NT, OS/2, and Linux
operating systems support this natively, and add-on packages can
enable the same thing for DOS, Windows, VMS, UNIX of all kinds, MVS,
and more. This package provides an SMB/CIFS server that can be used to
provide network services to SMB/CIFS clients.
Samba uses NetBIOS over TCP/IP (NetBT) protocols and does NOT
need the NetBEUI (Microsoft Raw NetBIOS frame) protocol.

%package client
Summary: Samba client programs
Group: Networking/Other
Requires: samba-common = %version-%release
Provides: samba-client-cups = %version-%release
Obsoletes: samba-client-cups < %version-%release

%description client
The samba-client package provides some SMB/CIFS clients to complement
the built-in SMB/CIFS filesystem in Linux. These clients allow access
of SMB/CIFS shares and printing to SMB/CIFS printers.

%package common
Summary: Files used by both Samba servers and clients
Group: System/Servers
Provides: samba-utils = %version-%release
Requires: libtalloc >= 2.0.1

%description common
Samba-common provides files necessary for both the server and client
packages of Samba.

%package -n libnetapi
Summary: Samba netapi library
Group: System/Libraries

%description -n libnetapi
Samba netapi library

%package -n libnetapi-devel
Summary: Samba netapi development files
Group: Development/Other

%description -n libnetapi-devel
Samba netapi development files

%package winbind
Summary: Samba winbind
Group: System/Servers
Requires: samba-common = %version-%release
Requires: samba-winbind-clients = %version-%release

%description winbind
The samba-winbind package provides the winbind daemon and some client tools.
Winbind enables Linux to be a full member in Windows domains and to use
Windows user and group accounts on Linux.

%package winbind-clients
Summary: Samba winbind clients
Group: System/Servers

%description winbind-clients
The samba-winbind-clients package provides the NSS library and a PAM
module necessary to communicate to the Winbind Daemon

%package winbind-devel
Summary: Developer tools for the winbind library
Group: Development/Other
Requires: samba-winbind = %version-%release

%description winbind-devel
The samba-winbind package provides developer tools for the wbclient library.

%package swat
Summary: The Samba SMB server Web configuration program
Group: Security/Networking
Requires: samba = %version-%release
Requires: samba-doc = %version-%release
Requires: xinetd

%description swat
The samba-swat package includes the new SWAT (Samba Web Administration
Tool), for remotely managing Samba's smb.conf file using your favorite
Web browser.

%package doc
Summary: Documentation for the Samba suite
Group: Networking/Other
Requires: samba-common = %version-%release
BuildArch: noarch

%description doc
The samba-doc package includes all the non-manpage documentation for the
Samba suite.

%package domainjoin-gui
Summary: Domainjoin GUI
Group: Networking/Other
Requires: samba-common = %version-%release

%description domainjoin-gui
The samba-domainjoin-gui package includes a domainjoin gtk application.

%package -n libsmbclient
Summary: The SMB client library
Group: Development/C

%description -n libsmbclient
The libsmbclient contains the SMB client library from the Samba suite.

%package -n libsmbclient-devel
Summary: Developer tools for the SMB client library
Group: Development/C
Requires: libsmbclient = %version-%release

%description -n libsmbclient-devel
The libsmbclient-devel package contains the header files and libraries needed to
develop programs that link against the SMB client library in the Samba suite.

%prep
# TAG: change for non-pre
%setup -q -n %name-%version
#%setup -q

# copy Red Hat specific scripts
mkdir packaging/Fedora
cp packaging/RHEL/setup/smbusers packaging/Fedora/
cp %SOURCE5 packaging/Fedora/
cp %SOURCE6 packaging/Fedora/
cp %SOURCE7 packaging/Fedora/
cp %SOURCE8 packaging/Fedora/winbind.init
cp %SOURCE9 packaging/Fedora/
cp %SOURCE10 packaging/Fedora/
cp %SOURCE11 packaging/Fedora/

# Upstream patches
#(none)
# generic patches
%patch102 -p1 -b .pipedir
#%patch104 -p1 -b .nmbd-netbiosname
%patch107 -p1 -b .grouppwd
%patch200 -p0 -b .inotify

sed -i 's/SAMBA_VERSION_VENDOR_SUFFIX=$/&\"%release\"/' %samba_source/VERSION
cd %samba_source
script/mkversion.sh
cd ..

#Remove smbldap-tools, they are already packaged separately in Fedora
rm -fr examples/LDAP/smbldap-tools-*/

pushd docs-xml
%autoreconf
popd

%build
pushd %samba_source
sh autogen.sh
%ifarch i386 sparc
RPM_OPT_FLAGS="$RPM_OPT_FLAGS -D_FILE_OFFSET_BITS=64"
%endif
%ifarch ia64
#libtoolize --copy --force     # get it to recognize IA-64
#autoheader
#autoconf
EXTRA="-D_LARGEFILE64_SOURCE"
%endif
CFLAGS="$RPM_OPT_FLAGS -D_GNU_SOURCE -DLDAP_DEPRECATED" %configure \
    --with-dnsupdate \
    --with-ads \
    --with-acl-support \
    --with-automount \
    --with-dnsupdate \
    --with-libsmbclient \
    --with-libsmbsharemodes \
    --with-mmap \
    --with-pam \
    --with-pam_smbpass \
    --with-quotas \
    --with-sendfile-support \
    --with-syslog \
    --with-utmp \
    --with-vfs \
    --with-winbind \
    --without-smbwrapper \
    --with-lockdir=/var/lib/samba \
    --with-piddir=/var/run \
    --with-mandir=%_mandir \
    --with-privatedir=/var/lib/samba/private \
    --with-logfilebase=/var/log/samba \
    --with-libdir=%_libdir \
    --with-modulesdir=%_libdir/samba \
    --with-configdir=%_sysconfdir/samba \
    --with-pammodulesdir=%_lib/security \
    --with-swatdir=%_datadir/swat \
    --with-shared-modules=idmap_ad,idmap_rid,idmap_adex,idmap_hash,idmap_tdb2 \
    --with-cifsupcall \
    --with-cifsumount \
    --with-cluster-support \
    --with-libtalloc=no \
    --enable-external-libtalloc=yes \
    --with-libtdb=no \
#    --enable-external-libtdb=yes \
#    --with-aio-support \

make  pch

make  LD_LIBRARY_PATH=$RPM_BUILD_DIR/%name-%version/%samba_source/bin \
%{?_smp_mflags} \
    all ../nsswitch/libnss_wins.so modules test_pam_modules test_nss_modules test_shlibs

make  LD_LIBRARY_PATH=$RPM_BUILD_DIR/%name-%version/%samba_source/bin \
%{?_smp_mflags} \
    -C lib/netapi/examples

make  debug2html smbfilter
popd

pushd docs-xml
%configure  --with-samba-sources=../source3
make smbdotconf/parameters.all.xml
make release
popd

%install
mkdir -p %buildroot/sbin
mkdir -p %buildroot/usr/{sbin,bin}
mkdir -p %buildroot%_initdir
mkdir -p %buildroot%_sysconfdir/{pam.d,logrotate.d,security}
mkdir -p %buildroot/%_lib/security
mkdir -p %buildroot/var/lib/samba
mkdir -p %buildroot/var/lib/samba/private
mkdir -p %buildroot/var/lib/samba/winbindd_privileged
mkdir -p %buildroot/var/lib/samba/scripts
mkdir -p %buildroot/var/log/samba/old
mkdir -p %buildroot/var/spool/samba
mkdir -p %buildroot%_datadir/swat/using_samba
mkdir -p %buildroot/var/run/winbindd
mkdir -p %buildroot%_libdir/samba
mkdir -p %buildroot%_pkgconfigdir

cd %samba_source

%makeinstall \
    BINDIR=%buildroot%_bindir \
    BASEDIR=%buildroot%prefix \
    SBINDIR=%buildroot%_sbindir \
    DATADIR=%buildroot%_datadir \
    LOCKDIR=%buildroot/var/lib/samba \
    PRIVATEDIR=%buildroot%_sysconfdir/samba \
    LIBDIR=%buildroot%_libdir/ \
    MODULESDIR=%buildroot%_libdir/samba \
    CONFIGDIR=%buildroot%_sysconfdir/samba \
    PAMMODULESDIR=%buildroot/%_lib/security \
    MANDIR=%buildroot%_mandir \
    VARDIR=%buildroot/var/log/samba \
    CODEPAGEDIR=%buildroot%_libdir/samba \
    SWATDIR=%buildroot%_datadir/swat \
    SAMBABOOK=%buildroot%_datadir/swat/using_samba \
    PIDDIR=%buildroot/var/run

cd ..

# Install other stuff
install -m644 packaging/Fedora/smb.conf.default %buildroot%_sysconfdir/samba/smb.conf
install -m755 %samba_source/script/mksmbpasswd.sh %buildroot%_bindir
install -m644 packaging/Fedora/smbusers %buildroot%_sysconfdir/samba/smbusers
install -m755 packaging/Fedora/smbprint %buildroot%_bindir
install -m755 packaging/Fedora/smb.init %buildroot%_initdir/smb
install -m755 packaging/Fedora/nmb.init %buildroot%_initdir/nmb
install -m755 packaging/Fedora/winbind.init %buildroot%_initdir/winbind
install -m644 packaging/Fedora/pam_winbind.conf %buildroot%_sysconfdir/security
#ln -s ../..%_initdir/smb  %buildroot%_sbindir/samba
install -m644 packaging/Fedora/samba.pamd %buildroot%_sysconfdir/pam.d/samba
install -m644 %SOURCE1 %buildroot%_sysconfdir/logrotate.d/samba
echo 127.0.0.1 localhost > %buildroot%_sysconfdir/samba/lmhosts
mkdir -p %buildroot%_sysconfdir/openldap/schema
install -m644 examples/LDAP/samba.schema %buildroot%_sysconfdir/openldap/schema/samba.schema

# winbind
mkdir -p %buildroot%_libdir
install -m 755 nsswitch/libnss_winbind.so %buildroot/%_lib/libnss_winbind.so.2
ln -sf /%_lib/libnss_winbind.so.2  %buildroot%_libdir/libnss_winbind.so
install -m 755 nsswitch/libnss_wins.so %buildroot/%_lib/libnss_wins.so.2
ln -sf /%_lib/libnss_wins.so.2  %buildroot%_libdir/libnss_wins.so

# libraries {
mkdir -p %buildroot%_libdir %buildroot%_includedir
build_libdir="%buildroot%_libdir"

# make install puts libraries in the wrong place
# (but at least gets the versioning right now)

list="smbclient smbsharemodes netapi talloc tdb wbclient"
for i in $list; do
    install -m 644 %samba_source/pkgconfig/$i.pc $build_libdir/pkgconfig/ || true
done

/sbin/ldconfig -n %buildroot%_libdir/

# }

mkdir -p %buildroot%_sysconfdir/xinetd.d
install -m644 %SOURCE2 %buildroot%_sysconfdir/xinetd.d/swat

mkdir -p %buildroot%_sysconfdir/sysconfig
install -m644 %SOURCE4 %buildroot%_sysconfdir/sysconfig/samba

install -m 755 %samba_source/lib/netapi/examples/bin/netdomjoin-gui %buildroot%_sbindir/netdomjoin-gui
mkdir -p %buildroot%_pixmapsdir/%name
install -m 644 %samba_source/lib/netapi/examples/netdomjoin-gui/samba.ico %buildroot%_pixmapsdir/%name/samba.ico
install -m 644 %samba_source/lib/netapi/examples/netdomjoin-gui/logo.png %buildroot%_pixmapsdir/%name/logo.png
install -m 644 %samba_source/lib/netapi/examples/netdomjoin-gui/logo-small.png %buildroot%_pixmapsdir/%name/logo-small.png

mkdir -p %buildroot%_man1dir
mkdir -p %buildroot%_man5dir
mkdir -p %buildroot%_man7dir
mkdir -p %buildroot%_man8dir
install -m 644 docs-xml/output/manpages-3/*.1 %buildroot%_man1dir
install -m 644 docs-xml/output/manpages-3/*.5 %buildroot%_man5dir
install -m 644 docs-xml/output/manpages-3/*.7 %buildroot%_man7dir
install -m 644 docs-xml/output/manpages-3/*.8 %buildroot%_man8dir

rm -f %buildroot%_man1dir/editreg.1*
rm -f %buildroot%_man1dir/log2pcap.1*
rm -f %buildroot%_man1dir/smbsh.1*
#rm -f %buildroot%_man1dir/smbget.1*
rm -f %buildroot%_man5dir/smbgetrc.5*
rm -f %buildroot%_man1dir/vfstest.1*
rm -f %buildroot%_man1dir/testprns.1*
rm -f %buildroot%_man8dir/smbmount.8*
rm -f %buildroot%_man8dir/smbmnt.8*
rm -f %buildroot%_man8dir/smbumount.8*

#rm -f %buildroot%_libdir/libtalloc.so.*
#rm -f %buildroot%_includedir/talloc.h
#rm -f %buildroot%_libdir/libtalloc.so
#rm -f %buildroot%_pkgconfigdir/talloc.pc

#rm -f %buildroot%_libdir/libtdb.so.*
#rm -f %buildroot%_includedir/tdb.h
#rm -f %buildroot%_libdir/libtdb.so
#rm -f %buildroot%_pkgconfigdir/tdb.pc
rm -f %buildroot%_bindir/tdbbackup
rm -f %buildroot%_bindir/tdbdump
rm -f %buildroot%_bindir/tdbtool
rm -f %buildroot%_man8dir/tdbbackup.8*
rm -f %buildroot%_man8dir/tdbdump.8*
rm -f %buildroot%_man8dir/tdbtool.8*

#cups backend
%define cups_serverbin %(cups-config --serverbin 2>/dev/null)
mkdir -p %buildroot%{cups_serverbin}/backend
ln -s %_bindir/smbspool %buildroot%{cups_serverbin}/backend/smb

pushd %buildroot/%_datadir/swat/help
ln -sf ../../doc/samba-doc-%version/htmldocs/manpages-3/ ./manpages
ln -sf ../../doc/samba-doc-%version/htmldocs/Samba3-HOWTO/
ln -sf ../../doc/samba-doc-%version/htmldocs/Samba3-ByExample/
ln -sf ../../doc/samba-doc-%version/htmldocs/Samba3-Developers-Guide/
popd

mkdir -p %buildroot/%systemd_unitdir
install -m644 smb.service %buildroot/%systemd_unitdir/
install -m644 nmb.service %buildroot/%systemd_unitdir/
install -m644 winbind.service %buildroot/%systemd_unitdir/

%find_lang pam_winbind
%find_lang net

%post
%post_service smb
%post_service nmb

%preun
%preun_service smb
%preun_service nmb

%post common
#migrate samba 3.0.x kerberos settings
grep 'use kerberos keytab' /etc/samba/smb.conf | \
    grep -iq yes && \
    subst 's/^use kerberos keytab.*$/dedicated keytab file = \/etc\/krb5.keytab\nkerberos method = dedicated keytab/' \
    /etc/samba/smb.conf
true

%pre winbind
%_sbindir/groupadd -g 88 wbpriv >/dev/null 2>&1 || :

%post winbind
%post_service winbind

%preun winbind
%preun_service winbind

%files
%_sbindir/smbd
%_sbindir/nmbd
%_bindir/mksmbpasswd.sh
%_bindir/smbstatus
%_bindir/eventlogadm
%config(noreplace) %_sysconfdir/samba/smbusers
%attr(755,root,root) %_initdir/smb
%attr(755,root,root) %_initdir/nmb
%systemd_unitdir/smb.service
%systemd_unitdir/nmb.service
%config(noreplace) %_sysconfdir/logrotate.d/samba
%config(noreplace) %_sysconfdir/pam.d/samba
%_man7dir/samba.7*
%_man8dir/nmbd.8*
%_man8dir/smbd.8*
%_man8dir/eventlogadm.8*
%_man8dir/vfs_*.8*
%_libdir/samba/vfs
%_libdir/samba/auth
%_libdir/samba/charset
%attr(1777,root,root) %dir /var/spool/samba
%dir %_sysconfdir/openldap/schema
%_sysconfdir/openldap/schema/samba.schema

%doc examples/autofs examples/LDAP examples/libsmbclient examples/misc examples/printer-accounting
%doc examples/printing

%files swat
%config(noreplace) %_sysconfdir/xinetd.d/swat
%_datadir/swat
%_sbindir/swat
%_man8dir/swat.8*
%attr(755,root,root) %_libdir/samba/*.msg

%files client
%_bindir/rpcclient
%_bindir/smbcacls
%_bindir/findsmb
%_bindir/smbget
%_bindir/nmblookup
%_bindir/smbclient
%_bindir/smbprint
%_bindir/smbspool
%_bindir/smbtar
%_bindir/smbtree
%_bindir/sharesec
%_bindir/smbta-util
%{cups_serverbin}/backend/smb
%_man1dir/findsmb.1*
%_man1dir/nmblookup.1*
%_man1dir/rpcclient.1*
%_man1dir/smbcacls.1*
%_man1dir/smbclient.1*
%_man1dir/smbtar.1*
%_man1dir/smbtree.1*
%_man1dir/smbget.1*
%_man1dir/sharesec.1*
%_man8dir/smbspool.8*
%_man8dir/smbta-util.8*

%files common -f net.lang
%attr(755,root,root) /%_lib/security/pam_smbpass.so
%dir %_libdir/samba
%_libdir/samba/lowcase.dat
%_libdir/samba/upcase.dat
%_libdir/samba/valid.dat
%_bindir/net
%_bindir/testparm
%_bindir/smbpasswd
%_bindir/pdbedit
%_bindir/profiles
%_bindir/smbcquotas
%_bindir/smbcontrol
%dir /var/lib/samba
%attr(700,root,root) %dir /var/lib/samba/private
%dir /var/lib/samba/scripts
%config(noreplace) %_sysconfdir/samba/smb.conf
%config(noreplace) %_sysconfdir/samba/lmhosts
%config(noreplace) %_sysconfdir/sysconfig/samba
%dir %_sysconfdir/samba
%attr(0700,root,root) %dir /var/log/samba
%attr(0700,root,root) %dir /var/log/samba/old
%_man1dir/profiles.1*
%_man1dir/smbcquotas.1*
%_man1dir/smbcontrol.1*
#%_man1dir/vfstest.1*
%_man1dir/testparm.1*
%_man1dir/smbstatus.1*
%_man5dir/smbpasswd.5*
%_man5dir/smb.conf.5*
%_man5dir/lmhosts.5*
%_man8dir/smbpasswd.8*
%_man8dir/pdbedit.8*
%_man8dir/net.8*
%doc README COPYING Manifest
%doc WHATSNEW.txt Roadmap

%files -n libnetapi
%attr(755,root,root) %_libdir/libnetapi.so.*

%files -n libnetapi-devel
%_libdir/libnetapi.so
%_includedir/netapi.h
%_pkgconfigdir/netapi.pc

%files winbind -f pam_winbind.lang
%_bindir/ntlm_auth
%_bindir/wbinfo
%_libdir/samba/idmap
%_libdir/samba/nss_info
%_sbindir/winbindd
%dir /var/run/winbindd
%attr(750,root,wbpriv) %dir /var/lib/samba/winbindd_privileged
%config(noreplace) %_sysconfdir/security/pam_winbind.conf
%_initdir/winbind
%systemd_unitdir/winbind.service
%_man1dir/ntlm_auth.1*
%_man1dir/wbinfo.1*
%_man8dir/pam_winbind.8*
%_man5dir/pam_winbind.conf.5*
%_man7dir/winbind_krb5_locator.7*
%_man8dir/winbindd.8*
%_man8dir/idmap_*.8*

%files winbind-clients
%_libdir/libnss_winbind.so
/%_lib/libnss_winbind.so.2
%_libdir/libnss_wins.so
/%_lib/libnss_wins.so.2
/%_lib/security/pam_winbind.so
%attr(755,root,root) %_libdir/libwbclient.so.*

%files winbind-devel
%_includedir/wbclient.h
%_libdir/libwbclient.so
%_pkgconfigdir/wbclient.pc

%files doc
%doc docs-xml/output/htmldocs

%files -n libsmbclient
%attr(755,root,root) %_libdir/libsmbclient.so.*
%attr(755,root,root) %_libdir/libsmbsharemodes.so.*

%files -n libsmbclient-devel
%_includedir/libsmbclient.h
%_includedir/smb_share_modes.h
%_libdir/libsmbclient.so
%_libdir/libsmbsharemodes.so
%_pkgconfigdir/smbclient.pc
%_pkgconfigdir/smbsharemodes.pc
%_man7dir/libsmbclient.7*

%files domainjoin-gui
%_sbindir/netdomjoin-gui
%dir %_pixmapsdir/samba
%_pixmapsdir/samba/samba.ico
%_pixmapsdir/samba/logo.png
%_pixmapsdir/samba/logo-small.png

%changelog
* Tue Jun 26 2012 Vitaly Kuznetsov <vitty@altlinux.ru> 3.6.6-alt1
- 3.6.6

* Thu May 03 2012 Vitaly Kuznetsov <vitty@altlinux.ru> 3.6.5-alt2
- add systemd unit files

* Wed May 02 2012 Vitaly Kuznetsov <vitty@altlinux.ru> 3.6.5-alt1
- 3.6.5 (CVE-2012-2111)

* Mon Apr 23 2012 Vitaly Kuznetsov <vitty@altlinux.ru> 3.6.4-alt2
- rebuild with krb5-1.10

* Wed Apr 11 2012 Vitaly Kuznetsov <vitty@altlinux.ru> 3.6.4-alt1
- 3.6.4 (CVE-2012-1182)

* Tue Feb 07 2012 Vitaly Kuznetsov <vitty@altlinux.ru> 3.6.3-alt1
- 3.6.3 (CVE-2012-0817)

* Thu Jan 26 2012 Vitaly Kuznetsov <vitty@altlinux.ru> 3.6.2-alt1
- 3.6.2

* Thu Aug 11 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 3.6.0-alt1
- 3.6.0

* Mon Aug 01 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 3.5.10-alt2
- CVE-2011-2724

* Thu Jul 28 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 3.5.10-alt1
- 3.5.10 (CVE-2011-2522, CVE-2011-2694)

* Tue Jul 26 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 3.5.9-alt2
- add docfiles location links to swat package (ALT #25909)

* Mon Jun 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 3.5.9-alt1
- 3.5.9

* Tue Mar 22 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 3.5.8-alt3
- move cifs.upcall to /sbin

* Fri Mar 18 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 3.5.8-alt2
- build with CIFS_DISABLE_SETUID_CHECK and CIFS_LEGACY_SETUID_CHECK

* Tue Mar 08 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 3.5.8-alt1
- 3.5.8

* Mon Feb 28 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 3.5.7-alt1
- 3.5.7 (CVE-2011-0719)

* Fri Oct 15 2010 Vitaly Kuznetsov <vitty@altlinux.ru> 3.5.6-alt1
- 3.5.6
- fix smb.conf.5 assembly (ALT #24303)

* Tue Sep 14 2010 Vitaly Kuznetsov <vitty@altlinux.ru> 3.5.5-alt1
- 3.5.5 (CVE-2010-3069)

* Sun Aug 22 2010 Vitaly Kuznetsov <vitty@altlinux.ru> 3.5.4-alt1
- 3.5.4

* Thu Jul 01 2010 Vitaly Kuznetsov <vitty@altlinux.ru> 3.5.2-alt1
- 3.5.2 with rhel6beta2 patches

* Thu Jun 24 2010 Vitaly Kuznetsov <vitty@altlinux.ru> 3.4.8-alt3
- samba.pamd: use common-login

* Tue Jun 01 2010 Vitaly Kuznetsov <vitty@altlinux.ru> 3.4.8-alt2
- symlink for cups backend resurrected (ALT #23575)

* Thu May 20 2010 Vitaly Kuznetsov <vitty@altlinux.ru> 3.4.8-alt1
- 3.4.8

* Thu May 13 2010 Vitaly Kuznetsov <vitty@altlinux.ru> 3.4.4-alt3
- packaged doc as noarch
- rebased onto upstream git

* Wed May 12 2010 Vitaly Kuznetsov <vitty@altlinux.ru> 3.4.4-alt2
- add provides for samba-client-cups/samba-utils

* Wed May 12 2010 Vitaly Kuznetsov <vitty@altlinux.ru> 3.4.4-alt1
- build from el6 for ALT

* Wed Nov 25 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.0.37-alt1.1
- Rebuilt with python 2.6

* Thu Oct 01 2009 Alexander Bokovoy <ab@altlinux.org> 3.0.37-alt1
- Security fixes:
    + CVE-2009-2813
    + CVE-2009-2906
    + CVE-2009-2948

* Sun Sep 20 2009 Dmitry V. Levin <ldv@altlinux.org> 3.0.36-alt3.1
- NMU.
- Uncompressed main tarball to ease its signature verification and
  to decrease srpm size.
- Resurrected libsmbclient smbc_attr_server fix.

* Tue Sep 15 2009 Alexander Bokovoy <ab@altlinux.org> 3.0.36-alt3
- Fixed:
    + #20167: delete restart from logrotate script
    + install proper build documentation, override stock one

* Mon Sep 14 2009 Alexander Bokovoy <ab@altlinux.org> 3.0.36-alt2
- Do not wait for Inkscape update, fix it by using abspath in paths passed to Inkscape

* Fri Aug 07 2009 Alexander Bokovoy <ab@altlinux.org> 3.0.36-alt1
- 3.0.36, final version in 3.0 series

* Tue Apr 07 2009 Alexander Bokovoy <ab@altlinux.org> 3.0.33-alt4
- Fix #19519: cover case when no options where specified

* Mon Mar 30 2009 Alexander Bokovoy <ab@altlinux.org> 3.0.33-alt3
- Back out static qualifier for smbc_attr_server, it is still used
  separately from libsmbclient in internal API of libmsrpc.

* Mon Mar 30 2009 Alexander Bokovoy <ab@altlinux.org> 3.0.33-alt2
- Backport cifs.upcall and updated mount.cifs/umount.cifs from 3.3 branch
  Fixed:
  + #19199
  + #15875
  + #17700
  + #18638

* Thu Nov 27 2008 Alexander Bokovoy <ab@altlinux.org> 3.0.33-alt1
- Security release 3.0.33:
  + CVE 2008-4314

* Sat Jul 19 2008 Alexander Bokovoy <ab@altlinux.org> 3.0.31-alt1
- 3.0.31:
  + added patches from v3-0-test
  + removed patch #44 (post 3.0.30 patches, accumulated in v3-0-test already)
  Fixed:
  + #16218
  + #16052
  + #4874
  + #16213

* Tue Jul 01 2008 Anton Farygin <rider@altlinux.ru> 3.0.30-alt3.1
- fixed build with autoconf-2.62
- fixed python requires

* Sat May 31 2008 Alexander Bokovoy <ab@altlinux.org> 3.0.30-alt3
- Fixed:
  + #5489 in Samba Bugzilla (Winbindd on PDC, jra)
  + #5504 in Samba Bugzilla (Winbindd wrong SIGTERM handling, jra)
  + Fix joining NT4 domains (gd)

* Thu May 29 2008 Alexander Bokovoy <ab@altlinux.org> 3.0.30-alt2
- Update documentation build to properly use networkless setup 

* Wed May 28 2008 Alexander Bokovoy <ab@altlinux.org> 3.0.30-alt1
- 3.0.30
- Security update for CVE-2008-1105

* Sun May 25 2008 Alexander Bokovoy <ab@altlinux.org> 3.0.29-alt1
- 3.0.29
- Fixed:
  + post release fixes from Steven Danneman (8dc4e979776)
  + removed ldb* manpages as ldb is only in Samba 3.2
  + removed manpages for VFS modules that are only in Samba 3.2
    or not supported in our Samba 3.0 build

* Sat Apr 12 2008 Alexander Bokovoy <ab@altlinux.org> 3.0.28a-alt3
- v3-0-test: Fixed bugs #5386, #5366 (Samba.org bugzilla)
- Removed rpcclient from samba-common, moved to samba-client.

* Fri Apr 11 2008 Alexander Bokovoy <ab@altlinux.org> 3.0.28a-alt2
- Accumulate post-3.0.28a fixes from 3-0-test git branch
- Add source/Makefile to samba-vfs-devel to satisfy out-of-tree builds of samba-vscan
- Improve documentation build, get back smbmount manpages
- Improve python bindings sub-package

* Tue Mar 25 2008 Alexander Bokovoy <ab@altlinux.org> 3.0.28a-alt1
- 3.0.28a
- Fixed:
  + pam_smbpass build
  + documentation build, including manpages
  + cups dependencies (libgnutls-devel is required to build any cups 
    client but libcups-devel lacks dependency)

* Fri Jan 25 2008 Grigory Batalov <bga@altlinux.ru> 3.0.28-alt1.1
- Rebuilt with python-2.5.

* Mon Dec 10 2007 Alexander Bokovoy <ab@altlinux.org> 3.0.28-alt1
- Fixed:
  + CVE-2007-6015:
  == Specifically crafted GETDC mailslot requests
  == can trigger a boundary error in the domain
  == controller GETDC mail slot support which
  == can be remotely exploited to execute arbitrary
  == code.
  + fix error path in local groups' addition (Volker)

* Mon Nov 26 2007 Alexander Bokovoy <ab@altlinux.org> 3.0.27a-alt1
- Fixed:
  + smbfs accesses to Samba 3.0.27 caused disruptions on server side in some situations

* Thu Nov 15 2007 Alexander Bokovoy <ab@altlinux.org> 3.0.27-alt1
- Security release 3.0.27:
  + CVS-2007-4572
    Stack buffer overflow in nmbd's logon request processing.
  + CVE-2007-5398
    Remote code execution in Samba's WINS server daemon (nmbd) 
    when processing name registration followed name query requests.
- Updated set of loadable modules:
  + added nss_info/rfc2307, nss_info/sfu, idmap/ad
- General spec file clean up
- Keep dependency on kernel-headers-std until Branch and Sisyphus policies
  would be synchronized

* Sun Nov 11 2007 Alexander Bokovoy <ab@altlinux.org> 3.0.26a-alt2
- Use git to handle the package
  + Fix #13210 (and a number of similar unreported bugs), now
    all pdb, auth, rpc, and idmap are included into %name-common

* Tue Sep 11 2007 Alexander Bokovoy <ab@altlinux.org> 3.0.26a-alt1
- Bugfix release
- Includes security fix for CVE-2007-4138

* Sun Sep 02 2007 Alexander Bokovoy <ab@altlinux.org> 3.0.25c-alt1
- New release
- Removed:
  + Python linkage patch, merged to upstream
- Added:
  + Post-release Python build fix patch from rev.24635 (Volker)

* Mon May 14 2007 Alexander Bokovoy <ab@altlinux.org> 3.0.25-alt1
- New release
- Security fixes for CVE-2007-2444, CVE-2007-2446, and CVE-2007-2447:
  + CVE-2007-2444
    Versions: Samba 3.0.23d - 3.0.25pre2
    Local SID/Name translation bug can result in user privilege elevation
  + CVE-2007-2446
    Versions: Samba 3.0.0 - 3.0.24
    Multiple heap overflows allow remote code execution
  + CVE-2007-2447
    Versions: Samba 3.0.0 - 3.0.24
    Unescaped user input parameters are passed as
    arguments to /bin/sh allowing for remote command
    execution
- Removed:
  + smbwrapper, as it is not supported anymore
- Fixed:
  + python build w.r.t. -pie

* Wed Apr 18 2007 Dmitry V. Levin <ldv@altlinux.org> 3.0.24-alt3
- Fixed /var/log/samba directory permissions (#5223).
- smbumount: Added mount options support (#11554).

* Tue Apr 17 2007 Dmitry V. Levin <ldv@altlinux.org> 3.0.24-alt2
- {smb,winbind}.init: Disabled by default (#11513).
- Relocated {mount,umount}.{cifs,smbfs} (#11124).
- Fixed -common %%pre script (#10799).

* Sat Feb 03 2007 Alexander Bokovoy <ab@altlinux.ru> 3.0.24-alt1
- 3.0.24: 3.0.23d plus security fixes:
  - CVE-2007-0454, only this one is relevant to ALT Linux distribution
  - CVE-2007-0453
  - CVE-2007-0452
- Fixed:
  - #10116, #3092

* Sat Jul 22 2006 Alexander Bokovoy <ab@altlinux.ru> 3.0.23a-alt1
- 3.0.23a 
- Removed:
  - XML, MySQL, and PgSQL experimental SAM backends (separate now)
- Fixed:
  - nss_wins lacked proper dependcies, fixed.

* Fri Jul 21 2006 Alexander Bokovoy <ab@altlinux.ru> 3.0.23-alt1
- 3.0.23
- Fixed:
  - get user token properly when winbindd is down (r17016, vlendec)
- Removed number of old patches and automount/NIS support
- Disabled documentation build by default, replaced by pre-built version

* Sun Feb 26 2006 Alexander Bokovoy <ab@altlinux.ru> 3.0.21c-alt1
- 3.0.21c 

* Tue Jan 31 2006 Vladimir Lettiev <crux@altlinux.ru> 3.0.21b-alt1
- 3.0.21b

* Sun Jan 08 2006 Vladimir Lettiev <crux@altlinux.ru> 3.0.21a-alt1
- 3.0.21a
- Fixed bugs: #6289, #6462, #7254
- hackaround smbcontrol bug (nmbd still exist after stopping service)

* Wed Dec 21 2005 Vladimir Lettiev <crux@altlinux.ru> 3.0.21-alt1
- 3.0.21
- use samba sources from svn branch SAMBA_3_0_RELEASE

* Wed Oct 19 2005 Vladimir Lettiev <crux@altlinux.ru> 3.0.21-alt0.pre1
- 3.0.21pre1
- updated samba-docs to 840 revision

* Sun Oct 16 2005 Vladimir Lettiev <crux@altlinux.ru> 3.0.20b-alt1
- 3.0.20b

* Fri Sep 16 2005 Vladimir Lettiev <crux@altlinux.ru> 3.0.20-alt2
- Post release patches:
	+ group_enum_v3 (ldap)
	+ AIX 5 & Win98 endless directory loop (samba bugs: #3010)
	+ Winbindd
	+ RegCreateKeyEx() Failures
	+ Usrmgr.exe and Groups
	+ net rpc shutdown (samba bugs: #3080)
	+ DOS Applications (samba bugs: #3044, #3060)
	+ x64 crashes
- Additional patches:
	+ statvfs-SAMBA-3.patch (VFS API's statvfs abstraction)

* Mon Aug 29 2005 Vladimir Lettiev <crux@altlinux.ru> 3.0.20-alt1
- 3.0.20
- added python module
- added utils package

* Wed Apr 20 2005 Alexander Bokovoy <ab@altlinux.ru> 3.0.14a-alt2
- Fixed:
    + the documentation Makefile phony targets
    + #6573
- 

* Sun Apr 17 2005 Alexander Bokovoy <ab@altlinux.ru> 3.0.14a-alt1
- 3.0.14a
- Fixed:
    + effective group id should be checked on delete requests too (jra)
    + a number of issues with documentation build
- Removed:
    + bin/editreg build as utils/editreg.c is too broken atm.
- Added:
    + pam_winbind manual page

* Thu Dec 16 2004 Dmitry V. Levin <ldv@altlinux.org> 3.0.10-alt1
- 3.0.10

* Sun Nov 21 2004 Vladimir Lettiev <crux@altlinux.ru> 3.0.9-alt1
- 3.0.9
- Fixed:
    + Problem updating roaming user profiles
    + Crash in smbd when printing from a Windows 9x client
    + Unresolved symbols in libsmbclient
    + Do not fail on setting file attributes with acl support enabled
- Updated samba-docs (SVN 20041121)
- Rediffed patches 17,38,40

* Sat Nov 13 2004 ALT QA Team Robot <qa-robot@altlinux.org> 3.0.8-alt1.1
- Rebuilt with openldap-2.2.18-alt3.

* Wed Nov 10 2004 Vladimir Lettiev <crux@altlinux.ru> 3.0.8-alt1
- 3.0.8 (include fix for CAN-2004-0930 -- smbd remote DoS vulnerability)

* Mon Nov 01 2004 Vladimir Lettiev <crux@altlinux.ru> 3.0.8-alt0.pre2.1
- 3.0.8pre2

* Wed Oct 27 2004 Vladimir Lettiev <crux@altlinux.ru> 3.0.8-alt0.pre1.2
- build documentation in pdf format (db2latex-xsl >= 0.8-alt0.pre1.2 required)
- gpl.tex replaced by gpl.xml

* Thu Sep 30 2004 Vladimir Lettiev <crux@altlinux.ru> 3.0.8-alt0.pre1.1
- 3.0.8pre1
- removed patches 1,2 (fixes included in upstream code)
- new documentation from cvs (20040930)
- added build dependency - dia (to generate png images)
- removed patch 20 (we don't build documentation in pdf format)
- changed patch 40 (to suit to small change in makefile)
- install section: corrected libsmclient.(a|so) installation
- new files: smbgetrc.5 (man), full_audit.so (vfs)

* Mon Sep 13 2004 Dmitry V. Levin <ldv@altlinux.org> 3.0.5-alt2
- Moved control files to separate package.
- Keep samba client helpers at mode "restricted" in the package,
  but default it to "wheelonly" in %%post when the package is
  first installed.  This avoids a race and fail-open behaviour.

* Sat Sep 11 2004 Dmitry V. Levin <ldv@altlinux.org> 3.0.5-alt1
- Applied patches from Gerald Carter.
- Fixed cifsmount.control.

* Tue Jul 20 2004 Stanislav Ievlev <inger@altlinux.org> 3.0.5-alt0.1
- 3.0.5

* Tue May 11 2004 ALT QA Team Robot <qa-robot@altlinux.org> 3.0.3-alt1.1
- Rebuilt with openssl-0.9.7d.

* Thu May 06 2004 Alexander Bokovoy <ab@altlinux.ru> 3.0.3-alt1
- Fixed:
    + smbwrapper breakage with 2.4 and 2.6 kernels (SYS_utimes)
    + MS04-012 security update broke Samba 3.0.3, fix it (Jeremy, Andrew Bartlett)
    + Rebuild with glibc 2.3 to get correct versioning for sendfile64

* Thu Apr 22 2004 Alexander Bokovoy <ab@altlinux.ru> 3.0.3-alt0.7
- 3.0.3RC1
- Fixed:
    + segfault in winbind (Volker Lendecke)
    + Adding a domain user to a XP local group did a lsalookupname on
      the user without domain prefix, and this then failed (Volker Lendecke)

* Wed Apr 14 2004 Alexander Bokovoy <ab@altlinux.ru> 3.0.3-alt0.6
- Fixed:
    + add missed provides: samba-client-devel for libsmbclient-devel subpackage

* Thu Apr 08 2004 Alexander Bokovoy <ab@altlinux.ru> 3.0.3-alt0.5
- Fixed:
    + #3937 (already fixed in 3.0.3-alt0.3)
- Updated:
    + Large documentation update:
	- Samba-3 by Example book by John Terpstra added
	- The Official Samba 3 HOWTO is complete now (with additional 5 chapters)

* Tue Apr 06 2004 Alexander Bokovoy <ab@altlinux.ru> 3.0.3-alt0.4
- Fixed:
    + #3923: separate libsmbclient shared library into libsmbclient package

* Tue Apr 06 2004 Alexander Bokovoy <ab@altlinux.ru> 3.0.3-alt0.3
- 3.0.3pre2
- Added:
    + ChangeLog for new subversion repository is in ChangeLog.svn.SAMBA_3_0.bz2
      Old ChangeLog is in ChangeLog.SAMBA_3_0.bz2
- Fixed:
    + smbfs issue (unconditional Tree Disconnect issued in cli_shutdown)
    + some mount.cifs fixes (Steve French)
    + postin scriplet fix in %name-common

* Fri Mar 26 2004 Alexander Bokovoy <ab@altlinux.ru> 3.0.3-alt0.2
- Fixed:
    + first time install was included into upgrade logic path

* Thu Mar 25 2004 Alexander Bokovoy <ab@altlinux.ru> 3.0.3-alt0.1
- 3.0.3pre1

* Wed Mar 17 2004 Alexander Bokovoy <ab@altlinux.ru> 3.0.2a-alt8
- Rebuild against Sisyphus
- Applied another pile of fixes from SAMBA_3_0 before 3.0.3pre1

* Tue Mar 16 2004 Alexander Bokovoy <ab@altlinux.ru> 3.0.2a-alt7
- Fixed:
    + Activate '\\' check in check_path_syntax() only for unix charsets
      that are known for having '\\' as second byte of multibyte character

* Fri Mar 12 2004 Alexander Bokovoy <ab@altlinux.ru> 3.0.2a-alt6
- Fixed:
    + resolve_wildcards() to use pstring instead of fstring
      because otherwise UTF-8 encoded name does not fit a buffer 
      (567 bytes in 255)
    + and smbclient too, use pstring instead fstring where filenames
      are processed
    + also, string overflow in vfs_recycle

* Wed Mar 10 2004 Alexander Bokovoy <ab@altlinux.ru> 3.0.2a-alt5
- 3.0.2a+fixes from SAMBA_3_0 branch for charset handling
- Fixed:
    + Wrap database relocation into preinstall scriptlet and run it
      only if we are upgrading from previous version. Make sure
      that smb and winbind services are correctly switched off and
      on before and after migration if needed.

* Tue Mar 02 2004 Alexander Bokovoy <ab@altlinux.ru> 3.0.2a-alt4
- Fixed:
    + Base relocation corner case with bases relocated at wrong location
      on previous update
- Added:
    + control facilities for cifsfs and smbfs now honor existing states on update

* Fri Feb 27 2004 Alexander Bokovoy <ab@altlinux.ru> 3.0.2a-alt3
- Fixed:
    + stupid problem with relocating databases into wrong location
    + name typo on cifsmount control facility

* Tue Feb 24 2004 Alexander Bokovoy <ab@altlinux.ru> 3.0.2a-alt2
- Fixed:
    + winbind and smb services are useful on level 5 too

* Sun Feb 15 2004 Alexander Bokovoy <ab@altlinux.ru> 3.0.2a-alt1
- Final 3.0.2a
- Updated:
    + documentation build is made non-interactive and does not
      require network access now
- Added:
    + %name-pdb-pgsql for PostgreSQL passdb backend
    + smbget in %name-common for wget-like resource fetches
- Removed:
    + utmp support in favor of smbstatus due to performance issues

* Thu Dec 11 2003 Alexander Bokovoy <ab@altlinux.ru> 3.0.1-alt0.3
- Final 3.0.1RC2
- Fixed:
    + #281, #875 in Samba Bugzilla
    + Uninitialized variable in passdb/passdb.c (Andy Polyakov)

* Wed Dec 10 2003 Alexander Bokovoy <ab@altlinux.ru> 3.0.1-alt0.2
- 3.0.1RC2
- Fixed:
    + Installation paths for manpages
    + Numerous links in both PDF and HTML versions of HOWTO Collection
- Added:
    + Build Samba-HOWTO-Collection and Samba-Developers-Guide in HTML
      explicitly

* Fri Dec 05 2003 Alexander Bokovoy <ab@altlinux.ru> 3.0.1-alt0.1
- 3.0.1rc1
- Added:
    + editreg, log2pcap, vfstest and their manpages
- Changed:
    + return to samba-* series, obsolete samba3-* ones
- Fixed:
    + samba-docs build for building with recent libxslt/xsltproc
    + Japanese and Turkish localisation for SWAT

* Thu Nov 27 2003 Alexander Bokovoy <ab@altlinux.ru> 3.0-alt46.2
- Since in AW there is no interactive user logons via PAM,
  system-auth-winbind does not to take care of pam_mkhomedir calls

* Fri Oct 31 2003 Alexander Bokovoy <ab@altlinux.ru> 3.0-alt46.1
- Rebuild for ALT Linux Sisyphus

* Thu Oct 30 2003 Alexander Bokovoy <ab@altlinux.ru> 3.0-alt46
- Added:
   + Specs for x86 and IQ31244 development board are integrated

* Thu Oct 30 2003 Alexander Bokovoy <ab@altlinux.ru> 3.0-alt45
- Fixed:
   + Fixes to check for wraps which could cause coredumps (jra)

* Tue Oct 28 2003 Alexander Bokovoy <ab@altlinux.ru> 3.0-alt44
- Added:
   + 3.0.1pre1
   + documentations from samba-docs CVS
- Fixed:
   + charset conversion in rNetServerGetInfo RAP call (ab)
   + script/installbin.sh fix updated

* Fri Oct 24 2003 Alexander Bokovoy <ab@altlinux.ru> 3.0-alt43
- Changed:
   + oem:version support now works for any combinations of OEM and version

* Fri Oct 10 2003 Alexander Bokovoy <ab@altlinux.ru> 3.0-alt42
- Fixed:
   + Bug #3144 (http://bugzilla.altlinux.ru)

* Tue Sep 30 2003 Alexander Bokovoy <ab@altlinux.ru> 3.0-alt41
- 3.0.0 final + post release fixes
- Added:
   + cifsvfs mount helper and control(8) support to it
   + Use only LinuxPAM and ignore OpenPAM
- Fixed:
   + SWAT tables (#413 in Samba's bugzilla, tpot)
   + Fix broken wins hook functionality (#528 in Samba's bugzilla, tpot)
   + Fix for valid users = %%S in homes share (jra)
   + documentation updated

* Fri Sep 19 2003 Alexander Bokovoy <ab@altlinux.ru> 3.0-alt40
- Fixed:
   + The -P option to smbclient no longer works - update all 
     smbprint scripts to remove it. (#473 in Samba's bugzilla, tpot)
   + 32 bit field in the user structs is actually 2 16-bit fields,
     bad_password_count and logon_count. JRA.

* Thu Sep 18 2003 Alexander Bokovoy <ab@altlinux.ru> 3.0-alt39
- Fixed
   + default ACEs
   + Fix for #470 - unable to display SIDs in ACLs. JRA.

* Wed Sep 17 2003 Alexander Bokovoy <ab@altlinux.ru> 3.0-alt38
- RC4+fixes
- Fixed:
   + NTLMv2 signing bug (#442 in Samba's bugzilla) which prevented
     mixed mode domain join

* Fri Sep 12 2003 Alexander Bokovoy <ab@altlinux.ru> 3.0-alt37
- Back out NTLMv2 patch as suspect to mixed mode domain join failure

* Thu Sep 11 2003 Alexander Bokovoy <ab@altlinux.ru> 3.0-alt36
- Fixed:
   + LDAP code didn't convert from/to UTF-8 in all cases (JRA)

* Wed Sep 10 2003 Alexander Bokovoy <ab@altlinux.ru> 3.0-alt35
- Fixed:
   + getgrouplist() enabler is moved to separate patch 39
   + machine account password change (jra)
   + typo fix which caused CPU spin (jra, Markus Ungermann)
- Added:
   + ability to change vendor string through smb.conf (oem: version)

* Wed Sep 10 2003 Alexander Bokovoy <ab@altlinux.ru> 3.0-alt34
- Fixed:
   + Optimisation in iconv(3) usage paths which broke non-ASCII (jra)

* Tue Sep 09 2003 Alexander Bokovoy <ab@altlinux.ru> 3.0-alt33
- RC3+fixes
- Added:
   + Allow getgrouplist() on glibc-2.2.6-alt0.10 as it contains 
     needed fix for CAN-2003-0689

* Mon Sep 01 2003 Alexander Bokovoy <ab@altlinux.ru> 3.0-alt32
- Rebuild for ALT Linux Sisyphus

* Mon Sep 01 2003 Alexander Bokovoy <ab@altlinux.ru> 3.0-alt31
- RC2 + fixes
- Added:
   + Return back Using Samba (2nd edition)
- Fixed:
   + CP850 and CP437 now provided by Samba itself on platforms
     which do not support iconv

* Fri Aug 22 2003 Alexander Bokovoy <ab@altlinux.ru> 3.0-alt30
- Fixed:
   + charset issues in nmbd
   + default charset behaviour for Solaris and iconv
- Disabled:
   + temprorary not package Using Samba as it moved to separate CVS module

* Fri Aug 22 2003 Alexander Bokovoy <ab@altlinux.ru> 3.0-alt29
- Attempt to fix mixed mode joining errors

* Wed Aug 20 2003 Alexander Bokovoy <ab@altlinux.ru> 3.0-alt28
- Use new version scheme

* Wed Aug 20 2003 Alexander Bokovoy <ab@altlinux.ru> 3.0-alt27
- 3.0RC1+post fixes

* Wed Aug 06 2003 Alexander Bokovoy <ab@altlinux.ru> 3.0-alt26
- CVS SAMBA_3_0 up to 2003/08/06

* Tue Jul 29 2003 Alexander Bokovoy <ab@altlinux.ru> 3.0-alt25
- Fixed:
   + user/group enumeration when RA == 0 (was broken since alt23) (jerry)
   + return code for quota flags change when we have no priviledges to do so (metze)

* Tue Jul 29 2003 Alexander Bokovoy <ab@altlinux.ru> 3.0-alt24
- Refine dependencies between subpackages
- Fix NT quotas and integrate them into upstream

* Mon Jul 28 2003 Alexander Bokovoy <ab@altlinux.ru> 3.0-alt23
- Updated:
   + Patch from Stephan Metzemacher for default_quota
   + Patch from Stephan Metzemacher for NT quota
   + CVS SAMBA_3_0 up to 2003/07/28
   + Re-added samba-3.0.release.tar.bz2 (as of beta3)

* Wed Jul 16 2003 Alexander Bokovoy <ab@altlinux.ru> 3.0-alt22
- 3.0beta3+post fixes
- Build documentation by default from Docbook sources
- remove convert_smbpassword as outdated script
- Fixed:
  + smbpasswd false errors when /etc/samba/smbpasswd does not exist

* Tue Jul 15 2003 Alexander Bokovoy <ab@altlinux.ru> 3.0-alt21
- Major re-arrangement of files between sub-packages, it makes
  more reasonable split of binaries according to their purpose.
  Also, a number of missing manpages were added.
- Spec file unification for ALT Linux and ApplianceWare versions.
- Defaults:
   + ALT Linux: build xml and mysql passdb, use well-commented smb.conf
   + AW: disable xml and mysql passdb, use specific smb.conf

* Wed Jul 09 2003 Alexander Bokovoy <ab@altlinux.ru> 3.0-alt20
- Changed:
    + Make %name-pdb-xml dependant on --enable/--disable xml
    + Make %name-pdb-mysql dependant on --enable/--disable mysql
    + Default for both is 'enable'
    + PreRequires glibc-gconv-modules

* Tue Jul 08 2003 Alexander Bokovoy <ab@altlinux.ru> 3.0-alt19
- Changed:
    + smb and winbind initscripts are using start-stop-daemon now
- Added:
    + reload-config command to smbcontrol. smbd, nmbd, and winbindd are aware of it.
    
* Tue Jul 08 2003 Alexander Bokovoy <ab@altlinux.ru> 3.0-alt18
- Stick to 2003-07-06 spanshot as Jerry and Jeremy started to rewrite
  bits of Auth and Idmap now and SAMBA_3_0 is broken currently.
- Apply open-dev-inode patch

* Fri Jul 04 2003 Alexander Bokovoy <ab@altlinux.ru> 3.0-alt17
- Apply Andrew Bartlett's LDAP fixes, to eliminate last bits of 
  idmap problems in beta2

* Fri Jul 04 2003 Alexander Bokovoy <ab@altlinux.ru> 3.0-alt16
- Fix idmap_init ignoring 'idmap backend' option
- Back out Jeremy's fixes to strupper/strlower as they are incomplete 
  and broke the build.

* Wed Jul 02 2003 Alexander Bokovoy <ab@altlinux.ru> 3.0-alt15
- 3.0beta2
- Updated:
   + release-cvs patch to include diff between SAMBA_3_0_RELEASE 
     and SAMBA_3_0 (only version string so far)

* Tue Jul 01 2003 Alexander Bokovoy <ab@altlinux.ru> 3.0-alt14
- Prepare for beta2
- Apply metze's move of default quota to VFS module
- Enable 'inherit acls' and 'inherit permissions' by default

* Wed Jun 25 2003 Alexander Bokovoy <ab@altlinux.ru> 3.0-alt12
- pre-beta2 (2003-06-25)

* Mon Jun 09 2003 Alexander Bokovoy <ab@altlinux.ru> 3.0-alt11
- Samba 3.0 beta 1 + post fixes for client plaintext auth
- Updated:
   + system-winbind pam module to reflect base packages
- Removed:
   + NT quota patch -- integrated into upstream

* Wed May 14 2003 Alexander Bokovoy <ab@altlinux.ru> 3.0-alt10
- 2003-05-14
- Fixed:
    + VFS API macros prefixes with SMB_ to avoid clashes with 
      system-specific VFS_ macros on some platforms (AIX)
    + Quota configuration now runs test cases during configure to
      gather detailed information about quota API divergence
- Added:
    + new idmap
    + new LDAP schema -- read examples/LDAP!

* Mon May 12 2003 Alexander Bokovoy <ab@altlinux.ru> 3.0-alt9
- 2003-05-12
- Fixed:
    + Cascaded VFS to finally support per-module local data storage
      (metze, ab, jelmer)
    + NT quotas stuff (metze, ab)

* Fri Apr 25 2003 Alexander Bokovoy <ab@altlinux.ru> 3.0-alt8
- Added:
    + Stephan Metzmacher's NT Quotas support (experimental)
    + post alpha23 (See ChangeLog.SAMBA_3_0)
    + support for winbindd privileged pipe for winbind group members
- Splitted:
    + pdb_xml to %name-pdb-xml
    + pdb_mysql to %name-pdb-mysql

* Wed Feb 05 2003 Alexander Bokovoy <ab@altlinux.ru> 3.0-alt7
- Fixed:
    + gencache must try to reopen its database in read-only mode
      if read-write/creation failed in order to keep non-priviledged
      clients continue working.

* Tue Feb 04 2003 Alexander Bokovoy <ab@altlinux.ru> 3.0-alt6
- alpha21 (SAMBA_3_0 as of 2003-02-04)
- control(8) support added for smbmount
- sendfile support enabled by default
- Add ntml_auth helper and smbgroupedit.8 man page

* Fri Aug 09 2002 Stanislav Ievlev <inger@altlinux.ru> 3.0-alt5.1
- fixed suid/sgid file permissions
- building is no SMP compatible

* Wed Aug 07 2002 Alexander Bokovoy <ab@altlinux.ru> 3.0-alt5
- Update to alpha18+post CVS fixes (really tons of changes)
- Updated:
    + Cascaded VFS integrated to upstream (ab, idra, abartlet)
    + Jan Kara quotas support
- Fixed:
    + block.so to use asprintf instead of strcat
    + spec file synchronized with 2.2 branch, new subpackages added
      (client-devel[-static], client-cups, vfs)

* Fri May 17 2002 Alexander Bokovoy <ab@altlinux.ru> 3.0-alt4
- Fixed:
    + paths for piddir, lockdir, and swat
- Slightly modified build procedure to deal with SMP builds

* Thu Apr 18 2002 Alexander Bokovoy <ab@altlinux.ru> 3.0-alt3
- Fixed:
    + xinet.d restart should affect samba3-swat only

* Thu Apr 18 2002 Alexander Bokovoy <ab@altlinux.ru> 3.0-alt2
- Fixed:
    + Wrong requires (samba-common instead of samba3-common)
    + lockdir should be specified directly now

* Mon Apr 15 2002 Alexander Bokovoy <ab@altlinux.ru> 3.0-alt1
- Merge ApplianceWare changes into ALT Linux
- Added
    + Cascaded VFS patch (me)
    + Smbfs unicode fixes ported from 2.2 (me)
- Changed:
    + smb.conf to follow 3.0 development

* Fri Apr 05 2002 Alexander Bokovoy <ab@optifacio.com> 3.0-16aw
- Fix libcap dependency

* Wed Apr 03 2002 Alexander Bokovoy <ab@optifacio.com> 3.0-15aw
- Fix dependencies for vfs devel package

* Tue Apr 02 2002 Alexander Bokovoy <ab@optifacio.com> 3.0-13aw
- Integrated latest spec changes from ALT Linux
- Prepared VFS devel package

* Fri Mar 29 2002 Alexander Bokovoy <ab@optifacio.com> 3.0-12aw
- Fixed:
    + nmbd shutdown bug (rewritten shutdown process)
    + AD paged controls bug

* Mon Mar 25 2002 Alexander Bokovoy <ab@optifacio.com> 3.0-11aw
- Bring back libnss_winbind.so build

* Mon Mar 25 2002 Alexander Bokovoy <ab@optifacio.com> 3.0-10aw
- Updated:
    + aw-smbstatus patch
    
* Mon Mar 25 2002 Alexander Bokovoy <ab@optifacio.com> 3.0-9aw
- Fixed:
    + bug with file truncate (#0001081)
    + initscript for nmbd

* Wed Mar 06 2002 Alexander Bokovoy <ab@optifacio.com> 3.0-8aw
- Fixed:
    + initscript for nmbd

* Mon Feb 18 2002 Alexander Bokovoy <ab@optifacio.com> 3.0-6aw
- Fixed:
    + net ads
    + signed/unsigned

* Fri Feb 15 2002 Alexander Bokovoy <ab@optifacio.com> 3.0-5aw
- Fixed:
    + Bug in 'net ads'

* Wed Feb 06 2002 Alexander Bokovoy <ab@optifacio.com> 3.0-4aw
- Uncommented smbpasswd

* Fri Feb 01 2002 Alexander Bokovoy <ab@optifacio.com> 3.0-3aw
- Samba CVS [20020201] update
- Fixed patch for smbstatus
- Reviewed set of utils

* Wed Jan 30 2002 Alexander Bokovoy <ab@optifacio.com> 3.0-2aw
- Use 3.0a14 as base

* Mon Jan 28 2002 Alexander Bokovoy <ab@optifacio.com> 3.0-1aw
- Move to 3.0

* Thu Jan 17 2002 Alexander Bokovoy <ab@optifacio.com> 2.2.2-alt11
- Fixed:
    + winbind default domain patch (me)
    + smb.conf (code pages information corrected, move to use own config)
    + popup message translation (Ihar Viarheichyk)
- Removed:
    + support for pam_smbpass, use winbind instead
- Changed:
    + changed attributes for smbmount/smbmnt to comply with relaity
    + winbindd moved to samba-common (server isn't required for its usage)
    + CUPS support splitted to samba-client-cups

* Fri Jan 04 2002 Alexander Bokovoy <ab@optifacio.com> 2.2.2-alt10
- Fixed:
    + bug in smbclient -L (jeremy)

* Fri Dec 21 2001 Alexander Bokovoy <ab@optifacio.com> 2.2.2-alt9
- Fixed:
    + pam_winbind's parse_domain_user updated to current version
    + system-auth-winbind updated to pam-config 1.1.1-alt1

* Thu Dec 20 2001 Alexander Bokovoy <ab@optifacio.com> 2.2.2-alt8
- Fixed:
    + winbind default domain patch (created new one)
    + Alpha_strcpy patch merged to upstream
- Updated:
    + system-auth-winbind to follow TCB integration
- Added:
    + make proto and winbindd_proto calls (they work again)

* Fri Nov 30 2001 Alexander Bokovoy <ab@optifacio.com> 2.2.2-alt7
- Build with new winbind code from HEAD

* Tue Nov 20 2001 Alexander Bokovoy <ab@optifacio.com> 2.2.2-alt6
- Fixed:
    + stop connection away problems (Tom Jansen)
    + error code handling in smbwrapper (new clierr code sync)
- Removed:
    + make proto call (prototypes for quotas get broken after it)

* Mon Nov 19 2001 Alexander Bokovoy <ab@optifacio.com> 2.2.2-alt5
- Fixed:
    + alpha_strcpy to handle non-latin1 characters (Ihar Viarheichyk)
    + back port of working Winbindd from HEAD (Jeremy Allison)
    + client-enc patch merged into upstream
    + pam_smbpass to remove conflicting namespaces with lib/util.c
- Updated:
    + Unified workgroup name patch
- Things left to do:
    + UTF-8 patch (Ihar Viarheichyk)

* Thu Nov 01 2001 Alexander Bokovoy <ab@optifacio.com> 2.2.2-alt4
- Fixed bug with non-ascii letters in smbclient and user and domain names
  More work is needed on user/domain area though. (Ihar Viarheichyk)
- Preparations for UTF-8/Unicode internal string processing patch by Ihar Viarheichyk
- Added recent ChangeLog for SAMBA_2_2 branch
- Version string changed to "ALT Linux/2.2.2" in order to comply with Tridge's call
  for easy identification of vendor-specific versions

* Sat Oct 20 2001 Dmitry V. Levin <ldv@alt-linux.org> 2.2.2-alt3
- Moved documentation to separate subpackage.
- Corrected documentation a bit, to fix dependencies.

* Thu Oct 18 2001 Alexander Bokovoy <ab@optifacio.com> 2.2.2-alt2
- rebuild against new glibc
- fix of spec cleanup for _shareddir.
- Fix Swat location for FHS conformance

* Mon Oct 15 2001 Alexander Bokovoy <ab@optifacio.com> 2.2.2-alt1
- 2.2.2
- minor spec clean up (Grigory Milev)

* Thu Oct 11 2001 Alexander Bokovoy <ab@optifacio.com> 2.2.1a-alt11
- Fixed:
+ Memory leaks in Winbindd (close to final fix)
+ SAM management
+ Most patches were successfully integrated into mainstream
- Last build of 2.2.2-pre, next one should be official 2.2.2
- Added:
+ System auth via winbind (fixed spelling errors in Mandrake's version)

* Thu Aug 30 2001 Alexander Bokovoy <ab@optifacio.com> 2.2.1a-alt10
- Fixed:
+ Winbindd talloc, new shiny challenge encryption protocols (tpot)
+ pam_smbpass and smb_passwd API changes (Steve Langasek and me, patch #516)
- Added:
+ preliminary support for ACLs

* Mon Aug 20 2001 Alexander Bokovoy <ab@optifacio.com> 2.2.1a-alt9
- Fixed:
+ Winbindd with some realoc-related problems
- Updated documentation (patch #30 has been merged into mainstream)

* Mon Aug 13 2001 Alexander Bokovoy <ab@optifacio.com> 2.2.1a-alt8
- Fixed:
+ Winbindd to properly set up default workgroup name
+ Winbindd to validate against current domain, not default one
- Added:
+ Winbind init script

* Mon Aug 13 2001 Alexander Bokovoy <ab@optifacio.com> 2.2.1a-alt7
- Fixed:
+ Symlinks /sbin/mount.smb and /sbin/mount.smbfs now point to /usr/bin/smbmount
+ SWAT documentation for winbindd has been fixed (samedit is outdated)

* Mon Aug 13 2001 Alexander Bokovoy <ab@optifacio.com> 2.2.1a-alt6
- Various fixes in /etc/samba/smb.conf
- Patch 21 is removed
- NSS patch for seamless domain integration enhanced. Users from default
  domain now are accepted without explicit DOMAIN exposure in the username.

* Wed Aug 08 2001 Alexander Bokovoy <ab@optifacio.com> 2.2.1a-alt5
- Symlink for libnss_winbind.so.2 added
- pam_smbpass.so and smbwrapper.so moved to /lib/security
- Help about pam_smbpass is added in README.pam_smbpass and into
  examples/pam_smbpass

* Wed Aug 08 2001 Alexander Bokovoy <ab@optifacio.com> 2.2.1a-alt4
- First build with Winbind support integrated
- See winbindd(8), smb.conf(5) for proper configuration
- Buildreq fixed for cups-devel (libcups-devel)
- smb start up script is fixed

* Tue Jul 31 2001 Stanislav Ievlev <inger@altlinux.ru> 2.2.1a-alt3
- Light spec cleanup.
- Returned right version of /etc/rc.d/init.d/smb

* Thu Jul 19 2001 AEN <aen@logic.ru> 2.2.1a-alt2
- fix permissions on /var/spool/samba
* Thu Jul 12 2001 AEN <aen@logic.ru> 2.2.1a-alt1
- 2.2.1a
- %post fixed

* Wed Jul 11 2001 AEN <aen@logic.ru> 2.2.1-alt7
- PreReq: libcups in samba-common
* Wed Jul 11 2001 AEN <aen@logic.ru> 2.2.1-alt6
- build oficial release
- sync with MDK

* Wed Jun 27 2001 AEN <aen@logic.ru> 2.2.1-alt5
- smb.init fixed -- thnx to  Sviatoslav Sviridov

* Sun Jun 24 2001 AEN <aen@logic.ru> 2.2.1-alt4
- new code with security fix
- %preun_service macros name fixed

* Thu Jun 14 2001 AEN <aen@logic.ru> 2.2.1-alt3
- cups problem  solved (patch from mdk)

* Wed May 30 2001 AEN <aen@logic.ru> 2.2.1-alt2
- new code from CVS
- configuration files moved to /etc/samba
- sync with MDK

* Mon May 21 2001 AEN <aen@logic.ru> 2.2.1-alt1
- new version
- alt patch adopted

* Wed Apr 25 2001 AEN <aen@logic.ru> 2.2.0-alt2
- inetd problem fixed
- sync with MDK

* Thu Apr 19 2001 AEN <aen@logic.ru> 2.0.8-alt2
- tmpdir patch

* Wed Apr 18 2001 AEN <aen@logic.ru>
- 2.0.8
- rh patches

* Wed Apr 18 2001 AEN <aen@logic.ru> 2.2.0-alt1
- new spec from samba tarball
- build for Sisyphus
- 1251 patch

* Wed Dec 06 2000 AEN <aen@logic.ru>
- 1251 patch
- build for RE

* Thu Nov 23 2000 Sylvestre Taburet <staburet@mandrakesoft.com> 2.0.7-20mdk
- removed dependencies on cups and cups-devel so one can install samba without using cups
- added /home/netlogon

* Mon Nov 20 2000 Till Kamppeter <till@mandrakesoft.com> 2.0.7-19mdk
- Changed default print command in /etc/smb.conf, so that the Windows
  driver of the printer has to be used on the client.
- Fixed bug in smbspool which prevented from printing from a
  Linux-Samba-CUPS client to a Windows server through the guest account.

* Mon Oct 16 2000 Till Kamppeter <till@mandrakesoft.com> 2.0.7-18mdk
- Moved "smbspool" (Samba client of CUPS) to the samba-client package

* Sat Oct 7 2000 Stefan van der Eijk <s.vandereijk@chello.nl> 2.0.7-17mdk
- Added RedHat's "quota" patch to samba-glibc21.patch.bz2, this fixes
  quota related compile problems on the alpha.

* Wed Oct 4 2000 Sylvestre Taburet <staburet@mandrakesoft.com> 2.0.7-16mdk
- Fixed 'guest ok = ok' flag in smb.conf

* Tue Oct 3 2000 Sylvestre Taburet <staburet@mandrakesoft.com> 2.0.7-15mdk
- Allowed guest account to print in smb.conf
- added swat icon in menu

* Tue Oct 3 2000 Sylvestre Taburet <staburet@mandrakesoft.com> 2.0.7-14mdk
- Removed rh ssl patch and --with-ssl flag: not appropriate for 7.2

* Tue Oct 3 2000 Sylvestre Taburet <staburet@mandrakesoft.com> 2.0.7-13mdk
- Changed fixinit patch.
- Changed smb.conf for better CUPS configuration.
- Thanks Fred for doing this ---vvv.

* Tue Oct  3 2000 Frederic Lepied <flepied@mandrakesoft.com> 2.0.7-12mdk
- menu entry for web configuration tool.
- merge with rh: xinetd + ssl + pam_stack.
- Added smbadduser rh-bugfix w/o relocation of config-files.

* Mon Oct  2 2000 Frederic Lepied <flepied@mandrakesoft.com> 2.0.7-11mdk
- added build requires on cups-devel and pam-devel.

* Mon Oct  2 2000 Till Kamppeter <till@mandrakesoft.com> 2.0.7-10mdk
- Fixed smb.conf entry for CUPS: "printcap name = lpstat", "lpstats" was
  wrong.

* Mon Sep 25 2000 Sylvestre Taburet <staburet@mandrakesoft.com> 2.0.7-9mdk
- Cosmetic changes to make rpmlint more happy

* Wed Sep 11 2000 Sylvestre Taburet <staburet@mandrakesoft.com> 2.0.7-8mdk
- added linkage to the using_samba book in swat

* Fri Sep 01 2000 Sylvestre Taburet <staburet@mandrakesoft.com> 2.0.7-7mdk
- Added CUPS support to smb.conf
- Added internationalization options to smb.conf [Global]

* Wed Aug 30 2000 Till Kamppeter <till@mandrakesoft.com> 2.0.7-6mdk
- Put "smbspool" to the files to install

* Wed Aug 30 2000 Sylvestre Taburet <staburet@mandrakesoft.com> 2.0.7-5mdk
- Did some cleaning in the patches

* Fri Jul 28 2000 Sylvestre Taburet <staburet@mandrakesoft.com> 2.0.7-4mdk
- relocated man pages from /usr/man to /usr/share/man for compatibility reasons

* Fri Jul 28 2000 Sylvestre Taburet <staburet@mandrakesoft.com> 2.0.7-3mdk
- added make_unicodemap and build of unicode_map.$i in the spec file

* Fri Jul 28 2000 Sylvestre Taburet <staburet@mandrakesoft.com> 2.0.7-2mdk
- renamed /etc/codepage/codepage.$i into /etc/codepage/unicode_map.$i to fix smbmount bug.

* Fri Jul 07 2000 Sylvestre Taburet <staburet@mandrakesoft.com> 2.0.7-1mdk
- 2.0.7

* Wed Apr 05 2000 Francis Galiegue <fg@mandrakesoft.com> 2.0.6-4mdk

- Titi sucks, does not put versions in changelog
- Fixed groups for -common and -client
- /usr/sbin/samba is no config file

* Thu Mar 23 2000 Thierry Vignaud <tvignaud@mandrakesoft.com>
- fix buggy post install script (pixel)

* Fri Mar 17 2000 Francis Galiegue <francis@mandrakesoft.com> 2.0.6-2mdk

- Changed group according to 7.1 specs
- Some spec file changes
- Let spec-helper do its job

* Thu Nov 25 1999 Chmouel Boudjnah <chmouel@mandrakesoft.com>
- 2.0.6.

* Tue Nov  2 1999 Chmouel Boudjnah <chmouel@mandrakesoft.com>
- Merge with rh changes.
- Split in 3 packages.

* Fri Aug 13 1999 Pablo Saratxaga <pablo@@mandrakesoft.com>
- corrected a bug with %post (the $1 parameter is "1" in case of
  a first install, not "0". That parameter is the number of packages
  of the same name that will exist after running all the steps if nothing
  is removed; so it is "1" after first isntall, "2" for a second install
  or an upgrade, and "0" for a removal)

* Wed Jul 28 1999 Pablo Saratxaga <pablo@@mandrakesoft.com>
- made smbmnt and smbumount suid root, and only executable by group 'smb'
  add to 'smb' group any user that should be allowed to mount/unmount
  SMB shared directories

* Fri Jul 23 1999 Chmouel Boudjnah <chmouel@mandrakesoft.com>
- 2.0.5a (bug security fix).

* Wed Jul 21 1999 Axalon Bloodstone <axalon@linux-mandrake.com>
- 2.0.5
- cs/da/de/fi/fr/it/tr descriptions/summaries

* Sun Jun 13 1999 Bernhard Rosenkränzer <bero@mandrakesoft.com>
- 2.0.4b
- recompile on a system that works ;)

* Wed Apr 21 1999 Chmouel Boudjnah <chmouel@mandrakesoft.com>
- Mandrake adaptations.
- Bzip2 man-pages.

* Fri Mar 26 1999 Bill Nottingham <notting@redhat.com>
- add a mount.smb to make smb mounting a little easier.
- smb filesystems apparently do not work on alpha. Oops.

* Thu Mar 25 1999 Bill Nottingham <notting@redhat.com>
- always create codepages

* Tue Mar 23 1999 Bill Nottingham <notting@redhat.com>
- logrotate changes

* Sun Mar 21 1999 Cristian Gafton <gafton@redhat.com>
- auto rebuild in the new build environment (release 3)

* Fri Mar 19 1999 Preston Brown <pbrown@redhat.com>
- updated init script to use graceful restart (not stop/start)

* Tue Mar  9 1999 Bill Nottingham <notting@redhat.com>
- update to 2.0.3

* Thu Feb 18 1999 Bill Nottingham <notting@redhat.com>
- update to 2.0.2

* Mon Feb 15 1999 Bill Nottingham <notting@redhat.com>
- swat swat

* Tue Feb  9 1999 Bill Nottingham <notting@redhat.com>
- fix bash2 breakage in post script

* Fri Feb  5 1999 Bill Nottingham <notting@redhat.com>
- update to 2.0.0

* Mon Oct 12 1998 Cristian Gafton <gafton@redhat.com>
- make sure all binaries are stripped

* Thu Sep 17 1998 Jeff Johnson <jbj@redhat.com>
- update to 1.9.18p10.
- fix %triggerpostun.

* Tue Jul 07 1998 Erik Troan <ewt@redhat.com>
- updated postun triggerscript to check $0
- clear /etc/codepages from %preun instead of %postun

* Mon Jun 08 1998 Erik Troan <ewt@redhat.com>
- made the %postun script a tad less agressive; no reason to remove
  the logs or lock file (after all, if the lock file is still there,
  samba is still running)
- the %postun and %preun should only exectute if this is the final
  removal
- migrated %triggerpostun from Red Hat's samba package to work around
  packaging problems in some Red Hat samba releases

* Sun Apr 26 1998 John H Terpstra <jht@samba.anu.edu.au>
- minor tidy up in preparation for release of 1.9.18p5
- added findsmb utility from SGI package

* Wed Mar 18 1998 John H Terpstra <jht@samba.anu.edu.au>
- Updated version and codepage info.
- Release to test name resolve order

* Sat Jan 24 1998 John H Terpstra <jht@samba.anu.edu.au>
- Many optimisations (some suggested by Manoj Kasichainula <manojk@io.com>
- Use of chkconfig in place of individual symlinks to /etc/rc.d/init/smb
- Compounded make line
- Updated smb.init restart mechanism
- Use compound mkdir -p line instead of individual calls to mkdir
- Fixed smb.conf file path for log files
- Fixed smb.conf file path for incoming smb print spool directory
- Added a number of options to smb.conf file
- Added smbadduser command (missed from all previous RPMs) - Doooh!
- Added smbuser file and smb.conf file updates for username map

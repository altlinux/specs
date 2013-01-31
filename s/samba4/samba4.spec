%define _localstatedir /var

# internal libs
%def_without talloc
%def_without tevent
%def_without tdb
%def_without ldb
%def_with ntdb

# build as separate package
%def_without libsmbclient
%def_without libwbclient
%def_without libnetapi
%def_without pam_smbpass

%def_with mitkrb5
%def_without dc
%def_with clustering_support
%def_without testsuite

%if_with testsuite
# The testsuite only works with a full build right now.
%def_without mitkrb5
%def_with dc
%endif

Name: samba4
Version: 4.0.2
Release: alt2
Group: System/Servers
Summary: The Samba4 CIFS and AD client and server suite
License: GPLv3+ and LGPLv3+
Url: http://www.samba.org/

Source: %name-%version.tar

# Red Hat specific replacement-files
Source1: samba.log
Source2: samba.xinetd
Source3: swat.desktop
Source4: samba.sysconfig
Source5: smb.init
Source6: samba.pamd
Source8: winbind.init
Source9: smb.conf.default
Source10: nmb.init
Source11: pam_winbind.conf
Source12: samba.conf.tmp

Source200: README.dc
Source201: README.downgrade

Patch: %name-%version-%release.patch

Conflicts: samba < %version
Requires: %name-winbind-clients = %version-%release
Requires(pre): %name-common = %version-%release

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
BuildRequires: libpopt-devel
BuildRequires: zlib-devel

BuildRequires: libiniparser-devel
BuildRequires: libkrb5-devel libssl-devel libcups-devel
BuildRequires: gawk libgtk+2-devel libcap-devel libuuid-devel
BuildRequires: inkscape libxslt xsltproc netpbm dblatex html2text docbook-style-xsl
%{?_without_talloc:BuildRequires: libtalloc-devel >= 2.0.8 libpytalloc-devel}
%{?_without_tevent:BuildRequires: libtevent-devel >= 0.9.17 python-module-tevent}
%{?_without_tdb:BuildRequires: libtdb-devel >= 1.2.11  python-module-tdb}
%{?_without_tdb:BuildRequires: libldb-devel >= 1.1.14 python-module-pyldb-devel}
%{?_with_clustering_support:BuildRequires: ctdb-devel}
%{?_with_testsuite:BuildRequires: ldb-tools}

BuildRequires: perl-Perl4-CoreLibs

%description
Samba is the standard Windows interoperability suite of programs for Linux and Unix.

%package client
Summary: Samba client programs
Group: Networking/Other
Requires: %name-common = %version-%release
Requires: %name-libs = %version-%release
%if_with libsmbclient
Requires: libsmbclient4 = %version-%release
%endif
Conflicts: samba-client < %version
Provides: samba-client = %version-%release

%description client
The %name-client package provides some SMB/CIFS clients to complement
the built-in SMB/CIFS filesystem in Linux. These clients allow access
of SMB/CIFS shares and printing to SMB/CIFS printers.

%package common
Summary: Files used by both Samba servers and clients
Group: System/Servers
Requires: %name-libs = %version-%release
%if_with libnetapi
Requires: libnetapi4 = %version-%release
%endif
Conflicts: samba-common < %version
Provides: samba-common = %version-%release

%description common
%name-common provides files necessary for both the server and client
packages of Samba.

%package dc
Summary: Samba AD Domain Controller
Group: System/Servers
Requires: %name-dc-libs = %version-%release

%description dc
The %name-dc package provides AD Domain Controller functionality

%package dc-libs
Summary: Samba AD Domain Controller Libraries
Group: System/Libraries
Requires: %name-common = %version-%release
Requires: %name-libs = %version-%release

%description dc-libs
The %name-dc-libs package contains the libraries needed by the DC to
link against the SMB, RPC and other protocols.

%package libs
Summary: Samba libraries
Group: System/Libraries
%if_with libnetapi
Requires: libnetapi4 = %version-%release
%else
Obsoletes: libnetapi4 < %version-%release
%endif
%if_with libwbclient
Requires: libwbclient4 = %version-%release
%else
Obsoletes: libwbclient4 < %version-%release
%endif
%if_with libsmbclient
Requires: libsmbclient4 = %version-%release
%else
Obsoletes: libsmbclient4 < %version-%release
%endif

%description libs
The %name-libs package contains the libraries needed by programs that
link against the SMB, RPC and other protocols provided by the Samba suite.

%package -n libsmbclient4
Summary: The SMB client library
Group: System/Libraries
Conflicts: libsmbclient < %version
Provides: libsmbclient = %version-%release

%description -n libsmbclient4
The libsmbclient contains the SMB client library from the Samba suite.

%package -n libsmbclient4-devel
Summary: Developer tools for the SMB client library
Group: Development/C
Requires: libsmbclient4 = %version-%release
Conflicts: libsmbclient-devel < %version
Provides: libsmbclient-devel = %version-%release

%description -n libsmbclient4-devel
The libsmbclient-devel package contains the header files and libraries needed to
develop programs that link against the SMB client library in the Samba suite.

%package -n libwbclient4
Summary: The winbind client library
Group: System/Libraries
Conflicts: libwbclient < %version
Conflicts: samba-winbind-clients < %version
Provides: libwbclient = %version-%release

%description -n libwbclient4
The libwbclient package contains the winbind client library from the Samba suite.

%package -n libwbclient4-devel
Summary: Developer tools for the winbind library
Group: Development/C
Requires: libwbclient4 = %version-%release
Conflicts: libwbclient-devel < %version
Provides: libwbclient-devel = %version-%release

%description -n libwbclient4-devel
The libwbclient-devel package provides developer tools for the wbclient library.

%package -n libnetapi4
Summary: Samba netapi library
Group: System/Libraries
Conflicts: libnetapi < %version
Provides: libnetapi = %version-%release

%description -n libnetapi4
Samba netapi library

%package -n libnetapi4-devel
Summary: Samba netapi development files
Group: Development/Other
Requires: libnetapi4 = %version-%release
Conflicts: libnetapi-devel < %version
Provides: libnetapi-devel = %version-%release

%description -n libnetapi4-devel
Samba netapi development files

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

%package test
Summary: Testing tools for Samba servers and clients
Group: Development/Tools
Requires: %name = %version-%release
Requires: %name-common = %version-%release
Requires: %name-dc = %version-%release
Requires: %name-libs = %version-%release
Requires: %name-winbind = %version-%release
%if_with libsmbclient
Requires: libsmbclient4 = %version-%release
%endif

%description test
samba4-test provides testing tools for both the server and client
packages of Samba.

%package test-devel
Summary: Testing devel files for Samba servers and clients
Group: Development/C
Requires: %name-test = %version-%release

%description test-devel
samba-test-devel provides testing devel files for both the server and client
packages of Samba.

%package winbind
Summary: Samba winbind
Group: System/Servers
Requires: %name-common = %version-%release
Requires: %name-libs = %version-%release
Conflicts: samba-winbind < %version
Provides: samba-winbind = %version-%release

%description winbind
The %name-winbind package provides the winbind NSS library, and some
client tools.  Winbind enables Linux to be a full member in Windows
domains and to use Windows user and group accounts on Linux.

%package winbind-clients
Summary: Samba winbind clients
Group: System/Servers
Requires: %name-winbind = %version-%release
%if_with libwbclient
Requires: libwbclient4 = %version-%release
%endif
Conflicts: samba-winbind-clients < %version
Provides: samba-winbind-clients = %version-%release

%description winbind-clients
The samba-winbind-clients package provides the NSS library and a PAM
module necessary to communicate to the Winbind Daemon

%package winbind-devel
Summary: Developer tools for the winbind library
Group: Development/Other
Requires: %name-winbind = %version-%release

%description winbind-devel
The samba-winbind package provides developer tools for the wbclient library.

%package swat
Summary: The Samba SMB server Web configuration program
Group: Security/Networking
Requires: %name = %version-%release
#Requires: %name-doc = %version-%release
Requires: xinetd
Conflicts: samba-swat < %version
Provides: samba-swat = %version-%release

%description swat
The samba-swat package includes the new SWAT (Samba Web Administration
Tool), for remotely managing Samba's smb.conf file using your favorite
Web browser.

%package doc
Summary: Documentation for the Samba suite
Group: Documentation
Requires: %name-common = %version-%release
BuildArch: noarch
Conflicts: samba-doc < %version
Provides: samba-doc = %version-%release

%description doc
The samba-doc package includes all the non-manpage documentation for the
Samba suite.

%prep
%setup -q
%patch -p1

%build

%define _talloc_lib ,talloc,pytalloc,pytalloc-util
%if_without talloc
%define _talloc_lib ,!talloc,!pytalloc,!pytalloc-util
%endif

%define _tevent_lib ,tevent,pytevent
%if_without tevent
%define _tevent_lib ,!tevent,!pytevent
%endif

%define _tdb_lib ,tdb,pytdb
%if_without tdb
%define _tdb_lib ,!tdb,!pytdb
%endif

%define _ldb_lib ,ldb,pyldb
%if_without ldb
%define _ldb_lib ,!ldb,!pyldb
%endif

%define _samba4_libraries heimdal,!zlib,!popt%{_talloc_lib}%{_tevent_lib}%{_tdb_lib}%{_ldb_lib}

%define _samba4_idmap_modules idmap_ad,idmap_rid,idmap_adex,idmap_hash,idmap_tdb2
%define _samba4_pdb_modules pdb_tdbsam,pdb_ldap,pdb_ads,pdb_smbpasswd,pdb_wbc_sam,pdb_samba4
%define _samba4_auth_modules auth_unix,auth_wbc,auth_server,auth_netlogond,auth_script,auth_samba4
# auth_domain needs to be static
%define _samba4_modules %_samba4_idmap_modules,%_samba4_pdb_modules,%_samba4_auth_modules

%define _libsmbclient %nil
%if_without libsmbclient
%define _libsmbclient smbclient,smbsharemodes,
%endif

%define _libwbclient %nil
%if_without libwbclient
%define _libwbclient wbclient,
%endif

%define _libnetapi %nil
%if_without libnetapi
%define _libnetapi netapi,
%endif

%define _samba4_private_libraries %{_libsmbclient}%{_libwbclient}%{_libnetapi}


%undefine _configure_gettext
%add_optflags -I/usr/include/krb5
%configure \
	--enable-fhs \
	--with-piddir=/var/run \
	--with-sockets-dir=/var/run/samba \
	--with-modulesdir=%_libdir/samba \
	--with-pammodulesdir=%_lib/security \
	--with-lockdir=/var/lib/samba \
	--with-privatedir=/var/lib/samba/private \
	--disable-gnutls \
	--disable-rpath-install \
	--with-shared-modules=%_samba4_modules \
	--builtin-libraries=ccan \
	--bundled-libraries=%_samba4_libraries \
	--with-pam \
	--with-ads \
	--private-libraries=%_samba4_private_libraries \
%if_with mitkrb5
	--with-system-mitkrb5 \
%endif
%if_without dc
	--without-ad-dc \
%endif
%if_with clustering_support
	--with-cluster-support \
	--enable-old-ctdb \
%endif
%if_without pam_smbpass
	--without-pam_smbpass \
%endif
%if_with testsuite
	--enable-selftest \
%endif
	--disable-ntdb

%make_build

# Build PIDL for installation into vendor directories before
# 'make proto' gets to it.
(cd pidl && perl Makefile.PL INSTALLDIRS=vendor )

%install
%make install DESTDIR=%buildroot PERL_INSTALL_ROOT=%buildroot

mkdir -p %buildroot/sbin
mkdir -p %buildroot/usr/{sbin,bin}
mkdir -p %buildroot/%_lib/security
mkdir -p %buildroot/var/lib/samba
mkdir -p %buildroot/var/lib/samba/{private,winbindd_privileged,scripts,sysvol}
mkdir -p %buildroot/var/log/samba/old
mkdir -p %buildroot/var/spool/samba
mkdir -p %buildroot%_datadir/swat/using_samba
mkdir -p %buildroot/var/run/{samba,winbindd}
mkdir -p %buildroot%_libdir/samba
mkdir -p %buildroot%_pkgconfigdir
mkdir -p %buildroot%_initdir
mkdir -p %buildroot%_unitdir
mkdir -p %buildroot%_sysconfdir/{pam.d,logrotate.d,security,sysconfig,xinetd.d}


# Install other stuff
install -m644 %SOURCE1 %buildroot%_sysconfdir/logrotate.d/samba
install -m644 %SOURCE9 %buildroot%_sysconfdir/samba/smb.conf
install -m644 %SOURCE11 %buildroot%_sysconfdir/security
install -m644 %SOURCE6 %buildroot%_sysconfdir/pam.d/samba
echo 127.0.0.1 localhost > %buildroot%_sysconfdir/samba/lmhosts
mkdir -p %buildroot%_sysconfdir/openldap/schema
install -m644 examples/LDAP/samba.schema %buildroot%_sysconfdir/openldap/schema/samba.schema
install -m644 %SOURCE2 %buildroot%_sysconfdir/xinetd.d/swat
install -m755 packaging/printing/smbprint %buildroot%_bindir/smbprint

mkdir -p %buildroot/lib/tmpfiles.d/
install -m644 %SOURCE12 %buildroot/lib/tmpfiles.d/samba.conf

install -m644 packaging/systemd/samba.sysconfig %buildroot%_sysconfdir/sysconfig/samba
install -m644 packaging/RHEL/setup/smbusers %buildroot%_sysconfdir/samba/smbusers

install -m755 %SOURCE10 %buildroot%_initrddir/nmb
install -m755 %SOURCE5 %buildroot%_initrddir/smb
install -m755 %SOURCE8 %buildroot%_initrddir/winbind

install -d -m 755 %buildroot%_defaultdocdir/%name
install -m 644 %SOURCE201 %buildroot%_defaultdocdir/%name/README.downgrade

%if_without dc
install -m 644 %SOURCE200 %buildroot%_defaultdocdir/%name/README.dc
install -m 644 %SOURCE200 %buildroot%_defaultdocdir/%name/README.dc-libs
%endif

for i in nmb smb winbind ; do
    cat packaging/systemd/$i.service | sed -e 's@Type=forking@Type=forking\nEnvironment=KRB5CCNAME=/run/samba/krb5cc_samba@g' >tmp$i.service
    install -m 0644 tmp$i.service %buildroot%_unitdir/$i.service
done

# NetworkManager online/offline script
install -d -m 0755 %buildroot%_sysconfdir/NetworkManager/dispatcher.d/
install -m 0755 packaging/NetworkManager/30-winbind-systemd \
            %buildroot%_sysconfdir/NetworkManager/dispatcher.d/30-winbind


# Clean out crap left behind by the PIDL install.
find %buildroot -type f -name .packlist -exec rm -f {} \;
rm -f %buildroot%perl_vendorlib/wscript_build
rm -rf %buildroot%perl_vendorlib/Parse/Yapp

# winbind
mv %buildroot%_libdir/libnss_winbind.so.2 %buildroot/%_lib/libnss_winbind.so.2
ln -sf /%_lib/libnss_winbind.so.2  %buildroot%_libdir/libnss_winbind.so
mv  %buildroot%_libdir/libnss_wins.so.2 %buildroot/%_lib/libnss_wins.so.2
ln -sf /%_lib/libnss_wins.so.2  %buildroot%_libdir/libnss_wins.so

mkdir -p  %buildroot%_libdir/krb5/plugins/libkrb5/winbind_krb5_locator.so
mv %buildroot%_libdir/winbind_krb5_locator.so %buildroot%_libdir/krb5/plugins/libkrb5/winbind_krb5_locator.so

ln -sf ldap.so  %buildroot%_libdir/samba/pdb/ldapsam.so

# Fix up permission on perl install.
%_fixperms %buildroot%perl_vendor_privlib

%find_lang pam_winbind
%find_lang net

%if_with testsuite
%check
TDB_NO_FSYNC=1 %make_build test
%endif

%post
%post_service smb
%post_service nmb

%preun
%preun_service smb
%preun_service nmb

%pre winbind
%_sbindir/groupadd -g 88 wbpriv >/dev/null 2>&1 || :

%post winbind
%post_service winbind

%preun winbind
%preun_service winbind

%files
%doc COPYING
%_bindir/smbstatus
%_bindir/eventlogadm
%_sbindir/nmbd
%_sbindir/smbd
%_libdir/samba/auth
%_libdir/samba/vfs
%config(noreplace) %_sysconfdir/samba/smbusers
%attr(755,root,root) %_initdir/smb
%attr(755,root,root) %_initdir/nmb
%_unitdir/nmb.service
%_unitdir/smb.service
%attr(1777,root,root) %dir /var/spool/samba
%dir %_sysconfdir/openldap/schema
%_sysconfdir/openldap/schema/samba.schema
%_man1dir/smbstatus.1*
%_man8dir/eventlogadm.8*
%_man8dir/smbd.8*
%_man8dir/nmbd.8*
%_man8dir/vfs_*.8*

%files client
%_bindir/cifsdd
%_bindir/dbwrap_tool
%_bindir/nmblookup
%_bindir/nmblookup4
%_bindir/oLschema2ldif
%_bindir/regdiff
%_bindir/regpatch
%_bindir/regshell
%_bindir/regtree
%_bindir/rpcclient
%_bindir/sharesec
%_bindir/smbcacls
%_bindir/smbclient
%_bindir/smbclient4
%_bindir/smbcquotas
%_bindir/smbget
#%_bindir/smbiconv
%_bindir/smbpasswd
%_bindir/smbprint
%_bindir/smbspool
%_bindir/smbta-util
%_bindir/smbtree
%_libdir/samba/libldb-cmdline.so
%_man1dir/nmblookup.1.gz
%_man1dir/oLschema2ldif.1.gz
%_man1dir/regdiff.1.gz
%_man1dir/regpatch.1.gz
%_man1dir/regshell.1.gz
%_man1dir/regtree.1.gz
%exclude %_man1dir/findsmb.1*
%_man1dir/log2pcap.1*
%_man1dir/nmblookup4.1*
%_man1dir/rpcclient.1*
%_man1dir/sharesec.1*
%_man1dir/smbcacls.1*
%_man1dir/smbclient.1*
%_man1dir/smbcquotas.1*
%_man1dir/smbget.1*
%_man5dir/smbgetrc.5*
%exclude %_man1dir/smbtar.1*
%_man1dir/smbtree.1*
%_man8dir/smbpasswd.8*
%_man8dir/smbspool.8*
%_man8dir/smbta-util.8*

## we don't build it for now
#%%if_with ntdb
#%_bindir/ntdbbackup
#%_bindir/ntdbdump
#%_bindir/ntdbrestore
#%_bindir/ntdbtool
#%%endif
%if_with tdb
%_bindir/tdbbackup
%_bindir/tdbdump
%_bindir/tdbrestore
%_bindir/tdbtool
%_man8dir/tdbbackup.8.gz
%_man8dir/tdbdump.8.gz
%_man8dir/tdbrestore.8.gz
%_man8dir/tdbtool.8.gz
%endif

%if_with ldb
%_bindir/ldbadd
%_bindir/ldbdel
%_bindir/ldbedit
%_bindir/ldbmodify
%_bindir/ldbrename
%_bindir/ldbsearch
%_man1dir/ldbadd.1.gz
%_man1dir/ldbdel.1.gz
%_man1dir/ldbedit.1.gz
%_man1dir/ldbmodify.1.gz
%_man1dir/ldbrename.1.gz
%_man1dir/ldbsearch.1.gz
%endif

%files common -f net.lang
/lib/tmpfiles.d/samba.conf
%_bindir/net
%_bindir/pdbedit
%_bindir/profiles
%_bindir/smbcontrol
%_bindir/testparm
%_datadir/samba/codepages
%config(noreplace) %_sysconfdir/logrotate.d/samba
%attr(0700,root,root) %dir /var/log/samba
%attr(0700,root,root) %dir /var/log/samba/old
%dir /var/run/samba
%dir /var/run/winbindd
%attr(700,root,root) %dir /var/lib/samba/private
%attr(755,root,root) %dir %_sysconfdir/samba
%config(noreplace) %_sysconfdir/samba/smb.conf
%config(noreplace) %_sysconfdir/samba/lmhosts
%config(noreplace) %_sysconfdir/sysconfig/samba
%_man1dir/profiles.1*
%_man1dir/smbcontrol.1*
%_man1dir/testparm.1*
%_man5dir/lmhosts.5*
%_man5dir/smb.conf.5*
%_man5dir/smbpasswd.5*
%_man7dir/samba.7*
%_man8dir/net.8*
%_man8dir/pdbedit.8*

# common libraries
%_libdir/samba/libpopt_samba3.so
%_libdir/samba/pdb

%files dc
%_libdir/samba/ldb
%_libdir/samba/libdfs_server_ad.so
%_libdir/samba/libdsdb-module.so

%if_with dc
%_bindir/samba-tool
%_sbindir/samba
%_sbindir/samba_kcc
%_sbindir/samba_dnsupdate
%_sbindir/samba_spnupdate
%_sbindir/samba_upgradedns
%_sbindir/upgradeprovision
%_libdir/mit_samba.so
%_libdir/samba/bind9/dlz_bind9.so
%_libdir/samba/libheimntlm-samba4.so.1
%_libdir/samba/libheimntlm-samba4.so.1.0.1
%_libdir/samba/libkdc-samba4.so.2
%_libdir/samba/libkdc-samba4.so.2.0.0
%_libdir/samba/libpac.so
%_libdir/samba/gensec
%dir /var/lib/samba/sysvol
%_datadir/samba/setup
%_man8dir/samba.8.gz
%_man8dir/samba-tool.8.gz
%else
%doc %_defaultdocdir/%name/README.dc
%exclude %_man8dir/samba.8*
%exclude %_man8dir/samba-tool.8*
%endif

%files dc-libs
%if_with dc
%_libdir/samba/libprocess_model.so
%_libdir/samba/libservice.so
%_libdir/samba/process_model
%_libdir/samba/service
%_libdir/libdcerpc-server.so.*
%_libdir/samba/libntvfs.so
%_libdir/samba/libposix_eadb.so
%else
%doc %_defaultdocdir/%name/README.dc-libs
%endif

%files devel
%_includedir/samba-4.0

%exclude %_includedir/samba-4.0/netapi.h
%exclude %_includedir/samba-4.0/torture.h
%if_with libsmbclient
%exclude %_includedir/samba-4.0/libsmbclient.h
%exclude %_includedir/samba-4.0/smb_share_modes.h
%endif
%if_with libwbclient
%exclude %_includedir/samba-4.0/wbclient.h
%endif

%_libdir/libdcerpc-atsvc.so
%_libdir/libdcerpc-binding.so
%_libdir/libdcerpc-samr.so
%_libdir/libdcerpc.so
%_libdir/libgensec.so
%_libdir/libndr-krb5pac.so
%_libdir/libndr-nbt.so
%_libdir/libndr-standard.so
%_libdir/libndr.so
%_libdir/libregistry.so
%_libdir/libsamba-credentials.so
%_libdir/libsamba-hostconfig.so
%_libdir/libsamba-policy.so
%_libdir/libsamba-util.so
%_libdir/libsamdb.so
%_libdir/libsmbclient-raw.so
%_libdir/libsmbconf.so
%_libdir/libtevent-util.so
%_libdir/libpdb.so
%_libdir/libsmbldap.so

%_pkgconfigdir/dcerpc.pc
%_pkgconfigdir/dcerpc_atsvc.pc
%_pkgconfigdir/dcerpc_samr.pc
%_pkgconfigdir/gensec.pc
%_pkgconfigdir/ndr.pc
%_pkgconfigdir/ndr_krb5pac.pc
%_pkgconfigdir/ndr_nbt.pc
%_pkgconfigdir/ndr_standard.pc
%_pkgconfigdir/registry.pc
%_pkgconfigdir/samba-credentials.pc
%_pkgconfigdir/samba-hostconfig.pc
%_pkgconfigdir/samba-policy.pc
%_pkgconfigdir/samba-util.pc
%_pkgconfigdir/samdb.pc
%_pkgconfigdir/smbclient-raw.pc

%if_with dc
%_libdir/libdcerpc-server.so
%_pkgconfigdir/dcerpc_server.pc
%endif

%files libs
%_libdir/libdcerpc-atsvc.so.*
%_libdir/libdcerpc-binding.so.*
%_libdir/libdcerpc-samr.so.*
%_libdir/libdcerpc.so.*
%_libdir/libgensec.so.*
%_libdir/libndr-krb5pac.so.*
%_libdir/libndr-nbt.so.*
%_libdir/libndr-standard.so.*
%_libdir/libndr.so.*
%_libdir/libregistry.so.*
%_libdir/libsamba-credentials.so.*
%_libdir/libsamba-hostconfig.so.*
%_libdir/libsamba-policy.so.*
%_libdir/libsamba-util.so.*
%_libdir/libsamdb.so.*
%_libdir/libsmbclient-raw.so.*
%_libdir/libsmbconf.so.*
%_libdir/libtevent-util.so.*
%_libdir/libpdb.so.*
%_libdir/libsmbldap.so.*

# libraries needed by the public libraries
%_libdir/samba/libCHARSET3.so
%_libdir/samba/libMESSAGING.so
%_libdir/samba/libLIBWBCLIENT_OLD.so
%_libdir/samba/libaddns.so
%_libdir/samba/libads.so
%_libdir/samba/libasn1util.so
%_libdir/samba/libauth.so
%_libdir/samba/libauth4.so
%_libdir/samba/libauth_sam_reply.so
%_libdir/samba/libauth_unix_token.so
%_libdir/samba/libauthkrb5.so
%_libdir/samba/libcli-ldap-common.so
%_libdir/samba/libcli-ldap.so
%_libdir/samba/libcli-nbt.so
%_libdir/samba/libcli_cldap.so
%_libdir/samba/libcli_smb_common.so
%_libdir/samba/libcli_spoolss.so
%_libdir/samba/libcliauth.so
#%{_libdir}/samba/libclidns.so
%_libdir/samba/libcluster.so
%_libdir/samba/libcmdline-credentials.so
%_libdir/samba/libdbwrap.so
%_libdir/samba/libdcerpc-samba.so
%_libdir/samba/libdcerpc-samba4.so
%_libdir/samba/liberrors.so
%_libdir/samba/libevents.so
%_libdir/samba/libflag_mapping.so
%_libdir/samba/libgpo.so
%_libdir/samba/libgse.so
%_libdir/samba/libinterfaces.so
%_libdir/samba/libkrb5samba.so
%_libdir/samba/libldbsamba.so
%_libdir/samba/liblibcli_lsa3.so
%_libdir/samba/liblibcli_netlogon3.so
%_libdir/samba/liblibsmb.so
%_libdir/samba/libsmb_transport.so
%_libdir/samba/libmsrpc3.so
%_libdir/samba/libndr-samba.so
%_libdir/samba/libndr-samba4.so
%_libdir/samba/libnet_keytab.so
%_libdir/samba/libnetif.so
%_libdir/samba/libnpa_tstream.so
%_libdir/samba/libprinting_migrate.so
%_libdir/samba/libreplace.so
%_libdir/samba/libsamba-modules.so
%_libdir/samba/libsamba-net.so
%_libdir/samba/libsamba-security.so
%_libdir/samba/libsamba-sockets.so
%_libdir/samba/libsamba_python.so
%_libdir/samba/libsamdb-common.so
%_libdir/samba/libsecrets3.so
%_libdir/samba/libserver-role.so
%_libdir/samba/libshares.so
%_libdir/samba/libsamba3-util.so
%_libdir/samba/libsmbd_base.so
%_libdir/samba/libsmbd_conn.so
%_libdir/samba/libsmbd_shim.so
%_libdir/samba/libsmbldaphelper.so
%_libdir/samba/libsmbpasswdparser.so
%_libdir/samba/libsmbregistry.so
%_libdir/samba/libtdb-wrap.so
%_libdir/samba/libtdb_compat.so
%_libdir/samba/libtrusts_util.so
%_libdir/samba/libutil_cmdline.so
#%_libdir/samba/libutil_ntdb.so
%_libdir/samba/libutil_reg.so
%_libdir/samba/libutil_setid.so
%_libdir/samba/libutil_tdb.so
%_libdir/samba/libxattr_tdb.so


%if_with dc
%_libdir/samba/libdb-glue.so
%_libdir/samba/libHDB_SAMBA4.so
%_libdir/samba/libasn1-samba4.so.*
%_libdir/samba/libgssapi-samba4.so.*
%_libdir/samba/libhcrypto-samba4.so.*
%_libdir/samba/libhdb-samba4.so.*
%_libdir/samba/libheimbase-samba4.so.*
%_libdir/samba/libhx509-samba4.so.*
%_libdir/samba/libkrb5-samba4.so.*
%_libdir/samba/libroken-samba4.so.*
%_libdir/samba/libwind-samba4.so.*
%endif

%if_with ldb
%_libdir/samba/libldb.so.*
%_libdir/samba/libpyldb-util.so.*
%endif
%if_with talloc
%_libdir/samba/libtalloc.so.*
%_libdir/samba/libpytalloc-util.so.*
%endif
%if_with tevent
%_libdir/samba/libtevent.so.*
%endif
%if_with tdb
%_libdir/samba/libtdb.so.*
%endif
## we don't build it for now
#%%if_with ntdb
#%_libdir/samba/libntdb.so.*
#%%endif
%if_without libsmbclient
%_libdir/samba/libsmbclient.so.*
%_libdir/samba/libsmbsharemodes.so.*
%endif
%if_without libwbclient
%_libdir/samba/libwbclient.so.*
%_libdir/samba/libwinbind-client.so
%endif
%if_without libnetapi
%_libdir/samba/libnetapi.so.*
%endif

%if_with libsmbclient
%files -n libsmbclient4
%_libdir/libsmbclient.so.*
%_libdir/libsmbsharemodes.so.*

%files -n libsmbclient4-devel
%_includedir/samba-4.0/libsmbclient.h
%_includedir/samba-4.0/smb_share_modes.h
%_libdir/libsmbclient.so
%_libdir/libsmbsharemodes.so
%_pkgconfigdir/smbclient.pc
%_pkgconfigdir/smbsharemodes.pc
%_man7dir/libsmbclient.7*
%endif

%if_with libwbclient
%files -n libwbclient4
%_libdir/libwbclient.so.*
%_libdir/samba/libwinbind-client.so

%files -n libwbclient4-devel
%_includedir/samba-4.0/wbclient.h
%_libdir/libwbclient.so
%_pkgconfigdir/wbclient.pc
%endif

%if_with libnetapi
%files -n libnetapi4
%_libdir/libnetapi.so.*

%files -n libnetapi4-devel
%_libdir/libnetapi.so
%_includedir/samba-4.0/netapi.h
%_pkgconfigdir/netapi.pc
%endif

%files pidl
%attr(755,root,root) %_bindir/pidl
%perl_vendor_privlib/*

%files -n python-module-%name
%python_sitelibdir/*

%files swat
%config(noreplace) %_sysconfdir/xinetd.d/swat
%config(noreplace) %_sysconfdir/pam.d/samba
%_datadir/samba/swat
%_sbindir/swat
%_man8dir/swat.8*
#%attr(755,root,root) %_libdir/samba/*.msg

%files test
%_bindir/gentest
%_bindir/locktest
%_bindir/masktest
%_bindir/ndrdump
%_bindir/smbtorture
%_libdir/libtorture.so.*
%_libdir/samba/libsubunit.so
%if_with dc
%_libdir/samba/libdlz_bind9_for_torture.so
%endif
%_man1dir/gentest.1*
%_man1dir/locktest.1*
%_man1dir/masktest.1*
%_man1dir/ndrdump.1*
%_man1dir/smbtorture.1*
%_man1dir/vfstest.1*

%if_with testsuite
# files to ignore in testsuite mode
%_libdir/samba/libnss_wrapper.so
%_libdir/samba/libsocket_wrapper.so
%_libdir/samba/libuid_wrapper.so
%endif

%files test-devel
%_includedir/samba-4.0/torture.h
%_libdir/libtorture.so
%_pkgconfigdir/torture.pc

%files winbind -f pam_winbind.lang
%_libdir/samba/idmap
%_libdir/samba/nss_info
%_libdir/samba/libnss_info.so
%_libdir/samba/libidmap.so
%_libdir/krb5/plugins/libkrb5/winbind_krb5_locator.so
%_sbindir/winbindd
%attr(750,root,wbpriv) %dir /var/lib/samba/winbindd_privileged
%_unitdir/winbind.service
%attr(755,root,root) %_initrddir/winbind
%_sysconfdir/NetworkManager/dispatcher.d/30-winbind
%_man7dir/winbind_krb5_locator.7*
%_man8dir/winbindd.8*
%_man8dir/idmap_*.8*

%files winbind-clients
%_bindir/ntlm_auth
%_bindir/wbinfo
%_libdir/libnss_winbind.so
/%_lib/libnss_winbind.so.*
%_libdir/libnss_wins.so
/%_lib/libnss_wins.so.*
/%_lib/security/pam_winbind.so
%config(noreplace) %_sysconfdir/security/pam_winbind.conf
%_man1dir/ntlm_auth.1.*
%_man1dir/wbinfo.1*
%_man5dir/pam_winbind.conf.5*
%_man8dir/pam_winbind.8*

%changelog
* Mon Feb 04 2013 Alexey Shabalin <shaba@altlinux.ru> 4.0.2-alt2
- obsoletes libnetapi4,libwbclient4,libsmbclient4 by samba4-libs if build without them

* Mon Feb 04 2013 Alexey Shabalin <shaba@altlinux.ru> 4.0.2-alt1
- 4.0.2
- fixed gensec: Allow login without a PAC by default (samba bug #9581)

* Fri Feb 01 2013 Alexey Shabalin <shaba@altlinux.ru> 4.0.1-alt3
- build without libnetapi
- add symlink ldapsam.so to ldap.so

* Thu Jan 31 2013 Alexey Shabalin <shaba@altlinux.ru> 4.0.1-alt2
- build without libsmbclient and libwbclient

* Mon Jan 28 2013 Alexey Shabalin <shaba@altlinux.ru> 4.0.1-alt1
- 4.0.1

* Fri Dec 21 2012 Alexey Shabalin <shaba@altlinux.ru> 4.0.0-alt2
- 4.0.0 release

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

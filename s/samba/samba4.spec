%set_verify_elf_method unresolved=relaxed
%add_findprov_skiplist /%_lib/*
%add_debuginfo_skiplist /%_lib

%define _localstatedir /var
%define libwbc_alternatives_version 0.13

# internal libs
%def_without talloc
%def_without tevent
%def_without tdb
%def_without ldb

%def_with profiling_data

# build as separate package
%def_with winbind
%def_with libsmbclient
%def_with libwbclient
%def_with libnetapi
%def_without pam_smbpass
%def_with doc

%def_with mitkrb5
%def_without dc
%def_with clustering_support
%def_without testsuite

%if_with testsuite
# The testsuite only works with a full build right now.
%def_without mitkrb5
%def_with dc
%endif

%def_with systemd
%def_enable avahi
%def_enable glusterfs
%def_with libcephfs

Name: samba
Version: 4.6.11
Release: alt2%ubt
Group: System/Servers
Summary: The Samba4 CIFS and AD client and server suite
License: GPLv3+ and LGPLv3+
Url: http://www.samba.org/

Source: %name-%version.tar

# Red Hat specific replacement-files
Source1: samba.log
Source5: smb.init
Source6: samba.pamd
Source8: winbind.init
Source9: smb.conf.default
Source10: nmb.init
Source11: pam_winbind.conf
Source12: ctdb.init

Source200: README.dc
Source201: README.downgrade

Patch: %name-%version-alt.patch
Patch10: samba-grouppwd.patch

# fedora patches
Patch100:         samba-4.4.2-s3-winbind-make-sure-domain-member-can-talk-to-trust.patch

Provides: samba4 = %version-%release
Obsoletes: samba4 < %version-%release

Provides: samba-swat = %version-%release
Obsoletes: samba-swat < %version-%release
Provides: samba4-swat = %version-%release
Obsoletes: samba4-swat < %version-%release
Provides: samba-doc = %version-%release
Obsoletes: samba-doc < %version-%release
Provides: samba4-doc = %version-%release
Obsoletes: samba4-doc < %version-%release

Requires(pre): %name-common = %version-%release
Requires: %name-libs = %version-%release
Requires: %name-common-tools = %version-%release
%if_with libwbclient
Requires: libwbclient = %version-%release
%endif

BuildRequires(pre):rpm-build-ubt

BuildRequires: libe2fs-devel
BuildRequires: libxfs-devel
BuildRequires: libacl-devel
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
BuildRequires: glibc-devel glibc-kernheaders
# BuildRequires: libbsd-devel
BuildRequires: setproctitle-devel
BuildRequires: libiniparser-devel
BuildRequires: libkrb5-devel libssl-devel libcups-devel
BuildRequires: gawk libgtk+2-devel libcap-devel libuuid-devel
%{?_with_doc:BuildRequires: inkscape libxslt xsltproc netpbm dblatex html2text docbook-style-xsl}
%{?_without_talloc:BuildRequires: libtalloc-devel >= 2.1.10 libpytalloc-devel}
%{?_without_tevent:BuildRequires: libtevent-devel >= 0.9.34 python-module-tevent}
%{?_without_tdb:BuildRequires: libtdb-devel >= 1.3.12  python-module-tdb}
%{?_without_ldb:BuildRequires: libldb-devel >= 1.1.29 python-module-pyldb-devel}
#{?_with_clustering_support:BuildRequires: ctdb-devel}
%{?_with_testsuite:BuildRequires: ldb-tools}
# Avoid trouble with rpm-macros-ubt-0.2-alt1.M80C.2.noarch.rpm
# where %__ubt_branch_id N.M80C in /usr/lib/rpm/macros.d/ubt
#if %ubt_id != "M70P"
#%{?_with_systemd:BuildRequires: systemd-devel}
#else
%{?_with_systemd:BuildRequires: libsystemd-devel}
#endif
%{?_enable_avahi:BuildRequires: libavahi-devel}
%{?_enable_glusterfs:BuildRequires: glusterfs3-devel >= 3.4.0.16}
%{?_with_libcephfs:BuildRequires: ceph-devel}
%{?_with_dc:BuildRequires: libgnutls-devel}

%description
Samba is the standard Windows interoperability suite of programs for Linux and Unix.

%package client
Summary: Samba client programs
Group: Networking/Other
Requires(pre): %name-common = %version-%release
Requires: %name-common-tools = %version-%release
Requires: %name-client-libs = %version-%release
%if_with libsmbclient
Requires: libsmbclient = %version-%release
%endif
Provides: samba4-client = %version-%release
Obsoletes: samba4-client < %version-%release
Provides: samba-client-cups = %version-%release
Obsoletes: samba-client-cups < %version-%release

%description client
The %name-client package provides some SMB/CIFS clients to complement
the built-in SMB/CIFS filesystem in Linux. These clients allow access
of SMB/CIFS shares and printing to SMB/CIFS printers.

%package client-libs
Summary: Samba client libraries
Group: Networking/Other
Conflicts: samba-common < %version-%release
Requires(pre): %name-common = %version-%release

%description client-libs
The samba-client-libs package contains internal libraries needed by the
SMB/CIFS clients.

%package common
Summary: Files used by both Samba servers and clients
Group: System/Servers
BuildArch: noarch
Provides: samba-utils = %version-%release
Provides: samba4-common = %version-%release
Obsoletes: samba4-common < %version-%release

%description common
%name-common provides files necessary for both the server and client
packages of Samba.

%package common-libs
Summary: Libraries used by both Samba servers and clients
Group: System/Libraries
Requires(pre): %name-common = %version-%release
Requires: %name-client-libs = %version-%release
%if_with libwbclient
Requires: libwbclient = %version-%release
%endif

%description common-libs
The samba-common-libs package contains internal libraries needed by the
SMB/CIFS clients.

%package common-tools
Summary: Tools for Samba servers and clients
Group: System/Servers
Requires: %name-libs = %version-%release

%description common-tools
The samba-common-tools package contains tools for Samba servers and
SMB/CIFS clients.

%package dc
Summary: Samba AD Domain Controller
Group: System/Servers
Requires: %name-libs = %version-%release
Requires: %name-dc-libs = %version-%release

Provides: samba4-dc = %version-%release
Obsoletes: samba4-dc < %version-%release

%description dc
The %name-dc package provides AD Domain Controller functionality

%package dc-libs
Summary: Samba AD Domain Controller Libraries
Group: System/Libraries
Requires: %name-common-libs = %version-%release
Requires: %name-libs = %version-%release
Provides: samba4-dc-libs = %version-%release
Obsoletes: samba4-dc-libs < %version-%release

%description dc-libs
The %name-dc-libs package contains the libraries needed by the DC to
link against the SMB, RPC and other protocols.

%package vfs-cephfs
Summary: Samba VFS module for Ceph distributed storage system
Group: System/Libraries
Requires: %name = %version-%release
Requires: %name-libs = %version-%release

%description vfs-cephfs
Samba VFS module for Ceph distributed storage system integration.

%package vfs-glusterfs
Summary: Samba VFS module for GlusterFS
Group: System/Libraries
Requires: %name = %version-%release
Requires: %name-libs = %version-%release

%description vfs-glusterfs
Samba VFS module for GlusterFS integration.

%package libs
Summary: Samba libraries
Group: System/Libraries
Provides: samba4-libs = %version-%release
Obsoletes: samba4-libs < %version-%release

Requires: %name-client-libs = %version-%release

%if_with libnetapi
Requires: libnetapi = %version-%release
%else
Obsoletes: libnetapi4 < %version-%release
%endif
%if_with libwbclient
Requires: libwbclient = %version-%release
%else
Obsoletes: libwbclient4 < %version-%release
%endif
%if_with libsmbclient
Requires: libsmbclient = %version-%release
%else
Obsoletes: libsmbclient4 < %version-%release
%endif

%description libs
The %name-libs package contains the libraries needed by programs that
link against the SMB, RPC and other protocols provided by the Samba suite.

%package -n libsmbclient
Summary: The SMB client library
Group: System/Libraries
Provides: libsmbclient4 = %version-%release
Obsoletes: libsmbclient4 < %version-%release
Requires(pre): %name-common = %version-%release
Requires: %name-client-libs = %version-%release

%description -n libsmbclient
The libsmbclient contains the SMB client library from the Samba suite.

%package -n libsmbclient-devel
Summary: Developer tools for the SMB client library
Group: Development/C
Requires: libsmbclient = %version-%release
Provides: libsmbclient4-devel = %version-%release
Obsoletes: libsmbclient4-devel < %version-%release

%description -n libsmbclient-devel
The libsmbclient-devel package contains the header files and libraries needed to
develop programs that link against the SMB client library in the Samba suite.

%package -n libwbclient
Summary: The winbind client library
Group: System/Libraries
Conflicts: samba-winbind-clients < %version
Provides: libwbclient4 = %version-%release
Obsoletes: libwbclient4 < %version-%release
Conflicts: samba-winbind-clients <= 3.6.12-alt1
Conflicts: samba4-libs < %version-%release
Requires: %name-client-libs = %version-%release

%description -n libwbclient
The libwbclient package contains the winbind client library from the Samba suite.

%package -n libwbclient-devel
Summary: Developer tools for the winbind library
Group: Development/C
Requires: libwbclient = %version-%release
Provides: libwbclient4-devel = %version-%release
Obsoletes: libwbclient4-devel < %version-%release

%description -n libwbclient-devel
The libwbclient-devel package provides developer tools for the wbclient library.

%package -n libnetapi
Summary: Samba netapi library
Group: System/Libraries
Provides: libnetapi4 = %version-%release
Obsoletes: libnetapi4 < %version-%release

%description -n libnetapi
Samba netapi library

%package -n python-module-%name
Summary: Samba Python libraries
Group: Networking/Other
Requires: %name-libs = %version-%release
Provides: python-module-samba4 = %version-%release
Obsoletes: python-module-samba4 < %version-%release

%add_python_req_skip Tdb

%description -n python-module-%name
The %name-python package contains the Python libraries needed by programs
that use SMB, RPC and other Samba provided protocols in Python programs.

%package devel
Summary: Developer tools for Samba libraries
Group: Development/C
Requires: %name-libs = %version-%release
Provides: samba4-devel = %version-%release
Obsoletes: samba4-devel < %version-%release
Provides: libnetapi-devel = %version-%release
Obsoletes: libnetapi-devel < %version-%release

%description devel
The %name-devel package contains the header files for the libraries
needed to develop programs that link against the SMB, RPC and other
libraries in the Samba suite.

%package pidl
Summary: Perl IDL compiler
Group: Development/Tools
BuildArch: noarch
# Requires: perl(:MODULE_COMPAT_%(eval "`perl -V:version`"; echo $version))
Provides: samba4-pidl = %version-%release
Obsoletes: samba4-pidl < %version-%release

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
Requires: libsmbclient = %version-%release
%endif
Provides: samba4-test = %version-%release
Obsoletes: samba4-test < %version-%release

%description test
samba4-test provides testing tools for both the server and client
packages of Samba.

%if_with winbind
%package winbind
Summary: Samba winbind
Group: System/Servers
Requires(pre): %name-common = %version-%release
Requires: %name-common-tools = %version-%release
Requires: %name-libs = %version-%release
Provides: samba4-winbind = %version-%release
Obsoletes: samba4-winbind < %version-%release
%if_with libwbclient
# There are working configurations exists where samba-winbind could be
# using with sssd. Also it could be already installed from installation DVD.
## Conflicts: libwbclient-sssd
Requires: libwbclient
%endif

%description winbind
The %name-winbind package provides the winbind NSS library, and some
client tools.  Winbind enables Linux to be a full member in Windows
domains and to use Windows user and group accounts on Linux.

%package winbind-clients
Summary: Samba winbind clients
Group: System/Servers
Requires: %name-winbind = %version-%release
%if_with libwbclient
Requires: libwbclient = %version-%release
%endif
Provides: samba4-winbind-clients = %version-%release
Obsoletes: samba4-winbind-clients < %version-%release

%description winbind-clients
The samba-winbind-clients package provides the NSS library and a PAM
module necessary to communicate to the Winbind Daemon

%package winbind-krb5-locator
Summary: Samba winbind krb5 locator
Group: System/Servers
%if_with libwbclient
Requires: libwbclient = %version-%release
Requires: %name-winbind = %version-%release
%else
Requires: %name-libs = %version-%release
%endif
Provides: samba4-winbind-krb5-locator = %version-%release
Obsoletes: samba4-winbind-krb5-locator < %version-%release

%description winbind-krb5-locator
The winbind krb5 locator is a plugin for the system kerberos library to allow
the local kerberos library to use the same KDC as samba and winbind use

%package winbind-devel
Summary: Developer tools for the winbind library
Group: Development/C
Requires: %name-winbind = %version-%release
Provides: samba4-winbind-devel = %version-%release
Obsoletes: samba4-winbind-devel < %version-%release

%description winbind-devel
The samba-winbind package provides developer tools for the wbclient library.
%endif

%package -n ctdb
Summary: A Clustered Database based on Samba's Trivial Database (TDB)
Group: System/Servers

# for ps and killall
Requires: psmisc
Requires: tdb-utils
# for pkill and pidof:
Requires: procps
# for netstat:
Requires: net-tools
Requires: ethtool
# for ip:
Requires: iproute
Requires: iptables
# for flock, getopt, kill:
Requires: util-linux

%description -n ctdb
CTDB is a cluster implementation of the TDB database used by Samba and other
projects to store temporary data. If an application is already using TDB for
temporary data it is very easy to convert that application to be cluster aware
and use CTDB instead.

%package -n ctdb-tests
Summary: CTDB clustered database test suite
Group: Development/Other
Requires: ctdb = %version-%release
Requires: nc

%description -n ctdb-tests
Test suite for CTDB.
CTDB is a cluster implementation of the TDB database used by Samba and other
projects to store temporary data. If an application is already using TDB for
temporary data it is very easy to convert that application to be cluster aware
and use CTDB instead.

%if_with doc
%package doc
Summary: Documentation for the Samba suite
Group: Documentation
Requires: %name-common = %version-%release
BuildArch: noarch

%description doc
The samba-doc package includes all the non-manpage documentation for the
Samba suite.
%endif

%prep
%setup -q
%patch -p1
%patch10 -p1
%patch100 -p 1 -b .samba-4.4.2-s3-winbind-make-sure-domain-member-can-talk-to-trust.patch

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

%define _ntdb_lib ,ntdb,pyntdb
%if_without ntdb
%define _ntdb_lib ,!ntdb,!pyntdb
%endif

%define _ldb_lib ,ldb,pyldb,pyldb-util
%if_without ldb
%define _ldb_lib ,!ldb,!pyldb,!pyldb-util
%endif

%define _samba4_libraries heimdal,!zlib,!popt%{_talloc_lib}%{_tevent_lib}%{_tdb_lib}%{_ldb_lib}

%define _samba4_idmap_modules idmap_ad,idmap_rid,idmap_adex,idmap_hash,idmap_tdb2,idmap_ldap
%define _samba4_pdb_modules pdb_tdbsam,pdb_ldap,pdb_ads,pdb_smbpasswd,pdb_wbc_sam,pdb_samba4
%define _samba4_auth_modules auth_unix,auth_wbc,auth_server,auth_netlogond,auth_script,auth_samba4
# auth_domain needs to be static
%define _samba4_modules %_samba4_idmap_modules,%_samba4_pdb_modules,%_samba4_auth_modules

%define _libsmbclient %nil
%if_without libsmbclient
%define _libsmbclient smbclient,
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
%configure \
	--enable-fhs \
	--with-piddir=/var/run \
	--with-sockets-dir=/var/run/samba \
	--with-modulesdir=%_libdir/samba \
	--with-pammodulesdir=%_lib/security \
	--with-lockdir=%_localstatedir/lib/samba \
	--with-cachedir=%_localstatedir/cache/samba \
	--with-privatedir=/var/lib/samba/private \
	--with-shared-modules=%_samba4_modules \
	--bundled-libraries=%_samba4_libraries \
	--with-pam \
	--with-ads \
	--with-pie \
	--with-relro \
	--without-fam \
	--private-libraries=%_samba4_private_libraries \
%if_with mitkrb5
	--with-system-mitkrb5 \
%endif
%if_without dc
	--without-ad-dc \
%endif
%if_with systemd
	--with-systemd \
%else
	--without-systemd \
%endif
%if_with clustering_support
	--with-cluster-support \
%endif
%if_with testsuite
	--enable-selftest \
%endif
%if_with profiling_data
	--with-profiling-data \
%endif
	%{subst_enable avahi} \
	%{subst_enable glusterfs} \
	--disable-rpath \
	--disable-rpath-install

[ -n "$NPROCS" ] || NPROCS=%__nprocs; export JOBS=$NPROCS
%make_build NPROCS=%__nprocs

%install
%makeinstall_std

mkdir -p %buildroot/sbin
mkdir -p %buildroot/usr/{sbin,bin}
mkdir -p %buildroot/%_lib/security
mkdir -p %buildroot/var/lib/samba
mkdir -p %buildroot/var/lib/ctdb
mkdir -p %buildroot%_localstatedir/cache/samba
mkdir -p %buildroot/var/lib/samba/{private,winbindd_privileged,scripts,sysvol}
mkdir -p %buildroot/var/log/samba/old
mkdir -p %buildroot/var/spool/samba
mkdir -p %buildroot/var/run/{samba,winbindd}
mkdir -p %buildroot%_libdir/samba
mkdir -p %buildroot%_pkgconfigdir
mkdir -p %buildroot%_initdir
mkdir -p %buildroot%_unitdir
mkdir -p %buildroot%_sysconfdir/{pam.d,logrotate.d,security,sysconfig}
mkdir -p %buildroot%_tmpfilesdir

# Move libwbclient.so* into private directory, it cannot be just libdir/samba
# because samba uses rpath with this directory.
install -d -m 0755 %buildroot%_libdir/samba/wbclient
mv %buildroot%_libdir/libwbclient.so* %buildroot%_libdir/samba/wbclient
if [ ! -f %buildroot%_libdir/samba/wbclient/libwbclient.so.%libwbc_alternatives_version ]
then
    echo "Expected libwbclient version not found, please check if version has changed."
    exit -1
fi
ln -s ../..%_libdir/samba/wbclient/libwbclient.so.%libwbc_alternatives_version %buildroot%_libdir/
ln -s ../..%_libdir/samba/wbclient/libwbclient.so.0 %buildroot%_libdir/
ln -s ../..%_libdir/samba/wbclient/libwbclient.so %buildroot%_libdir/

# Add alternatives for libwbclient
mkdir -p %buildroot%_altdir
printf '%_libdir/libwbclient.so.%libwbc_alternatives_version\t%_libdir/samba/wbclient/libwbclient.so.%libwbc_alternatives_version\t10\n' > %buildroot%_altdir/libwbclient-samba
printf '%_libdir/libwbclient.so.0\t%_libdir/samba/wbclient/libwbclient.so.0\t10\n' >> %buildroot%_altdir/libwbclient-samba

printf '%_libdir/libwbclient.so\t%_libdir/samba/wbclient/libwbclient.so\t10\n' > %buildroot%_altdir/libwbclient-devel-samba


# Install other stuff
install -m644 %SOURCE1 %buildroot%_sysconfdir/logrotate.d/samba
install -m644 %SOURCE9 %buildroot%_sysconfdir/samba/smb.conf
install -m644 %SOURCE11 %buildroot%_sysconfdir/security
install -m644 %SOURCE6 %buildroot%_sysconfdir/pam.d/samba
echo 127.0.0.1 localhost > %buildroot%_sysconfdir/samba/lmhosts
mkdir -p %buildroot%_sysconfdir/openldap/schema
install -m644 examples/LDAP/samba.schema %buildroot%_sysconfdir/openldap/schema/samba.schema
install -m755 packaging/printing/smbprint %buildroot%_bindir/smbprint


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
    cat packaging/systemd/$i.service | sed -e 's@\[Service\]@[Service]\nEnvironment=KRB5CCNAME=FILE:/run/samba/krb5cc_samba@g' >tmp$i.service
    install -m 0644 tmp$i.service %buildroot%_unitdir/$i.service
done
subst 's,Type=notify,Type=forking,' %buildroot%_unitdir/*.service
%if_with clustering_support
install -m755 %SOURCE12 %buildroot%_initrddir/ctdb
install -m 0644 ctdb/config/ctdb.service %buildroot%_unitdir
install -m 0644 ctdb/config/ctdbd.conf %buildroot%_sysconfdir/sysconfig/ctdb
echo "d /var/run/ctdb 755 root root" >> %buildroot%_tmpfilesdir/ctdb.conf
touch %buildroot%_sysconfdir/ctdb/nodes
%endif

install -m644 packaging/systemd/samba.conf.tmp %buildroot%_tmpfilesdir/%name.conf

# NetworkManager online/offline script
install -d -m 0755 %buildroot%_sysconfdir/NetworkManager/dispatcher.d/
install -m 0755 packaging/NetworkManager/30-winbind-systemd \
            %buildroot%_sysconfdir/NetworkManager/dispatcher.d/30-winbind


# Clean out crap left behind by the PIDL install.
find %buildroot -type f -name .packlist -exec rm -f {} \;
rm -f %buildroot%perl_vendorlib/wscript_build
rm -rf %buildroot%perl_vendorlib/Parse/Yapp

# winbind
ln -sf ..%_libdir/libnss_winbind.so %buildroot/%_lib/libnss_winbind.so.2
ln -sf ..%_libdir/libnss_wins.so    %buildroot/%_lib/libnss_wins.so.2

mkdir -p  %buildroot%_libdir/krb5/plugins/libkrb5
mv %buildroot%_libdir/winbind_krb5_locator.so %buildroot%_libdir/krb5/plugins/libkrb5/

#cups backend
%define cups_serverbin %(cups-config --serverbin 2>/dev/null)
mkdir -p %buildroot%{cups_serverbin}/backend
ln -s %_bindir/smbspool %buildroot%{cups_serverbin}/backend/smb

# Fix up permission on perl install.
%_fixperms %buildroot%perl_vendor_privlib

# remove tests form python modules
rm -rf %buildroot%python_sitelibdir/samba/{tests,external/subunit,external/testtool}

# Install documentation
%if_with doc
#mkdir -p %buildroot%_defaultdocdir/%name/
#cp -a docs-xml/output/htmldocs %buildroot%_defaultdocdir/%name/
%endif

# Cleanup man pages
%if_without libsmbclient
/bin/rm -f %buildroot%_man7dir/libsmbclient.7*
%endif

# Install pidl/lib/Parse/Pidl/Samba3/Template.pm
cp -a pidl/lib/Parse/Pidl/Samba3/Template.pm %buildroot%_datadir/perl5/Parse/Pidl/Samba3/

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

%if_with winbind
%pre winbind
%_sbindir/groupadd -f -r wbpriv >/dev/null 2>&1 || :

%post winbind
%post_service winbind

%preun winbind
%preun_service winbind
%endif

%post -n ctdb
%post_service ctdb

%preun -n ctdb
%preun_service ctdb

%files
%doc COPYING README WHATSNEW.txt
%doc examples/autofs examples/LDAP examples/misc
%doc examples/printer-accounting examples/printing
%doc %_defaultdocdir/%name/README.downgrade
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
%_sysconfdir/openldap/schema/samba.schema
%_sysconfdir/pam.d/samba
%if_with doc
%_man1dir/smbstatus.1*
%_man8dir/eventlogadm.8*
%_man8dir/smbd.8*
%_man8dir/nmbd.8*
%_man8dir/vfs_*.8*
%endif #doc

%if_with libcephfs
%exclude %_libdir/samba/vfs/ceph.so
%if_with doc
%exclude %_man8dir/vfs_ceph.8*
%endif #doc
%endif # ! libcephfs
%if_enabled glusterfs
%exclude %_libdir/samba/vfs/glusterfs.so
%if_with doc
%exclude %_man8dir/vfs_glusterfs.8*
%endif #doc
%endif # ! glusterfs

%files client
%_bindir/cifsdd
%_bindir/dbwrap_tool
%_bindir/findsmb
%_bindir/nmblookup
%_bindir/oLschema2ldif
%_bindir/regdiff
%_bindir/regpatch
%_bindir/regshell
%_bindir/regtree
%_bindir/rpcclient
%_bindir/samba-regedit
%_bindir/sharesec
%_bindir/smbcacls
%_bindir/smbclient
%_bindir/smbcquotas
%_bindir/smbget
#%_bindir/smbiconv
%_bindir/smbprint
%_bindir/smbspool
#_bindir/smbta-util
%_bindir/smbtar
%_bindir/smbtree
%_libexecdir/samba/smbspool_krb5_wrapper
%{cups_serverbin}/backend/smb
%if_with doc
%_man1dir/dbwrap_tool.1*
%_man1dir/nmblookup.1*
%_man1dir/oLschema2ldif.1*
%_man1dir/regdiff.1*
%_man8dir/samba-regedit.8*
%_man1dir/regpatch.1*
%_man1dir/regshell.1*
%_man1dir/regtree.1*
%exclude %_man1dir/findsmb.1*
%_man1dir/log2pcap.1*
%_man1dir/rpcclient.1*
%_man1dir/sharesec.1*
%_man1dir/smbcacls.1*
%_man1dir/smbclient.1*
%_man1dir/smbcquotas.1*
%_man1dir/smbget.1*
%_man5dir/smbgetrc.5*
%exclude %_man1dir/smbtar.1*
%_man1dir/smbtree.1*
%_man8dir/smbspool.8*
%_man8dir/smbspool_krb5_wrapper.8*
#_man8dir/smbta-util.8*
%_man8dir/cifsdd.8*
%endif #doc

%if_with ntdb
%_bindir/ntdbbackup
%_bindir/ntdbdump
%_bindir/ntdbrestore
%_bindir/ntdbtool
%if_with doc
%_man3dir/ntdb.3*
%_man8dir/ntdbbackup.8*
%_man8dir/ntdbdump.8*
%_man8dir/ntdbrestore.8*
%_man8dir/ntdbtool.8*
%endif #doc
%endif #ntdb
%if_with tdb
%_bindir/tdbbackup
%_bindir/tdbdump
%_bindir/tdbrestore
%_bindir/tdbtool
%if_with doc
%_man8dir/tdbbackup.8*
%_man8dir/tdbdump.8*
%_man8dir/tdbrestore.8*
%_man8dir/tdbtool.8*
%endif #doc
%endif #tdb

%if_with ldb
%_bindir/ldbadd
%_bindir/ldbdel
%_bindir/ldbedit
%_bindir/ldbmodify
%_bindir/ldbrename
%_bindir/ldbsearch
%if_with doc
%_man1dir/ldbadd.1*
%_man1dir/ldbdel.1*
%_man1dir/ldbedit.1*
%_man1dir/ldbmodify.1*
%_man1dir/ldbrename.1*
%_man1dir/ldbsearch.1*
%_libdir/samba/libldb-cmdline.so
%endif #doc
%endif #ldb

%files client-libs
%_libdir/libdcerpc-binding.so.*
%_libdir/libndr.so.*
%_libdir/libndr-krb5pac.so.*
%_libdir/libndr-nbt.so.*
%_libdir/libndr-standard.so.*
%_libdir/libsamba-credentials.so.*
%_libdir/libsamba-errors.so.*
%_libdir/libsamba-passdb.so.*
%_libdir/libsamba-util.so.*
%_libdir/libsamba-hostconfig.so.*
%_libdir/libsamdb.so.*
%_libdir/libsmbconf.so.*
%_libdir/libsmbldap.so.*
%_libdir/libtevent-util.so.*
%_libdir/libdcerpc.so.*

%dir %_libdir/samba
%_libdir/samba/libCHARSET3-samba4.so
%_libdir/samba/libaddns-samba4.so
%_libdir/samba/libads-samba4.so
%_libdir/samba/libasn1util-samba4.so
%_libdir/samba/libauth-sam-reply-samba4.so
%_libdir/samba/libauth-samba4.so
%_libdir/samba/libauthkrb5-samba4.so
%_libdir/samba/libcli-cldap-samba4.so
%_libdir/samba/libcli-ldap-common-samba4.so
%_libdir/samba/libcli-ldap-samba4.so
%_libdir/samba/libcli-nbt-samba4.so
%_libdir/samba/libcli-smb-common-samba4.so
%_libdir/samba/libcli-spoolss-samba4.so
%_libdir/samba/libcliauth-samba4.so
%_libdir/samba/libcmdline-credentials-samba4.so
%_libdir/samba/libdbwrap-samba4.so
%_libdir/samba/libdcerpc-samba-samba4.so
%_libdir/samba/libevents-samba4.so
%_libdir/samba/libflag-mapping-samba4.so
%_libdir/samba/libgenrand-samba4.so
%_libdir/samba/libgensec-samba4.so
%_libdir/samba/libgpo-samba4.so
%_libdir/samba/libgse-samba4.so
%_libdir/samba/libhttp-samba4.so
%_libdir/samba/libinterfaces-samba4.so
%_libdir/samba/libiov-buf-samba4.so
%_libdir/samba/libkrb5samba-samba4.so
%_libdir/samba/libldbsamba-samba4.so
%_libdir/samba/liblibcli-lsa3-samba4.so
%_libdir/samba/liblibcli-netlogon3-samba4.so
%_libdir/samba/liblibsmb-samba4.so
%_libdir/samba/libmessages-dgm-samba4.so
%_libdir/samba/libmessages-util-samba4.so
%_libdir/samba/libmsghdr-samba4.so
%_libdir/samba/libmsrpc3-samba4.so
%_libdir/samba/libndr-samba-samba4.so
%_libdir/samba/libndr-samba4.so
%_libdir/samba/libnet-keytab-samba4.so
%_libdir/samba/libnetif-samba4.so
%_libdir/samba/libnpa-tstream-samba4.so
%_libdir/samba/libprinting-migrate-samba4.so
%_libdir/samba/libregistry-samba4.so
%_libdir/samba/libreplace-samba4.so
%_libdir/samba/libsamba-cluster-support-samba4.so
%_libdir/samba/libsamba-debug-samba4.so
%_libdir/samba/libsamba-modules-samba4.so
%_libdir/samba/libsamba-security-samba4.so
%_libdir/samba/libsamba-sockets-samba4.so
%_libdir/samba/libsamba3-util-samba4.so
%_libdir/samba/libsamdb-common-samba4.so
%_libdir/samba/libsecrets3-samba4.so
%_libdir/samba/libserver-id-db-samba4.so
%_libdir/samba/libserver-role-samba4.so
%_libdir/samba/libsmb-transport-samba4.so
%_libdir/samba/libsmbclient-raw-samba4.so
%_libdir/samba/libsmbd-base-samba4.so
%_libdir/samba/libsmbd-conn-samba4.so
%_libdir/samba/libsmbd-shim-samba4.so
%_libdir/samba/libsmbldaphelper-samba4.so
%_libdir/samba/libsys-rw-samba4.so
%_libdir/samba/libsocket-blocking-samba4.so
%_libdir/samba/libtalloc-report-samba4.so
%_libdir/samba/libtdb-wrap-samba4.so
%_libdir/samba/libtime-basic-samba4.so
%_libdir/samba/libtorture-samba4.so
%_libdir/samba/libtrusts-util-samba4.so
%_libdir/samba/libutil-cmdline-samba4.so
%_libdir/samba/libutil-reg-samba4.so
%_libdir/samba/libutil-setid-samba4.so
%_libdir/samba/libutil-tdb-samba4.so

%if_without libwbclient
%_libdir/libwbclient.so.*
%_libdir/samba/wbclient/libwbclient.so.*
%_libdir/samba/libwinbind-client-samba4.so
%_altdir/libwbclient-samba
%endif # ! with_libwbclient

%if_without libsmbclient
%_libdir/samba/libsmbclient.so.*
%if_with doc
%_mandir/man7/libsmbclient.7*
%endif #doc
%endif # ! with_libsmbclient

%if_with talloc
%_libdir/samba/libtalloc.so.*
%_libdir/samba/libpytalloc-util.so.*
%if_with doc
%_man3dir/talloc.3.*
%endif #doc
%endif #talloc

%if_with tevent
%_libdir/samba/libtevent.so.*
%endif

%if_with tdb
%_libdir/samba/libtdb.so.*
%endif

%if_with ldb
%_libdir/samba/libldb.so.*
%if_with doc
%_man3dir/ldb.3.*
%endif #doc
%endif #ldb

%files common
%_tmpfilesdir/%name.conf
%config(noreplace) %_sysconfdir/logrotate.d/samba
%attr(0700,root,root) %dir /var/log/samba
%attr(0700,root,root) %dir /var/log/samba/old
%dir /var/run/samba
%dir /var/run/winbindd
%dir /var/lib/samba
%attr(755,root,root) %dir %_localstatedir/cache/samba
%attr(700,root,root) %dir /var/lib/samba/private
%attr(755,root,root) %dir %_sysconfdir/samba
%config(noreplace) %_sysconfdir/samba/smb.conf
%config(noreplace) %_sysconfdir/samba/lmhosts
%config(noreplace) %_sysconfdir/sysconfig/samba

%files common-libs
%_libdir/samba/libpopt-samba3-samba4.so

%_libdir/samba/pdb

%if_with pam_smbpass
%_libdir/security/pam_smbpass.so
%endif

%files common-tools  -f net.lang
%_bindir/mvxattr
%_bindir/net
%_bindir/pdbedit
%_bindir/profiles
%_bindir/smbcontrol
%_bindir/smbpasswd
%_bindir/testparm
%if_with doc
%_man1dir/mvxattr.1*
%_man1dir/profiles.1*
%_man1dir/smbcontrol.1*
%_man1dir/testparm.1*
%_man5dir/lmhosts.5*
%_man5dir/smb.conf.5*
%_man5dir/smbpasswd.5*
%_man7dir/samba.7*
%_man8dir/net.8*
%_man8dir/pdbedit.8*
%_man8dir/smbpasswd.8*
%endif #doc

%files dc
%if_with dc
%_bindir/samba-tool
%_sbindir/samba
%_sbindir/samba_kcc
%_sbindir/samba_dnsupdate
%_sbindir/samba_spnupdate
%_sbindir/samba_upgradedns
%_sbindir/upgradeprovision
%_libdir/samba/bind9/dlz_bind9.so
%_libdir/samba/libheimntlm-samba4.so.*
%_libdir/samba/libkdc-samba4.so.*
%_libdir/samba/libpac-samba4.so
%dir %_libdir/samba/gensec
%_libdir/samba/gensec/krb5.so
%dir /var/lib/samba/sysvol
%_datadir/samba/setup
%if_with doc
%_man8dir/samba.8*
%_man8dir/samba-tool.8*
%endif #doc
%else
%doc %_defaultdocdir/%name/README.dc
%if_with doc
%exclude %_man8dir/samba.8*
%exclude %_man8dir/samba-tool.8*
%endif #doc
%exclude %_libdir/samba/ldb/ildap.so
%exclude %_libdir/samba/ldb/ldbsamba_extensions.so
%endif

%files dc-libs
%if_with dc
%_libdir/samba/libprocess-model-samba4.so
%_libdir/samba/libservice-samba4.so
%dir %_libdir/samba/process_model
%_libdir/samba/process_model/standard.so
%dir %_libdir/samba/service
%_libdir/samba/service/cldap.so
%_libdir/samba/service/dcerpc.so
%_libdir/samba/service/dns.so
%_libdir/samba/service/dns_update.so
%_libdir/samba/service/drepl.so
%_libdir/samba/service/kcc.so
%_libdir/samba/service/kdc.so
%_libdir/samba/service/ldap.so
%_libdir/samba/service/nbtd.so
%_libdir/samba/service/ntp_signd.so
%_libdir/samba/service/s3fs.so
%_libdir/samba/service/smb.so
%_libdir/samba/service/web.so
%_libdir/samba/service/winbindd.so
%_libdir/samba/service/wrepl.so
%_libdir/libdcerpc-server.so.*
%_libdir/samba/libdfs-server-ad-samba4.so
%_libdir/samba/libdnsserver-common-samba4.so
%_libdir/samba/libdsdb-module-samba4.so
%_libdir/samba/libntvfs-samba4.so
%_libdir/samba/libposix-eadb-samba4.so
%_libdir/samba/bind9/dlz_bind9_9.so
%else
%doc %_defaultdocdir/%name/README.dc-libs
%endif

%files devel
%_includedir/samba-4.0

%exclude %_includedir/samba-4.0/netapi.h
#%exclude %_includedir/samba-4.0/torture.h
%if_with libsmbclient
%exclude %_includedir/samba-4.0/libsmbclient.h
%endif
%if_with libwbclient
%exclude %_includedir/samba-4.0/wbclient.h
%endif

%_libdir/libdcerpc-binding.so
%_libdir/libdcerpc-samr.so
%_libdir/libdcerpc.so
%_libdir/libndr-krb5pac.so
%_libdir/libndr-nbt.so
%_libdir/libndr-standard.so
%_libdir/libndr.so
%_libdir/libnetapi.so
%_libdir/libsamba-credentials.so
%_libdir/libsamba-errors.so
%_libdir/libsamba-hostconfig.so
%_libdir/libsamba-policy.so
%_libdir/libsamba-util.so
%_libdir/libsamdb.so
%_libdir/libsmbconf.so
%_libdir/libtevent-util.so
%_libdir/libsamba-passdb.so
%_libdir/libsmbldap.so

%_pkgconfigdir/dcerpc.pc
%_pkgconfigdir/dcerpc_samr.pc
%_pkgconfigdir/ndr.pc
%_pkgconfigdir/ndr_krb5pac.pc
%_pkgconfigdir/ndr_nbt.pc
%_pkgconfigdir/ndr_standard.pc
%_pkgconfigdir/netapi.pc
%_pkgconfigdir/samba-credentials.pc
%_pkgconfigdir/samba-hostconfig.pc
%_pkgconfigdir/samba-policy.pc
%_pkgconfigdir/samba-util.pc
%_pkgconfigdir/samdb.pc

%if_with dc
%_libdir/libdcerpc-server.so
%_pkgconfigdir/dcerpc_server.pc
%endif

%if_with libcephfs
%files vfs-cephfs
%_libdir/samba/vfs/ceph.so
%if_with doc
%_man8dir/vfs_ceph.8*
%endif #doc
%endif #vfs-cephfs

%if_enabled glusterfs
%files vfs-glusterfs
%_libdir/samba/vfs/glusterfs.so
%if_with doc
%_man8dir/vfs_glusterfs.8*
%endif #doc
%endif #vfs-glusterfs

%files libs
%_libdir/libdcerpc-samr.so.*
%_libdir/libsamba-policy.so.*

# libraries needed by the public libraries
%_libdir/samba/libMESSAGING-samba4.so
%_libdir/samba/libLIBWBCLIENT-OLD-samba4.so
%_libdir/samba/libauth4-samba4.so
%_libdir/samba/libauth-unix-token-samba4.so
%_libdir/samba/libcluster-samba4.so
%_libdir/samba/libdcerpc-samba4.so
%_libdir/samba/libdsdb-garbage-collect-tombstones-samba4.so
%_libdir/samba/libnon-posix-acls-samba4.so
%_libdir/samba/libposix-eadb-samba4.so
%_libdir/samba/libsamba-net-samba4.so
%_libdir/samba/libsamba-python-samba4.so
%_libdir/samba/libshares-samba4.so
%_libdir/samba/libsmbpasswdparser-samba4.so
%_libdir/samba/libxattr-tdb-samba4.so

%if_with dc
%_libdir/samba/libdb-glue-samba4.so
%_libdir/samba/libHDB-SAMBA4-samba4.so
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

%if_with libsmbclient
%files -n libsmbclient
%_libdir/libsmbclient.so.*

%files -n libsmbclient-devel
%_includedir/samba-4.0/libsmbclient.h
%_libdir/libsmbclient.so
%_pkgconfigdir/smbclient.pc
%if_with doc
%_man7dir/libsmbclient.7*
%endif #doc
%endif #libsmbclient-devel

%if_with libwbclient
%files -n libwbclient
%ghost %_libdir/libwbclient.so.*
%_libdir/samba/wbclient/libwbclient.so.*
%_libdir/samba/libwinbind-client-samba4.so
%_altdir/libwbclient-samba

%files -n libwbclient-devel
%_includedir/samba-4.0/wbclient.h
%ghost %_libdir/libwbclient.so
%_libdir/samba/wbclient/libwbclient.so
%_altdir/libwbclient-devel-samba
%_pkgconfigdir/wbclient.pc
%endif

%if_with libnetapi
%files -n libnetapi
%_libdir/libnetapi.so.*
%endif

%files pidl
%attr(755,root,root) %_bindir/pidl
%if_with doc
%_man1dir/pidl.1.*
%_man3dir/Parse::Pidl::*
%endif
%perl_vendor_privlib/*

%files -n python-module-%name
%python_sitelibdir/*

%if_with doc
#%files doc
#%doc docs-xml/output/htmldocs
%endif

%files test
%_bindir/gentest
%_bindir/locktest
%_bindir/masktest
%_bindir/ndrdump
%_bindir/smbtorture
%if_with doc
%_man1dir/gentest.1*
%_man1dir/locktest.1*
%_man1dir/masktest.1*
%_man1dir/ndrdump.1*
%_man1dir/smbtorture.1*
%_man1dir/vfstest.1*
%endif #doc

%if_with testsuite
# files to ignore in testsuite mode
%_libdir/samba/libnss-wrapper.so
%_libdir/samba/libsocket-wrapper.so
%_libdir/samba/libuid-wrapper.so
%endif

%if_without dc
%_libdir/samba/libdsdb-module-samba4.so
%endif

%if_with winbind
%files winbind -f pam_winbind.lang
%_libdir/samba/idmap
%_libdir/samba/nss_info
%_libdir/samba/libnss-info-samba4.so
%_libdir/samba/libidmap-samba4.so
%_sbindir/winbindd
%attr(750,root,wbpriv) %dir /var/lib/samba/winbindd_privileged
%_unitdir/winbind.service
%attr(755,root,root) %_initrddir/winbind
%_sysconfdir/NetworkManager/dispatcher.d/30-winbind

%if_with doc
%_man8dir/winbindd.8*
%_man8dir/idmap_*.8*
%endif #endif

%files winbind-clients
%_bindir/ntlm_auth
%_bindir/wbinfo
%_libdir/libnss_winbind.so*
/%_lib/libnss_winbind.so.*
%_libdir/libnss_wins.so*
/%_lib/libnss_wins.so.*
/%_lib/security/pam_winbind.so
%config(noreplace) %_sysconfdir/security/pam_winbind.conf
%if_with doc
%_man1dir/ntlm_auth.1.*
%_man1dir/wbinfo.1*
%_man5dir/pam_winbind.conf.5*
%_man8dir/pam_winbind.8*
%endif #doc

%files winbind-krb5-locator
%_libdir/krb5/plugins/libkrb5/winbind_krb5_locator.so
%if_with doc
%_man7dir/winbind_krb5_locator.7*
%endif #doc
%endif

%if_with clustering_support
%files -n ctdb
#doc ctdb/README
%config(noreplace) %_sysconfdir/sysconfig/ctdb
%dir %_sysconfdir/ctdb
%config(noreplace) %_sysconfdir/ctdb/nodes
%config(noreplace) %_sysconfdir/ctdb/notify.sh
%config(noreplace) %_sysconfdir/ctdb/debug-hung-script.sh
%config(noreplace) %_sysconfdir/ctdb/ctdb-crash-cleanup.sh
%config(noreplace) %_sysconfdir/ctdb/gcore_trace.sh
%config(noreplace) %_sysconfdir/ctdb/functions
%config(noreplace) %_sysconfdir/ctdb/debug_locks.sh
%_sysconfdir/ctdb/statd-callout
%dir /var/lib/ctdb
%_unitdir/ctdb.service
%_initdir/ctdb
%_tmpfilesdir/ctdb.conf

%_sysconfdir/ctdb/nfs-checks.d
%_sysconfdir/ctdb/nfs-linux-kernel-callout
%_sysconfdir/sudoers.d/ctdb
%_sysconfdir/ctdb/events.d
%dir %_sysconfdir/ctdb/notify.d
%_sysconfdir/ctdb/notify.d/README
%_sbindir/ctdbd
%_sbindir/ctdbd_wrapper
%_bindir/ctdb
%_bindir/ctdb_diagnostics
%_bindir/ltdbtool
%_bindir/onnode
%_bindir/ping_pong
%_libexecdir/ctdb/ctdb_event
%_libexecdir/ctdb/ctdb_eventd
%_libexecdir/ctdb/ctdb_killtcp
%_libexecdir/ctdb/ctdb_lock_helper
%_libexecdir/ctdb/ctdb_lvs
%_libexecdir/ctdb/ctdb_mutex_fcntl_helper
%_libexecdir/ctdb/ctdb_natgw
%_libexecdir/ctdb/ctdb_recovery_helper
%_libexecdir/ctdb/ctdb_takeover_helper
%_libexecdir/ctdb/smnotify

%if_with doc
%_man1dir/ctdb.1*
%_man1dir/ctdbd.1*
%_man1dir/onnode.1*
%_man1dir/ltdbtool.1*
%_man1dir/ping_pong.1*
%_man1dir/ctdb_diagnostics.1*
%_man1dir/ctdbd_wrapper.1*
%_man5dir/ctdbd.conf.5*
%_man7dir/ctdb.7*
%_man7dir/ctdb-tunables.7*
%_man7dir/ctdb-statistics.7*
%endif #doc

%files -n ctdb-tests
%_libexecdir/ctdb/tests
%_bindir/ctdb_run_tests
%_bindir/ctdb_run_cluster_tests
%_datadir/ctdb/tests
%doc ctdb/tests/README
%endif

%changelog
* Wed Nov 29 2017 Evgeny Sinelnikov <sin@altlinux.org> 4.6.11-alt2%ubt
- Backport from Heimdal upstream include/includedir directives for krb5.conf

* Tue Nov 21 2017 Evgeny Sinelnikov <sin@altlinux.org> 4.6.11-alt1%ubt
- Second autumn security release (Fixes: CVE-2017-14746, CVE-2017-15275)

* Thu Nov 16 2017 Evgeny Sinelnikov <sin@altlinux.org> 4.6.10-alt1%ubt
- Update for third autumn release with common bugfixes

* Wed Oct 25 2017 Evgeny Sinelnikov <sin@altlinux.org> 4.6.9-alt1%ubt
- Update for second autumn release with common bugfixes

* Wed Sep 27 2017 Alexey Shabalin <shaba@altlinux.ru> 4.6.8-alt2%ubt
- rebuild with new  libcephfs

* Wed Sep 20 2017 Evgeny Sinelnikov <sin@altlinux.ru> 4.6.8-alt1%ubt
- Update for autumn security release:
  + CVE-2017-12150 (SMB1/2/3 connections may not require signing where they
   should)
  + CVE-2017-12151 (SMB3 connections don't keep encryption across DFS redirects)
  + CVE-2017-12163 (Server memory information leak over SMB1)

* Wed Sep 20 2017 Evgeny Sinelnikov <sin@altlinux.ru> 4.6.7-alt3%ubt
- Avoid build trouble with ubt macros id on branch c8

* Fri Aug 18 2017 Evgeny Sinelnikov <sin@altlinux.ru> 4.6.7-alt2%ubt
- Clean code from old merged chunks
- Enable parallel build

* Wed Aug 09 2017 Evgeny Sinelnikov <sin@altlinux.ru> 4.6.7-alt1%ubt
- Update to second summer release

* Sat Jul 15 2017 Evgeny Sinelnikov <sin@altlinux.ru> 4.6.6-alt2%ubt
- Rebuild with universal build tag (aka ubt macros) for p7 and c7

* Wed Jul 12 2017 Evgeny Sinelnikov <sin@altlinux.ru> 4.6.6-alt1%ubt
- Update to summer security release
- Security fixes:
  + CVE-2017-11103 Orpheus' Lyre KDC-REP service name validation
  (Samba binaries built against MIT Kerberos are not vulnerable.)

* Tue Jun 06 2017 Evgeny Sinelnikov <sin@altlinux.ru> 4.6.5-alt1%ubt
- Udpate to first summer release

* Wed May 24 2017 Evgeny Sinelnikov <sin@altlinux.ru> 4.6.4-alt1%ubt
- Update to second spring security release
- Fix longtime initialization bug in ldb proxy
- Security fixes:
  + CVE-2017-7494 Remote code execution from a writable share

* Tue Apr 25 2017 Evgeny Sinelnikov <sin@altlinux.ru> 4.6.3-alt1%ubt
- Udpate to second spring release

* Wed Apr 19 2017 Evgeny Sinelnikov <sin@altlinux.ru> 4.6.2-alt3%ubt
- Remove conflict winbind with libwbclient-sssd due upgrade problems

* Wed Apr 12 2017 Evgeny Sinelnikov <sin@altlinux.ru> 4.6.2-alt2%ubt
- Fix problem with failed to create kerberos keytab during join to domain

* Fri Mar 31 2017 Evgeny Sinelnikov <sin@altlinux.ru> 4.6.2-alt1%ubt
- Update with regression fix of spring security release
- Revert winbind problem fixes with access user to keytab due troubles in 4.6.x

* Thu Mar 23 2017 Evgeny Sinelnikov <sin@altlinux.ru> 4.6.1-alt1%ubt
- Update to spring security release
- Fixed build --without docs (closes: 33118)
- Security fixes:
  + CVE-2017-2619 Symlink race allows access outside share definition

* Tue Mar 07 2017 Evgeny Sinelnikov <sin@altlinux.ru> 4.6.0-alt1%ubt
- Udpate to first spring release

* Wed Feb 01 2017 Evgeny Sinelnikov <sin@altlinux.ru> 4.5.5-alt1%ubt
- Update to winter release

* Sun Jan 01 2017 Evgeny Sinelnikov <sin@altlinux.ru> 4.5.3-alt3%ubt
- Fix winbind problem with access user to keytab

* Wed Dec 28 2016 Evgeny Sinelnikov <sin@altlinux.ru> 4.5.3-alt2%ubt
- Do not delete an existing valid credential cache for KEYRING type
- Set FQDN to lower at fill_mem_keytab_from_system_keytab()

* Mon Dec 19 2016 Evgeny Sinelnikov <sin@altlinux.ru> 4.5.3-alt1%ubt
- Update for release with security fixes:
  - CVE-2016-2123 (ndr_pull_dnsp_name contains an integer wrap problem)
  - CVE-2016-2125 (client code always requests a forwardable ticket)
  - CVE-2016-2126 (crash winbindd using a legitimate Kerberos ticket)

* Mon Dec 12 2016 Evgeny Sinelnikov <sin@altlinux.ru> 4.5.2-alt1%ubt
- Udpate to first winter release

* Sat Dec 03 2016 Evgeny Sinelnikov <sin@altlinux.ru> 4.5.1-alt2
- Add conflict winbind with libwbclient-sssd due compatibility
- Update build dependencies versions for external samba libraries

* Sat Oct 29 2016 Evgeny Sinelnikov <sin@altlinux.ru> 4.5.1-alt1
- Update with variety of fixes for autumn release

* Fri Sep 09 2016 Evgeny Sinelnikov <sin@altlinux.ru> 4.5.0-alt1
- Update to autumn release

* Sun Jul 10 2016 Andrey Cherepanov <cas@altlinux.org> 4.4.5-alt1
- Update for security release with CVE-2016-2119

* Tue May 24 2016 Alexey Shabalin <shaba@altlinux.ru> 4.4.3-alt2
- build with libsystemd without compat libs
- add patches from fedora
- add again samba-grouppwd.patch

* Wed May 04 2016 Andrey Cherepanov <cas@altlinux.org> 4.4.3-alt1
- New version

* Thu Apr 28 2016 Andrey Cherepanov <cas@altlinux.org> 4.4.2-alt2
- Fix CVE-2016-2110/NTLMSSP regression (https://bugzilla.samba.org/show_bug.cgi?id=11849)

* Tue Apr 12 2016 Andrey Cherepanov <cas@altlinux.org> 4.4.2-alt1
- New version
- Security fixes:
  - CVE-2015-5370 (Multiple errors in DCE-RPC code)
  - CVE-2016-2110 (Man in the middle attacks possible with NTLMSSP)
  - CVE-2016-2111 (NETLOGON Spoofing Vulnerability)
  - CVE-2016-2112 (LDAP client and server don't enforce integrity)
  - CVE-2016-2113 (Missing TLS certificate validation)
  - CVE-2016-2114 ("server signing = mandatory" not enforced)
  - CVE-2016-2115 (SMB IPC traffic is not integrity protected)
  - CVE-2016-2118 (SAMR and LSA man in the middle attacks possible)

* Tue Mar 22 2016 Andrey Cherepanov <cas@altlinux.org> 4.4.0-alt1
- New version (https://www.samba.org/samba/history/samba-4.4.0.html)

* Sun Mar 13 2016 Andrey Cherepanov <cas@altlinux.org> 4.3.6-alt2
- Rebuild with downgraded libtalloc

* Wed Mar 09 2016 Andrey Cherepanov <cas@altlinux.org> 4.3.6-alt1
- New version (https://www.samba.org/samba/history/samba-4.3.6.html)
- Security fixes:
  - CVE-2015-7560 (Incorrect ACL get/set allowed on symlink path)
  - CVE-2016-0771 (Out-of-bounds read in internal DNS server)
- Do not use specified GID for wbpriv group (ALT #31858)

* Thu Mar 03 2016 Andrey Cherepanov <cas@altlinux.org> 4.3.5-alt1
- New version (https://www.samba.org/samba/history/samba-4.3.5.html)

* Tue Jan 12 2016 Andrey Cherepanov <cas@altlinux.org> 4.3.4-alt1
- New version (https://www.samba.org/samba/history/samba-4.3.4.html)

* Thu Dec 24 2015 Andrey Cherepanov <cas@altlinux.org> 4.3.3-alt2
- Change services type from notify to forking

* Wed Dec 16 2015 Andrey Cherepanov <cas@altlinux.org> 4.3.3-alt1
- New version (https://www.samba.org/samba/history/samba-4.3.3.html)
- Security fixes:
  - CVE-2015-3223 (Denial of service in Samba Active Directory
  server)
  - CVE-2015-5252 (Insufficient symlink verification in smbd)
  - CVE-2015-5299 (Missing access control check in shadow copy
  code)
  - CVE-2015-5296 (Samba client requesting encryption vulnerable
  to downgrade attack)
  - CVE-2015-8467 (Denial of service attack against Windows
  Active Directory server)
  - CVE-2015-5330 (Remote memory read in Samba LDAP server)

* Tue Dec 08 2015 Igor Vlasenko <viy@altlinux.ru> 4.3.1-alt1.1
- NMU: dropped unused prehistoric BR: perl-Perl4-CoreLibs

* Fri Oct 23 2015 Alexey Shabalin <shaba@altlinux.ru> 4.3.1-alt1
- 4.3.1

* Thu Sep 10 2015 Alexey Shabalin <shaba@altlinux.ru> 4.3.0-alt1
- 4.3.0

* Wed Jul 15 2015 Alexey Shabalin <shaba@altlinux.ru> 4.2.3-alt1
- 4.2.3
- add alternatives for libwbclient

* Mon Mar 23 2015 Alexey Shabalin <shaba@altlinux.ru> 4.2.0-alt1
- 4.2.0

* Mon Feb 23 2015 Anton V. Boyarshinov <boyarsh@altlinux.ru> 4.1.17-alt1
- 4.1.17
- CVE-2015-0240 fixed

* Mon Jan 12 2015 Alexey Shabalin <shaba@altlinux.ru> 4.1.15-alt1
- 4.1.15

* Mon Dec 15 2014 Alexey Shabalin <shaba@altlinux.ru> 4.1.14-alt1
- 4.1.14

* Fri Nov 07 2014 Alexey Shabalin <shaba@altlinux.ru> 4.1.13-alt1
- 4.1.13

* Mon Sep 22 2014 Alexey Shabalin <shaba@altlinux.ru> 4.1.12-alt1
- 4.1.12

* Wed Aug 27 2014 Alexey Shabalin <shaba@altlinux.ru> 4.1.11-alt2
- update init scripts for ALTLinux

* Tue Aug 05 2014 Alexey Shabalin <shaba@altlinux.ru> 4.1.11-alt1
- 4.1.11
- fixed unstrcpy macro length is invalid(CVE-2014-3560)

* Mon Jul 28 2014 Alexey Shabalin <shaba@altlinux.ru> 4.1.10-alt1
- 4.1.10

* Tue Jun 24 2014 Alexey Shabalin <shaba@altlinux.ru> 4.1.9-alt1
- 4.1.9
- fixed nmbd denial of service(CVE-2014-0244)
- fixed Segmentation fault in smbd_marshall_dir_entry(CVE-2014-3493)

* Wed Jun 04 2014 Alexey Shabalin <shaba@altlinux.ru> 4.1.8-alt1
- 4.1.8
- fixed CVE-2014-0239, CVE-2014-0178

* Wed May 07 2014 Alexey Shabalin <shaba@altlinux.ru> 4.1.7-alt2
- add winbind-krb5-locator package

* Mon May 05 2014 Alexey Shabalin <shaba@altlinux.ru> 4.1.7-alt1
- 4.1.7

* Mon Mar 17 2014 Alexey Shabalin <shaba@altlinux.ru> 4.1.6-alt1
- 4.1.6
- fixed CVE-2013-4496, CVE-2013-6442

* Wed Jan 15 2014 Alexey Shabalin <shaba@altlinux.ru> 4.1.4-alt1
- 4.1.4

* Mon Dec 09 2013 Alexey Shabalin <shaba@altlinux.ru> 4.1.3-alt1
- 4.1.3
- fixed CVE-2013-4408, CVE-2012-6150

* Wed Dec 04 2013 Alexey Shabalin <shaba@altlinux.ru> 4.1.2-alt1
- 4.1.2
- drop swat package
- change build options:
  + --with-profiling-data
  + drop --disable-ntdb
  + --without-fam
  + drop --builtin-libraries=ccan
- build with avahi support
- build with external libntdb

* Wed Nov 27 2013 Alexey Shabalin <shaba@altlinux.ru> 4.0.12-alt1
- 4.0.12

* Tue Nov 12 2013 Alexey Shabalin <shaba@altlinux.ru> 4.0.11-alt1
- 4.0.11
- fixed CVE-2013-4475, CVE-2013-4476

* Tue Oct 08 2013 Alexey Shabalin <shaba@altlinux.ru> 4.0.10-alt1
- 4.0.10

* Mon Aug 26 2013 Alexey Shabalin <shaba@altlinux.ru> 4.0.9-alt1
- 4.0.9
- add -D options for default forking type start of services to sysV init and systemd

* Wed Aug 07 2013 Alexey Shabalin <shaba@altlinux.ru> 4.0.8-alt1
- 4.0.8
- fixed CVE-2013-4124

* Wed Jul 03 2013 Alexey Shabalin <shaba@altlinux.ru> 4.0.7-alt1
- 4.0.7

* Thu May 23 2013 Alexey Shabalin <shaba@altlinux.ru> 4.0.6-alt1
- 4.0.6

* Tue Apr 09 2013 Alexey Shabalin <shaba@altlinux.ru> 4.0.5-alt1
- 4.0.5

* Tue Mar 19 2013 Alexey Shabalin <shaba@altlinux.ru> 4.0.4-alt1
- 4.0.4 (fixed CVE-2013-186)
- add /var/cache/samba to samba-common package (ALT#28601)

* Mon Feb 25 2013 Alexey Shabalin <shaba@altlinux.ru> 4.0.3-alt2
- make systemctl reference indirect in packaging/NetworkManager/30-winbind-systemd (ALT#28585)

* Fri Feb 15 2013 Alexey Shabalin <shaba@altlinux.ru> 4.0.3-alt1
- 4.0.3
- build as default samba, replaced samba4 packages
- rename pdb_ldap to pdb_ldapsam

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

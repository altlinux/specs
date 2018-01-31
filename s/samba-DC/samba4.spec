%set_verify_elf_method unresolved=relaxed
%add_findprov_skiplist /%_lib/*
%add_debuginfo_skiplist /%_lib

%define rname samba
%define _localstatedir /var
%define libwbc_alternatives_version 0.13

# internal libs
%def_without talloc
%def_without tevent
%def_without tdb
%def_without ntdb
%def_without ldb
%def_with    winbind

%def_with profiling_data

# build as separate package
%def_without libsmbclient
%def_with libwbclient
%def_without libnetapi
%def_with doc

%def_with dc
%def_without ntvfs
%def_with clustering_support
%def_without testsuite

%if_with testsuite
# The testsuite only works with a full build right now.
%force_with dc
%endif

%if_with dc
%def_with ldb_modules
# Samba Active Directory Domain Controller implementation is not available with MIT Kereberos
%def_without mitkrb5
%else
%def_with mitkrb5
%endif

%def_with systemd
%def_enable avahi
%def_enable glusterfs
%def_with libcephfs

Name:    samba-DC
Version: 4.6.12
Release: alt2%ubt

Group:   System/Servers
Summary: Samba Active Directory Domain Controller
License: GPLv3+ and LGPLv3+
Url:     http://www.samba.org/

Source:  %rname-%version.tar

# Red Hat specific replacement-files
Source1: samba.log
Source5: smb.init
Source6: samba.pamd
Source8: winbind.init
Source9: smb.conf.default
Source10: nmb.init
Source11: pam_winbind.conf
Source12: ctdb.init
Source13: samba.limits
Source20: samba.init

Source200: README.dc
Source201: README.downgrade

Patch: %rname-%version-alt.patch
Patch10: samba-grouppwd.patch

# fedora patches
Patch100:         samba-4.4.2-s3-winbind-make-sure-domain-member-can-talk-to-trust.patch

Conflicts: %rname
Conflicts: %rname-dc

# Need for samba_upgradedns
Requires: tdb-utils
Requires(pre): %name-common = %version-%release
Requires: %name-libs = %version-%release
%if_with winbind
Requires: %name-winbind-clients = %version-%release
%endif
%if_with libwbclient
Requires: libwbclient-DC = %version-%release
%endif

BuildRequires(pre):rpm-build-ubt

BuildRequires: /proc
BuildRequires: libe2fs-devel
BuildRequires: libacl-devel
BuildRequires: libattr-devel
BuildRequires: libgnutls-devel
BuildRequires: libncurses-devel
BuildRequires: libpam-devel
BuildRequires: perl-devel
BuildRequires: perl-Parse-Yapp
BuildRequires: libpopt-devel
BuildRequires: python-devel
BuildRequires: libreadline-devel
BuildRequires: libldap-devel
BuildRequires: zlib-devel
BuildRequires: libarchive-devel >= 3.1.2

%if_with mitkrb5
BuildRequires: libssl-devel
BuildRequires: libkrb5-devel
%endif
BuildRequires: glibc-devel glibc-kernheaders
# https://bugzilla.samba.org/show_bug.cgi?id=9863
BuildConflicts: setproctitle-devel
BuildRequires: libiniparser-devel
BuildRequires: libcups-devel
BuildRequires: gawk libgtk+2-devel libcap-devel libuuid-devel
%{?_with_doc:BuildRequires: inkscape libxslt xsltproc netpbm dblatex html2text docbook-style-xsl}
%{?_without_talloc:BuildRequires: libtalloc-devel >= 2.1.10 libpytalloc-devel}
%{?_without_tevent:BuildRequires: libtevent-devel >= 0.9.34 python-module-tevent}
%{?_without_tdb:BuildRequires: libtdb-devel >= 1.3.12  python-module-tdb}
%{?_without_ntdb:BuildRequires: libntdb-devel >= 0.9  python-module-ntdb}
%{?_without_ldb:BuildRequires: libldb-devel >= 1.1.29 python-module-pyldb-devel}
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

%description
Samba is the standard Windows interoperability suite of programs for Linux and Unix.

%package client
Summary: Samba client programs
Group: Networking/Other
Requires: %name-common = %version-%release
Requires: %name-libs = %version-%release
%if_with libsmbclient
Requires: libsmbclient-DC = %version-%release
%endif
Conflicts: %rname-client

%description client
The %rname-client package provides some SMB/CIFS clients to complement
the built-in SMB/CIFS filesystem in Linux. These clients allow access
of SMB/CIFS shares and printing to SMB/CIFS printers.

%package common
Summary: Files used by both Samba servers and clients
Group: System/Servers
Requires: %name-libs = %version-%release
%if_with libnetapi
Requires: libnetapi-DC = %version-%release
%endif
Conflicts: %rname-common

%description common
%rname-common provides files necessary for both the server and client
packages of Samba.

%package libs
Summary: Samba libraries
Group: System/Libraries
Conflicts: %rname-dc-libs

%if_with libnetapi
Requires: libnetapi-DC = %version-%release
%endif
%if_with libwbclient
Requires: libwbclient-DC = %version-%release
%endif
%if_with libsmbclient
Requires: libsmbclient-DC = %version-%release
%endif
%if_with ldb_modules
Requires: libldb-modules-DC = %version-%release
%endif

%description libs
The %rname-libs package contains the libraries needed by programs that
link against the SMB, RPC and other protocols provided by the Samba suite.

%package common-libs
Summary: Samba common libraries
Group: System/Libraries

%description common-libs
The %rname-common-libs package contains the common libraries needed by modules that
link against the SMB, RPC and other protocols provided by the Samba suite.

%package -n libsmbclient-DC
Summary: The SMB client library
Group: System/Libraries
Conflicts: libsmbclient

%description -n libsmbclient-DC
The libsmbclient contains the SMB client library from the Samba suite.

%package -n libldb-modules-DC
Summary: The LDB domain controller modules
Group: System/Libraries

%description -n libldb-modules-DC
The libldb-modules-DC contains the ldb library modules from the Samba domain controller.

%package -n libsmbclient-DC-devel
Summary: Developer tools for the SMB client library
Group: Development/C
Requires: libsmbclient-DC = %version-%release
Conflicts: libsmbclient-devel

%description -n libsmbclient-DC-devel
The libsmbclient-devel package contains the header files and libraries needed to
develop programs that link against the SMB client library in the Samba suite.

%package -n libwbclient-DC
Summary: The winbind client library
Group: System/Libraries
Provides: libwbclient = %version-%release
Conflicts: libwbclient-sssd

%description -n libwbclient-DC
The libwbclient package contains the winbind client library from the Samba suite.

%package -n libwbclient-DC-devel
Summary: Developer tools for the winbind library
Group: Development/C
Requires: libwbclient-DC = %version-%release
Conflicts: libwbclient-devel

%description -n libwbclient-DC-devel
The libwbclient-devel package provides developer tools for the wbclient library.

%package -n libnetapi-DC
Summary: Samba netapi library
Group: System/Libraries
Conflicts: libnetapi

%description -n libnetapi-DC
Samba netapi library

%package -n libnetapi-DC-devel
Summary: Samba netapi development files
Group: Development/Other
Requires: libnetapi-DC = %version-%release
Conflicts: libnetapi-devel

%description -n libnetapi-DC-devel
Samba netapi development files

%package -n python-module-%name
Summary: Samba Python libraries
Group: Networking/Other
Requires: %name-common-libs = %version-%release
Conflicts: python-module-%rname

%add_python_req_skip Tdb

%description -n python-module-%name
The %rname-python package contains the Python libraries needed by programs
that use SMB, RPC and other Samba provided protocols in Python programs.

%package devel
Summary: Developer tools for Samba libraries
Group: Development/C
Requires: %name-libs = %version-%release
Conflicts: %rname-devel

%description devel
The %rname-devel package contains the header files for the libraries
needed to develop programs that link against the SMB, RPC and other
libraries in the Samba suite.

%package pidl
Summary: Perl IDL compiler
Group: Development/Tools
BuildArch: noarch
# Requires: perl(:MODULE_COMPAT_%(eval "`perl -V:version`"; echo $version))
Conflicts: %rname-pidl

%description pidl
The %rname-pidl package contains the Perl IDL compiler used by Samba
and Wireshark to parse IDL and similar protocols

%package test
Summary: Testing tools for Samba servers and clients
Group: Development/Tools
Requires: %name = %version-%release
Requires: %name-common = %version-%release
Requires: %name-libs = %version-%release
%if_with winbind
Requires: %name-winbind = %version-%release
%endif
%if_with libsmbclient
Requires: libsmbclient-DC = %version-%release
%endif
Conflicts: %rname-test

%description test
samba4-test provides testing tools for both the server and client
packages of Samba.

%if_with winbind
%package winbind
Summary: Samba winbind
Group: System/Servers
Requires: %name-common = %version-%release
Requires: %name-libs = %version-%release
Conflicts: %rname-winbind
%if_with libwbclient
# There are working configurations exists where samba-winbind could be
# using with sssd. Also it could be already installed from installation DVD.
## Conflicts: libwbclient-sssd
Requires: libwbclient-DC
%endif

%description winbind
The %rname-winbind package provides the winbind NSS library, and some
client tools.  Winbind enables Linux to be a full member in Windows
domains and to use Windows user and group accounts on Linux.

%package winbind-clients
Summary: Samba winbind clients
Group: System/Servers
Requires: %name-winbind = %version-%release
%if_with libwbclient
Requires: libwbclient-DC = %version-%release
%endif

%description winbind-clients
The samba-winbind-clients package provides the NSS library and a PAM
module necessary to communicate to the Winbind Daemon

%package winbind-krb5-locator
Summary: Samba winbind krb5 locator
Group: System/Servers
%if_with libwbclient
Requires: libwbclient-DC = %version-%release
Requires: %name-winbind = %version-%release
%else
Requires: %name-libs = %version-%release
%endif
Conflicts: %rname-winbind-krb5-locator

%description winbind-krb5-locator
The winbind krb5 locator is a plugin for the system kerberos library to allow
the local kerberos library to use the same KDC as samba and winbind use

%package winbind-devel
Summary: Developer tools for the winbind library
Group: Development/C
Requires: %name-winbind = %version-%release
Conflicts: %rname-winbind-devel

%description winbind-devel
The samba-winbind package provides developer tools for the wbclient library.
%endif

%if_with clustering_support
%package ctdb
Summary: A Clustered Database based on Samba's Trivial Database (TDB)
Group: System/Servers

Requires: %name-libs = %version-%release

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
Conflicts: ctdb

%description ctdb
CTDB is a cluster implementation of the TDB database used by Samba and other
projects to store temporary data. If an application is already using TDB for
temporary data it is very easy to convert that application to be cluster aware
and use CTDB instead.

%package ctdb-tests
Summary: CTDB clustered database test suite
Group: Development/Other
Requires: %name-libs = %version-%release
Requires: %name-ctdb = %version-%release
Requires: nc
Conflicts: ctdb-tests
Conflicts: ctdb-devel
Provides:  %name-ctdb-devel = %version-%release
Obsoletes: %name-ctdb-devel < %version-%release

%description ctdb-tests
Test suite for CTDB.
CTDB is a cluster implementation of the TDB database used by Samba and other
projects to store temporary data. If an application is already using TDB for
temporary data it is very easy to convert that application to be cluster aware
and use CTDB instead.
%endif

%if_with doc
%package doc
Summary: Documentation for the Samba suite
Group: Documentation
Requires: %name-common = %version-%release
BuildArch: noarch
Conflicts: %rname-doc

%description doc
The samba-doc package includes all the non-manpage documentation for the
Samba suite.
%endif

%package -n task-samba-dc
Summary: Samba Active Directory Domain Controller
Group: System/Servers
BuildArch: noarch
Provides: task-samba-ad-dc = %version-%release
Provides: task-ad-dc = %version-%release
Requires: samba-DC python-module-samba-DC samba-DC-common samba-DC-winbind-clients samba-DC-winbind samba-DC-client samba-DC-doc krb5-kinit
Conflicts: samba python-module-samba samba-common samba-winbind-clients samba-winbind samba-client samba-doc

%description -n task-samba-dc
Samba server acts as a Domain Controller that is compatible with
Microsoft Active Directory.

%package util-private-headers
Summary: libsamba_util private headers
Group: Development/C

%description util-private-headers
libsamba_util private headers.

%prep
%setup -q -n %rname-%version
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

%define _samba4_libraries heimdal,!zlib,!popt%{_talloc_lib}%{_tevent_lib}%{_tdb_lib}%{_ntdb_lib}%{_ldb_lib}

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
%if_with mitkrb5
%add_optflags -I/usr/include/krb5
%endif
#LDFLAGS="-Wl,-z,relro,-z,now" \
%if_with dc
%define _samba_libdir  %_libdir/samba-dc
%define _samba_mod_libdir  %_libdir/samba-dc
%else
%define _samba_libdir  %_libdir
%define _samba_mod_libdir  %_libdir/samba
%endif

%configure \
	--enable-fhs \
	--with-piddir=/var/run \
	--with-sockets-dir=/var/run/samba \
	--libdir=%_samba_libdir \
	--with-modulesdir=%_samba_mod_libdir \
	--with-privatelibdir=%_samba_mod_libdir \
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
%if_with winbind
	--with-winbind \
%else
	--without-winbind \
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
%if_with ntvfs
	--with-ntvfs-fileserver \
%endif
	%{subst_enable avahi}

[ -n "$NPROCS" ] || NPROCS=%__nprocs; export JOBS=$NPROCS
%make_build NPROCS=%__nprocs

%if_with doc
pushd docs-xml
export XML_CATALOG_FILES="file:///etc/xml/catalog file://$(pwd)/build/catalog.xml"
%autoreconf
%configure
%make_build smbdotconf/parameters.all.xml
%make_build release
popd
%endif

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
mkdir -p %buildroot%_samba_mod_libdir
mkdir -p %buildroot%_pkgconfigdir
mkdir -p %buildroot%_initdir
mkdir -p %buildroot%_unitdir
mkdir -p %buildroot%_sysconfdir/{pam.d,logrotate.d,security,sysconfig}

if [ ! -f %buildroot%_samba_libdir/libwbclient.so.%libwbc_alternatives_version ]
then
    echo "Expected libwbclient version not found, please check if version has changed."
    exit -1
fi
ln -s ../..%_samba_libdir/libwbclient.so.%libwbc_alternatives_version %buildroot%_libdir/
ln -s ../..%_samba_libdir/libwbclient.so.0 %buildroot%_libdir/
ln -s ../..%_samba_libdir/libwbclient.so %buildroot%_libdir/

# Add alternatives for libwbclient
mkdir -p %buildroot%_altdir
printf '%_libdir/libwbclient.so.%libwbc_alternatives_version\t%_samba_libdir/libwbclient.so.%libwbc_alternatives_version\t10\n' > %buildroot%_altdir/libwbclient-samba-dc
printf '%_libdir/libwbclient.so.0\t%_samba_libdir/libwbclient.so.0\t10\n' >> %buildroot%_altdir/libwbclient-samba-dc

printf '%_libdir/libwbclient.so\t%_samba_libdir/libwbclient.so\t10\n' > %buildroot%_altdir/libwbclient-devel-samba-dc
mkdir -p %buildroot/lib/tmpfiles.d

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
%if_with dc
install -m755 %SOURCE20 %buildroot%_initrddir/samba
%endif

# Put README in builddir
cp %SOURCE200 %SOURCE201 .

for i in nmb smb winbind samba; do
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

install -m644 packaging/systemd/samba.conf.tmp %buildroot%_tmpfilesdir/%rname.conf

# NetworkManager online/offline script
install -d -m 0755 %buildroot%_sysconfdir/NetworkManager/dispatcher.d/
install -m 0755 packaging/NetworkManager/30-winbind-systemd \
            %buildroot%_sysconfdir/NetworkManager/dispatcher.d/30-winbind


# Clean out crap left behind by the PIDL install.
find %buildroot -type f -name .packlist -exec rm -f {} \;
rm -f %buildroot%perl_vendorlib/wscript_build
rm -rf %buildroot%perl_vendorlib/Parse/Yapp

# winbind
%if_with winbind
mkdir -p %buildroot/%_lib
ln -sf ..%_samba_libdir/libnss_winbind.so %buildroot/%_lib/libnss_winbind.so.2
ln -sf ..%_samba_libdir/libnss_wins.so    %buildroot/%_lib/libnss_wins.so.2

mkdir -p  %buildroot%_libdir/krb5/plugins/libkrb5
mv %buildroot%_samba_libdir/winbind_krb5_locator.so %buildroot%_libdir/krb5/plugins/libkrb5/
%endif

#cups backend
%define cups_serverbin %(cups-config --serverbin 2>/dev/null)
mkdir -p %buildroot%{cups_serverbin}/backend
ln -s %_bindir/smbspool %buildroot%{cups_serverbin}/backend/smb

# Fix up permission on perl install.
%_fixperms %buildroot%perl_vendor_privlib

# remove tests form python modules
rm -rf %buildroot%python_sitelibdir/samba/{tests,external/subunit,external/testtool}

# move pkgconfig to standart path:
[ "%_libdir" != "%_samba_libdir" ] && mv %buildroot{%_samba_libdir/pkgconfig,%_libdir}

# Install documentation
%if_with doc
mkdir -p %buildroot%_defaultdocdir/%rname/
cp -a docs-xml/output/htmldocs %buildroot%_defaultdocdir/%rname/
%endif

# Cleanup man pages
%if_without libsmbclient
/bin/rm -f %buildroot%_man7dir/libsmbclient.7*
%endif

# Install pidl/lib/Parse/Pidl/Samba3/Template.pm
cp -a pidl/lib/Parse/Pidl/Samba3/Template.pm %buildroot%_datadir/perl5/Parse/Pidl/Samba3/

# Copy libsamba_util private headers
mkdir -p %buildroot%_includedir/samba-4.0/private/lib/util/charset
cp lib/util/*.h %buildroot%_includedir/samba-4.0/private/lib/util
cp lib/util/charset/*.h %buildroot%_includedir/samba-4.0/private/lib/util/charset
mkdir -p %buildroot%_includedir/samba-4.0/private/libcli/util
cp libcli/util/*.h %buildroot%_includedir/samba-4.0/private/libcli/util
subst 's,\.\./,,' %buildroot%_includedir/samba-4.0/private/lib/util/*.h

# Install limits
mkdir -p %buildroot%_sysconfdir/security/limits.d/
install -m644 %SOURCE13 %buildroot%_sysconfdir/security/limits.d/90-samba.conf

%find_lang pam_winbind
%find_lang net

%if_with testsuite
%check
TDB_NO_FSYNC=1 %make_build test
%endif

%post
%if_with dc
%post_service samba
%else
%post_service smb
%post_service nmb
%endif

%preun
%if_with dc
%preun_service samba
%else
%preun_service smb
%preun_service nmb
%endif

%if_with winbind
%pre winbind
%_sbindir/groupadd -f -r wbpriv >/dev/null 2>&1 || :

%post winbind
%post_service winbind

%preun winbind
%preun_service winbind
%endif

%files
%doc COPYING README WHATSNEW.txt
%doc examples/autofs examples/LDAP examples/misc
%doc examples/printer-accounting examples/printing
%doc README.downgrade
%_bindir/smbstatus
%_bindir/eventlogadm
%_sbindir/nmbd
%_sbindir/smbd
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
%endif

%if_with dc
%attr(755,root,root) %_initdir/samba
%_unitdir/samba.service
%_bindir/samba-tool
%_sbindir/samba
%_sbindir/samba_kcc
%_sbindir/samba_dnsupdate
%_sbindir/samba_spnupdate
%_sbindir/samba_upgradedns
%dir /var/lib/samba/sysvol
%_datadir/samba/setup
%if_with doc
%_man8dir/samba.8*
%_man8dir/samba-tool.8*
%endif #doc
%else
%doc README.dc
%if_with doc
%exclude %_man8dir/samba.8*
%exclude %_man8dir/samba-tool.8*
%endif #doc
%endif
%if_with libcephfs
%exclude %_samba_mod_libdir/vfs/ceph.so
%if_with doc
%exclude %_man8dir/vfs_ceph.8*
%endif #doc
%endif
%if_enabled glusterfs
%exclude %_samba_mod_libdir/vfs/glusterfs.so
%if_with doc
%exclude %_man8dir/vfs_glusterfs.8*
%endif #doc
%endif

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
%_bindir/smbpasswd
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
%_man8dir/smbpasswd.8*
%_man8dir/smbspool.8*
%_man8dir/smbspool_krb5_wrapper.8*
#_man8dir/smbta-util.8*
%_man8dir/cifsdd.8*
%endif

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
%endif
%_samba_mod_libdir/libldb-cmdline.so
%endif

%files common -f net.lang
%_tmpfilesdir/%rname.conf
%_bindir/mvxattr
%_bindir/net
%_bindir/pdbedit
%_bindir/profiles
%_bindir/smbcontrol
%_bindir/testparm
%config(noreplace) %_sysconfdir/logrotate.d/samba
%config(noreplace) %_sysconfdir/security/limits.d/90-samba.conf
%attr(0700,root,root) %dir /var/log/samba
%attr(0700,root,root) %dir /var/log/samba/old
%dir /var/run/samba
%dir /var/run/winbindd
%attr(755,root,root) %dir %_localstatedir/cache/samba
%attr(700,root,root) %dir /var/lib/samba/private
%attr(755,root,root) %dir %_sysconfdir/samba
%config(noreplace) %_sysconfdir/samba/smb.conf
%config(noreplace) %_sysconfdir/samba/lmhosts
%config(noreplace) %_sysconfdir/sysconfig/samba
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
%endif

# common libraries
%_samba_mod_libdir/libpopt-samba3-samba4.so
%_samba_mod_libdir/pdb

%files devel
%_includedir/samba-4.0

%exclude %_includedir/samba-4.0/netapi.h
%exclude %_includedir/samba-4.0/private
#%exclude %_includedir/samba-4.0/torture.h
%if_with libsmbclient
%exclude %_includedir/samba-4.0/libsmbclient.h
%endif
%if_with libwbclient
%exclude %_includedir/samba-4.0/wbclient.h
%endif

%_samba_libdir/libdcerpc-binding.so
%_samba_libdir/libdcerpc-samr.so
%_samba_libdir/libdcerpc.so
%_samba_libdir/libndr-krb5pac.so
%_samba_libdir/libndr-nbt.so
%_samba_libdir/libndr-standard.so
%_samba_libdir/libndr.so
%_samba_libdir/libsamba-credentials.so
%_samba_libdir/libsamba-errors.so
%_samba_libdir/libsamba-hostconfig.so
%_samba_libdir/libsamba-policy.so
%_samba_libdir/libsamba-util.so
%_samba_libdir/libsamdb.so
%_samba_libdir/libsmbconf.so
%_samba_libdir/libtevent-util.so
%_samba_libdir/libsamba-passdb.so
%_samba_libdir/libsmbldap.so

%_pkgconfigdir/dcerpc.pc
%_pkgconfigdir/dcerpc_samr.pc
%_pkgconfigdir/ndr.pc
%_pkgconfigdir/ndr_krb5pac.pc
%_pkgconfigdir/ndr_nbt.pc
%_pkgconfigdir/ndr_standard.pc
%_pkgconfigdir/samba-credentials.pc
%_pkgconfigdir/samba-hostconfig.pc
%_pkgconfigdir/samba-policy.pc
%_pkgconfigdir/samba-util.pc
%_pkgconfigdir/samdb.pc

%if_with dc
%_samba_libdir/libdcerpc-server.so
%_pkgconfigdir/dcerpc_server.pc
%endif

%files libs

%files common-libs
%_samba_libdir/libdcerpc-binding.so.*
%_samba_libdir/libdcerpc-samr.so.*
%_samba_libdir/libdcerpc.so.*
%_samba_libdir/libndr-krb5pac.so.*
%_samba_libdir/libndr-nbt.so.*
%_samba_libdir/libndr-standard.so.*
%_samba_libdir/libndr.so.*
%_samba_libdir/libsamba-credentials.so.*
%_samba_libdir/libsamba-errors.so.*
%_samba_libdir/libsamba-hostconfig.so.*
%_samba_libdir/libsamba-policy.so.*
%_samba_libdir/libsamba-util.so.*
%_samba_libdir/libsamdb.so.*
%_samba_libdir/libsmbconf.so.*
%_samba_libdir/libtevent-util.so.*
%_samba_libdir/libsamba-passdb.so.*
%_samba_libdir/libsmbldap.so.*
%_samba_mod_libdir/auth
%_samba_mod_libdir/vfs

# libraries needed by the public libraries
%_samba_mod_libdir/libCHARSET3-samba4.so
%_samba_mod_libdir/libMESSAGING-samba4.so
%_samba_mod_libdir/libLIBWBCLIENT-OLD-samba4.so
%_samba_mod_libdir/libaddns-samba4.so
%_samba_mod_libdir/libads-samba4.so
%_samba_mod_libdir/libasn1util-samba4.so
%_samba_mod_libdir/libauth-samba4.so
%_samba_mod_libdir/libauth4-samba4.so
%_samba_mod_libdir/libauth-sam-reply-samba4.so
%_samba_mod_libdir/libauth-unix-token-samba4.so
%_samba_mod_libdir/libauthkrb5-samba4.so
%_samba_mod_libdir/libcli-ldap-common-samba4.so
%_samba_mod_libdir/libcli-ldap-samba4.so
%_samba_mod_libdir/libcli-nbt-samba4.so
%_samba_mod_libdir/libcli-cldap-samba4.so
%_samba_mod_libdir/libcli-smb-common-samba4.so
%_samba_mod_libdir/libcli-spoolss-samba4.so
%_samba_mod_libdir/libcliauth-samba4.so
%_samba_mod_libdir/libcluster-samba4.so
%_samba_mod_libdir/libcmdline-credentials-samba4.so
%_samba_mod_libdir/libdbwrap-samba4.so
%_samba_mod_libdir/libdcerpc-samba-samba4.so
%_samba_mod_libdir/libdcerpc-samba4.so
%_samba_mod_libdir/libevents-samba4.so
%_samba_mod_libdir/libflag-mapping-samba4.so
%_samba_mod_libdir/libgenrand-samba4.so
%_samba_mod_libdir/libgensec-samba4.so
%_samba_mod_libdir/libgpo-samba4.so
%_samba_mod_libdir/libgse-samba4.so
%_samba_mod_libdir/libhttp-samba4.so
%_samba_mod_libdir/libinterfaces-samba4.so
%_samba_mod_libdir/libiov-buf-samba4.so
%_samba_mod_libdir/libkrb5samba-samba4.so
%_samba_mod_libdir/libldbsamba-samba4.so
%_samba_mod_libdir/liblibcli-lsa3-samba4.so
%_samba_mod_libdir/liblibcli-netlogon3-samba4.so
%_samba_mod_libdir/liblibsmb-samba4.so
%_samba_mod_libdir/libmessages-dgm-samba4.so
%_samba_mod_libdir/libmessages-util-samba4.so
%_samba_mod_libdir/libmsghdr-samba4.so
%_samba_mod_libdir/libsmb-transport-samba4.so
%_samba_mod_libdir/libmsrpc3-samba4.so
%_samba_mod_libdir/libndr-samba-samba4.so
%_samba_mod_libdir/libndr-samba4.so
%_samba_mod_libdir/libnet-keytab-samba4.so
%_samba_mod_libdir/libnetif-samba4.so
%_samba_mod_libdir/libnon-posix-acls-samba4.so
%_samba_mod_libdir/libnpa-tstream-samba4.so
%_samba_mod_libdir/libprinting-migrate-samba4.so
%_samba_mod_libdir/libregistry-samba4.so
%_samba_mod_libdir/libsamba-cluster-support-samba4.so
%_samba_mod_libdir/libsamba-debug-samba4.so
%_samba_mod_libdir/libsamba-modules-samba4.so
%_samba_mod_libdir/libsamba-net-samba4.so
%_samba_mod_libdir/libsamba-security-samba4.so
%_samba_mod_libdir/libsamba-sockets-samba4.so
%_samba_mod_libdir/libsamba-python-samba4.so
%_samba_mod_libdir/libsamdb-common-samba4.so
%_samba_mod_libdir/libsecrets3-samba4.so
%_samba_mod_libdir/libserver-id-db-samba4.so
%_samba_mod_libdir/libserver-role-samba4.so
%_samba_mod_libdir/libshares-samba4.so
%_samba_mod_libdir/libsamba3-util-samba4.so
%_samba_mod_libdir/libsmbclient-raw-samba4.so
%_samba_mod_libdir/libsmbd-base-samba4.so
%_samba_mod_libdir/libsmbd-conn-samba4.so
%_samba_mod_libdir/libsmbd-shim-samba4.so
%_samba_mod_libdir/libsmbldaphelper-samba4.so
%_samba_mod_libdir/libsmbpasswdparser-samba4.so
%_samba_mod_libdir/libsys-rw-samba4.so
%_samba_mod_libdir/libsocket-blocking-samba4.so
%_samba_mod_libdir/libtalloc-report-samba4.so
%_samba_mod_libdir/libtdb-wrap-samba4.so
%_samba_mod_libdir/libtime-basic-samba4.so
%_samba_mod_libdir/libtorture-samba4.so
%_samba_mod_libdir/libtrusts-util-samba4.so
%_samba_mod_libdir/libutil-cmdline-samba4.so
%_samba_mod_libdir/libutil-reg-samba4.so
%_samba_mod_libdir/libutil-setid-samba4.so
%_samba_mod_libdir/libutil-tdb-samba4.so
%_samba_mod_libdir/libxattr-tdb-samba4.so

%if_with dc
%_samba_mod_libdir/bind9/dlz_bind9.so
%_samba_mod_libdir/bind9/dlz_bind9_9.so
%_samba_mod_libdir/bind9/dlz_bind9_10.so
%_samba_mod_libdir/bind9/dlz_bind9_11.so
%_samba_mod_libdir/libheimntlm-samba4.so.1
%_samba_mod_libdir/libheimntlm-samba4.so.1.0.1
%_samba_mod_libdir/libkdc-samba4.so.2
%_samba_mod_libdir/libkdc-samba4.so.2.0.0
%_samba_mod_libdir/libpac-samba4.so
%_samba_mod_libdir/libdnsserver-common-samba4.so
%_samba_mod_libdir/libdfs-server-ad-samba4.so
%_samba_mod_libdir/libdsdb-module-samba4.so
%_samba_mod_libdir/libdsdb-garbage-collect-tombstones-samba4.so
%if_without ldb_modules
%_samba_mod_libdir/ldb
%endif
%_samba_mod_libdir/gensec
%_samba_mod_libdir/libdb-glue-samba4.so
%_samba_mod_libdir/libHDB-SAMBA4-samba4.so
%_samba_mod_libdir/libasn1-samba4.so.*
%_samba_mod_libdir/libcom_err-samba4.so.*
%_samba_mod_libdir/libgssapi-samba4.so.*
%_samba_mod_libdir/libhcrypto-samba4.so.*
%_samba_mod_libdir/libhdb-samba4.so.*
%_samba_mod_libdir/libheimbase-samba4.so.*
%_samba_mod_libdir/libhx509-samba4.so.*
%_samba_mod_libdir/libkrb5-samba4.so.*
%_samba_mod_libdir/libroken-samba4.so.*
%_samba_mod_libdir/libwind-samba4.so.*
%_samba_mod_libdir/libprocess-model-samba4.so
%_samba_mod_libdir/libservice-samba4.so
%_samba_mod_libdir/process_model
%_samba_mod_libdir/service
%_samba_libdir/libdcerpc-server.so.*
%if_with ntvfs
%_samba_mod_libdir/libntvfs-samba4.so
%endif
%_samba_mod_libdir/libposix-eadb-samba4.so
%else
%doc README.dc-libs
%_samba_mod_libdir/libdnsserver-common-samba4.so
%endif

%if_with ldb
%_samba_mod_libdir/libldb.so.*
%_samba_mod_libdir/libpyldb-util.so.*
%endif
%if_with talloc
%_samba_mod_libdir/libtalloc.so.*
%_samba_mod_libdir/libpytalloc-util.so.*
%endif
%if_with tevent
%_samba_mod_libdir/libtevent.so.*
%endif
%if_with tdb
%_samba_mod_libdir/libtdb.so.*
%endif
%if_with ntdb
%_samba_mod_libdir/libntdb.so.*
%endif
%if_without libsmbclient
%_samba_mod_libdir/libsmbclient.so.*
%endif
%if_without libwbclient
%_samba_mod_libdir/libreplace-samba4.so
%_samba_mod_libdir/libwbclient.so.*
%_samba_mod_libdir/libwinbind-client-samba4.so
%endif
%if_without libnetapi
%_samba_mod_libdir/libnetapi.so.*
%endif

%if_with ldb_modules
%files -n libldb-modules-DC
%_samba_mod_libdir/ldb
%endif

%if_with libsmbclient
%files -n libsmbclient-DC
%_samba_libdir/libsmbclient.so.*

%files -n libsmbclient-DC-devel
%_includedir/samba-4.0/libsmbclient.h
%_samba_libdir/libsmbclient.so
%_pkgconfigdir/smbclient.pc
%if_with doc
%_man7dir/libsmbclient.7*
%endif #doc
%endif

%if_with libwbclient
%files -n libwbclient-DC
%ghost %_libdir/libwbclient.so.*
%_samba_libdir/libwbclient.so.*
%_samba_mod_libdir/libwinbind-client-samba4.so
%_samba_mod_libdir/libreplace-samba4.so
%_altdir/libwbclient-samba-dc

%files -n libwbclient-DC-devel
%_includedir/samba-4.0/wbclient.h
%ghost %_libdir/libwbclient.so
%_samba_libdir/libwbclient.so
%_pkgconfigdir/wbclient.pc
%_altdir/libwbclient-devel-samba-dc
%endif

%if_with libnetapi
%files -n libnetapi-DC
%_samba_libdir/libnetapi.so.*

%files -n libnetapi-DC-devel
%_samba_libdir/libnetapi.so
%_includedir/samba-4.0/netapi.h
%_pkgconfigdir/netapi.pc
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
%files doc
%doc %_defaultdocdir/%rname/htmldocs
%endif

%files test
%_bindir/gentest
%_bindir/locktest
%_bindir/masktest
%_bindir/ndrdump
%_bindir/smbtorture
#%_samba_libdir/libtorture.so.*
%if_with dc
%_samba_mod_libdir/libdlz-bind9-for-torture-samba4.so
%else
%_samba_mod_libdir/libdsdb-module-samba4.so
%endif
%if_with doc
%_man1dir/gentest.1*
%_man1dir/locktest.1*
%_man1dir/masktest.1*
%_man1dir/ndrdump.1*
%_man1dir/smbtorture.1*
%_man1dir/vfstest.1*
%endif

%if_with testsuite
# files to ignore in testsuite mode
%_samba_mod_libdir/libnss-wrapper-samba4.so
%_samba_mod_libdir/libsocket-wrapper-samba4.so
%_samba_mod_libdir/libuid-wrapper-samba4.so
%endif

%if_with winbind
%files winbind -f pam_winbind.lang
%_samba_mod_libdir/idmap
%_samba_mod_libdir/nss_info
%_samba_mod_libdir/libnss-info-samba4.so
%_samba_mod_libdir/libidmap-samba4.so
%_sbindir/winbindd
%attr(750,root,wbpriv) %dir /var/lib/samba/winbindd_privileged
%_unitdir/winbind.service
%attr(755,root,root) %_initrddir/winbind
%_sysconfdir/NetworkManager/dispatcher.d/30-winbind
%if_with doc
%_man8dir/winbindd.8*
%_man8dir/idmap_*.8*
%endif

%files winbind-clients
%_bindir/ntlm_auth
%_bindir/wbinfo
%_samba_libdir/libnss_winbind.so*
/%_lib/libnss_winbind.so.*
%_samba_libdir/libnss_wins.so*
/%_lib/libnss_wins.so.*
/%_lib/security/pam_winbind.so
%config(noreplace) %_sysconfdir/security/pam_winbind.conf
%if_with doc
%_man1dir/ntlm_auth.1.*
%_man1dir/wbinfo.1*
%_man5dir/pam_winbind.conf.5*
%_man8dir/pam_winbind.8*
%endif

%files winbind-krb5-locator
%_libdir/krb5/plugins/libkrb5/winbind_krb5_locator.so
%if_with doc
%_man7dir/winbind_krb5_locator.7*
%endif #doc
%endif

%if_with clustering_support
%files ctdb
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
%endif

%files ctdb-tests
%_libexecdir/ctdb/tests
%_bindir/ctdb_run_tests
%_bindir/ctdb_run_cluster_tests
%_datadir/ctdb/tests
%endif

%files -n task-samba-dc

%files util-private-headers
%_includedir/samba-4.0/private

%changelog
* Tue Jan 23 2018 Evgeny Sinelnikov <sin@altlinux.org> 4.6.12-alt2%ubt
- Fix trouble with joined machine account moving when it already exists.
  Move it only if the admin specified an explicit OU (Samba bug #12696)

* Thu Dec 21 2017 Evgeny Sinelnikov <sin@altlinux.org> 4.6.12-alt1%ubt
- Update to first winter release with common bugfixes (closes: 33210)

* Thu Nov 23 2017 Evgeny Sinelnikov <sin@altlinux.org> 4.6.11-alt2%ubt
- Backport from Heimdal upstream include/includedir directives for krb5.conf

* Tue Nov 21 2017 Evgeny Sinelnikov <sin@altlinux.org> 4.6.11-alt1%ubt
- Second autumn security release (Fixes: CVE-2017-14746, CVE-2017-15275)

* Thu Nov 16 2017 Evgeny Sinelnikov <sin@altlinux.org> 4.6.10-alt1%ubt
- Update for third autumn release with common bugfixes

* Wed Oct 25 2017 Evgeny Sinelnikov <sin@altlinux.org> 4.6.9-alt1%ubt
- Update for second autumn release with common bugfixes

* Thu Oct 12 2017 Evgeny Sinelnikov <sin@altlinux.org> 4.6.8-alt3%ubt
- Fix KDC not works in configuration with trusted domain (samba bug #13078)

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

* Wed Aug 09 2017 Evgeny Sinelnikov <sin@altlinux.ru> 4.6.7-alt1%ubt
- Update to second summer release

* Sat Jul 15 2017 Evgeny Sinelnikov <sin@altlinux.ru> 4.6.6-alt2%ubt
- Rebuild with universal build tag (aka ubt macros) for p7 and c7

* Wed Jul 12 2017 Evgeny Sinelnikov <sin@altlinux.ru> 4.6.6-alt1%ubt
- Update to summer security release
- Security fixes:
  + CVE-2017-11103 Orpheus' Lyre KDC-REP service name validation

* Tue Jun 20 2017 Evgeny Sinelnikov <sin@altlinux.ru> 4.6.5-alt2%ubt
- Remove conflict samba-DC-libs with samba-libs
- Adjust python module requirement to samba-DC-common-libs
- Add conflict python-module-samba-DC with python-module-samba

* Tue Jun 06 2017 Evgeny Sinelnikov <sin@altlinux.ru> 4.6.5-alt1%ubt
- Udpate to first summer release

* Mon Jun 05 2017 Evgeny Sinelnikov <sin@altlinux.ru> 4.6.4-alt2%ubt
- Add libldb-modules-DC package with domain controller ldb modules for ldb-tools
- Add samba-DC-common-libs with libraries for common modules
- Append list of libraries consists in libwbclient-DC to not require
  samba-DC-common-libs

* Wed May 24 2017 Evgeny Sinelnikov <sin@altlinux.ru> 4.6.4-alt1%ubt
- Update to second spring security release
- Fix longtime initialization bug in ldb proxy
- Security fixes:
  + CVE-2017-7494 Remote code execution from a writable share

* Tue Apr 25 2017 Evgeny Sinelnikov <sin@altlinux.ru> 4.6.3-alt1%ubt
- Udpate to second spring release
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
- Revert removed unused DCERPC_FAULT_UNK_IF for openchange

* Wed Feb 01 2017 Evgeny Sinelnikov <sin@altlinux.ru> 4.5.5-alt1%ubt
- Update to winter release
- Fix PAM winbind problem with access user to keytab

* Wed Dec 28 2016 Evgeny Sinelnikov <sin@altlinux.ru> 4.5.3-alt2%ubt
- Do not delete an existing valid credential cache for KEYRING type
- Set FQDN to lower at fill_mem_keytab_from_system_keytab()

* Mon Dec 19 2016 Evgeny Sinelnikov <sin@altlinux.ru> 4.5.3-alt1%ubt
- Update for release with security fixes:
  - CVE-2016-2123 (ndr_pull_dnsp_name contains an integer wrap problem)
  - CVE-2016-2125 (client code always requests a forwardable ticket)
  - CVE-2016-2126 (crash winbindd using a legitimate Kerberos ticket)

* Mon Dec 19 2016 Evgeny Sinelnikov <sin@altlinux.ru> 4.5.2-alt1%ubt
- Udpate to first winter release

* Sat Dec 03 2016 Evgeny Sinelnikov <sin@altlinux.ru> 4.5.1-alt2
- Add conflict winbind with libwbclient-sssd due compatibility
- Update build dependencies versions for external samba libraries
- Build with separate libwbclient-DC

* Fri Oct 28 2016 Evgeny Sinelnikov <sin@altlinux.ru> 4.5.1-alt1
- Update with variety of fixes for autumn release

* Thu Sep 08 2016 Evgeny Sinelnikov <sin@altlinux.ru> 4.5.0-alt1
- Update to new autumn release

* Fri Jul 08 2016 Evgeny Sinelnikov <sin@altlinux.ru> 4.4.5-alt1
- Update for security release with CVE-2016-2119

* Thu Jun 30 2016 Evgeny Sinelnikov <sin@altlinux.ru> 4.4.4-alt3
- Apply fixes for DRSUAPI limits of too strict for some workloads,
  e.g. DRSUAPI replication with large objects.
   https://bugzilla.samba.org/show_bug.cgi?id=11948
 + Set DCERPC_NCACN_{REQUEST,RESPONSE}_DEFAULT_MAX_SIZE
 + Allow a total reassembled response payload of 240 MBytes

* Wed Jun 29 2016 Andrey Cherepanov <cas@altlinux.org> 4.4.4-alt2
- Package libsamba_util private headers to package
  samba-DC-util-private-headers

* Fri Jun 10 2016 Evgeny Sinelnikov <sin@altlinux.ru> 4.4.4-alt1
- Update to new version

* Tue May 24 2016 Alexey Shabalin <shaba@altlinux.ru> 4.4.3-alt3
- build with libsystemd without compat libs
- add patches from fedora
- add again samba-grouppwd.patch

* Mon May 23 2016 Evgeny Sinelnikov <sin@altlinux.ru> 4.4.3-alt2
- Fix rpc_server/drsuapi: Set msDS_IntId as attid for linked attributes if exists

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
- Remove samba-DC-test-build and samba-DC-ctdb-devel

* Sun Mar 13 2016 Andrey Cherepanov <cas@altlinux.org> 4.3.6-alt2
- Rebuild with new libtalloc

* Wed Mar 09 2016 Andrey Cherepanov <cas@altlinux.org> 4.3.6-alt1
- New version (https://www.samba.org/samba/history/samba-4.3.6.html)
- Security fixes:
  - CVE-2015-7560 (Incorrect ACL get/set allowed on symlink path)
  - CVE-2016-0771 (Out-of-bounds read in internal DNS server)
- Do not use specified GID for wbpriv group

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

* Tue Dec 08 2015 Igor Vlasenko <viy@altlinux.ru> 4.3.2-alt1.1
- NMU: dropped unused prehistoric BR: perl-Perl4-CoreLibs

* Tue Dec 01 2015 Andrey Cherepanov <cas@altlinux.org> 4.3.2-alt1
- New version (https://www.samba.org/samba/history/samba-4.3.2.html)
- Enable RPATH in installed files to correct link using .pc files

* Thu Nov 26 2015 Andrey Cherepanov <cas@altlinux.org> 4.3.1-alt3
- Remove libxfs-qa-devel from build requirements
- Package samba-DC-ctdb, samba-DC-ctdb-devel and samba-DC-ctdb-tests

* Mon Nov 16 2015 Andrey Cherepanov <cas@altlinux.org> 4.3.1-alt2
- Enable clustering support

* Tue Oct 20 2015 Andrey Cherepanov <cas@altlinux.org> 4.3.1-alt1
- New version (https://www.samba.org/samba/history/samba-4.3.1.html)
- New metapackage task-samba-dc to install complete Domain Controller

* Tue Sep 22 2015 Andrey Cherepanov <cas@altlinux.org> 4.3.0-alt2
- Exclude libnss_win* from debuginfo
- Make libnss_win* symlinks to /lib*
- Package unit samba.service for systemd
- Add conditional build of winbind part
- Move all libraries to samba-DC-libs
- Remove duplicated requirements

* Thu Sep 10 2015 Andrey Cherepanov <cas@altlinux.org> 4.3.0-alt1
- New version (https://www.samba.org/samba/history/samba-4.3.0.html)
- Requires /proc for doc generation

* Mon Aug 24 2015 Andrey Cherepanov <cas@altlinux.org> 4.2.3-alt2
- Build in dc mode in %_libdir/samba-dc to prevent link conflict
  with ordinary samba in repository
- Build without libsmbclient, libwbclient and libnetapi
- Move documentation to /usr/share/doc/samba

* Tue Jul 14 2015 Andrey Cherepanov <cas@altlinux.org> 4.2.3-alt1
- New version of Samba AD DC

* Mon Jun 01 2015 Andrey Cherepanov <cas@altlinux.org> 4.2.2-alt1
- New version of Samba AD DC

* Wed Apr 29 2015 Andrey Cherepanov <cas@altlinux.org> 4.2.1-alt1
- New version of Samba AD DC
- Fix post/postun hooks for samba init script

* Fri Apr 10 2015 Andrey Cherepanov <cas@altlinux.org> 4.2.0-alt1
- New version of Samba AD DC
- Enable documentation build

* Mon Feb 23 2015 Andrey Cherepanov <cas@altlinux.org> 4.1.17-alt1
- New version
- Security fixes:
  + fixes CVE-2015-0240 (security flaw in the smbd file server daemon)

* Thu Jan 15 2015 Andrey Cherepanov <cas@altlinux.org> 4.1.16-alt1
- New version
- Security fixes:
  + CVE-2014-8143: Samba's AD DC allows the administrator to delegate
    creation of user or computer accounts to specific users or groups.
    However, all released versions of Samba's AD DC did not implement the
    additional required check on the UF_SERVER_TRUST_ACCOUNT bit in the
    userAccountControl attributes.

* Wed Jan 14 2015 Andrey Cherepanov <cas@altlinux.org> 4.1.15-alt1
- New version

* Thu Dec 25 2014 Andrey Cherepanov <cas@altlinux.org> 4.1.14-alt0.M70P.1
- New version
- Disable build documentation because it cannot built

* Mon Oct 20 2014 Andrey Cherepanov <cas@altlinux.org> 4.1.13-alt0.M70P.1
- New version
- Do not use pidfile to stop service samba

* Tue Oct 14 2014 Andrey Cherepanov <cas@altlinux.org> 4.1.12-alt0.M70P.1
- New version

* Mon Oct 13 2014 Andrey Cherepanov <cas@altlinux.org> 4.1.11-alt1.M70P.1
- Build in DC mode
- Fix mitkrb5 support with and without DC mode
- Build on all available cores. Increase build and install verbosity
- Add setproctitle support
- Set verbosity level of make by VERBOSE option (-v, -vv or -vvv)
- Remove missing upgradeprovision programm
- Add initscript for samba
- Add dlz_bind9_9.so
- Rename to samba-DC conflicted by ordinary samba
- Add tdb-utils for samba_upgradedns program
- Use %%force_with to really set flag for tests

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

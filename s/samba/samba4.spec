%define _unpackaged_files_terminate_build 1
%set_verify_elf_method unresolved=relaxed
%add_findprov_skiplist /%_lib/*
%add_debuginfo_skiplist /%_lib

%define rname samba
%define dcname samba-DC
%define _localstatedir /var

# If one of those versions change, we need to make sure we rebuilt or adapt
# projects comsuming those. This is e.g. sssd, openchange, evolution-mapi, ...
%define libdcerpc_binding_so_version 0
%define libdcerpc_samr_so_version 0
%define libdcerpc_server_core_so_version 0
%define libdcerpc_so_version 0
%define libndr_krb5pac_so_version 0
%define libndr_nbt_so_version 0
%define libndr_so_version 4
%define libndr_standard_so_version 0
%define libnetapi_so_version 1
%define libsamba_credentials_so_version 1
%define libsamba_errors_so_version 1
%define libsamba_hostconfig_so_version 0
%define libsamba_passdb_so_version 0
%define libsamba_util_so_version 0
%define libsamdb_so_version 0
%define libsmbconf_so_version 0
%define libsmbldap_so_version 2
%define libtevent_util_so_version 0

%define libsmbclient_so_version 0
%define libwbclient_so_version 0

# internal libs
%def_without talloc
%def_without tevent
%def_without tdb
%def_without ldb
%def_with    winbind

%def_with profiling_data
%def_with snapper

# build as separate package
%def_with libsmbclient
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
%endif

%def_with mitkrb5
%def_with separate_heimdal_server
%def_with systemd
%def_enable avahi
%def_enable spotlight

%ifarch x86_64 aarch64 ppc64le
%def_with libcephfs
%def_enable cephfs
%else
%def_without libcephfs
%def_disable cephfs
%endif

%if_with clustering_support
%if_with libcephfs
%def_enable ceph_mutex
%else
%def_disable ceph_mutex
%endif
%ifarch %e2k
%def_disable pcp_pmda
%def_disable etcd_mutex
%else
%def_disable pcp_pmda
%def_enable etcd_mutex
%endif
%else
%def_disable ceph_mutex
%def_disable pcp_pmda
%def_disable etcd_mutex
%endif

%ifarch %e2k
%def_disable io_uring
%else
%def_enable io_uring
%endif

%ifarch %e2k armh
%def_disable glusterfs
%else
%def_enable glusterfs
%endif

%define _samba_libdir  %_libdir
%define _samba_libexecdir  %_libexecdir/samba
%define _samba_mod_libdir  %_libdir/samba
%define _samba_dc_libdir  %_libdir/samba-dc
%define _samba_dc_mod_libdir  %_libdir/samba-dc
%define _samba_dc_pythonarchdir  %_samba_dc_mod_libdir/python%_python3_version
%define _samba_piddir /run
%define _samba_sockets_dir /run/samba

%if_with separate_heimdal_server
%add_python3_compile_include %_samba_dc_mod_libdir/python%_python3_version
%add_python_compile_exclude %_samba_dc_mod_libdir/python%_python3_version
%endif

Name:    samba
Version: 4.20.5
Release: alt1

Group:   System/Servers
Summary: The Samba4 CIFS and AD client and server suite
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
Source21: smbusers
Source22: smb.conf.example
Source23: usershares.conf
Source24: smb-conf-usershares.control
Source25: role-usershares.control
Source26: samba-usershares.role
Source27: role-sambashare.control
Source28: smb-conf-usershare-allow-list.control
Source29: smb-conf-usershare-deny-list.control
Source30: smb-conf-usershare-owner-only.control
Source31: smb-conf-usershare-allow-guests.control

Source200: README.dc
Source201: README.downgrade

Patch: %rname-%version-alt.patch
Patch10: samba-grouppwd.patch

Provides: samba4 = %version-%release
Obsoletes: samba4 < %version-%release
Provides: samba-swat = %version-%release
Obsoletes: samba-swat < %version-%release

# Need for samba_upgradedns
Requires: tdb-utils

Requires(pre): %name-common = %version-%release
Requires: %name-libs = %version-%release
Requires: %name-dcerpc = %version-%release
%if_with libwbclient
Requires: libwbclient = %version-%release
%endif

BuildRequires: alternatives
BuildRequires: /proc
BuildRequires: libe2fs-devel
BuildRequires: libacl-devel
BuildRequires: libattr-devel
BuildRequires: libgnutls-devel
BuildRequires: libncurses-devel
BuildRequires: libpam-devel
BuildRequires: perl-devel
BuildRequires: perl-Parse-Yapp
BuildRequires: perl-JSON
BuildRequires: libpopt-devel
BuildRequires(pre): rpm-build-python3
BuildRequires(pre): rpm-macros-alternatives
BuildRequires: python3-devel
BuildRequires: libreadline-devel
BuildRequires: libldap-devel
BuildRequires: zlib-devel
BuildRequires: libarchive-devel >= 3.1.2
BuildRequires: libjansson-devel
BuildRequires: libgpgme-devel
%if_with io_uring
BuildRequires: liburing-devel >= 0.4
%endif
BuildRequires: /usr/bin/rpcgen
BuildRequires: libtirpc-devel
BuildRequires: libtasn1-devel
BuildRequires: libtasn1-utils

%if_enabled pcp_pmda
BuildRequires: libpcp-devel
%endif
%if_enabled ceph_mutex
BuildRequires: librados-devel
%endif
%if_enabled etcd_mutex
BuildRequires: python3-module-etcd
%endif

%if_with mitkrb5
BuildRequires: libssl-devel
BuildRequires: libkrb5-devel
%if_with dc
BuildRequires: krb5-kdc
%endif
%endif

%if_with dc
BuildRequires: flex
BuildRequires: liblmdb-devel >= 0.9.16
BuildRequires: python3-module-markdown
BuildRequires: python3-module-dns
%endif

%if_with separate_heimdal_server
BuildRequires: perl-JSON-PP
%endif

BuildRequires: glibc-devel glibc-kernheaders
# https://bugzilla.samba.org/show_bug.cgi?id=9863
BuildConflicts: setproctitle-devel
BuildRequires: libiniparser-devel
BuildRequires: libcups-devel
BuildRequires: gawk libcap-devel libuuid-devel
%{?_with_doc:BuildRequires: libxslt xsltproc netpbm dblatex html2text docbook-style-xsl}

%if_with snapper
BuildRequires: libdbus-devel
%endif

%if_without talloc
BuildRequires: libtalloc-devel >= 2.4.2
BuildRequires: python3-module-talloc-devel
%endif

%if_without tevent
BuildRequires: libtevent-devel >= 0.16.1
BuildRequires: python3-module-tevent
%endif

%if_without tdb
BuildRequires: libtdb-devel >= 1.4.10
BuildRequires: python3-module-tdb
%endif

%if_without ldb
%define ldb_version 2.9.1
BuildRequires: libldb-devel = %ldb_version
BuildRequires: python3-module-pyldb-devel
%endif
%{?_with_testsuite:BuildRequires: ldb-tools}
%{?_with_systemd:BuildRequires: libsystemd-devel}
%{?_enable_avahi:BuildRequires: libavahi-devel}
%{?_enable_glusterfs:BuildRequires: libglusterfs-api-devel}
%{?_with_libcephfs:BuildRequires: ceph-devel}

# Build spotlight without tracker backend if enabled.
#{?_enable_spotlight:BuildRequires: tracker-devel}

%description
Samba is the standard Windows interoperability suite of programs for Linux and Unix.

%package -n admx-samba
Summary: Samba ADMX policy templates
Group: System/Configuration/Other
BuildArch: noarch

BuildRequires: admx-lint

%description -n admx-samba
admx-samba provides ADMX policy templates for Samba project.

%package dc-common
Summary: Files used by MIT and Heimdal Active Directory Domain Services servers
Group: System/Servers
BuildArch: noarch
Requires: admx-samba = %version-%release
Requires: lmdb-utils

%description dc-common
%rname-dc-common provides files necessary for both MIT and Heimdal
Active Directory Domain Services servers separately builded and packaged.

%package dc
Summary: Samba Active Directory Domain Controller with Heimdal Kerberos
Group: Networking/Other
Obsoletes: %dcname < %version-%release
Provides: %dcname = %version-%release
Requires: %name-dc-client = %version-%release
Requires: %name-dc-common = %version-%release
%if_without separate_heimdal_server
Requires: %name = %version-%release
Requires: %name-winbind = %version-%release
%if_with mitkrb5
Requires: krb5-kdc
%endif
%else
Requires: tdb-utils
Requires: %name-winbind-common = %version-%release
Requires(pre): %name-common = %version-%release
%endif
Conflicts: %name-dc-mitkrb5

# Workaround for unneeded python2.7 requires
%add_python_req_skip bisect
%add_python_req_skip ctypes
%add_python_req_skip json
%add_python_req_skip logging
%add_python_req_skip ldb
%add_python_req_skip tdb
%add_python_req_skip xml

%description dc
Samba as Active Directory Domain Services (AD DS) also called a domain controller,
build with Heimdal Kerberos server and libraries.

%package dc-mitkrb5
Summary: Samba Active Directory Domain Controller with MIT Kerberos
Group: Networking/Other
Requires: %name = %version-%release
Requires: %name-dc-client = %version-%release
Requires: %name-dc-common = %version-%release
Requires: %name-winbind = %version-%release
Requires: krb5-kdc
Conflicts: %name-dc

%description dc-mitkrb5
Samba as Active Directory Domain Services (AD DS) also called a domain controller,
build with MIT Kerberos server and libraries.

%package client
Summary: Samba client programs
Group: Networking/Other
Requires: %name-common-client = %version-%release
Provides: samba-utils = %version-%release
Provides: samba-client-cups = %version-%release
Obsoletes: samba-client-cups < %version-%release

%description client
The %rname-client package provides some SMB/CIFS clients to complement
the built-in SMB/CIFS filesystem in Linux. These clients allow access
of SMB/CIFS shares and printing to SMB/CIFS printers.

%package gpupdate
Summary: Samba GPO support for clients
Group: Networking/Other
%ifnarch loongarch64
Requires: cepces
%endif
Requires: certmonger
Requires: libldb-modules-ldap = %version-%release
Requires: python3-module-%name = %version-%release

%description gpupdate
This package provides the samba-gpupdate tool to apply Group Policy Objects
(GPO) on Samba clients.

%package dc-client
Summary: Samba Active Directory client programs
Group: Networking/Other
Requires: %name-client = %version-%release
Provides: %dcname-client = %version-%release
Obsoletes: %dcname-client < 4.10

%description dc-client
The %rname-client package provides Active Directory Domain Services clients.

%package common-client
Summary: Files used by both Samba clients
Group: System/Configuration/Other
BuildArch: noarch

%description common-client
%rname-common provides files necessary for both the client packages of Samba.

%package common
Summary: Files used by both Samba servers
Group: System/Servers
BuildArch: noarch
%if_with winbind
Requires: %name-winbind-common = %version-%release
%endif
Requires: %name-common-client = %version-%release
Provides: %dcname-common = %version-%release
Obsoletes: %dcname-common < 4.10

%description common
%rname-common provides files necessary for both the server packages of Samba.

%package libs
Summary: Samba libraries
Group: System/Libraries
Requires: %name-common-libs = %version-%release
%if_without ldb
Requires: libldb = %ldb_version
%endif

%if_without libsmbclient
Provides: libsmbclient = %version-%release
Obsoletes: libsmbclient < %version-%release
%endif
%if_without libwbclient
Provides: libwbclient = %version-%release
Obsoletes: libwbclient < %version-%release
%endif
%if_without libnetapi
Provides: libnetapi = %version-%release
Obsoletes: libnetapi < %version-%release
%endif

%description libs
The %rname-libs package contains the libraries needed by programs that
link against the SMB, RPC and other protocols provided by the Samba suite.

%package vfs-cephfs
Summary: Samba VFS module for Ceph distributed storage system
Group: System/Libraries

%description vfs-cephfs
Samba VFS module for Ceph distributed storage system integration.

%package vfs-glusterfs
Summary: Samba VFS module for GlusterFS
Group: System/Libraries

%description vfs-glusterfs
Samba VFS module for GlusterFS integration.

%package vfs-snapper
Summary: Samba VFS module exposes snapshots managed by snapper as shadow-copies
Group: System/Libraries

%description vfs-snapper
Samba VFS module for exposes snapshots managed by snapper for use by Samba. This
provides the ability for remote SMB clients to access shadow-copies via Windows
Explorer using the "previous versions" dialog.

Snapshots can also be created and remove remotely, using the File Server Remote
VSS Protocol (FSRVP). Snapshot creation and deletion requests are forwarded to
snapper via DBus

%package krb5-printing
Summary: Samba CUPS backend for printing with Kerberos
Group: System/Configuration/Printing
Requires(pre): %name-client
Requires: %name-client = %version-%release

%description krb5-printing
If you need Kerberos for print jobs to a printer connection to cups via the SMB
backend, then you need to install that package. It will allow cups to access
the Kerberos credentials cache of the user issuing the print job.

%package dc-libs
Summary: Samba libraries
Group: System/Libraries
Provides: %dcname-libs = %version-%release
Obsoletes: %dcname-libs < 4.10
Provides: libldb-modules-DC = %version-%release
Obsoletes: libldb-modules-DC < 4.10
Provides: libldb-modules-dc = %version-%release
Obsoletes: libldb-modules-dc < 4.17

%if_with ldb_modules
Requires: libldb-modules-ldap = %version-%release
%endif

%description dc-libs
The %rname-libs package contains the libraries needed by programs that
link against the SMB, RPC and other protocols provided by the Samba suite.

%package common-libs
Summary: Samba common libraries
Group: System/Libraries
Provides: %dcname-common-libs = %version-%release
Obsoletes: %dcname-common-libs < 4.10
Provides: %rname-client-libs = %version-%release
Obsoletes: %rname-client-libs < 4.10

%description common-libs
The %rname-common-libs package contains the common libraries needed by modules that
link against the SMB, RPC and other protocols provided by the Samba suite.

%package common-tools
Summary: Tools for Samba servers and clients
Group: System/Servers
Requires: %name-common-client = %version-%release
Provides: %dcname-common-tools = %version-%release
Obsoletes: %dcname-common-tools < 4.10
Conflicts: gnustep-gworkspace

%description common-tools
The %rname-common-tools package contains tools for Samba servers and
SMB/CIFS clients.

%package -n libsmbclient
Summary: The SMB client library
Group: System/Libraries
Provides: libsmbclient-DC = %version-%release
Obsoletes: libsmbclient-DC < 4.10

%description -n libsmbclient
The libsmbclient contains the SMB client library from the Samba suite.

%package -n libldb-modules-ldap
Summary: Samba ldap modules for ldb
Group: System/Libraries
Requires: %name-libs = %version-%release
Provides: ldbsamba_extensions = %version-%release
Provides: %name-ldb-ldap-modules = %version-%release

%description -n libldb-modules-ldap
This package contains the ldb ldap modules required by samba-tool and
samba-gpupdate.

%package -n libsmbclient-devel
Summary: Developer tools for the SMB client library
Group: Development/C
Requires: libsmbclient = %version-%release
Provides: libsmbclient-DC-devel = %version-%release
Obsoletes: libsmbclient-DC-devel < 4.10

%description -n libsmbclient-devel
The libsmbclient-devel package contains the header files and libraries needed to
develop programs that link against the SMB client library in the Samba suite.

%package -n libwbclient
Summary: The winbind client library
Group: System/Libraries
Provides: libwbclient-DC = %version-%release
Obsoletes: libwbclient-DC < 4.10
Obsoletes: libwbclient-sssd

%description -n libwbclient
The libwbclient package contains the winbind client library from the Samba suite.

%package -n libwbclient-devel
Summary: Developer tools for the winbind library
Group: Development/C
Requires: libwbclient = %version-%release
Provides: libwbclient-DC-devel = %version-%release
Obsoletes: libwbclient-DC-devel < 4.10

%description -n libwbclient-devel
The libwbclient-devel package provides developer tools for the wbclient library.

%package -n libnetapi
Summary: Samba netapi library
Group: System/Libraries
Provides: libnetapi-DC = %version-%release
Obsoletes: libnetapi-DC < 4.10

%description -n libnetapi
Samba netapi library

%package -n libnetapi-devel
Summary: Samba netapi development files
Group: Development/Other
Requires: libnetapi = %version-%release
Conflicts: libnetapi-devel
Provides: libnetapi-DC-devel = %version-%release
Obsoletes: libnetapi-DC-devel < 4.10

%description -n libnetapi-devel
Samba netapi development files

%package -n python3-module-%name
Summary: Samba Python3 libraries
Group: Networking/Other
#Requires: %name-libs = %version-%release
Provides: python3-module-%dcname = %version-%release
Obsoletes: python3-module-%dcname < 4.10
Requires: %name-libs = %version-%release

# these modules currently don't support Python3 and aren't packaged
%add_python3_req_skip dsdb
%add_python3_req_skip param
%add_python3_req_skip passdb
%add_python3_req_skip samba.dsdb

%add_python3_req_skip samba._ldb
%add_python3_req_skip samba.auth
%add_python3_req_skip samba.credentials
%add_python3_req_skip samba.dcerpc.base
%add_python3_req_skip samba.dcerpc.dnsp
%add_python3_req_skip samba.dcerpc.drsuapi
%add_python3_req_skip samba.dcerpc.misc
%add_python3_req_skip samba.dcerpc.netlogon
%add_python3_req_skip samba.dcerpc.samr
%add_python3_req_skip samba.dcerpc.security
%add_python3_req_skip samba.gpo
%add_python3_req_skip samba.messaging
%add_python3_req_skip samba.net
%add_python3_req_skip samba.netbios
%add_python3_req_skip samba.ntstatus
%add_python3_req_skip samba.param
%add_python3_req_skip samba.posix_eadb
%add_python3_req_skip samba.registry
%add_python3_req_skip samba.security
%add_python3_req_skip samba.xattr_native
%add_python3_req_skip samba.xattr_tdb

# Python3 not fully migrated yet
%add_python3_req_skip ConfigParser
%add_python3_req_skip StringIO

%description -n python3-module-%name
The %rname-python3 package contains the Python3 libraries needed by programs
that use SMB, RPC and other Samba provided protocols in Python3 programs.

%package -n python3-module-%name-devel
Summary: Samba Python3 development libraries
Group: Development/Other
Requires: python3-module-%name = %version-%release

%description -n python3-module-%name-devel
The python3-module-%name package contains the Python3 libraries development files.

%package devel
Summary: Developer tools for Samba libraries
Group: Development/C
Requires: %name-libs = %version-%release
Provides: %dcname-devel = %version-%release
Obsoletes: %dcname-devel < 4.10

%if_without libsmbclient
Provides: libsmbclient-devel = %version-%release
Obsoletes: libsmbclient-devel < %version-%release
%endif
%if_without libwbclient
Provides: libwbclient-devel = %version-%release
Obsoletes: libwbclient-devel < %version-%release
%endif
%if_without libnetapi
Provides: libnetapi-devel = %version-%release
Obsoletes: libnetapi-devel < %version-%release
%endif

%description devel
The %rname-devel package contains the header files for the libraries
needed to develop programs that link against the SMB, RPC and other
libraries in the Samba suite.

%package pidl
Summary: Perl IDL compiler
Group: Development/Tools
BuildArch: noarch
# Requires: perl(:MODULE_COMPAT_%(eval "`perl -V:version`"; echo $version))
Provides: %dcname-pidl = %version-%release
Obsoletes: %dcname-pidl < 4.10

%description pidl
The %rname-pidl package contains the Perl IDL compiler used by Samba
and Wireshark to parse IDL and similar protocols

%package test
Summary: Testing tools for Samba servers and clients
Group: Development/Tools
Requires: %name = %version-%release
Requires: %name-common = %version-%release
%if_with winbind
Requires: %name-winbind = %version-%release
%endif
Provides: %dcname-test = %version-%release
Obsoletes: %dcname-test < 4.10

%description test
%rname-test provides testing tools for both the server and client
packages of Samba.

%package usershares
Summary: Provides support for non-root user shares
Group: System/Servers
PreReq: control
Requires: %name = %version-%release
Requires: %name-common-tools = %version-%release
Requires: libnss-role

%description usershares
Installing this package will provide a configuration file, group and
directories to support non-root user shares. You can configure them
as a user using the `net usershare` command.

%package winbind-common
Summary: Files used by MIT and Heimdal Winbind servers
Group: System/Servers
Requires: %name-common-client = %version-%release

%description winbind-common
%rname-winbind-common provides files necessary for both MIT and Heimdal
Winbind servers separately builded and packaged.

%package winbind
Summary: Samba winbind
Group: System/Servers
Requires: %name-libs = %version-%release
Requires: %name-dcerpc = %version-%release
Requires: %name-winbind-common = %version-%release
Provides: %dcname-winbind = %version-%release
Obsoletes: %dcname-winbind < 4.10

%description winbind
The %rname-winbind package provides the winbind NSS library, and some
client tools.  Winbind enables Linux to be a full member in Windows
domains and to use Windows user and group accounts on Linux.

%package winbind-clients
Summary: Samba winbind clients
Group: System/Servers
Requires: %name-winbind = %version-%release
Provides: %dcname-winbind-clients = %version-%release
Obsoletes: %dcname-winbind-clients < 4.10

%description winbind-clients
The samba-winbind-clients package provides the NSS library and a PAM
module necessary to communicate to the Winbind Daemon

%package winbind-krb5-locator
Summary: Samba winbind krb5 locator
Group: System/Servers
Provides: %dcname-winbind-krb5-locator = %version-%release
Obsoletes: %dcname-winbind-krb5-locator < 4.10

%description winbind-krb5-locator
The winbind krb5 locator is a plugin for the system kerberos library to allow
the local kerberos library to use the same KDC as samba and winbind use

%package winbind-krb5-localauth
Summary: Samba winbind krb5 plugin for mapping user accounts
Group: System/Servers
Provides: %dcname-winbind-krb5-localauth = %version-%release
Obsoletes: %dcname-winbind-krb5-localauth < 4.10

%description winbind-krb5-localauth
The winbind krb5 localauth is a plugin that permits the MIT Kerberos libraries
that Kerberos principals can be validated against local user accounts.

%package dcerpc
Summary: DCE RPC binaries
Group: System/Servers
Requires: samba-libs = %version-%release

%description dcerpc
The samba-dcerpc package contains binaries that serve DCERPC over named pipes.

%package ctdb
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
Provides: ctdb = %version-%release

%description ctdb
CTDB is a cluster implementation of the TDB database used by Samba and other
projects to store temporary data. If an application is already using TDB for
temporary data it is very easy to convert that application to be cluster aware
and use CTDB instead.

%package ctdb-pcp-pmda
Summary: CTDB PCP pmda support
Group: System/Servers
Requires: %name-ctdb = %version-%release
Provides: ctdb-pcp-pmda = %version-%release

%description ctdb-pcp-pmda
Performance Co-Pilot (PCP) support for CTDB

%package ctdb-etcd-mutex
Summary: CTDB ETCD mutex helper
Group: System/Servers
Requires: %name-ctdb = %version-%release
Provides: ctdb-etcd-mutex = %version-%release

%description ctdb-etcd-mutex
Support for using an existing ETCD cluster as a mutex helper for CTDB

%package ctdb-ceph-mutex
Summary: CTDB ceph mutex helper
Group: System/Servers
Requires: %name-ctdb = %version-%release
Provides: ctdb-ceph-mutex = %version-%release

%description ctdb-ceph-mutex
Support for using an existing CEPH cluster as a mutex helper for CTDB

%package ctdb-tests
Summary: CTDB clustered database test suite
Group: Development/Other
Requires: %name-ctdb = %version-%release
Requires: nc
Conflicts: ctdb-tests
Conflicts: ctdb-devel
Provides:  %name-ctdb-devel = %version-%release
Obsoletes: %name-ctdb-devel < %version-%release
Provides: %dcname-ctdb-tests = %version-%release
Obsoletes: %dcname-ctdb-tests < 4.10

%description ctdb-tests
Test suite for CTDB.
CTDB is a cluster implementation of the TDB database used by Samba and other
projects to store temporary data. If an application is already using TDB for
temporary data it is very easy to convert that application to be cluster aware
and use CTDB instead.

%package doc
Summary: Documentation for the Samba suite
Group: Documentation
Requires: %name-common = %version-%release
BuildArch: noarch
Provides: %dcname-doc = %version-%release
Obsoletes: %dcname-doc < 4.10

%description doc
The samba-doc package includes all the non-manpage documentation for the
Samba suite.

%package -n task-samba-dc
Summary: Complete Samba Active Directory Domain Controller with Heimdal Kerberos
Group: System/Servers
BuildArch: noarch
Provides: task-samba-ad-dc = %version-%release
Provides: task-ad-dc = %version-%release
Requires: samba-dc samba-winbind-clients %{?_with_doc:samba-doc} krb5-kinit ldb-tools

%description -n task-samba-dc
Samba server acts as a Domain Controller that is compatible with
Microsoft Active Directory.

%package -n task-samba-dc-mitkrb5
Summary: Complete Samba Active Directory Domain Controller with MIT Kerberos
Group: System/Servers
BuildArch: noarch
Requires: samba-dc-mitkrb5 %{?_with_doc:samba-doc} krb5-kinit ldb-tools

%description -n task-samba-dc-mitkrb5
Samba server acts as a Domain Controller that is compatible with
Microsoft Active Directory with MIT Kerberos server and libraries.

%package util-private-headers
Summary: libsamba_util private headers
Group: Development/C
Provides: %dcname-util-private-headers = %version-%release
Obsoletes: %dcname-util-private-headers < 4.10

%description util-private-headers
libsamba_util private headers.

%prep
%setup -q -n %rname-%version
%patch -p1
%patch10 -p1

%if_with separate_heimdal_server
rm -rf ../%rname-%version-separate-heimdal-server
cp -a ../%rname-%version ../%rname-%version-separate-heimdal-server
%endif

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

%define _ldb_lib ,ldb,pyldb,pyldb-util
%if_without ldb
%define _ldb_lib ,!ldb,!pyldb,!pyldb-util
%endif

%define _samba4_libraries heimdal,!zlib,!popt%{_talloc_lib}%{_tevent_lib}%{_tdb_lib}%{_ldb_lib}

%define _vfs_snapper_lib vfs_snapper
%if_without snapper
%define _vfs_snapper_lib !vfs_snapper
%endif

%define _samba4_idmap_modules idmap_ad,idmap_rid,idmap_adex,idmap_hash,idmap_tdb2
%define _samba4_pdb_modules pdb_tdbsam,pdb_ldap,pdb_ads,pdb_smbpasswd,pdb_wbc_sam,pdb_samba4
%define _samba4_auth_modules auth_unix,auth_wbc,auth_server,auth_netlogond,auth_script,auth_samba4
%define _samba4_vfs_modules %{_vfs_snapper_lib}
# auth_domain needs to be static
%define _samba4_modules %_samba4_idmap_modules,%_samba4_pdb_modules,%_samba4_auth_modules,%_samba4_vfs_modules

%define _libsmbclient %nil
%if_without libsmbclient
%define _libsmbclient smbclient,smbsharemodes,
%endif

%define _libwbclient %nil
%if_without libwbclient
%define _libwbclient wbclient,
%endif

%define _samba4_private_libraries %{_libsmbclient}%{_libwbclient}

%undefine _configure_gettext

%define configure_common() \
	%configure \\\
	--enable-fhs \\\
	--vendor-suffix=%release \\\
	--with-piddir=%_samba_piddir \\\
	--with-sockets-dir=%_samba_sockets_dir \\\
	--with-lockdir=%_localstatedir/lib/samba \\\
	--with-cachedir=%_localstatedir/cache/samba \\\
	--with-privatedir=/var/lib/samba/private \\\
	--with-shared-modules=%_samba4_modules \\\
	--bundled-libraries=%_samba4_libraries \\\
	--with-ads \\\
	--with-pie \\\
	--with-relro \\\
	--without-fam \\\
	--private-libraries=%_samba4_private_libraries \\\
%if_with systemd \
	--systemd-install-services \\\
	--with-systemddir=%_unitdir \\\
%endif \
%if_with winbind \
	--with-winbind \\\
%else \
	--without-winbind \\\
%endif \
%if_with testsuite \
	--enable-selftest \\\
%endif \
%if_with profiling_data \
	--with-profiling-data \\\
%endif \
	%{subst_enable spotlight} \\\
	%{subst_enable avahi} \\\
	%{subst_enable cephfs} \\\
	%{subst_enable glusterfs} \\\
	%*

%configure_common \
%if_with mitkrb5 \
	--with-system-mitkrb5 \
%endif \
%if_without dc \
	--without-ad-dc \
%else \
%if_with mitkrb5 \
	--with-experimental-mit-ad-dc \
%endif \
%if_with ntvfs \
	--with-ntvfs-fileserver \
%endif \
%endif \
%if_with clustering_support \
	--with-cluster-support \
%if_enabled pcp_pmda \
	--enable-pmda \
%endif \
%if_enabled etcd_mutex \
	--enable-etcd-reclock \
%endif \
%if_enabled ceph_mutex \
	--enable-ceph-reclock \
%endif \
%endif \
	--libdir=%_samba_libdir \
	--with-modulesdir=%_samba_mod_libdir \
	--with-privatelibdir=%_samba_mod_libdir \
	--with-pammodulesdir=/%_lib/security \
	--with-pam

%if_with separate_heimdal_server
pushd ../%rname-%version-separate-heimdal-server

%configure_common \
	--libdir=%_samba_dc_libdir \
	--libexecdir=%_samba_dc_libdir \
	--with-modulesdir=%_samba_dc_mod_libdir \
	--with-privatelibdir=%_samba_dc_mod_libdir \
	--pythonarchdir=%_samba_dc_pythonarchdir \
	--without-pam

%make_build NPROCS=%__nprocs V=2 -Onone

popd
%endif

# Make sure we do not build with heimdal code
rm -rfv third_party/heimdal

%make_build NPROCS=%__nprocs V=2 -Onone

pushd pidl
%__perl Makefile.PL PREFIX=%_prefix

%make_build V=2 -Onone
popd

%if_with doc
pushd docs-xml
export XML_CATALOG_FILES="file:///etc/xml/catalog file://$(pwd)/build/catalog.xml"
%autoreconf
%configure
%make_build smbdotconf/parameters.all.xml V=2 -Onone
%make_build release V=2 -Onone
popd
%endif

%install
%if_without separate_heimdal_server
%makeinstall_std V=2 -Onone %_smp_mflags
%else
pushd ../%rname-%version-separate-heimdal-server

%makeinstall_std V=2 -Onone %_smp_mflags

popd

mkdir -p %buildroot%_altdir

mv %buildroot%_bindir %buildroot%_samba_dc_mod_libdir/bin
mv %buildroot%_sbindir %buildroot%_samba_dc_mod_libdir/sbin
for f in samba samba_kcc samba_dnsupdate samba_spnupdate samba_upgradedns eventlogadm nmbd smbd winbindd; do
    printf "%_sbindir/$f\t%_samba_dc_mod_libdir/sbin/$f\t50\n" >> %buildroot%_altdir/samba-heimdal
done
printf "%_bindir/wbinfo\t%_samba_dc_mod_libdir/bin/wbinfo\t50\n" >> %buildroot%_altdir/samba-heimdal
printf "%_bindir/ntlm_auth\t%_samba_dc_mod_libdir/bin/ntlm_auth\t50\n" >> %buildroot%_altdir/samba-heimdal
printf "%_bindir/pdbedit\t%_samba_dc_mod_libdir/bin/pdbedit\t50\n" >> %buildroot%_altdir/samba-heimdal
printf "%_samba_mod_libdir/ldb\t%_samba_dc_mod_libdir/ldb\t50\n" >> %buildroot%_altdir/samba-heimdal

printf "%_bindir/samba-tool-plus\t%_samba_dc_mod_libdir/bin/samba-tool-plus\t50\n" >> %buildroot%_altdir/samba-heimdal
printf "%_bindir/samba-tool\t%_samba_dc_mod_libdir/bin/samba-tool\t50\n" >> %buildroot%_altdir/samba-heimdal
chmod 0755 %buildroot%_samba_dc_mod_libdir/bin/samba-tool

printf "%_sbindir/samba_downgrade_db\t%_samba_dc_mod_libdir/sbin/samba_downgrade_db\t50\n" >> %buildroot%_altdir/samba-heimdal
chmod 0755 %buildroot%_samba_dc_mod_libdir/sbin/samba_downgrade_db

mkdir -p %buildroot%_libdir/krb5/plugins/libkrb5
touch %buildroot%_libdir/krb5/plugins/libkrb5/winbind_krb5_locator.so
printf "%_libdir/krb5/plugins/libkrb5/winbind_krb5_locator.so\t%_samba_dc_mod_libdir/krb5/winbind_krb5_locator.so\t50\n" >> %buildroot%_altdir/samba-heimdal
printf "%_libdir/krb5/plugins/libkrb5/winbind_krb5_locator.so\t%_samba_dc_mod_libdir/krb5/async_dns_krb5_locator.so\t40\n" >> %buildroot%_altdir/samba-heimdal

%makeinstall_std V=2 -Onone %_smp_mflags

rm -f %buildroot%_altdir/samba-mit
touch %buildroot%_altdir/samba-mit
mkdir %buildroot%_samba_mod_libdir/sbin
for f in eventlogadm nmbd smbd; do
    mv %buildroot%_sbindir/$f %buildroot%_samba_mod_libdir/sbin/
    printf "%_sbindir/$f\t%_samba_mod_libdir/sbin/$f\t20\n" >> %buildroot%_altdir/samba-mit
done
for f in samba samba_kcc samba_dnsupdate samba_spnupdate samba_upgradedns; do
    mv %buildroot%_sbindir/$f %buildroot%_samba_mod_libdir/sbin/
    printf "%_sbindir/$f\t%_samba_mod_libdir/sbin/$f\t20\n" >> %buildroot%_altdir/samba-mit-dc
done

mkdir %buildroot%_samba_mod_libdir/bin
mv %buildroot%_bindir/wbinfo %buildroot%_samba_mod_libdir/bin/
mv %buildroot%_bindir/ntlm_auth %buildroot%_samba_mod_libdir/bin/
mv %buildroot%_sbindir/winbindd %buildroot%_samba_mod_libdir/sbin/
printf "%_sbindir/winbindd\t%_samba_mod_libdir/sbin/winbindd\t20\n" > %buildroot%_altdir/samba-mit-winbind
printf "%_bindir/wbinfo\t%_samba_mod_libdir/bin/wbinfo\t20\n" >> %buildroot%_altdir/samba-mit-winbind
printf "%_bindir/ntlm_auth\t%_samba_mod_libdir/bin/ntlm_auth\t20\n" >> %buildroot%_altdir/samba-mit-winbind

mv %buildroot%_bindir/pdbedit %buildroot%_samba_mod_libdir/bin/
printf "%_bindir/pdbedit\t%_samba_mod_libdir/bin/pdbedit\t20\n" > %buildroot%_altdir/samba-mit-common-tools

mv %buildroot%_samba_mod_libdir/ldb %buildroot%_samba_mod_libdir/ldb.mit
printf "%_samba_mod_libdir/ldb\t%_samba_mod_libdir/ldb.mit\t20\n" > %buildroot%_altdir/samba-mit-dc-modules

mv %buildroot%_bindir/samba-tool %buildroot%_samba_mod_libdir/bin/
printf "%_bindir/samba-tool\t%_samba_mod_libdir/bin/samba-tool\t20\n" > %buildroot%_altdir/samba-mit-dc-client
chmod 0755 %buildroot%_samba_mod_libdir/bin/samba-tool

mv %buildroot%_sbindir/samba_downgrade_db %buildroot%_samba_mod_libdir/sbin/
printf "%_sbindir/samba_downgrade_db\t%_samba_mod_libdir/sbin/samba_downgrade_db\t20\n" >> %buildroot%_altdir/samba-mit-dc-client
chmod 0755 %buildroot%_samba_mod_libdir/sbin/samba_downgrade_db

%endif

mkdir -p %buildroot/sbin
mkdir -p %buildroot/usr/{sbin,bin}
mkdir -p %buildroot/%_lib/security
mkdir -p %buildroot/var/lib/samba
mkdir -p %buildroot/var/lib/ctdb
mkdir -p %buildroot%_localstatedir/cache/samba
mkdir -p %buildroot/var/lib/samba/{private,winbindd_privileged,scripts,sysvol,drivers,usershares}
mkdir -p %buildroot/var/log/samba/old
mkdir -p %buildroot/var/spool/samba
mkdir -p %buildroot%_samba_piddir/winbindd
mkdir -p %buildroot%_samba_sockets_dir
mkdir -p %buildroot%_samba_mod_libdir
mkdir -p %buildroot%_pkgconfigdir
mkdir -p %buildroot%_initdir
mkdir -p %buildroot%_unitdir
mkdir -p %buildroot%_sysconfdir/{pam.d,logrotate.d,security,sysconfig}

mkdir -p %buildroot%_tmpfilesdir

# Install other stuff
install -m644 %SOURCE1 %buildroot%_sysconfdir/logrotate.d/samba
install -m644 %SOURCE9 %buildroot%_sysconfdir/samba/smb.conf
install -m644 %SOURCE22 %buildroot%_sysconfdir/samba/smb.conf.example
install -m644 %SOURCE23 %buildroot%_sysconfdir/samba/usershares.conf
install -m644 %SOURCE11 %buildroot%_sysconfdir/security
install -m644 %SOURCE6 %buildroot%_sysconfdir/pam.d/samba
echo 127.0.0.1 localhost > %buildroot%_sysconfdir/samba/lmhosts
mkdir -p %buildroot%_sysconfdir/openldap/schema
install -m644 examples/LDAP/samba.schema %buildroot%_sysconfdir/openldap/schema/samba.schema
install -m755 packaging/printing/smbprint %buildroot%_bindir/smbprint
install -Dm755 %SOURCE24 %buildroot%_controldir/smb-conf-usershares
install -Dm755 %SOURCE28 %buildroot%_controldir/smb-conf-usershare-allow-list
install -Dm755 %SOURCE29 %buildroot%_controldir/smb-conf-usershare-deny-list
install -Dm755 %SOURCE30 %buildroot%_controldir/smb-conf-usershare-owner-only
install -Dm755 %SOURCE31 %buildroot%_controldir/smb-conf-usershare-allow-guests
install -Dm755 %SOURCE25 %buildroot%_controldir/role-usershares
install -Dm755 %SOURCE27 %buildroot%_controldir/role-sambashare
install -Dm644 %SOURCE26 %buildroot%_sysconfdir/role.d/samba-usershares.role

cp packaging/systemd/samba.sysconfig packaging/systemd/samba.sysconfig.alt
echo "KRB5CCNAME=FILE:/run/samba/krb5cc_samba" >>packaging/systemd/samba.sysconfig.alt
install -m644 packaging/systemd/samba.sysconfig.alt %buildroot%_sysconfdir/sysconfig/samba
install -m644 %SOURCE21 %buildroot%_sysconfdir/samba/smbusers

install -m755 %SOURCE10 %buildroot%_initrddir/nmb
install -m755 %SOURCE5 %buildroot%_initrddir/smb
install -m755 %SOURCE8 %buildroot%_initrddir/winbind
%if_with dc
install -m755 %SOURCE20 %buildroot%_initrddir/samba
%endif

# Put README in builddir
cp %SOURCE200 %SOURCE201 .

%if_with clustering_support
install -m755 %SOURCE12 %buildroot%_initrddir/ctdb
echo "d %_samba_piddir/ctdb 755 root root" >> %buildroot%_tmpfilesdir/ctdb.conf
touch %buildroot%_sysconfdir/ctdb/nodes
%endif

echo "d %_samba_piddir/samba 755 root root" > %buildroot%_tmpfilesdir/%rname.conf

# NetworkManager online/offline script
install -d -m 0755 %buildroot%_sysconfdir/NetworkManager/dispatcher.d/
install -m 0755 packaging/NetworkManager/30-winbind-systemd \
            %buildroot%_sysconfdir/NetworkManager/dispatcher.d/30-winbind

pushd pidl
make DESTDIR=%buildroot install_vendor

# Clean out crap left behind by the PIDL install.
find %buildroot -type f -name .packlist -exec rm -f {} \;
rm -f %buildroot%perl_vendorlib/wscript_build
rm -f %buildroot%perl_vendor_archlib/perllocal.pod
popd

# winbind
%if_with winbind
mkdir -p %buildroot/%_lib

mkdir -p %buildroot%_libdir/krb5/plugins/libkrb5
touch %buildroot%_libdir/krb5/plugins/libkrb5/winbind_krb5_locator.so
printf "%_libdir/krb5/plugins/libkrb5/winbind_krb5_locator.so\t%_samba_mod_libdir/krb5/winbind_krb5_locator.so\t20\n" >> %buildroot%_altdir/samba-mit-winbind-krb5-locator
printf "%_libdir/krb5/plugins/libkrb5/winbind_krb5_locator.so\t%_samba_mod_libdir/krb5/async_dns_krb5_locator.so\t10\n" >> %buildroot%_altdir/samba-mit-winbind-krb5-locator
%if_with mitkrb5
mv %buildroot%_samba_mod_libdir/krb5/winbind_krb5_localauth.so %buildroot%_libdir/krb5/plugins/libkrb5/
%endif
%endif

#cups backend
%define cups_serverbin %(cups-config --serverbin 2>/dev/null)
mkdir -p %buildroot%cups_serverbin/backend
ln -s %_bindir/smbspool %buildroot%cups_serverbin/backend/smb

printf "%cups_serverbin/backend/smb\t%_bindir/smbspool\t20\n" > %buildroot%_altdir/samba-printing
printf "%cups_serverbin/backend/smb\t%_samba_libexecdir/smbspool_krb5_wrapper\t50\n" > %buildroot%_altdir/samba-krb5-printing

# Fix up permission on perl install.
%_fixperms %buildroot%perl_vendor_privlib

# remove tests form python modules
rm -rf %buildroot%python3_sitelibdir/samba/{tests,subunit,external/subunit,external/testtool}
rm -f %buildroot%python3_sitelibdir/samba/third_party/iso8601/test_*.py
%if_with separate_heimdal_server
rm -rf %buildroot%_samba_dc_mod_libdir/python%_python3_version/samba/{tests,subunit,external/subunit,external/testtool}
rm -f %buildroot%_samba_dc_mod_libdir/python%_python3_version/samba/third_party/iso8601/test_*.py
%endif

# remove cmocka library
rm -f %buildroot%_samba_mod_libdir/libcmocka-private-samba.so
%if_with separate_heimdal_server
rm -f %buildroot%_samba_dc_mod_libdir/libcmocka-private-samba.so
%endif

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

# Install traffic tools
install -m755 script/traffic_learner %buildroot%_bindir/traffic_learner
install -m755 script/traffic_replay %buildroot%_bindir/traffic_replay
#install -m755 script/traffic_summary.pl %buildroot%_bindir/traffic_summary (perl-XML-Twig requires)

# Compatiblity symlink for admx policy templates
#ln -s ../PolicyDefinitions %buildroot%_datadir/samba/admx

# Prepare to validation admx policy templates
for file in %buildroot%_datadir/PolicyDefinitions/*.admx %buildroot%_datadir/PolicyDefinitions/*-*/*.adml; do
    grep -q "^\(<policyDefinitions\|<policyDefinitionResources\) .*xmlns:xsd=" "$file" ||
        sed -i 's/^\(<policyDefinitions\|<policyDefinitionResources\)/\1 xmlns:xsd="http:\/\/www.w3.org\/2001\/XMLSchema"/' "$file"
    grep -q "^\(<policyDefinitions\|<policyDefinitionResources\) .*xmlns:xsi=" "$file" ||
        sed -i 's/^\(<policyDefinitions\|<policyDefinitionResources\)/\1 xmlns:xsi="http:\/\/www.w3.org\/2001\/XMLSchema-instance"/' "$file"
    grep -q "^\(<policyDefinitions\|<policyDefinitionResources\) .*xmlns=" "$file" ||
        sed -i 's/^\(<policyDefinitions\|<policyDefinitionResources\)/\1 xmlns="http:\/\/schemas.microsoft.com\/GroupPolicy\/2006\/07\/PolicyDefinitions"/' "$file"
done

# Provide compatiblity with __init__ function for samba.gp.* classes
touch %buildroot%python3_sitelibdir/samba/gp/__init__.py
touch %buildroot%python3_sitelibdir/samba/gp/util/__init__.py

%find_lang pam_winbind
%find_lang net

%check
for file in \
            %buildroot%_datadir/PolicyDefinitions/*.admx \
            %buildroot%_datadir/PolicyDefinitions/*/*.adml
do
    admx-lint --input_file "$file"
done

%if_with testsuite
TDB_NO_FSYNC=1 %make_build test V=2 -Onone
%endif

%post
%post_service smb
%post_service nmb

%preun
%preun_service smb
%preun_service nmb

%pre common
%_sbindir/groupadd -f -r printadmin >/dev/null 2>&1 || :

%if_with dc
%post dc
%post_service samba

%preun dc
%preun_service samba
%endif

%if_with winbind
%pre winbind-common
%_sbindir/groupadd -f -r wbpriv >/dev/null 2>&1 || :

%post winbind
%post_service winbind

%preun winbind
%preun_service winbind
%endif

%pre usershares
%_sbindir/groupadd -f -r usershares >/dev/null 2>&1 || :

# Enable sambashare group as role with usershares priviledge for compatility
# during upgrade from previous manual managed installations.
%triggerin -n %name-usershares -- %name < 4.16.7-alt4
control role-sambashare enabled

%files
%doc COPYING README.md WHATSNEW.txt
%doc examples/autofs examples/LDAP examples/misc
%doc examples/printer-accounting examples/printing
%doc README.downgrade
%if_with separate_heimdal_server
%_altdir/samba-mit
%_samba_mod_libdir/sbin/eventlogadm
%_samba_mod_libdir/sbin/nmbd
%_samba_mod_libdir/sbin/smbd
%else
%_sbindir/eventlogadm
%_sbindir/nmbd
%_sbindir/smbd
%endif
%_samba_libexecdir/samba-bgqd
%config(noreplace) %_sysconfdir/samba/smbusers
%attr(755,root,root) %_initdir/smb
%attr(755,root,root) %_initdir/nmb
%_unitdir/nmb.service
%_unitdir/smb.service
%_unitdir/samba-bgqd.service

%dir %_samba_mod_libdir/vfs
%_samba_mod_libdir/vfs/*.so

%if_with libcephfs
%exclude %_samba_mod_libdir/vfs/ceph*.so
%endif

%if_enabled glusterfs
%exclude %_samba_mod_libdir/vfs/glusterfs.so
%endif

%if_with snapper
%exclude %_samba_mod_libdir/vfs/snapper.so
%endif

%dir %_samba_mod_libdir/auth
%_samba_mod_libdir/auth/unix.so

%attr(775,root,printadmin) %dir /var/lib/samba/drivers

%files dcerpc
%dir %_samba_libexecdir
%_samba_libexecdir/samba-dcerpcd
%_samba_libexecdir/rpcd_classic
%_samba_libexecdir/rpcd_epmapper
%_samba_libexecdir/rpcd_fsrvp
%_samba_libexecdir/rpcd_lsad
%_samba_libexecdir/rpcd_mdssvc
%_samba_libexecdir/rpcd_spoolss
%_samba_libexecdir/rpcd_winreg
%_samba_libexecdir/rpcd_witness
%if_with doc
%_man8dir/samba-dcerpcd.8*
%endif

%if_with dc
%files -n admx-samba
%_datadir/PolicyDefinitions/*.admx
%_datadir/PolicyDefinitions/*/*.adml

%files dc-common
%dir /var/lib/samba/sysvol
%dir %_datadir/samba/setup
%_datadir/samba/setup
%if_with doc
%_man8dir/samba.8*
%endif #doc

%files dc
%attr(755,root,root) %_initdir/samba
%_unitdir/samba.service
%if_without separate_heimdal_server
%_sbindir/samba
%_sbindir/samba_kcc
%_sbindir/samba_dnsupdate
%_sbindir/samba_spnupdate
%_sbindir/samba_upgradedns
%_sbindir/samba_downgrade_db
%else #!separate_heimdal_server
%_unitdir/winbind.service
%attr(755,root,root) %_initrddir/winbind
%_sysconfdir/NetworkManager/dispatcher.d/30-winbind
%doc COPYING README.md WHATSNEW.txt
%doc examples/autofs examples/LDAP examples/misc
%doc examples/printer-accounting examples/printing
%_altdir/samba-heimdal
#_samba_dc_mod_libdir/sbin/eventlogadm
#_samba_dc_mod_libdir/sbin/nmbd
#_samba_dc_mod_libdir/sbin/smbd
#_samba_dc_mod_libdir/sbin/samba
#_samba_dc_mod_libdir/sbin/samba_kcc
#_samba_dc_mod_libdir/sbin/samba_dnsupdate
#_samba_dc_mod_libdir/sbin/samba_spnupdate
#_samba_dc_mod_libdir/sbin/samba_upgradedns
#_samba_dc_mod_libdir/sbin/winbindd
#_samba_dc_mod_libdir/bin/
%dir %_samba_dc_mod_libdir
%_samba_dc_libdir/
%ghost %_libdir/krb5/plugins/libkrb5/winbind_krb5_locator.so

%files -n task-samba-dc-mitkrb5

%files dc-mitkrb5
%attr(755,root,root) %_initdir/samba
%_unitdir/samba.service
%_altdir/samba-mit-dc
%_samba_mod_libdir/sbin/samba
%_samba_mod_libdir/sbin/samba_kcc
%_samba_mod_libdir/sbin/samba_dnsupdate
%_samba_mod_libdir/sbin/samba_spnupdate
%_samba_mod_libdir/sbin/samba_upgradedns
%endif #!separate_heimdal_server

%_samba_mod_libdir/auth/samba4.so

%files gpupdate
%_sbindir/samba-gpupdate
%if_with doc
%_man8dir/samba-gpupdate.8*
%endif

%files dc-client
%if_with separate_heimdal_server
%_altdir/samba-mit-dc-client
%_samba_mod_libdir/bin/samba-tool
%_samba_mod_libdir/sbin/samba_downgrade_db
%else
%_bindir/samba-tool
%_sbindir/samba_downgrade_db
%endif
%if_with doc
%_man8dir/samba-tool.8*
%_man8dir/samba_downgrade_db.8*
%endif #doc
%endif #dc

%files krb5-printing
%_altdir/samba-krb5-printing
%attr(0700,root,root) %_samba_libexecdir/smbspool_krb5_wrapper
%if_with doc
%_man8dir/smbspool_krb5_wrapper.8*
%endif

%files client
%_bindir/cifsdd
%_bindir/dbwrap_tool
%_bindir/dumpmscat
%_bindir/mdsearch
%_bindir/mvxattr
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
%_bindir/wspsearch
%_altdir/samba-printing
# Samba CUPS backend for printing with Kerberos support or not controlled
# by whether the samba-krb5-printing package is installed or not:
#  %_bindir/smbspool or %_samba_libexecdir/smbspool_krb5_wrapper
#   -> %cups_serverbin/backend/smb
%ghost %cups_serverbin/backend/smb
%if_with doc
%_man1dir/dbwrap_tool.1*
%_man1dir/mdsearch.1*
%_man1dir/mvxattr.1*
%_man1dir/nmblookup.1*
%_man1dir/oLschema2ldif.1*
%_man1dir/regdiff.1*
%_man8dir/samba-regedit.8*
%_man1dir/regpatch.1*
%_man1dir/regshell.1*
%_man1dir/regtree.1*
%_man1dir/log2pcap.1*
%_man1dir/rpcclient.1*
%_man1dir/sharesec.1*
%_man1dir/smbcacls.1*
%_man1dir/smbclient.1*
%_man1dir/smbcquotas.1*
%_man1dir/smbget.1*
%exclude %_man1dir/smbtar.1*
%_man1dir/smbtree.1*
%_man1dir/wspsearch.1*
%_man5dir/smbpasswd.5*
%_man8dir/smbpasswd.8*
%_man8dir/smbspool.8*
#_man8dir/smbta-util.8*
%_man8dir/cifsdd.8*
%endif

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
%_samba_mod_libdir/libldb-cmdline-private-samba.so
%endif

%files common-client
%attr(755,root,root) %dir %_sysconfdir/samba
%config(noreplace) %_sysconfdir/samba/smb.conf
%_sysconfdir/samba/smb.conf.example
%config(noreplace) %_sysconfdir/samba/lmhosts

%if_with doc
%_man5dir/lmhosts.5*
%_man5dir/smb.conf.5*
%endif

%files common
%_sysconfdir/pam.d/samba
%if_without winbind
%dir /var/lib/samba
%attr(710,root,root) %dir /var/lib/samba/private
%endif
%_tmpfilesdir/%rname.conf
%config(noreplace) %_sysconfdir/logrotate.d/samba
%config(noreplace) %_sysconfdir/security/limits.d/90-samba.conf
%attr(0700,root,root) %dir /var/log/samba
%attr(0700,root,root) %dir /var/log/samba/old
%dir %_samba_sockets_dir
%attr(755,root,root) %dir %_localstatedir/cache/samba
%config(noreplace) %_sysconfdir/sysconfig/samba
%attr(1777,root,root) %dir /var/spool/samba
%_sysconfdir/openldap/schema/samba.schema

%dir %_datadir/samba
%if_enabled spotlight
%dir %_datadir/samba/mdssvc
%_datadir/samba/mdssvc/elasticsearch_mappings.json
%endif

%if_with doc
%_man7dir/samba.7*

%_man8dir/eventlogadm.8*
%_man8dir/smbd.8*
%_man8dir/nmbd.8*
%_man8dir/samba-bgqd.8*
%_man8dir/vfs_*.8*

%if_with libcephfs
%exclude %_man8dir/vfs_ceph.8*
%exclude %_man8dir/vfs_ceph_new.8*
%exclude %_man8dir/vfs_ceph_snapshots.8*
%endif
%if_enabled glusterfs
%exclude %_man8dir/vfs_glusterfs.8*
%endif
%if_with snapper
%exclude %_man8dir/vfs_snapper.8*
%endif
%endif #doc

%files common-tools -f net.lang
%_bindir/net
%if_with separate_heimdal_server
%_altdir/samba-mit-common-tools
%_samba_mod_libdir/bin/pdbedit
%else
%_bindir/pdbedit
%endif
%_bindir/profiles
%_bindir/samba-log-parser
%_bindir/smbcontrol
%_bindir/smbstatus
%_bindir/testparm
%if_with doc
%_man1dir/profiles.1*
%_man1dir/samba-log-parser.1*
%_man1dir/smbcontrol.1*
%_man1dir/smbstatus.1*
%_man1dir/testparm.1*
%_man8dir/net.8*
%_man8dir/pdbedit.8*
%endif #doc

%files devel
%dir %_includedir/samba-4.0
%_includedir/samba-4.0

%exclude %_includedir/samba-4.0/private
#%exclude %_includedir/samba-4.0/torture.h

%if_with libnetapi
%exclude %_includedir/samba-4.0/netapi.h
%else
%_samba_libdir/libnetapi.so
%_pkgconfigdir/netapi.pc
%endif

%if_with libsmbclient
%exclude %_includedir/samba-4.0/libsmbclient.h
%else
%_samba_libdir/libsmbclient.so
%_pkgconfigdir/smbclient.pc
%if_with doc
%_man7dir/libsmbclient.7*
%endif
%endif

%if_with libwbclient
%exclude %_includedir/samba-4.0/wbclient.h
%else
%_samba_libdir/libwbclient.so
%_pkgconfigdir/wbclient.pc
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
%_pkgconfigdir/samba-util.pc
%_pkgconfigdir/samdb.pc

%if_with dc
%_samba_libdir/libdcerpc-server-core.so
%_samba_libdir/libdcerpc-server.so
%_pkgconfigdir/dcerpc_server.pc
%endif

%files common-libs
# libraries needed by the public libraries
%_samba_libdir/libdcerpc.so.%{libdcerpc_so_version}*
%_samba_libdir/libdcerpc-samr.so.%{libdcerpc_samr_so_version}*
%_samba_libdir/libdcerpc-server-core.so.%{libdcerpc_server_core_so_version}*
%_samba_libdir/libdcerpc-binding.so.%{libdcerpc_binding_so_version}*
%_samba_libdir/libndr-krb5pac.so.%{libndr_krb5pac_so_version}*
%_samba_libdir/libndr-nbt.so.%{libndr_nbt_so_version}*
%_samba_libdir/libndr-standard.so.%{libndr_standard_so_version}*
%_samba_libdir/libndr.so.%{libndr_so_version}*
%_samba_libdir/libsamba-credentials.so.%{libsamba_credentials_so_version}*
%_samba_libdir/libsamba-errors.so.%{libsamba_errors_so_version}*
%_samba_libdir/libsamba-hostconfig.so.%{libsamba_hostconfig_so_version}*
%_samba_libdir/libsamba-passdb.so.%{libsamba_passdb_so_version}*
%_samba_libdir/libsamba-util.so.%{libsamba_util_so_version}*
%_samba_libdir/libsamdb.so.%{libsamdb_so_version}*
%_samba_libdir/libsmbconf.so.%{libsmbconf_so_version}*
%_samba_libdir/libsmbldap.so.%{libsmbldap_so_version}*
%_samba_libdir/libtevent-util.so.%{libtevent_util_so_version}*

# common libraries
%_samba_mod_libdir/libCHARSET3-private-samba.so
%_samba_mod_libdir/libLIBWBCLIENT-OLD-private-samba.so
%_samba_mod_libdir/libMESSAGING-SEND-private-samba.so
%_samba_mod_libdir/libaddns-private-samba.so
%_samba_mod_libdir/libasn1util-private-samba.so
%_samba_mod_libdir/libauth-unix-token-private-samba.so
%_samba_mod_libdir/libauthkrb5-private-samba.so
%_samba_mod_libdir/libcli-cldap-private-samba.so
%_samba_mod_libdir/libcli-ldap-common-private-samba.so
%_samba_mod_libdir/libcli-ldap-private-samba.so
%_samba_mod_libdir/libcli-nbt-private-samba.so
%_samba_mod_libdir/libcli-smb-common-private-samba.so
%_samba_mod_libdir/libcliauth-private-samba.so
%_samba_mod_libdir/libclidns-private-samba.so
%_samba_mod_libdir/libcluster-private-samba.so
%_samba_mod_libdir/libcmdline-private-samba.so
%_samba_mod_libdir/libcmdline-contexts-private-samba.so
%_samba_mod_libdir/libcommon-auth-private-samba.so
%if_with clustering_support
%_samba_mod_libdir/libctdb-event-client-private-samba.so
%endif
%_samba_mod_libdir/libdbwrap-private-samba.so
%_samba_mod_libdir/libdcerpc-pkt-auth-private-samba.so
%_samba_mod_libdir/libdcerpc-samba-private-samba.so
%if_with dc
%_samba_mod_libdir/libdfs-server-ad-private-samba.so
%endif
%_samba_mod_libdir/libevents-private-samba.so
%_samba_mod_libdir/libflag-mapping-private-samba.so
%_samba_mod_libdir/libgenrand-private-samba.so
%_samba_mod_libdir/libgensec-private-samba.so
%_samba_mod_libdir/libgse-private-samba.so
%_samba_mod_libdir/libhttp-private-samba.so
%_samba_mod_libdir/libinterfaces-private-samba.so
%_samba_mod_libdir/libiov-buf-private-samba.so
%_samba_mod_libdir/libkrb5samba-private-samba.so
%_samba_mod_libdir/libldbsamba-private-samba.so
%_samba_mod_libdir/liblibcli-lsa3-private-samba.so
%_samba_mod_libdir/liblibsmb-private-samba.so
%_samba_mod_libdir/libmessages-dgm-private-samba.so
%_samba_mod_libdir/libmessages-util-private-samba.so
%_samba_mod_libdir/libmsghdr-private-samba.so
%_samba_mod_libdir/libmsrpc3-private-samba.so
%_samba_mod_libdir/libndr-samba-private-samba.so
%_samba_mod_libdir/libndr-samba4-private-samba.so
%_samba_mod_libdir/libnetif-private-samba.so
%_samba_mod_libdir/libnpa-tstream-private-samba.so
%_samba_mod_libdir/libposix-eadb-private-samba.so
%if_without libwbclient
%_samba_mod_libdir/libreplace-private-samba.so
%_samba_mod_libdir/libwbclient.so.*
%endif
%_samba_mod_libdir/libsamba-cluster-support-private-samba.so
%_samba_mod_libdir/libsamba-debug-private-samba.so
%_samba_mod_libdir/libsamba-modules-private-samba.so
%_samba_mod_libdir/libsamba-security-private-samba.so
%_samba_mod_libdir/libsamba-sockets-private-samba.so
%_samba_mod_libdir/libsamba3-util-private-samba.so
%_samba_mod_libdir/libsamdb-common-private-samba.so
%_samba_mod_libdir/libsecrets3-private-samba.so
%_samba_mod_libdir/libserver-id-db-private-samba.so
%_samba_mod_libdir/libserver-role-private-samba.so
%_samba_mod_libdir/libshares-private-samba.so
%_samba_mod_libdir/libsmb-transport-private-samba.so
%_samba_mod_libdir/libsmbclient-raw-private-samba.so
%_samba_mod_libdir/libsmbd-shim-private-samba.so
%_samba_mod_libdir/libsmbpasswdparser-private-samba.so
%_samba_mod_libdir/libstable-sort-private-samba.so
%_samba_mod_libdir/libsocket-blocking-private-samba.so
%_samba_mod_libdir/libsys-rw-private-samba.so
%_samba_mod_libdir/libtalloc-report-printf-private-samba.so
%_samba_mod_libdir/libtalloc-report-private-samba.so
%_samba_mod_libdir/libtdb-wrap-private-samba.so
%_samba_mod_libdir/libtime-basic-private-samba.so
%_samba_mod_libdir/libtorture-private-samba.so
%_samba_mod_libdir/libutil-reg-private-samba.so
%_samba_mod_libdir/libutil-setid-private-samba.so
%_samba_mod_libdir/libutil-tdb-private-samba.so
%_samba_mod_libdir/libxattr-tdb-private-samba.so

%if_with ldb
%_samba_libdir/libldb.so.*
%_samba_libdir/libpyldb-util.so.*
%endif
%if_with talloc
%_samba_libdir/libtalloc.so.*
%_samba_libdir/libpytalloc-util.so.*
%endif
%if_with tevent
%_samba_libdir/libtevent.so.*
%endif
%if_with tdb
%_samba_libdir/libtdb.so.*
%endif

%if_without libsmbclient
%_samba_libdir/libsmbclient.so.%{libsmbclient_so_version}*
%endif
%if_without libwbclient
%_samba_libdir/libwbclient.so.%{libwbclient_so_version}*
%endif

%files libs
%dir %_samba_mod_libdir/pdb
%_samba_mod_libdir/pdb

%_samba_mod_libdir/libREG-FULL-private-samba.so
%_samba_mod_libdir/libRPC-SERVER-LOOP-private-samba.so
%_samba_mod_libdir/libRPC-WORKER-private-samba.so

%_samba_mod_libdir/libMESSAGING-private-samba.so
%_samba_mod_libdir/libads-private-samba.so
%_samba_mod_libdir/libauth-private-samba.so
%_samba_mod_libdir/libcli-spoolss-private-samba.so
%_samba_mod_libdir/libdcerpc-samba4-private-samba.so
%_samba_mod_libdir/libgpext-private-samba.so
%_samba_mod_libdir/libgpo-private-samba.so
%_samba_mod_libdir/liblibcli-netlogon3-private-samba.so
%_samba_mod_libdir/libmscat-private-samba.so
%_samba_mod_libdir/libnet-keytab-private-samba.so

%_samba_mod_libdir/libprinter-driver-private-samba.so
%_samba_mod_libdir/libprinting-migrate-private-samba.so
%_samba_mod_libdir/libregistry-private-samba.so
%_samba_mod_libdir/libsmbldaphelper-private-samba.so
%_samba_mod_libdir/libsmbd-base-private-samba.so
%_samba_mod_libdir/libtrusts-util-private-samba.so

%if_without libnetapi
%_samba_libdir/libnetapi.so.%{libnetapi_so_version}*
%endif

%if_with libcephfs
%files vfs-cephfs
%_samba_mod_libdir/vfs/ceph*.so
%if_with doc
%_man8dir/vfs_ceph.8*
%_man8dir/vfs_ceph_new.8*
%_man8dir/vfs_ceph_snapshots.8*
%endif
%endif

%if_enabled glusterfs
%files vfs-glusterfs
%_samba_mod_libdir/vfs/glusterfs.so
%if_with doc
%_man8dir/vfs_glusterfs.8*
%endif
%endif

%if_with snapper
%files vfs-snapper
%_samba_mod_libdir/vfs/snapper.so
%if_with doc
%_man8dir/vfs_snapper.8*
%endif
%endif

%if_with dc
%files dc-libs
%_samba_mod_libdir/bind9/dlz_bind9_10.so
%_samba_mod_libdir/bind9/dlz_bind9_11.so
%_samba_mod_libdir/bind9/dlz_bind9_12.so
%_samba_mod_libdir/bind9/dlz_bind9_14.so
%_samba_mod_libdir/bind9/dlz_bind9_16.so
%_samba_mod_libdir/bind9/dlz_bind9_18.so
%if_without mitkrb5
%_samba_mod_libdir/libheimntlm-samba4.so.1
%_samba_mod_libdir/libheimntlm-samba4.so.1.0.1
%_samba_mod_libdir/libkdc-samba4.so.2
%_samba_mod_libdir/libkdc-samba4.so.2.0.0
%endif #!mitkrb5
%_samba_mod_libdir/libad-claims-private-samba.so
%_samba_mod_libdir/libauth4-private-samba.so
%_samba_mod_libdir/libauthn-policy-util-private-samba.so
%_samba_mod_libdir/libdb-glue-private-samba.so
%_samba_mod_libdir/libdnsserver-common-private-samba.so
%_samba_mod_libdir/libdsdb-module-private-samba.so
%_samba_mod_libdir/libdsdb-garbage-collect-tombstones-private-samba.so
%_samba_mod_libdir/libpac-private-samba.so
%_samba_mod_libdir/libscavenge-dns-records-private-samba.so
%if_with ldb_modules
%if_with separate_heimdal_server
%_samba_mod_libdir/ldb.mit
%exclude %_samba_mod_libdir/ldb.mit/ldbsamba_extensions.so
%exclude %_samba_mod_libdir/ldb.mit/ildap.so
%else
%_samba_mod_libdir/ldb
%exclude %_samba_mod_libdir/ldb/ldbsamba_extensions.so
%exclude %_samba_mod_libdir/ldb/ildap.so
%endif
%else
%if_with separate_heimdal_server
%_altdir/samba-mit-dc-modules
%dir %_samba_mod_libdir/ldb.mit
%_samba_mod_libdir/ldb.mit
%else
%dir %_samba_mod_libdir/ldb
%_samba_mod_libdir/ldb
%endif
%endif
%dir %_samba_mod_libdir/gensec
%_samba_mod_libdir/gensec
%if_without mitkrb5
%_samba_mod_libdir/libHDB-SAMBA4-private-samba.so
%_samba_mod_libdir/libasn1-private-samba.so
%_samba_mod_libdir/libcom_err-private-samba.so
%_samba_mod_libdir/libgssapi-private-samba.so
%_samba_mod_libdir/libhcrypto-private-samba.so
%_samba_mod_libdir/libhdb-private-samba.so
%_samba_mod_libdir/libheimbase-private-samba.so
%_samba_mod_libdir/libhx509-private-samba.so
%_samba_mod_libdir/libkrb5-private-samba.so
%_samba_mod_libdir/libroken-private-samba.so
%_samba_mod_libdir/libwind-private-samba.so
%else
%_samba_libdir/krb5/plugins/kdb/samba.so
%endif #!mitkrb5
%_samba_mod_libdir/libprocess-model-private-samba.so
%_samba_mod_libdir/libservice-private-samba.so
%_samba_mod_libdir/process_model
%_samba_mod_libdir/service
%_samba_libdir/libdcerpc-server.so.*
%if_with ntvfs
%_samba_mod_libdir/libntvfs-private-samba.so
%endif
%else
%doc README.dc-libs
%_samba_mod_libdir/libdnsserver-common-private-samba.so
%endif

%if_with ldb_modules
%files -n libldb-modules-ldap
%if_with separate_heimdal_server
%_altdir/samba-mit-dc-modules
%dir %_samba_mod_libdir/ldb.mit
%_samba_mod_libdir/ldb.mit/ldbsamba_extensions.so
%_samba_mod_libdir/ldb.mit/ildap.so
%else
%dir %_samba_mod_libdir/ldb
%_samba_mod_libdir/ldb/ldbsamba_extensions.so
%_samba_mod_libdir/ldb/ildap.so
%endif
%endif

%if_with libsmbclient
%files -n libsmbclient
%_samba_libdir/libsmbclient.so.%{libsmbclient_so_version}*

%files -n libsmbclient-devel
%dir %_includedir/samba-4.0
%_includedir/samba-4.0/libsmbclient.h
%_samba_libdir/libsmbclient.so
%_pkgconfigdir/smbclient.pc
%if_with doc
%_man7dir/libsmbclient.7*
%endif #doc
%endif

%if_with libwbclient
%files -n libwbclient
%_libdir/libwbclient.so.%{libwbclient_so_version}*
%_samba_mod_libdir/libreplace-private-samba.so

%files -n libwbclient-devel
%dir %_includedir/samba-4.0
%_includedir/samba-4.0/wbclient.h
%_samba_libdir/libwbclient.so
%_pkgconfigdir/wbclient.pc
%endif

%if_with libnetapi
%files -n libnetapi
%_samba_libdir/libnetapi.so.%{libnetapi_so_version}*

%files -n libnetapi-devel
%_samba_libdir/libnetapi.so
%dir %_includedir/samba-4.0
%_includedir/samba-4.0/netapi.h
%_pkgconfigdir/netapi.pc
%endif

%files pidl
%attr(755,root,root) %_bindir/pidl
%if_with doc
%_man1dir/pidl.1.*
%endif
%perl_vendor_privlib/*

%files -n python3-module-%name
%python3_sitelibdir/samba/
%_libdir/libsamba*.cpython-*.so.*
%_samba_mod_libdir/libsamba*.cpython-*.so

%files -n python3-module-%name-devel
%_pkgconfigdir/samba*.cpython-*.pc
%_libdir/libsamba*.cpython-*.so

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
%_bindir/traffic_learner
%_bindir/traffic_replay
#%_samba_libdir/libtorture.so.*
%if_with dc
%_samba_mod_libdir/libdlz-bind9-for-torture-private-samba.so
%else
%_samba_mod_libdir/libdsdb-module-private-samba.so
%endif
%if_with doc
%_man1dir/gentest.1*
%_man1dir/locktest.1*
%_man1dir/masktest.1*
%_man1dir/ndrdump.1*
%_man1dir/smbtorture.1*
%_man7dir/traffic_learner.7*
%_man7dir/traffic_replay.7*
%endif

%if_with testsuite
# files to ignore in testsuite mode
%_samba_mod_libdir/libnss-wrapper-private-samba.so
%_samba_mod_libdir/libsocket-wrapper-private-samba.so
%_samba_mod_libdir/libuid-wrapper-private-samba.so
%endif

%files usershares
%config(noreplace) %_sysconfdir/samba/usershares.conf
%config(noreplace) %_sysconfdir/role.d/samba-usershares.role
%attr(1770,root,usershares) %dir /var/lib/samba/usershares
%_controldir/smb-conf-usershares
%_controldir/role-usershares
%_controldir/role-sambashare
%_controldir/smb-conf-usershare-allow-list
%_controldir/smb-conf-usershare-deny-list
%_controldir/smb-conf-usershare-owner-only
%_controldir/smb-conf-usershare-allow-guests

%if_with winbind
%files winbind-common
%dir /var/lib/samba
%attr(710,root,root) %dir /var/lib/samba/private
%attr(750,root,wbpriv) %dir /var/lib/samba/winbindd_privileged
%dir %_samba_piddir/winbindd
%if_with doc
%_man8dir/winbindd.8*
%_man8dir/idmap_*.8*
%endif

%files winbind -f pam_winbind.lang
%_unitdir/winbind.service
%attr(755,root,root) %_initrddir/winbind
%_sysconfdir/NetworkManager/dispatcher.d/30-winbind
%_samba_mod_libdir/idmap
%_samba_mod_libdir/nss_info
%_samba_mod_libdir/libnss-info-private-samba.so
%_samba_mod_libdir/libidmap-private-samba.so
%if_with separate_heimdal_server
%_altdir/samba-mit-winbind
%_samba_mod_libdir/sbin/winbindd
%_samba_mod_libdir/bin/wbinfo
%_samba_mod_libdir/bin/ntlm_auth
%else
%_bindir/ntlm_auth
%_bindir/wbinfo
%_sbindir/winbindd
%endif
%if_with doc
%_man1dir/ntlm_auth.1.*
%_man1dir/wbinfo.1*
%endif

%files winbind-clients
%_samba_libdir/libnss_winbind.so*
%_samba_libdir/libnss_wins.so*
/%_lib/security/pam_winbind.so
%config(noreplace) %_sysconfdir/security/pam_winbind.conf
%if_with doc
%_man5dir/pam_winbind.conf.5*
%_man8dir/pam_winbind.8*
%endif

%files winbind-krb5-locator
%ghost %_libdir/krb5/plugins/libkrb5/winbind_krb5_locator.so
%_altdir/samba-mit-winbind-krb5-locator
%_samba_mod_libdir/krb5/winbind_krb5_locator.so
%_samba_mod_libdir/krb5/async_dns_krb5_locator.so
%if_with doc
%_man8dir/winbind_krb5_locator.8*
%endif #doc

%if_with mitkrb5
%files winbind-krb5-localauth
%_libdir/krb5/plugins/libkrb5/winbind_krb5_localauth.so
%if_with doc
%_man8dir/winbind_krb5_localauth.8*
%endif #doc
%endif #mitkrb5
%endif #winbind

%if_with clustering_support
%files ctdb
#doc ctdb/README
%dir %_sysconfdir/ctdb
%config(noreplace) %_sysconfdir/ctdb/nodes
%config(noreplace) %_sysconfdir/ctdb/notify.sh
%config(noreplace) %_sysconfdir/ctdb/debug-hung-script.sh
%config(noreplace) %_sysconfdir/ctdb/ctdb-crash-cleanup.sh
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
%dir %_sysconfdir/ctdb/events
%dir %_sysconfdir/ctdb/events/notification
%dir %_sysconfdir/ctdb/events/legacy
%_sysconfdir/ctdb/events/notification/README
%dir %_datadir/ctdb/events/legacy
%_datadir/ctdb/events/legacy/*.script
%_sbindir/ctdbd
%_bindir/ctdb
%_bindir/ctdb_diagnostics
%_bindir/ltdbtool
%_bindir/onnode
%_bindir/ping_pong
%_libexecdir/ctdb/ctdb-config
%_libexecdir/ctdb/ctdb-event
%_libexecdir/ctdb/ctdb-eventd
%_libexecdir/ctdb/ctdb-path
%_libexecdir/ctdb/ctdb_killtcp
%_libexecdir/ctdb/ctdb_lock_helper
%_libexecdir/ctdb/ctdb_lvs
%_libexecdir/ctdb/ctdb_mutex_fcntl_helper
%_libexecdir/ctdb/ctdb_natgw
%_libexecdir/ctdb/ctdb_recovery_helper
%_libexecdir/ctdb/ctdb_takeover_helper
%_libexecdir/ctdb/tdb_mutex_check
%_libexecdir/ctdb/smnotify

%if_with doc
%_man1dir/ctdb.1*
%_man1dir/ctdbd.1*
%_man1dir/onnode.1*
%_man1dir/ltdbtool.1*
%_man1dir/ping_pong.1*
%_man1dir/ctdb_diagnostics.1*
%_man5dir/ctdb.conf.5*
%_man5dir/ctdb-script.options.5*
%_man5dir/ctdb.sysconfig.5*
%_man7dir/ctdb.7*
%_man7dir/ctdb-tunables.7*
%_man7dir/ctdb-statistics.7*
%endif

%if_with testsuite
%files ctdb-tests
%doc ctdb/tests/README
%_libexecdir/ctdb/tests
%_bindir/ctdb_local_daemons
%_bindir/ctdb_run_tests
%_bindir/ctdb_run_cluster_tests
%_datadir/ctdb/tests
%endif #testsuite

%if_enabled pcp_pmda
%files ctdb-pcp-pmda
%dir %_localstatedir/lib/pcp/pmdas/ctdb
%_localstatedir/lib/pcp/pmdas/ctdb/Install
%_localstatedir/lib/pcp/pmdas/ctdb/README
%_localstatedir/lib/pcp/pmdas/ctdb/Remove
%_localstatedir/lib/pcp/pmdas/ctdb/domain.h
%_localstatedir/lib/pcp/pmdas/ctdb/help
%_localstatedir/lib/pcp/pmdas/ctdb/pmdactdb
%_localstatedir/lib/pcp/pmdas/ctdb/pmns
%endif

%if_enabled etcd_mutex
%files ctdb-etcd-mutex
%_libexecdir/ctdb/ctdb_etcd_lock
%_man7dir/ctdb-etcd.7*
%endif

%if_enabled ceph_mutex
%files ctdb-ceph-mutex
%_libexecdir/ctdb/ctdb_mutex_ceph_rados_helper
%_man7dir/ctdb_mutex_ceph_rados_helper.7*
%endif
%endif #clustering_support

%files -n task-samba-dc

%files util-private-headers
%dir %_includedir/samba-4.0/private
%_includedir/samba-4.0/private

%changelog
* Sat Sep 21 2024 Evgeny Sinelnikov <sin@altlinux.org> 4.20.5-alt1
- Update to maintenance release of Samba 4.20
- Major fixes from upstream (Samba#15695, Samba#15699, Samba#15698, Samba#15696,
                             Samba#15686, Samba#15700, Samba#15677)
  + "inherit permissions = yes" triggers assert() in vfs_default.
  + Incorrect FSCTL_QUERY_ALLOCATED_RANGES response when truncated.
  + samba-tool can not load the default configuration file (upstream update).
  + Compound SMB2 requests don't return NT_STATUS_NETWORK_SESSION_EXPIRED for
    all requests, confuses MacOSX clients.
  + Add vfs_ceph_new module (based on low level API).
  + Crash when readlinkat fails.
  + ntlm_auth make logs more consistent with length check.

* Thu Aug 22 2024 Evgeny Sinelnikov <sin@altlinux.org> 4.20.4-alt2
- Replace all libraries needed by the public libraries to common-libs:
  + libdcerpc.so.0
  + libdcerpc-server-core.so.0
  + libsamba-passdb.so.0
- Replace some common private libraries to common-libs (for public libraries):
  + libdcerpc-pkt-auth-private-samba.so
  + libhttp-private-samba.so
  + libsmbclient-raw-private-samba.so

* Wed Aug 21 2024 Evgeny Sinelnikov <sin@altlinux.org> 4.20.4-alt1
- Update to stable release of Samba 4.20 (Samba#15673):
  + Due --version-* options are still not ergonomic, and they reject tilde
    characters, so, revert the commit changed the script for generating the ABI
    symbol version broken the ABI by changing all dots to underscores.
    This reverts the commit partially to preserve the dots in the version part.
- Replace some common private libraries to common-libs (for libsmclient):
  + libreplace-private-samba.so
  + libcli-smb-common-private-samba.so
  + libgse-private-samba.so
  + liblibsmb-private-samba.so

* Fri Aug 16 2024 Andrey Limachko <liannnix@altlinux.org> 4.20.3-alt2
- Fix duplication of pdc srv record after role transfer (thx Evgenii Sozonov).

* Fri Aug 02 2024 Evgeny Sinelnikov <sin@altlinux.org> 4.20.3-alt1
- Update to stable release of Samba 4.20
- Major fixes from upstream (Samba#15683, Samba#15655, Samba#15685, Samba#15603,
                             Samba#15621)
  + Running samba-bgqd as a standalone systemd service does not work.
  + When claims enabled with heimdal kerberos, unable to log on to a
    Windows computer when user account need to change their own password.
  + Samba does not parse SDDL found in defaultSecurityDescriptor in
    AD_DS_Classes_Windows_Server_v1903.ldf
  + Heimdal ignores _gsskrb5_decapsulate errors in init_sec_context/repl_mutual.
  + s4:ldap_server: does not support tls channel bindings for sasl binds.

* Fri Jul 19 2024 Evgeny Sinelnikov <sin@altlinux.org> 4.20.2-alt2
- New option 'idmap reverse cache update' to control reverse name to sid cache
  behaviour that Winbind's idmap interface additionally saved to namemap cache,
  when found unknown sid during sid to name query. This option solves the
  compatibility problem of foreign SIDs getting stuck in trust relationships
  from the SIDHistory attribute.
  By default, this option is disabled (so, compatibility behaviour is enabled).

* Thu Jul 18 2024 Evgeny Sinelnikov <sin@altlinux.org> 4.20.2-alt1
- Update to stable release of Samba 4.20
- Replace winbind_krb5_locator.so and async_dns_krb5_locator.so
  to mutually exclusive alterantives placed into libkrb5 plugins directory as
  symlink named winbind_krb5_locator.so.
- Major fixes from upstream (Samba#15662, Samba#15569, Samba#15625, Samba#15654,
                             Samba#13019, Samba#14981, Samba#15412, Samba#15573,
                             Samba#15620, Samba#15642, Samba#15659, Samba#15664,
                             Samba#15666, Samba#15435, Samba#15633, Samba#15653)
  + Regression DFS not working with widelinks = true.
  + vfs_widelinks with DFS shares breaks case insensitivity.
  + ldb qsort might r/w out of bounds with an intransitive compare function.
  + Many qsort() comparison functions are non-transitive, which can lead to
    out-of-bounds access in some circumstances.
  + New options --vendor-name and --vendor-patch-revision arguments allows
    distributions and packagers to put their name in the Samba version string.
  + Dynamic DNS updates with the internal DNS are not working.
  + netr_LogonSamLogonEx returns NR_STATUS_ACCESS_DENIED with SysvolReady=0.
  + Anonymous smb3 signing/encryption should be allowed (similar to
    Windows Server 2022).
  + Panic in dreplsrv_op_pull_source_apply_changes_trigger.
  + s4:nbt_server: does not provide unexpected handling, so winbindd can't use
    nmb requests instead cldap.
  + winbindd, net ads join and other things don't work on an ipv6 only host.
  + Segmentation fault when deleting files in vfs_recycle.
  * Panic in vfs_offload_token_db_fetch_fsp().
  + "client use kerberos" and --use-kerberos is ignored for the machine account.
  + samba-gpupdate - Invalid NtVer in netlogon_samlogon_response.
  + idmap_ad creates an incorrect local krb5.conf in case of trusted domain lookups.

* Sun May 26 2024 Evgeny Sinelnikov <sin@altlinux.org> 4.20.1-alt2
- Fix clean memory for force dns canonicalize destination hostname option.

* Fri May 10 2024 Evgeny Sinelnikov <sin@altlinux.org> 4.20.1-alt1
- Update to stable release of Samba 4.20
- Add support separate builds generated with samba-pidl.
- Major changes from upstream:
  + dns update debug message is too noisy (Samba#15630).
  + Do not fail PAC validation for RFC8009 checksums types (Samba#15635).
  + Improve performance of lookup_groupmem() in idmap_ad (Samba#15605).
  + Smbcacls incorrectly propagates inheritance with Inherit-Only
    flag (Samba#15636).
  + http library doesn't support 'chunked transfer encoding' (Samba#15611).
  + Provide a systemd service file for the background queue daemon (Samba#15600).

* Tue Apr 09 2024 Evgeny Sinelnikov <sin@altlinux.org> 4.20.0-alt1
- Update to stable release of Samba 4.20
- Major changes from upstream:
  + The password access tool "samba-tool user getpassword" and the password sync
    tool "samba-tool user syncpasswords" allow attributes to be chosen for output.
  + samba-tool has been extended to provide client-side support for Group Managed
    Service accounts (reading the current and previous gMSA password and writing
    a Kerberos Ticket Granting Ticket (TGT) to a local credentials cache).
  + Windows Search Protocol (WSP) experimental command line client "wspsearch".
  + 'smbcacls' has been extended to allow DACLs to be saved and restored to/from
    a file (in interchangeable format with windows cmd line tool 'icacls.exe').
  + samba-tool now allows users to be associated with claims, the creation and
    management of authentication policies and silos.
  + AD DC support for Authentication Silos and Authentication Policies with
    (functional level must be set to 2012_R2 or later / 2016 latest supported).
  + Support of Conditional ACEs, Resource Attribute ACEs and the Security
    Descriptor Definition Language (SDDL) extensions for conditional ACEs and
    resource attribute ACEs.
  + The Workstation Service Remote Protocol [MS-WKST] calls NetWkstaGetInfo
    and NetWkstaEnumUsers) returns the list of locally logged on users, which
    getting the list from utmp, is not Y2038 safe and has been removed.

* Tue Apr 09 2024 Evgeny Sinelnikov <sin@altlinux.org> 4.19.6-alt1
- Update to maintenance release of Samba 4.19
- Fixes from upstream (Samba#15580):
  + Packet marshalling push support missing for
     CTDB_CONTROL_TCP_CLIENT_DISCONNECTED and
     CTDB_CONTROL_TCP_CLIENT_PASSED.

* Thu Mar 28 2024 Evgeny Sinelnikov <sin@altlinux.org> 4.19.5-alt2
- Add support 'client force dns canonicalize hostname' global parameter, enables
  client library tries to resolve canonical name. This feature allows to
  communicate via kerberos to services using CNAME records without adding SPNs.
- Fixes updated from upstream for smbd:
  + If we fail to close file_handle ensure we should reset the fd (Samba#15527).
  + simplify handling of failing fstat() after unlinking file (Samba#15527).
- Fixes updated from upstream for gpo:
  + libgpo: Do not segfault if we don't have a valid security descriptor (Samba#15599).
  + python:gp: Implement client site lookup in site_dn_for_machine() (Samba#15588).
  + librpc:idl: Make netlogon_samlogon_response public (Samba#15588).

* Mon Mar 11 2024 Evgeny Sinelnikov <sin@altlinux.org> 4.19.5-alt1
- Update to stable release of Samba 4.19
- Fixes from upstream:
  + Windows 2016 fails to restore previous version of a file from a shadow_copy2
    snapshot (Samba#13688).
  + smbd fixes (Samba#12421, Samba#15550).
  + samba-gpupdate fixes (Samba#15548, Samba#15557, Samba#15552, Samba#15558).
  + smbpasswd reset permissions only if not 0600 (Samba#15555).

* Thu Feb 15 2024 Arseny Maslennikov <arseny@altlinux.org> 4.19.4-alt2
- NMU: remove useless symlinks to nss_winbind and nss_wins.
  See also: https://altlinux.org/Usrmerge.

* Tue Jan 16 2024 Evgeny Sinelnikov <sin@altlinux.org> 4.19.4-alt1
- Update to stable release of Samba 4.19
- Fixes from upstream:
  + net changesecretpw cannot set the machine account password if secrets.tdb
    is empty (Samba#13577).
  + Following intermediate abolute share-local symlinks is broken (Samba#15505).
    ctdb RELEASE_IP causes a crash in release_ip if a connection to a non-public
    address disconnects first (Samba#15523).
  + shadow_copy2 broken when current fileset's directories are removed (Samba#15544).
  + 'force user = localunixuser' doesn't work if 'allow trusted domains = no'
    is set (Samba#15469).
  + smbget: debug logging doesn't work (Samba#15525), username in the smburl and
    interactive password entry doesn't work (Samba#15532), auth function doesn't
    set values for password prompt correctly (Samba#15538).
  + Unable to copy and write files from clients to Ceph cluster via SMB Linux
    gateway with Ceph VFS module (Samba#15440).
  + Multichannel refresh network information (Samba#15547).

* Tue Dec 12 2023 Evgeny Sinelnikov <sin@altlinux.org> 4.19.3-alt2
- Replace samba service pam config to samba-common due regression with password
  authentication in security = user mode with obey pam restrictions = yes.

* Tue Dec 05 2023 Evgeny Sinelnikov <sin@altlinux.org> 4.19.3-alt1
- Update to stable release of Samba 4.19 with fixes of the Samba CVE for
  Deleted Object tombstones visible in AD LDAP to normal users (CVE-2018-14628).
- Security fixes:
  + CVE-2018-14628: Wrong ntSecurityDescriptor values for "CN=Deleted Objects"
                    allow read of object tombstones over LDAP
                    (Administrator action required!)
                    https://www.samba.org/samba/security/CVE-2018-14628.html

* Mon Nov 06 2023 Evgeny Sinelnikov <sin@altlinux.org> 4.19.2-alt1
- Update to stable release of Samba 4.19 with latest bugfixes and new features:
 + Migrated smbget to use common command line parser. This has some advantages
   as you get all the feature it provides like Kerberos authentication. The
   support for smbgetrc has been removed.
 + gpupdate changes: The libgpo.get_gpo_list function has been deprecated in
   favor of an implementation written in python,  connects to Active Directory
   using the SamDB module, instead of ADS (which is what libgpo uses).
 + Improved winbind logging and a new tool for parsing the winbind logs. Winbind
   logs (if smb.conf 'winbind debug traceid = yes' is set) contain new trace
   header fields 'traceid' and 'depth'.
 + AD database prepared to Functional Level 2016 standards for new domains.
   While Samba still provides only Functional Level 2008R2 by default, Samba as
   an AD DC will now, in provision ensure that the blank database is already
   prepared for Functional Level 2016, with AD Schema 2019.
 + Kerberos Claims, Authentication Silos and NTLM authentication policies.
   The primary limitation is that while Samba can read and write claims
   in the directory, and populate the PAC, Samba does not yet use them
   for access control decisions.
 + Improved KDC Auditing now provides Samba-style JSON audit logging of all
   issued Kerberos tickets, including if they would fail a policy that is not
   yet enforced. Additionally most failures are audited.
 + Kerberos Armoring (FAST) Support for Windows clients. In domains where the
   domain controller functional level is set to 2012, 2012_R2 or 2016, Windows
   clients will, if configured via GPO, use FAST to protect user passwords
   between (in particular) a workstation and the KDC on the AD DC. This is a
   significant security improvement, as weak passwords in an AS-REQ are no
   longer available for offline attack.
 + Claims compression in the AD PAC. Samba as an AD DC will compress "AD claims"
   using the same compression algorithm as Microsoft Windows.
 + Resource SID compression in the AD PAC. Samba as an AD DC will now correctly
   populate the various PAC group membership buffers, splitting global and local
   groups correctly.
 + Resource Based Constrained Delegation (RBCD) support in both MIT and Heimdal.
   Samba 4.17 added to samba-tool delegation the 'add-principal' and
   'del-principal' subcommands in order to manage RBCD, and the database changes
   made by these tools are now honoured by the Heimdal KDC once Samba is upgraded.
 + New samba-tool support for silos, claims, sites and subnets.
   samba-tool can now list, show, add and manipulate Authentication Silos
   (silos) and Active Directory Authentication Claims (claims).
 + Updated Heimdal import. Samba's Heimdal branch (known as lorikeet-heimdal)
   has been updated to the current pre-8.0 (master) tree from upstream Heimdal,
   ensuring that this vendored copy, included in our release remains as close as
   possible to the current upstream code.
 + Revocation support in Heimdal KDC for PKINIT certificates. Samba will now
   correctly honour the revocation of 'smart card' certificates used for PKINIT
   Kerberos authentication.
 + Require encrypted connection to modify unicodePwd on the AD DC.
 + Samba AD TLS Certificates can be reloaded. The TLS certificates used for
   Samba's AD DC LDAP server were previously only read on startup, and this
   meant that when then expired it was required to restart Samba, disrupting
   service to other users (smbcontrol ldap_server reload-certs).

* Wed Nov 01 2023 Evgeny Sinelnikov <sin@altlinux.org> 4.18.8-alt1
- Update to maintenance release of Samba 4.18 with latest bugfixes and new features:
 + SMB Server performance improvements. The locking overhead for contended path
   based operations is reduced by an additional factor of ~ 3 compared to 4.17.
 + More succinct samba-tool error messages.
 + Accessing the old samba-tool messages with full Python stack trace by using
   the argument '-d3'.
 + New samba-tool dsacl subcommand for deleting ACES
 + Colour output with samba-tool --color and
 + No colour with NO_COLOR environment variable
 + New wbinfo option --change-secret-at which forces the trust account password
   to be changed at a specified domain controller.
 + New option acl_xattr:security_acl_name to change the NT ACL default protected
   location security.NTACL not accessible from normal users outside of Samba.
 + New option server addresses as per-share parameter to limit share visibility
   and accessibility to specific server IP addresses. This option can offer a
   different set of shares per interface.
 + Azure Active Directory / Office365 synchronisation improvements with the
   Azure AD Connect cloud sync tool which now supported for password hash
   synchronisation, allowing Samba AD Domains to synchronise passwords with this
   popular cloud environment.

* Sun Oct 22 2023 Evgeny Sinelnikov <sin@altlinux.org> 4.17.12-alt2
- Revert services type from forking to notify.

* Sat Oct 17 2023 Evgeny Sinelnikov <sin@altlinux.org> 4.17.12-alt1
- Update to security release of Samba 4.17
- Security fixes (Samba#15422, Samba#15424, Samba#15439, Samba#15473, Samba#15474):
 + CVE-2023-3961:  Unsanitized pipe names allow SMB clients to connect as root
                   to existing unix domain sockets on the file system.
                   https://www.samba.org/samba/security/CVE-2023-3961.html

 + CVE-2023-4091:  SMB client can truncate files to 0 bytes by opening files
                   with OVERWRITE disposition when using the acl_xattr Samba VFS
                   module with the smb.conf setting
                   "acl_xattr:ignore system acls = yes"
                   https://www.samba.org/samba/security/CVE-2023-4091.html

 + CVE-2023-4154:  An RODC and a user with the GET_CHANGES right can view all
                   attributes, including secrets and passwords.  Additionally,
                   the access check fails open on error conditions.
                   https://www.samba.org/samba/security/CVE-2023-4154.html

 + CVE-2023-42669: Calls to the rpcecho server on the AD DC can request that the
                   server block for a user-defined amount of time, denying
                   service.
                   https://www.samba.org/samba/security/CVE-2023-42669.html

 + CVE-2023-42670: Samba can be made to start multiple incompatible RPC
                   listeners, disrupting service on the AD DC.
                   https://www.samba.org/samba/security/CVE-2023-42670.html

* Sat Oct 07 2023 Evgeny Sinelnikov <sin@altlinux.org> 4.17.11-alt2
- New build scheme with separate upstream, altlinux and sisyphus branches.

* Sat Sep 23 2023 Evgeny Sinelnikov <sin@altlinux.org> 4.17.11-alt1
- Update to security release of Samba 4.17
- smbd fileserver fixes (Samba#15419, Samba#15420, Samba#15430, Samba#15432,
                         Samba#15417, Samba#15346, Samba#15453, Samba#15435):
  + Weird filename can cause assert to fail in openat_pathref_fsp_nosymlink().
  + reply_sesssetup_and_X() can dereference uninitialized tmp pointer.
  + Missing return in reply_exit_done().
  + TREE_CONNECT without SETUP causes smbd to use uninitialized pointer.
  + Renaming results in NT_STATUS_SHARING_VIOLATION if previously attempted
    to remove the destination.
  + 2-3min delays at reconnect with smb2_validate_sequence_number:
    bad message_id 2.
  + File doesn't show when user doesn't have permission if
    aio_pthread is loaded.
  + Regression DFS not working with widelinks = true.

- replication fixes (Samba#15401, Samba#15407)
  + Improve GetNChanges to address some (but not all "Azure AD Connect")
    syncronisation tool looping during the initial user sync phase.
  + Samba replication logs show (null) DN.

- tools fixes (Samba#15384, Samba#15441, Samba#15451):
  + net ads lookup (with unspecified realm) fails
  + samba-tool ntacl get segfault if aio_pthread appended.
  + ctdb_killtcp fails to work with --enable-pcap and libpcap >= 1.9.1.

- other protocol fixes (Samba#15446, Samba#9959, Samba#15463
                        Samba#15449, Samba#15342, Samba#15427):
  + DCERPC_PKT_CO_CANCEL and DCERPC_PKT_ORPHANED can't be parsed.
  + Windows client join fails if a second container CN=System exists somewhere.
  + macOS mdfind returns only 50 results.
  + mdssvc: Do an early talloc_free() in _mdssvc_open().
  + Spotlight sometimes returns no results on latest macOS.
  + Spotlight results return wrong date in result list.

- Compatibility fixes of spec (thx asheplyakov@):
  + added missing BR: alternatives.
  + added rpm-macros-alterinatives as a pre-requirement.
  + added missing build-requirements: flex, liblmdb-devel.
  + dropped obsolete build dependency on gtk+2.
  + samba-client: libldb-cmdline-samba4.so.

- Disabled tracker backend in spotlight (obsolete with version less than 3.x).
- Disabled glusterfs on armh due it not supported on this architecture.

* Sun Jul 23 2023 Evgeny Sinelnikov <sin@altlinux.org> 4.17.10-alt1
- Update to maintenance release of Samba 4.17:
  + Secure channel faulty since Windows 10/11 update 07/2023 (KB5028166).

- Security fixes (Samba#15418):
  + CVE-2022-2127:  When winbind is used for NTLM authentication, a maliciously
                    crafted request can trigger an out-of-bounds read in winbind
                    and possibly crash it.
                    https://www.samba.org/samba/security/CVE-2022-2127.html

  + CVE-2023-3347:  SMB2 packet signing is not enforced if an admin configured
                    "server signing = required" or for SMB2 connections to Domain
                    Controllers where SMB2 packet signing is mandatory.
                    https://www.samba.org/samba/security/CVE-2023-3347.html

  + CVE-2023-34966: An infinite loop bug in Samba's mdssvc RPC service for
                    Spotlight can be triggered by an unauthenticated attacker by
                    issuing a malformed RPC request.
                    https://www.samba.org/samba/security/CVE-2023-34966.html

  + CVE-2023-34967: Missing type validation in Samba's mdssvc RPC service for
                    Spotlight can be used by an unauthenticated attacker to
                    trigger a process crash in a shared RPC mdssvc worker process.
                    https://www.samba.org/samba/security/CVE-2023-34967.html

  + CVE-2023-34968: As part of the Spotlight protocol Samba discloses the server-
                    side absolute path of shares and files and directories in
                    search results.
                    https://www.samba.org/samba/security/CVE-2023-34968.html

* Mon Jul 10 2023 Evgeny Sinelnikov <sin@altlinux.org> 4.17.9-alt1
- Update to maintenance release of Samba 4.17:
  + smbd_scavenger crashes when service smbd is stopped (Samba#15275).
  + vfs_fruit might cause a failing open for delete (Samba#15378).
  + named crashes on DLZ zone update (Samba#14030).
  + winbind recurses into itself via rpcd_lsad (Samba#15361).
  + cli_list loops 100%% CPU against pre-lanman2 servers (Samba#15382).
  + smbclient leaks fds with showacls (Samba#15391).
  + aes256 smb3 encryption algorithms are not allowed in
    smb3_sid_parse() (Samba#15374).
  + winbindd gets stuck on NT_STATUS_RPC_SEC_PKG_ERROR (Samba#15413).
  + smbget memory leak if failed to download files recursively (Samba#15403).
- Add check with admx-lint for group policy templates validation.

* Sun May 21 2023 Evgeny Sinelnikov <sin@altlinux.org> 4.17.8-alt1
- Update to maintenance release of Samba 4.17:
  + log flood: smbd_calculate_access_mask_fsp: Access denied: message level
    should be lower (Samba#15302).
  + Floating point exception (FPE) via cli_pull_send at
    source3/libsmb/clireadwrite.c (Samba#15306).
  + Reduce flapping of ridalloc test (Samba#15329).
  + large_ldap test is unreliable (Samba#15351).
  + New filename parser doesn't check veto files smb.conf parameter (Samba#15143).
  + mdssvc may crash when initializing (Samba#15354).
  + Large directory optimization broken for non-lcomp path elements (Samba#15313).
  + streams_depot fails to create streams (Samba#15357).
  + shadow_copy2 and streams_depot don't play well together (Samba#15358).
  + wbinfo -u fails on ad dc with >1000 users (Samba#15366).
  + winbindd idmap child contacts the domain controller without a
    need (Samba#15317).
  + idmap_autorid may fail to map sids of trusted domains for the first
    time (Samba#15318).
  + idmap_hash doesn't use ID_TYPE_BOTH for reverse mappings (Samba#15319).
  + net ads search -P doesn't work against servers in other domains (Samba#15323).
  + DS ACEs might be inherited to unrelated object classes (Samba#15338).
  + Temporary smbXsrv_tcon_global.tdb can't be parsed (Samba#15353).
  + Setting veto files = /.*/ break listing directories (Samba#15360).
  + CVE-2020-25720 [SECURITY] Create Child permission should not
    allow full write to all attributes (additional changes) (Samba#14810).
  + Reduce flapping of ridalloc test (Samba#15329).
  + dsgetdcname: assumes local system uses IPv4 (Samba#15325).

* Wed Mar 29 2023 Evgeny Sinelnikov <sin@altlinux.org> 4.17.7-alt1
- Update to maintenance release of Samba 4.17 with update libldb to 2.6.2:
  + ldb wildcard matching makes excessive allocations (Samba#15331).

- Security fixes (Samba#15276, Samba#15270, Samba#15315, Samba#14810):
  + CVE-2023-0225: An incomplete access check on dnsHostName allows authenticated
                   but otherwise unprivileged users to delete this attribute from
                   any object in the directory.
                   https://www.samba.org/samba/security/CVE-2023-0225.html

  + CVE-2023-0922: The Samba AD DC administration tool, when operating against a
                   remote LDAP server, will by default send new or reset
                   passwords over a signed-only connection.
                   https://www.samba.org/samba/security/CVE-2023-0922.html

  + CVE-2023-0614: The fix in 4.6.16, 4.7.9, 4.8.4 and 4.9.7 for CVE-2018-10919
                   Confidential attribute disclosure via LDAP filters was
                   insufficient and an attacker may be able to obtain
                   confidential BitLocker recovery keys from a Samba AD DC.
                   Installations with such secrets in their Samba AD should
                   assume they have been obtained and need replacing.
                   https://www.samba.org/samba/security/CVE-2023-0614.html

  + CVE-2020-25720 Create Child permission should not allow full write to all
                   attributes (additional changes).

* Wed Mar 15 2023 Evgeny Sinelnikov <sin@altlinux.org> 4.17.6-alt1
- Update to maintenance release of Samba 4.17:
  + streams_xattr is creating unexpected locks on folders (Samba#15314).
  + Use of the Azure AD Connect cloud sync tool is now supported for password
    hash synchronisation, allowing Samba AD Domains to synchronise passwords
    with this popular cloud environment (Samba#10635).
  + New samba-dcerpc architecture does not scale gracefully (Samba#15310).
  + vfs_ceph incorrectly uses fsp_get_io_fd() instead of fsp_get_pathref_fd()
    in close and fstat (Samba#15307).
  + fd_load() function implicitly closes the fd where it should not (Samba#15311).
- Revert not treat of missing include file as an error in handle_include().
  This behavior differs between the source3 and source4 parts of Samba.
  So, it should be the same and just not an error (Closes #44214).

* Sat Mar 11 2023 Michael Shigorin <mike@altlinux.org> 4.17.5-alt2
- Fix doc knob

* Tue Feb 28 2023 Evgeny Sinelnikov <sin@altlinux.org> 4.17.5-alt1
- Update to stable release of Samba 4.17 with latest bugfixes and new features:
  + Support Protected Users security group introduced in Windows Server 2012 R2.
  + Resource Based Constrained Delegation (RBCD) support with samba-dc-mitkrb5.
  + Customizable DNS listening port to use another DNS server as a front and
    forward to Samba.
  + Operation without the (unsalted) NT password hash security support.
  + Suppport for modern Python API for smbconf.
  + JSON support for smbstatus.
  + LanMan Authentication and password storage removed from the AD DC.
- Configure without the SMB1 Server not enabled yet.

* Mon Feb 20 2023 Evgeny Sinelnikov <sin@altlinux.org> 4.16.9-alt1
- Update to maintenance release of Samba 4.16
- Security fixes:
  + CVE-2022-38023: Samba should refuse RC4 (aka md5) based SChannel on
    NETLOGON (Samba#15240).
- Major fixes:
  + smbc_getxattr() return value is incorrect (Samba#14808).
  + samba-tool gpo listall fails IPv6 only - finddcs() fails to find DC when
    there is only an AAAA record for the DC in DNS (Samba#15226).
  + smbd crashes if an FSCTL request is done on a stream handle (Samba#15236).
  + auth3_generate_session_info_pac leaks wbcAuthUserInfo (Samba#15286).
  + Leak in wbcCtxPingDc2 (Samba#15164).
  + irpc_destructor may crash during shutdown (Samba#15280).
- Share enumeration (netshareenum) fixes:
  + %U for include directive doesn't work for share listing (Samba#15243).
  + Shares missing from netshareenum response in samba 4.17.4 (Samba#15266).
  + Access based share enum does not work in Samba 4.16+ (Samba#15265).
  + Crash during share enumeration (Samba#15267).

* Mon Dec 15 2022 Evgeny Sinelnikov <sin@altlinux.org> 4.16.8-alt1
- Update to maintenance release of Samba 4.16 with fixes of the Samba CVE for
  the Windows Kerberos Elevation of Privilege Vulnerability disclosed by
  Microsoft on Nov 8 2022 (CVE-2022-37967, CVE-2022-37966).
- Security fixes:
  + CVE-2022-37966: A Samba Active Directory DC will issue weak rc4-hmac
                    session keys for use between modern clients and servers
                    despite all modern Kerberos implementations supporting
                    the aes256-cts-hmac-sha1-96 cipher.
                    On Samba Active Directory DCs and members
                    'kerberos encryption types = legacy' would force
                    rc4-hmac as a client even if the server supports
                    aes128-cts-hmac-sha1-96 and/or aes256-cts-hmac-sha1-96
                    (Samba#13135, Samba#15219, Samba#15237).
                     https://www.samba.org/samba/security/CVE-2022-37966.html

  + CVE-2022-37967: A service account with the special constrained
                    delegation permission could forge a more powerful
                    ticket than the one it was presented with (Samba#15231).
                     https://www.samba.org/samba/security/CVE-2022-37967.html

  + CVE-2022-38023: The "RC4" protection of the NetLogon Secure channel uses the
                    same algorithms as rc4-hmac cryptography in Kerberos,
                    and so must also be assumed to be weak (Samba#15240).
                     https://www.samba.org/samba/security/CVE-2022-38023.html

* Mon Dec 12 2022 Evgeny Sinelnikov <sin@altlinux.org> 4.16.7-alt5
- Update text of summary for role-usershares and smb-conf-usershares.
- Update default usershare prefix allow and deny lists:
  + usershare prefix deny list = /etc /dev /sys /proc
  + usershare prefix allow list = /home /srv /mnt /media /var
- Add new controls for samba-usershares:
  + smb-conf-usershare-allow-list
  + smb-conf-usershare-deny-list
  + smb-conf-usershare-owner-only
  + smb-conf-usershare-allow-guests

* Thu Dec 08 2022 Evgeny Sinelnikov <sin@altlinux.org> 4.16.7-alt4
- Add role-sambashare control for compatibility during upgrade from previous
  manual managed settings of usershares.
- Trigger sambashare as role with privilege usershares (Closes: #44379).

* Sat Dec 03 2022 Evgeny Sinelnikov <sin@altlinux.org> 4.16.7-alt3
- Avoid cycle dependencies on common service files.
- Fix cycle dependencies on libRPC and libREG samba4 libraries.

* Tue Nov 29 2022 Evgeny Sinelnikov <sin@altlinux.org> 4.16.7-alt2
- Add role-usershares control allow or disallow for group users using of
  samba usershares as privilege.
- Add compatibility support for sambashare group as common privilege assigned
  to usershares group (Closes: #44379).

* Tue Nov 22 2022 Evgeny Sinelnikov <sin@altlinux.org> 4.16.7-alt1
- Update to maintenance release of Samba 4.16 (Samba#15203)
- Security fixes:
  + CVE-2022-42898: Samba's Kerberos libraries and AD DC failed to guard against
                    integer overflows when parsing a PAC on a 32-bit system, which
                    allowed an attacker with a forged PAC to corrupt the heap.
                    https://www.samba.org/samba/security/CVE-2022-42898.html
    Workaround and mitigations:
    * No workaround on 32-bit systems as an AD DC
    * file servers are only impacted if in a non-AD domain
    * 64-bit systems are not exploitable

* Mon Nov 07 2022 Evgeny Sinelnikov <sin@altlinux.org> 4.16.6-alt2
- Don't treat a missing include file as an error in handle_include().
  This behavior differs between the source3 and source4 parts of Samba.
  So, it should be the same and just not an error (Closes #44214).

* Thu Oct 27 2022 Evgeny Sinelnikov <sin@altlinux.org> 4.16.6-alt1
- Update to maintenance release of Samba 4.16 (Samba#15134)
- Security fixes:
  + CVE-2022-3437: There is a limited write heap buffer overflow in the GSSAPI
                   unwrap_des() and unwrap_des3() routines of Heimdal (included
                   in Samba).
                   https://www.samba.org/samba/security/CVE-2022-3437.html
- Add samba-usershares package for support for non-root user shares.
- Default smb.conf simplified - homes, printers and print$ shares enabled by
  default. Original large default example smb.conf replaced to smb.conf.example.

* Mon Sep 12 2022 Evgeny Sinelnikov <sin@altlinux.org> 4.16.5-alt1
- Update to latest stable release of Samba 4.16
- Major fixes:
  + Possible use after free of connection_struct when iterating
    smbd_server_connection->connections (Samba#15128).
  + Spotlight RPC service returns wrong response when Spotlight is
    disabled on a share (Samba#15086).
  + acl_xattr VFS module may unintentionally use filesystem
    permissions instead of ACL from xattr (Samba#15126).
  + Missing SMB2-GETINFO access checks from MS-SMB2 3.3.5.20.1.
    assert failed: !is_named_stream(smb_fname)") at
    ../../lib/util/fault.c:197 (Samba#15153).
  + Missing READ_LEASE break could cause data corruption (Samba#15148).
  + rpcclient can crash using setuserinfo(2) (Samba#15124).
  + Samba fails to build with glibc 2.36 caused by including
    <sys/mount.h> in libreplace (Samba#15132).
  + SMB1 negotiation can fail to handle connection errors (Samba#15152).
  + samba-tool domain join segfault when joining a samba ad domain (Samba#15078).

* Thu Sep 08 2022 Evgeny Sinelnikov <sin@altlinux.org> 4.16.4-alt2
- Add support (Heimdal only) of "ignore requester sid" global option for the
  correct operation of trust relationships with oldest versions of MS AD without
  KB5008380 Authentication updates (CVE-2021-42287).

* Sun Jul 31 2022 Evgeny Sinelnikov <sin@altlinux.org> 4.16.4-alt1
- Update to latest stable release of Samba 4.16
- Major fixes:
  + New samba-dcerpcd binary to provide DCERPC in the member server setup.
  + Heimdal-8.0pre used for Samba Internal Kerberos, adds FAST support.
  + Certificate Auto Enrollment support with internal group policy mechanism.
  + Ability to add ports to dns forwarder addresses in internal DNS backend.
  + Older SMB1 protocol SMBCopy command removed.
  + SMB1 server-side wildcard expansion removed.
  + SMB1 protocol has been deprecated, particularly older dialects.
  + No longer using Linux mandatory locks for sharemodes.

* Sun Jul 31 2022 Evgeny Sinelnikov <sin@altlinux.org> 4.15.9-alt1
- Update to security release of Samba 4.15
- Security fixes:
  + CVE-2022-2031:  Samba AD users can bypass certain restrictions associated
                    with changing passwords (Samba#15047).
  + CVE-2022-32744: Samba AD users can forge password change requests for any
                    user (Samba#15074).
  + CVE-2022-32745: Samba AD users can crash the server process with an LDAP add
                    or modify request (Samba#15008).
  + CVE-2022-32746: Samba AD users can induce a use-after-free in the server
                    process with an LDAP add or modify request (Samba#15009).
  + CVE-2022-32742: Server memory information leak via SMB1 (Samba#15085).

* Mon Jun 27 2022 Evgeny Sinelnikov <sin@altlinux.org> 4.15.8-alt1
- Update to maintenance release of Samba 4.15 with latest bugfixes:
  + Setting fruit:resource = stream in vfs_fruit causes a panic (Samba#15099).
  + Fix logging dsdb audit to specific files (Samba#15076).
  + Fix vfs_gpfs with vfs_shadowcopy2 fail to restore file if original file had
    been deleted (Samba#15069).
  + Remove netgroups support (Samba#15087).
  + Fix smbclient commands del & deltree fail with
    NT_STATUS_OBJECT_PATH_NOT_FOUND with DFS (Samba#15100).
  + Fix out-by-4 error in smbd read reply max_send clamp (Samba#14443).
  + s3:libads: Check if we have a valid sockaddr (Samba#15106).
  + smbd: Make non_widelink_open() robust for non-cwd dirfsp (Samba#15105).

* Mon Jun 27 2022 Evgeny Sinelnikov <sin@altlinux.org> 4.15.7-alt4
- Add samba-krb5-printing with CUPS backend for printing with Kerberos support.
- Fix samba-tool domain backup DC with forced local samdb.

* Mon Jun 20 2022 Evgeny Sinelnikov <sin@altlinux.org> 4.15.7-alt3
- samba-dc: Replace internal helper program performing asynchronous
  printing-related jobs (samba-bgqd) to internal package directory.

* Sun Jun 19 2022 Evgeny Sinelnikov <sin@altlinux.org> 4.15.7-alt2
- Revert get_naming_master() for dc replica join, which requires due only domain
  naming master can create application directory partitions.
- Fix smbd doesn't handle UPNs for looking up names (Samba#15054).
- Fix net ads info shows LDAP Server: 0.0.0.0 (Samba#14674).
- Fix logging dsdb audit to specific files does not work (Samba#15076).
- Fix use pathref fd instead of io fd in vfs_default_durable_cookie (Samba#15042).
- Fix vfs_gpfs recalls=no option prevents listing files (Samba#15055).
- Fix smbget manpage (no &stdarg.encrypt anymore).

* Mon Jun 06 2022 Evgeny Sinelnikov <sin@altlinux.org> 4.15.7-alt1
- Update to release of Samba 4.15 with SMB multi-channel, Offline Domain Join,
  samba-tool dns zoneoptions for aging control, samba-tool domain backup offline
  with the LMDB backend and always use enterprise principals for Kerberos (so
  that the DC will be able to redirect ticket requests to the right DC) support.

* Tue Apr 05 2022 Evgeny Sinelnikov <sin@altlinux.org> 4.14.13-alt1
- Update to latest bugfix release of Samba 4.14
- Fixes:
  + Renaming file on DFS root fails with NT_STATUS_OBJECT_PATH_NOT_FOUND.
  + Samba does not response STATUS_INVALID_PARAMETER when opening 2 objects with
    same lease key.
  + NT error code is not set when overwriting a file during rename in libsmbclient.
  + net ads info shows LDAP Server: 0.0.0.0 depending on contacted server.
  + wbinfo -a doesn't work reliable with upn names.
  + Problem when winbind renews Kerberos.
  + NT_STATUS_ACCESS_DENIED translates into EPERM instead of EACCES in
    SMBC_server_internal.
  + Multpile RODC fixes:
    - Simple bind doesn't work against an RODC (with non-preloaded users).
    - Crash of winbind on RODC.
    - Uncached logon on RODC always fails once.
    - Changing the machine password against an RODC likely destroys the domain join.
    - Simple bind doesn't work against an RODC (with non-preloaded users).
  + Avoid mixing the main krbtgt account keys with an RODC if the
    msDS-KeyVersionNumber is larger than 65535 (set 16 upper bits to zero).
  + Use Heimdal 8.0 (pre) rather than an earlier snapshot.
  + LDAP simple binds should honour "old password allowed period".
  + Fix ldap simple bind with TLS auditing.
  + "password hash userPassword schemes = CryptSHA256" does not seem to work
    with samba-tool.

* Thu Mar 03 2022 Evgeny Sinelnikov <sin@altlinux.org> 4.14.12-alt2
- Fix linking of some libraries (libsmbldap.so.2.1.0, libpopt-samba3-samba4.so,
  libsamba-modules-samba4.so, winbind_krb5_locator.so and smbpasswd.so):
  + find-requires: ERROR: /usr/lib/rpm/lib.req failed.

* Tue Feb 09 2022 Evgeny Sinelnikov <sin@altlinux.org> 4.14.12-alt1
- Update to latest security release of Samba 4.14
- Security fixes:
  + CVE-2021-44142: Out-of-Bound Read/Write on Samba vfs_fruit module.
  + CVE-2022-0336:  Re-adding an SPN skips subsequent SPN conflict checks.

* Thu Jan 27 2022 Evgeny Sinelnikov <sin@altlinux.org> 4.14.11-alt3
- Update for the latest fixes release of Samba 4.14
  + Fix resolv_wrapper with glibc 2.34
  + kill_tcp_connections does not work
  + Failed to parse NTLMv2_RESPONSE length 95 - Buffer Size Error -
    NT_STATUS_BUFFER_TOO_SMALL
  + Can't connect to Windows shares not requiring authentication using KDE/Gnome
  + Duplicate SMB file_ids leading to Windows client cache poisoning
  + Missing pop_sec_ctx() in error path inside close_directory()
  + rpc_server/netlogon: let CSDVersion="" wipe operatingSystemServicePack

* Sun Jan 16 2022 Evgeny Sinelnikov <sin@altlinux.org> 4.14.11-alt2
- Apply s4u support patch for samba-4.15 (due already updated kdb code base):
  + basic local realm S4U support
  + enable S4U client support for MIT build
  + wip: for canonicalization with new MIT kdc code

* Wed Dec 15 2021 Evgeny Sinelnikov <sin@altlinux.org> 4.14.11-alt1
- Update to latest maintenance release of Samba 4.14.
- Fix broken of recursive directory delete with veto files.
- Fix directory containing dangling symlinks cannot be deleted by
  SMB2 alone when they are the only entry in the directory.

* Mon Dec 13 2021 Evgeny Sinelnikov <sin@altlinux.org> 4.14.10-alt3
- Update for the latest fixes release of Samba 4.14
  + CVE-2020-25727 idmap_nss, krb5 and s3-auth regressions
  + CVE-2021-3670 ldap_server, dsdb/anr and ldb (libldb-2.3.2-alt2) regressions
  + smbd: s3-dsgetdcname: handle num_ips == 0
  + dsdb: Use DSDB_SEARCH_SHOW_EXTENDED_DN when searching for the local replicated object
  + lib: handle NTTIME_THAW in nt_time_to_full_timespec()
  + IPA DC: add missing checks
  + s3:winbindd: fix "allow trusted domains = no" regression
- Update tob more compatible with ALT distributions:
  + loadparm: Set parameter "min domain uid" deafult value to 500.

* Sat Nov 13 2021 Evgeny Sinelnikov <sin@altlinux.org> 4.14.10-alt2
- Add support samba-tool-plus alternative for samba-dc build with heimdal.

* Sun Nov 07 2021 Evgeny Sinelnikov <sin@altlinux.org> 4.14.10-alt1
- Update to latest security release of Samba 4.14
- Security fixes:
  + CVE-2016-2124:  SMB1 client connections can be downgraded to plaintext
                    authentication.
                    https://www.samba.org/samba/security/CVE-2016-2124.html
  + CVE-2020-25717: A user on the domain can become root on domain members.
                    https://www.samba.org/samba/security/CVE-2020-25717.html
  + CVE-2020-25718: Samba AD DC did not correctly sandbox Kerberos tickets
                    issued by an RODC.
                    https://www.samba.org/samba/security/CVE-2020-25718.html
  + CVE-2020-25719: Samba AD DC did not always rely on the SID and PAC in
                    Kerberos tickets.
                    https://www.samba.org/samba/security/CVE-2020-25719.html
  + CVE-2020-25721: Kerberos acceptors need easy access to stable AD identifiers
                    (eg objectSid).
                    https://www.samba.org/samba/security/CVE-2020-25721.html
  + CVE-2020-25722: Samba AD DC did not do suffienct access and conformance
                    checking of data stored.
                    https://www.samba.org/samba/security/CVE-2020-25722.html
  + CVE-2021-3738:  Use after free in Samba AD DC RPC server.
                    https://www.samba.org/samba/security/CVE-2021-3738.html
  + CVE-2021-23192: Subsequent DCE/RPC fragment injection vulnerability.
                    https://www.samba.org/samba/security/CVE-2021-23192.html

* Sun Nov 07 2021 Evgeny Sinelnikov <sin@altlinux.org> 4.14.9-alt2
- Rebuild with updated ldb-2.3.2 with backported all C code changes from
  ldb-2.4.1 to be available for Samba 4.14.x.

* Mon Nov 01 2021 Evgeny Sinelnikov <sin@altlinux.org> 4.14.9-alt1
- Update to latest security release of Samba 4.14
- Backport bronze bit fixes, tests, and selftest improvements. Provide a fix
  for MS in Samba [SECURITY] 'Bronze bit' S4U2Proxy Constrained Delegation
  bypass in Samba with embedded Heimdal (Fixes: CVE-2020-17049).

* Wed Oct 06 2021 Evgeny Sinelnikov <sin@altlinux.org> 4.14.8-alt1
- Update to latest security release of Samba 4.14
- Fix performance regressions in lsa_LookupSids3/LookupNames4 since Samba 4.9 by
  using an explicit database handle cache and address a signifcant in database
  access in the AD DC since Samba 4.12.
- Fix an unuthenticated user can crash the AD DC KDC by omitting the server name
  in a TGS-REQ (Fixes: CVE-2021-3671).

* Tue Oct 05 2021 Evgeny Sinelnikov <sin@altlinux.org> 4.14.7-alt5
- Add pythonarchdir repplacement due compatibility with alt security
  python trust mode (enabled if /etc/alt/security/python-trust exists).

* Mon Sep 20 2021 Ivan A. Melnikov <iv@altlinux.org> 4.14.7-alt4
- Use parallel make install.
- Make building and installing more verbose.
- Explicitly list architectures where ceph is enabled
  (fixes build on riscv64).

* Wed Sep 01 2021 Evgeny Sinelnikov <sin@altlinux.org> 4.14.7-alt3
- Fix net ads join segmentation fault problem if ldap SRV host record not found.

* Tue Aug 31 2021 Evgeny Sinelnikov <sin@altlinux.org> 4.14.7-alt2
- Add dependency lmdb-utils to samba-dc-common due it is necessary
  for mdb store backend permits database sizes greater than 4Gb

* Tue Aug 24 2021 Evgeny Sinelnikov <sin@altlinux.org> 4.14.7-alt1
- Update to latest release of Samba 4.14 with smbd fixes

* Mon Jul 19 2021 Evgeny Sinelnikov <sin@altlinux.org> 4.14.6-alt1
- Update to latest release of Samba 4.14 with smbd and samba-tool fixes

* Fri Jun 04 2021 Evgeny Sinelnikov <sin@altlinux.org> 4.14.5-alt1
- Update to latest release of Samba 4.14 with ensure POSIX default ACL
  is mapped into returned Windows ACL for directory handles and fix
  uninitialized memory read in process_symlink_open() when used with
  vfs_shadow_copy2() for smbd.

* Mon May 17 2021 Evgeny Sinelnikov <sin@altlinux.org> 4.14.4-alt4
- winbindd: Fix a startup race with allocate_gid (Samba#14678)

* Fri May 14 2021 Evgeny Sinelnikov <sin@altlinux.org> 4.14.4-alt3
- Update with latest fixes (Samba#14695, Samba#14696)

* Fri May 14 2021 Michael Shigorin <mike@altlinux.org> 4.14.4-alt2.1
- Fix doc knob

* Thu May 06 2021 Evgeny Sinelnikov <sin@altlinux.org> 4.14.4-alt2
- Fix backward compatibility to fixed version of libldb with CVE-2021-20254.
- Replace auth and vfs libraries from samba-libs to samba-dc-libs and samba packages.
- Build without separated libnetapi private library.

* Fri Apr 30 2021 Evgeny Sinelnikov <sin@altlinux.org> 4.14.4-alt1
- Fix buffer overrun in sids_to_unixids() (Fixes: CVE-2021-20254)
- Final migration to /run directory (Closes: 35891, 36652, 39992)
- Avoid build problems on e2k

* Mon Apr 12 2021 Evgeny Sinelnikov <sin@altlinux.org> 4.14.2-alt3
- Multiple build fixes:
  + Revert to use macros for e2k (due ALT#36315 was fixed).
  + Add samba-common-client subpackage with smb.conf and its staff only.
  + Add dumpmscat utility with libtasn1-devel and libtasn1-utils buildrequires.
  + Replace mdfind and mvxattr to samba-client from samba-common-tools.
  + Support pdbedit in separate heimdal server build.
  + Add /usr/include/samba-4.0 directory to devel packages.
  + Shift shared libraries between samba-libs and samba-common-libs to avoid
    cyclical dependencies.

* Sun Apr 11 2021 Evgeny Sinelnikov <sin@altlinux.org> 4.14.2-alt2
- Add separate admx-samba subpackage with Samba ADMX policy templates.
- Replace ADMX policy templates to common PolicyDefinitions directory.
- Set buildarch of samba-common and samba-dc-common to noarch.

* Thu Mar 25 2021 Evgeny Sinelnikov <sin@altlinux.org> 4.14.2-alt1
- Update to latest stable security release of the Samba 4.14
- Security fixes:
  + CVE-2020-27840: Heap corruption via crafted DN strings
  + CVE-2021-20277: Out of bounds read in AD DC LDAP server

* Mon Mar 22 2021 Evgeny Sinelikov <sin@altlinux.org> 4.14.0-alt1
- Update to release of Samba 4.14 with client Group Policy support

* Sat Mar 13 2021 Evgeny Sinelikov <sin@altlinux.org> 4.13.5-alt1
- Update to latest release of Samba 4.13

* Mon Feb 08 2021 Evgeny Sinelikov <sin@altlinux.org> 4.13.4-alt1
- Update to latest release of Samba 4.13:
  + Insecure wide links functionality has been moved into a separate VFS module;
  + NT4-like 'classic' Samba domain controller mode and SMBv1 only protocol
    options has been deprecated.
- Add snapper VFS module in separate samba-vfs-snapper package due it requires DBus.
- Add samba group policy ADMX files to samba-dc-common package.
- Add elasticsearch backend mappings json file for Metadata Search Service (mdssvc)
  to samba-common package.

* Mon Jan 18 2021 Evgeny Sinelikov <sin@altlinux.org> 4.12.11-alt1
- Update to latest release of Samba 4.12

* Thu Nov 19 2020 Evgeny Sinelikov <sin@altlinux.org> 4.12.10-alt2
- Spotlight searches against an SMB server mdfind utility in samba-common-tools
  conflicts with gnustep-gworkspace due it also includes mdfind (closes: 39295)

* Thu Nov 12 2020 Evgeny Sinelikov <sin@altlinux.org> 4.12.10-alt1
- Update to latest release of Samba 4.12

* Thu Oct 29 2020 Evgeny Sinelikov <sin@altlinux.org> 4.12.9-alt1
- Update to latest stable security release of the Samba 4.12
- Security fixes:
  + CVE-2020-14318: Missing handle permissions check in SMB1/2/3 ChangeNotify
  + CVE-2020-14323: Unprivileged user can crash winbind
  + CVE-2020-14383: An authenticated user can crash the DCE/RPC DNS with easily crafted records

* Thu Oct 08 2020 Evgeny Sinelikov <sin@altlinux.org> 4.12.8-alt1
- Update to newest release of Samba 4.12

* Thu Oct 08 2020 Evgeny Sinelikov <sin@altlinux.org> 4.11.14-alt1
- Update to latest stable security release of the Samba 4.11

* Sat Sep 19 2020 Evgeny Sinelikov <sin@altlinux.org> 4.11.13-alt1
- Update to latest stable security release of the Samba 4.11
- Security fixes:
  + CVE-2020-1472: Unauthenticated domain takeover via netlogon ("ZeroLogon")
    https://www.samba.org/samba/security/CVE-2020-1472.html

* Wed Aug 26 2020 Evgeny Sinelikov <sin@altlinux.org> 4.11.12-alt1
- Update to latest stable security release of the Samba 4.11

* Sun Aug 02 2020 Evgeny Sinelikov <sin@altlinux.org> 4.11.11-alt2
- Update to latest fixes from testing
- Remove derecated libwbclient install as alternative with libwbclient-sssd
- Fix pygpo double memory free stackframe in py_ads_get_gpo_list()

* Tue Jul 07 2020 Evgeny Sinelikov <sin@altlinux.org> 4.11.11-alt1
- Update to latest stable security release of the Samba 4.11
- Security fixes:
  + CVE-2020-10730: NULL pointer de-reference and use-after-free in Samba AD DC
                    LDAP Server with ASQ, VLV and paged_results
  + CVE-2020-10745: Parsing and packing of NBT and DNS packets can consume excessive CPU
  + CVE-2020-10760: LDAP Use-after-free in Samba AD DC Global Catalog with paged_results and VLV
  + CVE-2020-14303: Empty UDP packet DoS in Samba AD DC nbtd

* Tue Jun 30 2020 Evgeny Sinelikov <sin@altlinux.org> 4.11.10-alt1
- Update to latest stable bugfix release of the Samba 4.11
- Build with ldb 2.0.11, LMDB databases can grow without bounds.
- Fix glusterfs build requires (Closes: 38038)

* Wed May 27 2020 Evgeny Sinelikov <sin@altlinux.org> 4.11.9-alt2
- Apply patches from fedora:
  + Add use the new des_crypt56_gnutls() and remove builtin DES crypto
  + Remove DES support if MIT Kerberos version does not support it
  + Create working private krb5.conf due it used by DNS update tool and should
    have enough details to authenticate with GSS-TSIG when running nsupdate

* Wed May 27 2020 Evgeny Sinelikov <sin@altlinux.org> 4.11.9-alt1
- Update to latest stable bugfix release of the Samba 4.11

* Tue Apr 28 2020 Evgeny Sinelikov <sin@altlinux.org> 4.11.8-alt1
- Update to latest stable security release of the Samba 4.11
- Security fixes:
  + CVE-2020-10700: Fix use-after-free in AD DC LDAP server when ASQ and paged_results combined
  + CVE-2020-10704: Fix LDAP Denial of Service (stack overflow) in Samba AD DC

* Tue Mar 10 2020 Evgeny Sinelikov <sin@altlinux.org> 4.11.7-alt1
- Update to latest spring release of Samba 4.11
- Fix search with scope ONE and small result sets with ldb-2.0.9

* Thu Feb 06 2020 Evgeny Sinelikov <sin@altlinux.org> 4.11.6-alt1
- Update to newest release of Samba 4.11

* Fri Jan 24 2020 Evgeny Sinelikov <sin@altlinux.org> 4.10.13-alt1
- Update to latest stable release of the Samba 4.10
- Security fixes:
  + CVE-2019-14902: Replication of ACLs set to inherit down a subtree on AD Directory not automatic
  + CVE-2019-14907: Crash after failed character conversion at log level 3 or above
  + CVE-2019-19344: Use after free during DNS zone scavenging in Samba AD DC

* Thu Jan 23 2020 Grigory Ustinov <grenka@altlinux.org> 4.10.11-alt2
- Build without python2 support
- Get rid of ubt macros

* Fri Dec 13 2019 Evgeny Sinelikov <sin@altlinux.org> 4.10.11-alt1
- Update to last security winter release
- Security fixes:
  + CVE-2019-14861: Samba AD DC zone-named record Denial of Service in DNS management server
  + CVE-2019-14870: DelegationNotAllowed not being enforced in protocol transition on Samba AD DC

* Tue Oct 29 2019 Evgeny Sinelikov <sin@altlinux.org> 4.10.10-alt1
- Update to second security autumn release
- Security fixes:
  + CVE-2019-10218 Client code can return filenames containing path separators
  + CVE-2019-14833 Samba AD DC check password script does not receive the full password
  + CVE-2019-14847 User with "get changes" permission can crash AD DC LDAP server via dirsync

* Sat Oct 19 2019 Evgeny Sinelikov <sin@altlinux.org> 4.10.9-alt1
- Update to latest autumn release

* Tue Sep 11 2019 Evgeny Sinelikov <sin@altlinux.org> 4.10.8-alt2
- Add requires samba-dc-mitkrb5 for samba
- Use krb5.conf from the Samba private directory in MIT KDC service

* Tue Sep 03 2019 Evgeny Sinelikov <sin@altlinux.org> 4.10.8-alt1
- Update to first security autumn release
- Fix samba-gpupdate check sysvol path with ignore case for compatibility
- Security fixes:
  + CVE-2019-10197 Permissions check deny can allow user to escape from the share

* Thu Aug 22 2019 Evgeny Sinelikov <sin@altlinux.org> 4.10.7-alt1
- Update to final summer release with fixed joining a Windows pre-2008R2 DC
- Fix lookup requests from AD DCs over LSA RPC to FreeIPA domain controller

* Wed Aug 14 2019 Evgeny Sinelikov <sin@altlinux.org> 4.10.6-alt2
- Change lstat to stat check in directory_create_or_exist for compatibility
  with oldstyle /var/run due it symlink in modern linux installations

* Mon Aug 12 2019 Evgeny Sinelikov <sin@altlinux.org> 4.10.6-alt1
- Update to latest summer release

* Wed Jul 31 2019 Evgeny Sinelikov <sin@altlinux.org> 4.10.5-alt1
- Update to latest security release
- Security fixes:
  + CVE-2019-12435 Samba AD DC Denial of Service in DNS management server (dnsserver)
  + CVE-2019-12436 Samba AD DC LDAP server crash (paged searches)

* Fri Jul 19 2019 Evgeny Sinelikov <sin@altlinux.org> 4.10.3-alt5
- Partial fixes for SMBLoris vulnerability on smbd
  + Add smbd read timeout parameter
  + Set max smbd processes to 768

* Thu Jul 04 2019 Evgeny Sinelikov <sin@altlinux.org> 4.10.3-alt4
- Remove conflict to libwbclient-sssd due problem that apt install
  it for with gssntlmssp-debuginfo (Closes: 36750)
- New metapackage task-samba-dc-mitkrb5 to install complete Domain Controller
  with MIT Kerberos server and libraries

* Mon Jun 14 2019 Evgeny Sinelikov <sin@altlinux.org> 4.10.3-alt3
- Add requires samba-common-tools for samba-common

* Mon May 27 2019 Evgeny Sinelikov <sin@altlinux.org> 4.10.3-alt2
- Build with MIT and Heimdal separately
- Fix upgrade of latest samba-4.9 builds from branches

* Mon May 27 2019 Evgeny Sinelikov <sin@altlinux.org> 4.10.3-alt1
- Update to latest security release
- Security fixes:
  + CVE-2018-16860 Samba AD DC S4U2Self/S4U2Proxy unkeyed checksum

* Mon May 27 2019 Evgeny Sinelikov <sin@altlinux.org> 4.10.2-alt2
- Initial support build with MIT and Heimdal separately:
  + Replace common DC and Winbind common files to separate subpackages
  + Add samba-vfs-cephfs and samba-vfs-glusterfs subpackages

* Thu Apr 11 2019 Evgeny Sinelikov <sin@altlinux.org> 4.10.2-alt1
- Update to spring security release
- Security fixes:
  + CVE-2019-3870 World writable files in Samba AD DC private/ dir
  + CVE-2019-3880 Save registry file outside share as unprivileged user

* Tue Apr 09 2019 Evgeny Sinelikov <sin@altlinux.org> 4.10.1-alt1
- Update to second release of Samba 4.10

* Wed Mar 20 2019 Evgeny Sinelikov <sin@altlinux.org> 4.10.0-alt1
- Update to first release of Samba 4.10

* Tue Mar 19 2019 Evgeny Sinelikov <sin@altlinux.org> 4.9.5-alt2
- Fix build compatibility for newest architectures with not exists
  macroses on stable branches

* Fri Mar 15 2019 Evgeny Sinelikov <sin@altlinux.org> 4.9.5-alt1
- Update to latest release with security ldb fixes (CVE-2019-3824)
- Prepare to replace runtime files from /var/run to /run directory

* Sat Feb 23 2019 Alexey Shabalin <shaba@altlinux.org> 4.9.4-alt4
- disable support ceph on 32-bit arch

* Mon Jan 28 2019 Evgeny Sinelikov <sin@altlinux.org> 4.9.4-alt3
- Merge samba and samba-DC packages into single package
- Rename samba-DC to samba-dc for compatibilty

* Tue Jan 02 2019 Evgeny Sinelikov <sin@altlinux.org> 4.9.4-alt2
- Merge and rebuild for e2k
- Change group access for private directory due effective mask with acl

* Thu Dec 20 2018 Evgeny Sinelnikov <sin@altlinux.org> 4.9.4-alt1
- Update to first winter security release
- Security fixes regressions:
  + CVE-2018-16853 Do not segfault if client is not set
  + CVE-2018-14629 Fix CNAME loop prevention using counter regression

* Wed Nov 28 2018 Evgeny Sinelnikov <sin@altlinux.org> 4.9.3-alt1
- Update to autumn security release
- Revert Samba DC to build with internal Heimdal Kerberos implementation
- Clean test module of third_party/iso8601 and subunit modules
- Security fixes:
  + CVE-2018-14629 Unprivileged adding of CNAME record causing loop in AD Internal DNS server
  + CVE-2018-16841 Double-free in Samba AD DC KDC with PKINIT
  + CVE-2018-16851 NULL pointer de-reference in Samba AD DC LDAP server
  + CVE-2018-16852 NULL pointer de-reference in Samba AD DC DNS servers
  + CVE-2018-16853 Samba AD DC S4U2Self crash in experimental MIT Kerberos configuration (unsupported)
  + CVE-2018-16857 Bad password count in AD DC not always effective

* Sat Oct 13 2018 Evgeny Sinelnikov <sin@altlinux.org> 4.9.1-alt1
- Rebuild latest release of Samba 4.9 without ubt macros

* Thu Oct 11 2018 Evgeny Sinelnikov <sin@altlinux.org> 4.8.6-alt1
- Update to latest autumn release
- Disable ubt macros due binary package identity change

* Tue Sep 25 2018 Evgeny Sinelnikov <sin@altlinux.org> 4.9.1-alt1.S1
- Update to second release of Samba 4.9

* Tue Sep 18 2018 Evgeny Sinelnikov <sin@altlinux.org> 4.9.0-alt1.S1
- Update to first release of Samba 4.9

* Fri Sep 14 2018 Alexey Sheplyakov <asheplyakov@altlinux.org> 4.8.5-alt2.S1
- Fixed the patch which allows joining to Windows based domain controllers

* Fri Aug 24 2018 Evgeny Sinelnikov <sin@altlinux.org> 4.8.5-alt1.S1
- Update to latest summer release

* Tue Aug 14 2018 Evgeny Sinelnikov <sin@altlinux.org> 4.8.4-alt1.S1
- Update to summer security release
- Security fixes:
  + CVE-2018-1139 Weak authentication protocol allowed
  + CVE-2018-1140 Denial of Service Attack on DNS and LDAP server
  + CVE-2018-10858 Insufficient input validation on client directory
    listing in libsmbclient
  + CVE-2018-10918 Denial of Service Attack on AD DC DRSUAPI server
  + CVE-2018-10919 Confidential attribute disclosure from the AD LDAP server
+ Build with subpackage for Python3

* Wed Jul 07 2018 Evgeny Sinelnikov <sin@altlinux.org> 4.8.3-alt2.S1
- Rebuild Samba DC with MIT Kerberos
- Fix join.py with automatically connect to domain naming master

* Wed Jul 04 2018 Evgeny Sinelnikov <sin@altlinux.org> 4.8.3-alt1.S1
- Update to new summer release of Samba 4.8

* Thu Jun 21 2018 Evgeny Sinelnikov <sin@altlinux.org> 4.7.8-alt1.S1
- Update to first summer release of Samba 4.7
- Fix doc knob: task-samba-dc should conditionally R: samba-DC-doc
- Rebuild for e2k with missing SYS_setgroups32
- Disable glusterfs and cephfs for e2k
- Disable cephfs support for mipsel

* Fri Jun 08 2018 Evgeny Sinelnikov <sin@altlinux.org> 4.7.7-alt2.S1
- Split samba-DC-common to separate samba-DC-common-tools
- Fix build against new python Sisyphus release with libnsl2

* Fri Apr 27 2018 Evgeny Sinelnikov <sin@altlinux.org> 4.8.1-alt1.S1
- Update to latest release of Samba 4.8

* Thu Apr 19 2018 Evgeny Sinelnikov <sin@altlinux.org> 4.7.7-alt1.S1
- Update to first spring release of Samba 4.7

* Fri Mar 23 2018 Evgeny Sinelnikov <sin@altlinux.org> 4.7.6-alt1.S1
- Update to latest winter release of Samba 4.7

* Thu Mar 15 2018 Evgeny Sinelnikov <sin@altlinux.org> 4.6.14-alt1.S1.1
- Rebuild security release (Fixes: CVE-2018-1050, CVE-2018-1057) with old
  ceph version without libceph-common for c7/c8

* Mon Mar 12 2018 Evgeny Sinelnikov <sin@altlinux.org> 4.6.14-alt1.S1
- Update to spring security release
- Security fixes:
  + CVE-2018-1050 Codenomicon crashes in spoolss server code
  + CVE-2018-1057 Unprivileged user can change any user (and admin) password

* Tue Feb 20 2018 Evgeny Sinelnikov <sin@altlinux.org> 4.6.13-alt1.S1
- Update to second winter release with common bugfixes

* Tue Jan 23 2018 Evgeny Sinelnikov <sin@altlinux.org> 4.6.12-alt2.S1
- Fix trouble with joined machine account moving when it already exists.
  Move it only if the admin specified an explicit OU (Samba bug #12696)

* Fri Jan 05 2018 Evgeny Sinelnikov <sin@altlinux.org> 4.7.4-alt1.S1
- Update to first winter release of Samba 4.7

* Thu Dec 21 2017 Evgeny Sinelnikov <sin@altlinux.org> 4.6.12-alt1.S1
- Update to first winter release with common bugfixes (closes: 33210)

* Thu Nov 23 2017 Evgeny Sinelnikov <sin@altlinux.org> 4.6.11-alt2.S1
- Backport from Heimdal upstream include/includedir directives for krb5.conf

* Tue Nov 21 2017 Evgeny Sinelnikov <sin@altlinux.org> 4.7.3-alt1.S1
- Update for second autumn security release of Samba 4.7

* Tue Nov 21 2017 Evgeny Sinelnikov <sin@altlinux.org> 4.6.11-alt1.S1
- Second autumn security release (Fixes: CVE-2017-14746, CVE-2017-15275)

* Fri Nov 17 2017 Evgeny Sinelnikov <sin@altlinux.org> 4.7.2-alt1.S1
- Update to third autumn release of Samba 4.7

* Thu Nov 16 2017 Evgeny Sinelnikov <sin@altlinux.org> 4.6.10-alt1.S1
- Update for third autumn release with common bugfixes

* Tue Nov 14 2017 Evgeny Sinelnikov <sin@altlinux.org> 4.7.1-alt1.S1
- Update for second autumn release with common bugfixes of Samba 4.7

* Wed Oct 25 2017 Evgeny Sinelnikov <sin@altlinux.org> 4.7.0-alt2.S1
- Fix KDC not works in configuration with trusted domain (samba bug #13078)

* Wed Oct 25 2017 Evgeny Sinelnikov <sin@altlinux.org> 4.6.9-alt1.S1
- Update for second autumn release with common bugfixes

* Thu Oct 12 2017 Evgeny Sinelnikov <sin@altlinux.org> 4.6.8-alt3.S1
- Fix KDC not works in configuration with trusted domain (samba bug #13078)

* Wed Sep 27 2017 Alexey Shabalin <shaba@altlinux.ru> 4.6.8-alt2.S1
- rebuild with new  libcephfs

* Fri Sep 22 2017 Evgeny Sinelnikov <sin@altlinux.ru> 4.7.0-alt1.S1
- Update to new autumn release of Samba 4.7
- Revert removed lpcfg_register_defaults_hook() for openchange

* Wed Sep 20 2017 Evgeny Sinelnikov <sin@altlinux.ru> 4.6.8-alt1.S1
- Update for autumn security release:
  + CVE-2017-12150 (SMB1/2/3 connections may not require signing where they
   should)
  + CVE-2017-12151 (SMB3 connections don't keep encryption across DFS redirects)
  + CVE-2017-12163 (Server memory information leak over SMB1)

* Wed Sep 20 2017 Evgeny Sinelnikov <sin@altlinux.ru> 4.6.7-alt3.S1
- Avoid build trouble with ubt macros id on branch c8

* Fri Aug 18 2017 Evgeny Sinelnikov <sin@altlinux.ru> 4.6.7-alt2.S1
- Clean code from old merged chunks

* Wed Aug 09 2017 Evgeny Sinelnikov <sin@altlinux.ru> 4.6.7-alt1.S1
- Update to second summer release

* Sat Jul 15 2017 Evgeny Sinelnikov <sin@altlinux.ru> 4.6.6-alt2.S1
- Rebuild with universal build tag (aka ubt macros) for p7 and c7

* Wed Jul 12 2017 Evgeny Sinelnikov <sin@altlinux.ru> 4.6.6-alt1.S1
- Update to summer security release
- Security fixes:
  + CVE-2017-11103 Orpheus' Lyre KDC-REP service name validation

* Tue Jun 20 2017 Evgeny Sinelnikov <sin@altlinux.ru> 4.6.5-alt2.S1
- Remove conflict samba-DC-libs with samba-libs
- Adjust python module requirement to samba-DC-common-libs
- Add conflict python-module-samba-DC with python-module-samba

* Tue Jun 06 2017 Evgeny Sinelnikov <sin@altlinux.ru> 4.6.5-alt1.S1
- Udpate to first summer release

* Mon Jun 05 2017 Evgeny Sinelnikov <sin@altlinux.ru> 4.6.4-alt2.S1
- Add libldb-modules-DC package with domain controller ldb modules for ldb-tools
- Add samba-DC-common-libs with libraries for common modules
- Append list of libraries consists in libwbclient-DC to not require
  samba-DC-common-libs

* Wed May 24 2017 Evgeny Sinelnikov <sin@altlinux.ru> 4.6.4-alt1.S1
- Update to second spring security release
- Fix longtime initialization bug in ldb proxy
- Security fixes:
  + CVE-2017-7494 Remote code execution from a writable share

* Tue Apr 25 2017 Evgeny Sinelnikov <sin@altlinux.ru> 4.6.3-alt1.S1
- Udpate to second spring release
- Remove conflict winbind with libwbclient-sssd due upgrade problems

* Wed Apr 12 2017 Evgeny Sinelnikov <sin@altlinux.ru> 4.6.2-alt2.S1
- Fix problem with failed to create kerberos keytab during join to domain

* Fri Mar 31 2017 Evgeny Sinelnikov <sin@altlinux.ru> 4.6.2-alt1.S1
- Update with regression fix of spring security release
- Revert winbind problem fixes with access user to keytab due troubles in 4.6.x

* Thu Mar 23 2017 Evgeny Sinelnikov <sin@altlinux.ru> 4.6.1-alt1.S1
- Update to spring security release
- Fixed build --without docs (closes: 33118)
- Security fixes:
  + CVE-2017-2619 Symlink race allows access outside share definition

* Tue Mar 07 2017 Evgeny Sinelnikov <sin@altlinux.ru> 4.6.0-alt1.S1
- Udpate to first spring release
- Revert removed unused DCERPC_FAULT_UNK_IF for openchange

* Wed Feb 01 2017 Evgeny Sinelnikov <sin@altlinux.ru> 4.5.5-alt1.S1
- Update to winter release
- Fix PAM winbind problem with access user to keytab

* Wed Dec 28 2016 Evgeny Sinelnikov <sin@altlinux.ru> 4.5.3-alt2.S1
- Do not delete an existing valid credential cache for KEYRING type
- Set FQDN to lower at fill_mem_keytab_from_system_keytab()

* Mon Dec 19 2016 Evgeny Sinelnikov <sin@altlinux.ru> 4.5.3-alt1.S1
- Update for release with security fixes:
  - CVE-2016-2123 (ndr_pull_dnsp_name contains an integer wrap problem)
  - CVE-2016-2125 (client code always requests a forwardable ticket)
  - CVE-2016-2126 (crash winbindd using a legitimate Kerberos ticket)

* Mon Dec 19 2016 Evgeny Sinelnikov <sin@altlinux.ru> 4.5.2-alt1.S1
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

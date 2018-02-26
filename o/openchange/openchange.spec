%def_disable python
%def_disable server

# Licensing Note: The code is GPLv3+ and the IDL files are public domain.

Name: openchange
Version: 1.0
Release: alt1
Group: Networking/Mail
Summary: Provides access to Microsoft Exchange servers using native protocols
License: GPLv3+ and Public Domain
Url: http://www.openchange.org/

Source: %name-%version.tar
Patch: %name-%version-%release.patch

BuildRequires: flex
BuildRequires: libtalloc-devel
BuildRequires: libtevent-devel
BuildRequires: libldb-devel
BuildRequires: libtdb-devel
BuildRequires: bison
BuildRequires: samba4-devel
BuildRequires: samba4-pidl
BuildRequires: libical-devel
BuildRequires: libpopt-devel
BuildRequires: libmagic-devel
BuildRequires: zlib-devel
BuildRequires: libsqlite3-devel
BuildRequires: doxygen
BuildRequires: libxslt
BuildRequires: python-devel

### Patches ###

# OpenChange's libmapi conflicts with Zarafa's libmapi.
# Zarafa is older than OpenChange, so it wins.
# Patch10: libmapi-0.8.2-libmapi-conflict.patch

# RH bug #552984
# Patch11: openchange-0.9-generate-xml-doc.patch

%description
OpenChange aims to provide a portable Open Source implementation of Microsoft Exchange Server and Exchange protocols.
Exchange is a groupware server designed to work with Microsoft Outlook, and providing features such as
a messaging server, shared calendars, contact databases, public folders, notes and tasks.

OpenChange provides libraries to access Microsoft Exchange servers
using native protocols.

%package -n libmapi
Summary: libmapi is a Main client-side library
Group: System/Libraries

%description -n libmapi
Main client-side library. libmapi closely reflects the underlying protocol
operations (Exchange RPC) being performed between the client and the
server. For more information, consult the API documentation (either
build yourself, or online at

%package -n libmapiadmin
Summary: Administration client library for the MAPI (Exchange/Outlook) protocol
Group: System/Libraries
Requires: libmapi = %version-%release

%description -n libmapiadmin
Library that allows remote administration of MAPI (Exchange/Outlook) servers.

%package -n libmapiproxy
Summary: Proxy library for the MAPI (Exchange/Outlook) protocol
Group: System/Libraries
Requires: libmapi = %version-%release

%description -n libmapiproxy
This is a library that allows proxying of the MAPI (Exchange/Outlook) protocol.

%package -n libmapistore
Summary: Storage library for MAPI objects
Group: System/Libraries

%description -n libmapistore
Library that can store arbitrary MAPI objects.

%package -n libocpf
Summary: Scripting library for the MAPI protocol
Group: System/Libraries
Requires: libmapi = %version-%release

%description -n libocpf
Library that reads and runs files in the OCPF scripting language,
a domain-specific language for the MAPI protocol.
Currently implemented features include sending and receiving mail and
enumerating the address book.

%package devel
Summary: Developer tools for OpenChange libraries
Group: Development/C
Requires: libmapi = %version-%release
Requires: libmapiadmin = %version-%release
Requires: libmapiproxy = %version-%release
Requires: libmapistore = %version-%release
Requires: libocpf = %version-%release

%description devel
This package provides the development tools and headers for
OpenChange, providing libraries to access Microsoft Exchange servers
using native protocols.

%package client
Summary: User tools for OpenChange libraries
Group: Networking/Mail
Requires: libmapi = %version-%release
Requires: libmapiadmin = %version-%release
Requires: libmapistore = %version-%release
Requires: libocpf = %version-%release

%description client
This package provides the user tools for OpenChange, providing access to
Microsoft Exchange servers using native protocols.

%package -n python-module-%name
Summary: Python bindings for OpenChange libraries
Group: Development/Python
Requires: libmapi = %version-%release

%description -n python-module-%name
This module contains a wrapper that allows the use of OpenChange via Python.

%package server
Summary: Server-side modules for OpenChange
Group: System/Servers
Requires: libmapi = %version-%release
Requires: sqlite3

%description server
This package provides the server elements for OpenChange.

%prep
%setup -q
%patch -p1

%build
mkdir bin
mkdir setup/mapistore

./autogen.sh
%configure \
%if_enabled python
	--enable-pymapi \
%endif
	--with-modulesdir=%_libdir/samba

# Parallel builds prohibited by makefile
make
make doxygen

%install
%makeinstall_std

cp -r libmapi++ %buildroot%_includedir

rm -rf %buildroot%_libdir/nagios/check_exchange
rm -rf %buildroot%prefix/modules
rm -rf %buildroot%_datadir/js
rm -rf %buildroot%_datadir/setup

mkdir %buildroot%_mandir
cp -r doc/man/man1 %buildroot%_mandir
# cp -r apidocs/man/man3 %buildroot%_mandir

# Avoid a file conflict with man-pages package.
# Page is still reachable as "mapi_obj_bookmark".
rm -f %buildroot%_man3dir/index.3.gz

%if_disabled python
rm -rf %buildroot%python_sitelibdir/openchange
%endif

%if_disabled server
# XXX There is no configure switch to disable the server
#     libraries in OpenChange 0.9, so just delete them.
rm -f %buildroot%_libdir/libmapiserver.so*
#rm -f %buildroot%_libdir/libmapistore.so*
#rm -f %buildroot%_libdir/mapistore_backends/mapistore_sqlite3.so
rm -f %buildroot%_pkgconfigdir/libmapiserver.pc
%endif

%files -n libmapi
%doc ChangeLog COPYING IDL_LICENSE.txt VERSION
%_libdir/libmapi-openchange.so.*

%files -n libmapiadmin
%_libdir/libmapiadmin.so.*

%files -n libmapiproxy
%_libdir/libmapiproxy.so.*
%_libdir/samba/dcerpc_mapiproxy

%files -n libmapistore
%_libdir/libmapistore.so.*

%files -n libocpf
%_libdir/libocpf.so.*

%files devel
%_includedir/*
%_libdir/*.so
%_pkgconfigdir/*
# %_man3dir/*
%doc apidocs/html/libmapi
%doc apidocs/html/libocpf
%doc apidocs/html/overview
%doc apidocs/html/index.html

%files client
%_bindir/*
%_man1dir/*
%_datadir/mapitest/*

%if_enabled python
%files -n python-module-%name
%python_sitelibdir/openchange
%endif

%if_enabled server
%files server
%_libdir/libmapiserver.so.*
%_libdir/mapistore_backends/mapistore_fsocpf.so
%_libdir/mapistore_backends/mapistore_mstoredb.so
%_libdir/samba/dcerpc_server
%_libdir/samba/dcerpc_mapiproxy_server
%_datadir/setup/*
%endif

%changelog
* Fri Mar 30 2012 Alexey Shabalin <shaba@altlinux.ru> 1.0-alt1
- 1.0
- add libmapiadmin, libmapiproxy, libmapistore, libocpf packages

* Wed Aug 24 2011 Alexey Shabalin <shaba@altlinux.ru> 0.11-alt1
- 0.11

* Wed May 11 2011 Alexey Shabalin <shaba@altlinux.ru> 0.11-alt0.2
- rename libmapi so as not to conflict with Zarafa

* Thu Apr 14 2011 Alexey Shabalin <shaba@altlinux.ru> 0.11-alt0.1
- pre 0.11 snapshot

* Tue Aug 17 2010 Alexey Shabalin <shaba@altlinux.ru> 0.9-alt1
- initial build for ALT Linux Sisyphus, based on fedora spec

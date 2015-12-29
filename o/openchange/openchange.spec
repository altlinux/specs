%def_enable python
%def_enable server

# Licensing Note: The code is GPLv3+ and the IDL files are public domain.

Name:    openchange
Version: 2.4
Release: alt3.zentyal16
Group:   Networking/Mail
Summary: Provides access to Microsoft Exchange servers using native protocols
License: GPLv3+ and Public Domain
Url:     http://www.openchange.org/
# VCS:   https://github.com/zentyal/openchange

Source:  %name-%version.tar
Patch:   %name-%version-%release.patch

BuildRequires(pre): rpm-build-apache2
BuildRequires(pre): apache2-common
BuildRequires(pre): rpm-build-python
BuildRequires: flex
BuildRequires: libtalloc-devel
BuildRequires: libtevent-devel
BuildRequires: libldb-devel
BuildRequires: libtdb-devel
BuildRequires: bison
BuildRequires: samba-DC-devel >= 4.0.0
BuildRequires: python-module-samba-DC
BuildRequires: samba-DC-pidl
BuildRequires: doxygen
BuildRequires: libical-devel
BuildRequires: libmagic-devel
BuildRequires: libmysqlclient-devel
BuildRequires: libmemcached-devel >= 1.0.18
BuildRequires: libnanomsg-devel
BuildRequires: libpopt-devel
BuildRequires: libsqlite3-devel
BuildRequires: libxslt
BuildRequires: python-devel
BuildRequires: zlib-devel
BuildRequires: python-module-pylons
BuildRequires: python-module-PasteScript
BuildRequires: python-module-PasteDeploy

%filter_from_requires /^\/usr\/%_lib\/samba-dc\/lib/d

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
Requires: samba-DC-libs

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
Requires: samba-DC-libs

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
Requires: libocpf = %version-%release
%if_enabled server
Requires: libmapiproxy = %version-%release
Requires: libmapistore = %version-%release
%endif
Requires: samba-DC-devel

%description devel
This package provides the development tools and headers for
OpenChange, providing libraries to access Microsoft Exchange servers
using native protocols.

%package client
Summary: User tools for OpenChange libraries
Group: Networking/Mail
Requires: libmapi = %version-%release
Requires: libmapiadmin = %version-%release
Requires: libocpf = %version-%release
%if_enabled server
Requires: libmapistore = %version-%release
%endif

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

%package ocsmanager
Summary: OpenChange - web services
Group: Networking/Mail
Requires: apache2-common
Requires: python-module-pylons
Requires: python-module-PasteScript

%description ocsmanager
This packages provides web services for OpenChange in the form of a Pylons
application.

%package rpcproxy
Summary: OpenChange - RPC-over-HTTP proxy
Group: Networking/Mail
Requires: apache2-mod_wsgi

%description rpcproxy
This package contains a a RPC-over-HTTP python implementation
for Samba, using wsgi.

%prep
%setup -q
%patch -p1

%build
mkdir -p bin
mkdir -p setup/mapistore

./autogen.sh
%configure \
%if_enabled python
	--enable-pymapi \
%endif
	--with-modulesdir=%_libdir/samba-dc

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
rm -f %buildroot%_bindir/check_fasttransfer
%endif

# ocsmanager
install -Dm644 mapiproxy/services/ocsmanager/ocsmanager.ini %buildroot%_sysconfdir/ocsmanager/ocsmanager.ini
install -dm750 %buildroot%_logdir/ocsmanager

install -Dm644 mapiproxy/services/ocsmanager/ocsmanager-apache.conf %buildroot%apache2_mods_available/ocsmanager.conf
install -Dm755 openchange-ocsmanager.init %buildroot%_initdir/openchange-ocsmanager
install -dm700 %buildroot%_cachedir/ntlmauthhandler
pushd mapiproxy/services/ocsmanager
%python_install --prefix=/usr
# HACK: fix wrong installed egg files on x86_64
test "%python_sitelibdir" != "%python_sitelibdir_noarch" && mv %buildroot%python_sitelibdir_noarch/*.egg-* %buildroot%python_sitelibdir
popd

# rpcproxy
install -Dm0644 mapiproxy/services/web/rpcproxy/rpcproxy.conf %buildroot%apache2_mods_available/rpcproxy.conf
install -Dm0644 mapiproxy/services/web/rpcproxy/rpcproxy.wsgi %buildroot%_libexecdir/openchange/web/rpcproxy/rpcproxy.wsgi
pushd mapiproxy/services/web/rpcproxy
cp -a rpcproxy %buildroot%_libexecdir/openchange/web/rpcproxy
popd

%files -n libmapi
%doc CHANGES.md COPYING IDL_LICENSE.txt README.md README.smbconf.md
%doc apidocs/html/libmapi
%doc apidocs/html/libocpf
%doc apidocs/html/overview
%doc apidocs/html/index.html
%_libdir/libmapi.so.*

%files -n libmapiadmin
%_libdir/libmapiadmin.so.*

%files -n libocpf
%_libdir/libocpf.so.*

%files devel
%_includedir/*
%_libdir/*.so
%_pkgconfigdir/*
# %_man3dir/*

%files client
%_bindir/*
%_man1dir/*
%_datadir/mapitest/*

%if_enabled python
%files -n python-module-%name
%python_sitelibdir/openchange
%endif

%if_enabled server
%files -n libmapiproxy
%_libdir/libmapiproxy.so.*
%_libdir/samba-dc/dcerpc_mapiproxy

%files -n libmapistore
%_libdir/libmapistore.so.*

%files server
%_sbindir/*
%_libdir/libmapiserver.so.*
%_libdir/samba-dc/dcerpc_server
%_libdir/samba-dc/dcerpc_mapiproxy_server
%_datadir/samba/setup/*
%endif

%files ocsmanager
%config(noreplace) %_initdir/openchange-ocsmanager
%config(noreplace) %_sysconfdir/ocsmanager/*
%config(noreplace) %apache2_mods_available/ocsmanager.conf
%python_sitelibdir/ocsmanager*
%_logdir/ocsmanager
%attr(0700, %apache2_name, %apache2_group) %_cachedir/ntlmauthhandler

%files rpcproxy
%config(noreplace) %apache2_mods_available/rpcproxy.conf
%_libexecdir/openchange/web/rpcproxy

%changelog
* Thu Dec 24 2015 Andrey Cherepanov <cas@altlinux.org> 2.4-alt3.zentyal16
- Package openchange-ocsmanager and openchange-rpcproxy

* Wed Dec 09 2015 Andrey Cherepanov <cas@altlinux.org> 2.4-alt2.zentyal16
- New version 2.4-zentyal16

* Mon Dec 07 2015 Andrey Cherepanov <cas@altlinux.org> 2.4-alt1.zentyal13
- Rebase to 2.4-zentyal13 from https://github.com/zentyal/openchange

* Mon Nov 30 2015 Andrey Cherepanov <cas@altlinux.org> 2.3-alt1
- New version
- Enable openchange-server build

* Fri Apr 05 2013 Alexey Shabalin <shaba@altlinux.ru> 2.0-alt1
- 2.0

* Mon Feb 18 2013 Alexey Shabalin <shaba@altlinux.ru> 1.0-alt2.1
- rebuild

* Tue Jan 15 2013 Alexey Shabalin <shaba@altlinux.ru> 1.0-alt2
- fix http://tracker.openchange.org/issues/397
- fix http://tracker.openchange.org/issues/398
- fix https://bugzilla.gnome.org/show_bug.cgi?id=682449

* Sun Dec 09 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0-alt1.1
- Fixed build with flex 2.5.37

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

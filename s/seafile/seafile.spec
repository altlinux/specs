Name: seafile
Version: 3.1.5
Release: alt1
Summary: Full-fledged cloud storage platform

Group: Networking/File transfer
License: GPLv3
Url: https://github.com/haiwen/seafile

Packager: Konstantin Artyushkin <akv@altlinux.org>

# Source-url: https://github.com/haiwen/seafile/archive/v%version.tar.gz
Source: %name-%version.tar

Requires: python-module-mako
Requires: python-module-webpy
Requires: python-module-simplejson

Requires: lib%name = %version-%release

# Automatically added by buildreq on Sun Nov 10 2013
# optimized out: glib2-devel gnu-config libevent-devel libgio-devel libsearpc-devel mariadb-client mariadb-common pkg-config python-base python-devel python-module-distribute python-module-zope python-modules
BuildRequires: intltool libssl-devel libuuid-devel python-module-mwlib python-module-paste python-module-peak
BuildRequires: zlib-devel libfuse-devel vala libjansson-devel libjson-glib-devel

BuildRequires: libsearpc-devel >= 3.0.4
BuildRequires: libccnet-devel >= 3.1.0

BuildRequires: libsqlite3-devel >= 3.7
BuildRequires: libevent-devel >= 2.0
BuildRequires: libarchive-devel >= 2.8.5

# server requires
BuildRequires: libzdb-devel >= 2.12
BuildRequires: libevhtp-devel >= 1.2.9

Requires: ccnet >= 3.1.0

%description
Seafile is a next-generation open source cloud storage system
with advanced support for file syncing, privacy protection and teamwork.

Collections of files are called libraries, and each library can be synced separately.
A library can be encrypted with a user chosen password.
This password is not stored on the server,
so even the server admin cannot view a file's contents.

Seafile allows users to create groups with file syncing,
wiki, and discussion to enable easy collaboration around documents within a team.

%package server
Summary: Seafile server
Group: Networking/File transfer
Requires: lib%name = %version-%release

%description server
Seafile server.
Seafile is a next-generation open source cloud storage system
with advanced support for file syncing, privacy protection and teamwork.

%package -n lib%name
Summary: Seafile library files
Group: Networking/File transfer

%description -n lib%name
The lib%name package contains libraries for Seafile.

%package -n lib%name-devel
Summary: Development files for lib%name
Requires: lib%name = %version-%release
Group: Networking/File transfer

%description -n lib%name-devel
The lib%name-devel package contains libraries and header files for
developing applications that use lib%name.

%prep
%setup
# remove buildroot from .pc file
%__subst 's/(DESTDIR)//' lib/libseafile.pc.in

%build
%autoreconf
%configure --enable-client --enable-server --disable-static
# FIXME: breakes build
#make_build
%make

%install
%makeinstall_std

%files
%_bindir/seafile
%_bindir/seaf-cli
%_bindir/seaf-daemon
%_man1dir/seaf-cli.1.*
%_man1dir/seaf-daemon*.1.*

%files server
%_bindir/fileserver
%_bindir/seaf-fsck
%_bindir/seaf-fuse
%_bindir/seaf-migrate
%_bindir/seaf-server
%_bindir/seaf-server-init
%_bindir/seafile-admin
%_bindir/seafile-controller
%_bindir/seafserv-gc
%_bindir/seafserv-tool

%python_sitelibdir/seaserv/

%files -n lib%name
%_libdir/*.so.*
%python_sitelibdir/%name/

%files -n lib%name-devel
%_includedir/*
%_libdir/*.so
%_pkgconfigdir/lib%name.pc

%changelog
* Thu Aug 28 2014 Vitaly Lipatov <lav@altlinux.ru> 3.1.5-alt1
- new version 3.1.5 (with rpmrb script)
- add ccnet requires

* Sun Aug 24 2014 Vitaly Lipatov <lav@altlinux.ru> 3.1.4-alt1
- new version (3.1.4) with rpmgs script
- cleanup spec
- build server part

* Fri Aug 22 2014 Konstantin Artyushkin <akv@altlinux.org> 3.1.0-alt5
- update buildrequires

* Mon Aug 04 2014 Konstantin Artyushkin <akv@altlinux.org> 3.1.0-alt4
- + libjansson-devel

* Mon Aug 04 2014 Konstantin Artyushkin <akv@altlinux.org> 3.1.0-alt3
- update to 3.1.0

* Mon Aug 04 2014 Konstantin Artyushkin <akv@altlinux.org> 3.1.0-alt2
- update source

* Sun Nov 10 2013 Denis Baranov <baraka@altlinux.ru> 2.0.4-alt2
- Fix some error in repository

* Sun Nov 10 2013 Denis Baranov <baraka@altlinux.ru> 2.0.4-alt1
- Initial build libseafile for ALTLinux


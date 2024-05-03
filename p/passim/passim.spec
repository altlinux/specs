%define _unpackaged_files_terminate_build 1
%define abiversion 1
%def_enable check

Name: passim
Version: 0.1.8
Release: alt1

Summary: Local caching server
License: LGPL-2.1-only
Group: System/Servers
Url: https://github.com/hughsie/passim

Source: %name-%version.tar

Requires: lib%name%abiversion = %EVR

BuildRequires(pre): rpm-macros-meson
BuildRequires: meson
BuildRequires: gobject-introspection-devel
BuildRequires: libsystemd-devel
BuildRequires: libgio-devel
BuildRequires: libsoup3.0-devel
BuildRequires: libgnutls-devel
BuildRequires: libappstream-glib
BuildRequires: /proc

%description
Passim is a daemon that allows software to share files on your local network.

%package -n lib%name%abiversion
Summary: Local caching server library
Group: System/Libraries

%description -n lib%name%abiversion
libpassim is a library that allows software to share files on your local network
using the passimd daemon.

%package -n lib%name-devel
Summary: Development package for %name
Group: Development/C
Requires: lib%name%abiversion = %EVR

%description -n lib%name-devel
Files for development with %name.

%prep
%setup

%build
%meson \
	-Dintrospection=enabled
%meson_build

%install
%meson_install
# remove sample data file
rm -v %buildroot%_localstatedir/passim/data/*-HELLO.md
%find_lang %name

%check
%__meson_test
appstream-util validate-relax --nonet %buildroot%_datadir/metainfo/org.freedesktop.Passim.metainfo.xml

%files -f %name.lang
%doc README.md LICENSE
%_bindir/passim
%_unitdir/passim.service
%_libdir/girepository-1.0/Passim-1.0.typelib
%_libexecdir/passimd
%_localstatedir/passim
%_iconsdir/hicolor/scalable/apps/org.freedesktop.Passim.png/
%_datadir/dbus-1/interfaces/org.freedesktop.Passim.xml
%_datadir/dbus-1/system-services/org.freedesktop.Passim.service
%_datadir/dbus-1/system.d/org.freedesktop.Passim.conf
%_datadir/metainfo/org.freedesktop.Passim.metainfo.xml
%_datadir/passim
%_man1dir/passim.1*
/lib/sysusers.d/passim.conf
%config(noreplace) %_sysconfdir/passim.conf

%files -n lib%name%abiversion
%_libdir/libpassim.so.%abiversion
%_libdir/libpassim.so.%abiversion.0.0

%files -n lib%name-devel
%_datadir/gir-1.0/Passim-1.0.gir
%_includedir/passim-1
%_libdir/libpassim*.so
%_pkgconfigdir/passim.pc

%changelog
* Thu May 02 2024 Ajrat Makhmutov <rauty@altlinux.org> 0.1.8-alt1
- New version.

* Thu Apr 18 2024 Ajrat Makhmutov <rauty@altlinux.org> 0.1.7-alt1
- New version.

* Fri Feb 16 2024 Ajrat Makhmutov <rauty@altlinux.org> 0.1.5-alt1
- First build for ALT.

%define _unpackaged_files_terminate_build 1
%def_with avahi

Name: phodav
Version: 3.0
Release: alt1
Summary: A WebDAV server using libsoup

Group: Networking/WWW
License: LGPLv2+
Url: https://wiki.gnome.org/phodav

Source: %name-%version.tar
Source2: spice-webdavd.init
Source3: spice-webdavd.sysconfig

BuildRequires(pre): meson >= 0.50
BuildRequires: gtk-doc
BuildRequires: libattr-devel
BuildRequires: pkgconfig(gio-unix-2.0) >= 2.44
BuildRequires: pkgconfig(libsoup-3.0) >= 3.0.0 pkgconfig(libxml-2.0)
%{?_with_avahi:BuildRequires: pkgconfig(avahi-gobject) pkgconfig(avahi-client)}
BuildRequires: pkgconfig(systemd) pkgconfig(udev)
BuildRequires: xmlto asciidoc

%description
phodav is a WebDAV server implementation using libsoup (RFC 4918).

%package -n lib%name
Summary: A library to serve files with WebDAV
Group: System/Libraries

%description -n lib%name
phodav is a WebDAV server implementation using libsoup (RFC 4918).
This package provides the library.

%package -n lib%name-devel
Summary: Header files, libraries and development documentation for %name
Group: Development/C
Requires: lib%name = %version-%release
Requires: pkgconfig(libsoup-3.0) >= 3.0.0

%description -n lib%name-devel
The libphodav-devel package includes the header files for libphodav.

%package -n chezdav
Summary: A simple WebDAV server program
Group: System/Servers
Requires: lib%name = %version-%release

%description -n chezdav
The chezdav package contains a simple tool to share a directory
with WebDAV. The service is announced over mDNS for clients to discover.

%package -n spice-webdavd
Summary: Spice daemon for the DAV channel
Group: Graphical desktop/Other
Requires: avahi-daemon dbus

%description -n spice-webdavd
The spice-webdavd package contains a daemon to proxy WebDAV request to
the Spice virtio channel.

%prep
%setup
echo "%version" > .tarball-version

%build
%meson
%meson_build

%install
%meson_install
install -pD -m755 %SOURCE2 %buildroot%_initdir/spice-webdavd
install -pD -m644 %SOURCE3 %buildroot/etc/sysconfig/spice-webdavd

%find_lang %name-3.0 --with-gnome

%post -n spice-webdavd
%post_service spice-webdavd

%preun -n spice-webdavd
%preun_service spice-webdavd

%files -n lib%name -f %name-3.0.lang
%doc NEWS COPYING
%_libdir/*.so.*

%files -n lib%name-devel
%_includedir/*
%_libdir/*.so
%_pkgconfigdir/*.pc
%_datadir/gtk-doc/html/phodav*

%files -n chezdav
%_bindir/chezdav
%_man1dir/chezdav.1*

%files -n spice-webdavd
%doc NEWS COPYING
%_sbindir/spice-webdavd
%_udevrulesdir/70-spice-webdavd.rules
%_unitdir/spice-webdavd.service
%_initdir/spice-webdavd
%config(noreplace) /etc/sysconfig/spice-webdavd

%changelog
* Mon Aug 29 2022 Alexey Shabalin <shaba@altlinux.org> 3.0-alt1
- new version 3.0

* Wed Nov 25 2020 Alexey Shabalin <shaba@altlinux.org> 2.5-alt1
- new version 2.5

* Wed Mar 25 2020 Alexey Shabalin <shaba@altlinux.org> 2.4-alt1
- new version 2.4

* Sat Mar 16 2019 Alexey Shabalin <shaba@altlinux.org> 2.3-alt1
- 2.3

* Tue Mar 28 2017 Alexey Shabalin <shaba@altlinux.ru> 2.2-alt1
- 2.2

* Fri Dec 30 2016 Alexey Shabalin <shaba@altlinux.ru> 2.1-alt1
- 2.1

* Thu Apr 09 2015 Alexey Shabalin <shaba@altlinux.ru> 2.0-alt1
- 2.0

* Mon Oct 06 2014 Alexey Shabalin <shaba@altlinux.ru> 0.4-alt2
- webdavd: remove systemd target, use only service

* Fri Apr 18 2014 Alexey Shabalin <shaba@altlinux.ru> 0.4-alt1
- initial build

%def_without telepathy

Name: remmina
Version: 1.2.0
Release: alt0.rc17
Summary: Remote Desktop Client

Group: Networking/Remote access
License: GPLv2+ and MIT
Url: http://remmina.sourceforge.net
Source: %name-%version.tar

Requires: icon-theme-hicolor

BuildRequires: cmake
BuildRequires: desktop-file-utils
BuildRequires: gettext pkgconfig(libpcre)
BuildRequires: intltool
BuildRequires: libappstream-glib
BuildRequires: libgcrypt-devel
BuildRequires: libjpeg-devel libtasn1-devel libpng-devel libpixman-devel zlib-devel
BuildRequires: pkgconfig(glib-2.0) >= 2.28 pkgconfig(gio-2.0) pkgconfig(gobject-2.0) pkgconfig(gmodule-2.0) pkgconfig(gthread-2.0)
BuildRequires: pkgconfig(avahi-ui) >= 0.6.30
BuildRequires: pkgconfig(avahi-ui-gtk3) >= 0.6.30
BuildRequires: pkgconfig(freerdp2) >= 2.0.0
BuildRequires: pkgconfig(winpr2)
BuildRequires: pkgconfig(gtk+-3.0) pkgconfig(gdk-pixbuf-2.0) pkgconfig(pango) pkgconfig(cairo) pkgconfig(atk)
BuildRequires: pkgconfig(libsecret-1)
BuildRequires: pkgconfig(libssh) >= 0.6
BuildRequires: pkgconfig(libvncserver)
%{?_with_telepathy:BuildRequires: pkgconfig(telepathy-glib)}
BuildRequires: pkgconfig(vte-2.91)
BuildRequires: pkgconfig(xkbfile)
BuildRequires: pkgconfig(harfbuzz)
BuildRequires: pkgconfig(spice-client-gtk-3.0)

%add_findreq_skiplist %_datadir/%name/external_tools/*

%description
Remmina is a remote desktop client written in GTK+, aiming to be useful for
system administrators and travelers, who need to work with lots of remote
computers in front of either large monitors or tiny netbooks.

Remmina supports multiple network protocols in an integrated and consistent
user interface. Currently RDP, VNC, XDMCP and SSH are supported

%package devel
Summary: remmina development headers
Group: Development/Other

%description devel
Files required to build plugins for remmina

%package plugins
Summary: A set of plugins for remmina
Group: Networking/Remote access
Requires: %name freerdp-plugins-standard

%description plugins
A set of plugins for %name remote desktop client

%package plugins-gnome
Summary: A set of plugins-gnome for remmina
Group: Networking/Remote access
Requires: %name-plugins

%description plugins-gnome
A set of plugins-gnome for %name remote desktop client

%prep
%setup

#? Hack: https://github.com/FreeRDP/Remmina/issues/292
sed -i 's#install(DIRECTORY include/remmina DESTINATION include/remmina #install(DIRECTORY remmina/include/remmina DESTINATION include/ #' CMakeLists.txt

%build
%cmake \
    -DCMAKE_BUILD_TYPE=Release \
    -DWITH_APPINDICATOR=OFF \
    -DWITH_AVAHI=ON \
    -DWITH_FREERDP=ON \
    -DWITH_GCRYPT=ON \
    -DWITH_GETTEXT=ON \
    -DWITH_LIBSSH=ON \
     %{?_without_telepathy:-DWITH_TELEPATHY=OFF} \
    -DWITH_VTE=ON \
    -DREMMINA_PLUGINDIR=%_libdir/remmina/plugins

%cmake_build

%install
%cmakeinstall_std

mkdir -p %buildroot%_pkgconfigdir
install -p -m 644 remmina/%name.pc.in %buildroot%_pkgconfigdir/%name.pc

subst "s|@prefix@|%_prefix|g" %buildroot%_pkgconfigdir/%name.pc
subst "s|@exec_prefix@|%_exec_prefix|g" %buildroot%_pkgconfigdir/%name.pc
subst "s|@libdir@|%_libdir|g" %buildroot%_pkgconfigdir/%name.pc
subst "s|@includedir@|%_includedir|g" %buildroot%_pkgconfigdir/%name.pc
subst "s|@VERSION@|%version|g" %buildroot%_pkgconfigdir/%name.pc

%find_lang %name

%files -f %name.lang
%doc AUTHORS CHANGELOG.md README.md
%_bindir/%name
%_datadir/appdata/*.appdata.xml
%_datadir/applications/*.desktop
%_iconsdir/*/*/*/*
%_datadir/%name
%dir %_libdir/remmina
%dir %_libdir/remmina/plugins

%files plugins
%_libdir/remmina/plugins/*.so
%exclude %_libdir/remmina/plugins/remmina-plugins-gnome.so

%files plugins-gnome
%_libdir/remmina/plugins/remmina-plugins-gnome.so

%files devel
%_includedir/%name
%_pkgconfigdir/*

%changelog
* Tue Jan 10 2017 Alexey Shabalin <shaba@altlinux.ru> 1.2.0-alt0.rc17
- 1.2.0-rcgit.17

* Tue Apr 12 2016 Alexey Shabalin <shaba@altlinux.ru> 1.2.0-alt0.rc11.1
- add skip requires for external tools

* Thu Apr 07 2016 Alexey Shabalin <shaba@altlinux.ru> 1.2.0-alt0.rc11
- 1.2.0.rcgit.11

* Tue Aug 04 2015 Michael Shigorin <mike@altlinux.org> 1.1.2-alt2
- fixed plugins path on non-x86_64
- fixed build (closes: #31184)
- added missing R: %name (closes: #27266)

* Sat Mar 21 2015 Mikhail Kolchin <mvk@altlinux.org> 1.1.2-alt1
- new version

* Thu Mar 12 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.0-alt3.1
- Fixed build

* Wed Sep 18 2013 Andrey Cherepanov <cas@altlinux.org> 1.0.0-alt3
- Revert "FreeRDP moved from kbd to locale" (see https://github.com/FreeRDP/Remmina/pull/31)

* Thu Mar 22 2012 Slava Dubrovskiy <dubrsl@altlinux.org> 1.0.0-alt2
- build from git ffba771dcd70e37635e9c8ff3a905273c933294a (ALT #27099)

* Fri Feb 10 2012 Slava Dubrovskiy <dubrsl@altlinux.org> 1.0.0-alt1
- new version

* Tue Jan 17 2012 Slava Dubrovskiy <dubrsl@altlinux.org> 0.9.99.1-alt1.git
- new version
- union of package remmina and reminna-plugins
- fix (ALT #26205)

* Tue Feb 01 2011 Mykola Grechukh <gns@altlinux.ru> 0.9.3-alt1
- new version

* Sun Jan 30 2011 Denis Baranov <baraka@altlinux.ru> 0.9.2-alt1
- new version 0.9.2 (with rpmrb script)

* Thu Oct 28 2010 Mykola Grechukh <gns@altlinux.ru> 0.8.3-alt1
- new version

* Thu Aug 12 2010 Mykola Grechukh <gns@altlinux.ru> 0.8.1-alt1
- new version

* Tue Jul 20 2010 Mykola Grechukh <gns@altlinux.ru> 0.8.0-alt1
- first build for ALT Linux

* Wed May 05 2010 Damien Durand <splinux@fedoraproject.org> - 0.7.5-1
- Upstream release, 0.7.5
- Remove the old "DSO" patch

* Tue Mar 16 2010 Christoph Wickert <cwickert@fedoraproject.org> - 0.7.4-2
- Add patch to fix DSO issue

* Sat Feb 27 2010 Damien Durand <splinux@fedoraproject.org> 0.7.4-1
- Update to 0.7.4
- Fix License tag

* Sun Feb 14 2010 Damien Durand <splinux@fedoraproject.org> 0.7.3-1
- Upstream release
- Add rdesktop, xorg-x11-server-Xephyr in Requires
- Add grdc in Provides/Obsoletes
- Add --enable-vnc=dl in %%configure
- Remove unneeded README.LibVNCServer
- Fix "icons/hicolor" path

* Thu Jan 07 2010 Damien Durand <splinux@fedoraproject.org> 0.7.2-2
- Fix Summary
- Split BuildRequires

* Thu Jan 07 2010 Damien Durand <splinux@fedoraproject.org> 0.7.2-1
- Initial release

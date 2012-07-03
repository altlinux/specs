Name: remmina
Version: 1.0.0
Release: alt2
Summary: Remote Desktop Client

Group: Networking/Remote access
License: GPLv2+ and MIT
Url: http://remmina.sourceforge.net
Source: %name-%version.tar

Requires: icon-theme-hicolor

BuildRequires: cmake desktop-file-utils intltool libavahi-ui-devel libgcrypt-devel libssh-devel libunique-devel libvte3-devel libavahi-ui-gtk3-devel libpng-devel libpixman-devel xorg-glproto-devel xorg-dri2proto-devel libXau-devel libXdmcp-devel libXext-devel libXdamage-devel libXxf86vm-devel libxkbfile-devel libtelepathy-glib-devel
BuildRequires: libfreerdp-devel gettext libgnome-keyring-devel libgnutls-devel libXxf86misc-devel libXv-devel libXrandr-devel libXpm-devel libXinerama-devel
BuildRequires: libjpeg-devel libtasn1-devel libp11-kit-devel libvncserver-devel

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
Requires: freerdp-plugins-standard

%description plugins
A set of plugins for remote desktop client - remmina

%package plugins-gnome
Summary: A set of plugins-gnome for remmina
Group: Networking/Remote access
Requires: %name-plugins

%description plugins-gnome
A set of plugins-gnome for remote desktop client - remmina

%prep
%setup

sed -i '/target_link_libraries/s/)/ -lgnutls)/' remmina-plugins/vnc/CMakeLists.txt

%build
%cmake	-DWITH_APPINDICATOR=OFF \
	-DWITH_TELEPATHY=OFF \
	-DCMAKE_INSTALL_LIBDIR=%_lib
	
%make_build -C BUILD

%install
%makeinstall_std -C BUILD

mkdir -p %buildroot%_pkgconfigdir
install -p -m 644 remmina/%name.pc.in %buildroot%_pkgconfigdir/%name.pc

subst "s|@prefix@|%_prefix|g" %buildroot%_pkgconfigdir/%name.pc
subst "s|@exec_prefix@|%_exec_prefix|g" %buildroot%_pkgconfigdir/%name.pc
subst "s|@libdir@|%_libdir|g" %buildroot%_pkgconfigdir/%name.pc
subst "s|@includedir@|%_includedir|g" %buildroot%_pkgconfigdir/%name.pc
subst "s|@VERSION@|%version|g" %buildroot%_pkgconfigdir/%name.pc

%find_lang %name
%find_lang %name-plugins

%files -f %name.lang
%doc remmina/AUTHORS remmina/ChangeLog remmina/COPYING remmina/README
%_bindir/%name
%_datadir/applications/*.desktop
%_iconsdir/*/*/*/*

%files plugins -f %name-plugins.lang
%_libdir/remmina/plugins/*.so
%exclude %_libdir/remmina/plugins/remmina-plugins-gnome.so

%files plugins-gnome
%_libdir/remmina/plugins/remmina-plugins-gnome.so

%files devel
%_includedir/%name
%_pkgconfigdir/*

%changelog
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

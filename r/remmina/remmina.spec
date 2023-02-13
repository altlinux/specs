%define _unpackaged_files_terminate_build 1
%def_without telepathy
%def_with kwallet
%def_with gvnc
%def_with x2go

Name: remmina
Version: 1.4.27
Release: alt2
Summary: Remote Desktop Client

Group: Networking/Remote access
License: GPLv2+ and MIT
Url: http://remmina.sourceforge.net
Source: %name-%version.tar
#Source1: ru.po
Patch0: %name-%version.patch

Requires: icon-theme-hicolor

Obsoletes: %name-plugins-nx < %EVR
Obsoletes: %name-plugins-st < %EVR
Obsoletes: %name-plugins-xdmcp < %EVR

BuildRequires(pre): cmake >= 3.4.0
BuildRequires: gcc-c++
BuildRequires: python3-dev
BuildRequires: desktop-file-utils xdg-utils
BuildRequires: gettext pkgconfig(libpcre2-8) pkgconfig(libffi)
BuildRequires: intltool
BuildRequires: libappstream-glib
BuildRequires: libgcrypt-devel libssl-devel
BuildRequires: libjpeg-devel libtasn1-devel libpng-devel libpixman-devel zlib-devel
BuildRequires: pkgconfig(glib-2.0) >= 2.30 pkgconfig(gio-2.0) pkgconfig(gobject-2.0) pkgconfig(gmodule-2.0) pkgconfig(gthread-2.0)
BuildRequires: pkgconfig(avahi-ui-gtk3) >= 0.6.30 pkgconfig(avahi-client) >= 0.6.30
BuildRequires: pkgconfig(freerdp2) >= 2.0.0 libcups-devel
BuildRequires: pkgconfig(winpr2)
BuildRequires: pkgconfig(gtk+-3.0) >= 3.14.0 pkgconfig(gdk-pixbuf-2.0) pkgconfig(pango)
BuildRequires: pkgconfig(atk)
BuildRequires: pkgconfig(cairo)
BuildRequires: pkgconfig(wayland-client) pkgconfig(wayland-cursor) pkgconfig(wayland-egl) pkgconfig(wayland-scanner) pkgconfig(xkbcommon)
BuildRequires: pkgconfig(libsecret-1)
%{?_with_kwallet:BuildRequires: kf5-kwallet-devel}
BuildRequires: pkgconfig(libssh) >= 0.6
BuildRequires: pkgconfig(libvncserver)
%{?_with_gvnc:BuildRequires: pkgconfig(gvnc-1.0) pkgconfig(gvncpulse-1.0) pkgconfig(gtk-vnc-2.0)}
%{?_with_telepathy:BuildRequires: pkgconfig(telepathy-glib) pkgconfig(dbus-glib-1)}
%{?_with_x2go:BuildRequires: pyhoca-cli}
BuildRequires: pkgconfig(vte-2.91)
BuildRequires: pkgconfig(xkbfile)
BuildRequires: pkgconfig(harfbuzz)
BuildRequires: pkgconfig(spice-client-gtk-3.0)
BuildRequires: pkgconfig(json-glib-1.0)
BuildRequires: pkgconfig(libsoup-3.0) pkgconfig(webkit2gtk-4.1)
BuildRequires: pkgconfig(libsodium)
BuildRequires: pkgconfig(ayatana-appindicator3-0.1)

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
BuildArch: noarch

Requires: %name
Requires: %name-plugins-exec
Requires: %name-plugins-secret
Requires: %name-plugins-rdp
Requires: %name-plugins-vnc
Requires: %name-plugins-spice

%description plugins
A set of plugins for %name remote desktop client

%package plugins-exec
Summary: External execution plugin for Remmina Remote Desktop Client
Group: Networking/Remote access
Requires: %name = %EVR

%description plugins-exec
Remmina is a remote desktop client written in GTK+, aiming to be useful for
system administrators and travelers, who need to work with lots of remote
computers in front of either large monitors or tiny net-books.

This package contains the plugin to execute external processes (commands or
applications) from the Remmina window.

%package plugins-secret
Summary: Keyring integration for Remmina Remote Desktop Client
Group: Networking/Remote access
Requires: %name = %EVR
Provides: %name-plugins-gnome = %EVR
Obsoletes: %name-plugins-gnome < %EVR

%description plugins-secret
Remmina is a remote desktop client written in GTK+, aiming to be useful for
system administrators and travelers, who need to work with lots of remote
computers in front of either large monitors or tiny net-books.

This package contains the plugin with keyring support for the Remmina remote
desktop client.

%package plugins-kwallet
Summary: Kwallet integration for Remmina Remote Desktop Client
Group: Networking/Remote access
Requires: %name = %EVR

%description plugins-kwallet
Remmina is a remote desktop client written in GTK+, aiming to be useful for
system administrators and travelers, who need to work with lots of remote
computers in front of either large monitors or tiny net-books.

This package contains the plugin with kwallet support for the Remmina remote
desktop client.

%package plugins-rdp
Summary: RDP plugin for Remmina Remote Desktop Client
Group: Networking/Remote access
Requires: %name = %EVR
Requires: freerdp-plugins-standard

%description plugins-rdp
Remmina is a remote desktop client written in GTK+, aiming to be useful for
system administrators and travelers, who need to work with lots of remote
computers in front of either large monitors or tiny net-books.

This package contains the Remote Desktop Protocol (RDP) plugin for the Remmina
remote desktop client.

%package plugins-vnc
Summary: VNC plugin for Remmina Remote Desktop Client
Group: Networking/Remote access
Requires: %name = %EVR

%description plugins-vnc
Remmina is a remote desktop client written in GTK+, aiming to be useful for
system administrators and travelers, who need to work with lots of remote
computers in front of either large monitors or tiny net-books.

This package contains the VNC plugin for the Remmina remote desktop
client.

%package plugins-gvnc
Summary: GTK-VNC plugin for Remmina Remote Desktop Client
Group: Networking/Remote access
Requires: %name = %EVR

%description plugins-gvnc
Remmina is a remote desktop client written in GTK+, aiming to be useful for
system administrators and travelers, who need to work with lots of remote
computers in front of either large monitors or tiny net-books.

This package contains the GTK-VNC plugin for the Remmina remote desktop
client.

%package plugins-spice
Summary: SPICE plugin for Remmina Remote Desktop Client
Group: Networking/Remote access
Requires: %name = %EVR

%description plugins-spice
Remmina is a remote desktop client written in GTK+, aiming to be useful for
system administrators and travelers, who need to work with lots of remote
computers in front of either large monitors or tiny net-books.

This package contains the SPICE plugin for the Remmina remote desktop
client.

%package plugins-www
Summary: WWW plugin for Remmina Remote Desktop Client
Group: Networking/Remote access
Requires: %name = %EVR

%description plugins-www
Remmina is a remote desktop client written in GTK+, aiming to be useful for
system administrators and travelers, who need to work with lots of remote
computers in front of either large monitors or tiny net-books.

This package contains the WWW plugin (web browser with authentication) for the
Remmina remote desktop client.

%package plugins-x2go
Summary: X2GO plugin for Remmina Remote Desktop Client
Group: Networking/Remote access
Requires: %name = %EVR
Requires: pyhoca-cli

%description plugins-x2go
Remmina is a remote desktop client written in GTK+, aiming to be useful for
system administrators and travelers, who need to work with lots of remote
computers in front of either large monitors or tiny net-books.

This package contains the X2GO plugin for the Remmina remote desktop
client.

%package plugins-python
Summary: Pyhton plugin for Remmina Remote Desktop Client
Group: Networking/Remote access
Requires: %name = %EVR

%description plugins-python
Remmina is a remote desktop client written in GTK+, aiming to be useful for
system administrators and travelers, who need to work with lots of remote
computers in front of either large monitors or tiny net-books.

This package contains the python plugin for the Remmina remote desktop client.

%package gnome-session
Summary: Gnome Shell session for Remmina kiosk mode
Group: Networking/Remote access
Requires: %name = %EVR
Requires: gnome-session

%description gnome-session
Remmina is a remote desktop client written in GTK+, aiming to be useful for
system administrators and travelers, who need to work with lots of remote
computers in front of either large monitors or tiny net-books.

This package contains Remmina kiosk mode, including a Gnome Shell session
that shows up under the display manager session menu.

%prep
%setup
%patch0 -p1

#cp -f %%SOURCE1 po/

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
    -DWITH_KIOSK_SESSION=ON \
    -DWITH_NEWS=OFF \
    %{?_with_gvnc:-DWITH_GVNC=ON} \
    %{?_with_x2go:-DWITH_X2GO=ON} \
    %{?_with_kwallet:-DWITH_KF5WALLET=ON} \
    -DWITH_PYTHON=ON \
    -DREMMINA_RUNTIME_PLUGINDIR=%_libdir/remmina/plugins \
    -DREMMINA_PLUGINDIR=%_libdir/remmina/plugins

%cmake_build

%install
%cmakeinstall_std

mkdir -p %buildroot%_pkgconfigdir
install -p -m 644 data/%name.pc.in %buildroot%_pkgconfigdir/%name.pc

subst "s|@prefix@|%prefix|g" %buildroot%_pkgconfigdir/%name.pc
subst "s|@exec_prefix@|%_exec_prefix|g" %buildroot%_pkgconfigdir/%name.pc
subst "s|@libdir@|%_libdir|g" %buildroot%_pkgconfigdir/%name.pc
subst "s|@includedir@|%_includedir|g" %buildroot%_pkgconfigdir/%name.pc
subst "s|@VERSION@|%version|g" %buildroot%_pkgconfigdir/%name.pc

%find_lang %name

%files -f %name.lang
%doc AUTHORS CHANGELOG.md README.md
%_bindir/%name
%_bindir/remmina-file-wrapper
%_datadir/metainfo/*.appdata.xml
%_datadir/mime/*/*.xml
%_datadir/applications/*.desktop
%_iconsdir/hicolor/*/actions/*
%_iconsdir/hicolor/*/apps/*
%_iconsdir/hicolor/apps/*
%_iconsdir/hicolor/*/emblems/org.remmina.Remmina-ssh-symbolic.svg
%_iconsdir/hicolor/*/emblems/org.remmina.Remmina-sftp-symbolic.svg
%_iconsdir/hicolor/*/emblems/org.remmina.Remmina-tool-symbolic.svg
%_iconsdir/hicolor/*/status/org.remmina.Remmina-status.svg
%_datadir/%name
%_man1dir/remmina.1.*
%_man1dir/remmina-file-wrapper.1.*
%dir %_libdir/remmina
%dir %_libdir/remmina/plugins

%files plugins
%files plugins-exec
%_libdir/remmina/plugins/remmina-plugin-exec.so

%files plugins-secret
%_libdir/remmina/plugins/remmina-plugin-secret.so

%if_with kwallet
%files plugins-kwallet
%_libdir/remmina/plugins/remmina-plugin-kwallet.so
%endif

%files plugins-rdp
%_libdir/remmina/plugins/remmina-plugin-rdp.so
%_iconsdir/hicolor/*/emblems/org.remmina.Remmina-rdp-ssh-symbolic.svg
%_iconsdir/hicolor/*/emblems/org.remmina.Remmina-rdp-symbolic.svg

%files plugins-vnc
%_libdir/remmina/plugins/remmina-plugin-vnc.so
%_iconsdir/hicolor/*/emblems/org.remmina.Remmina-vnc-ssh-symbolic.svg
%_iconsdir/hicolor/*/emblems/org.remmina.Remmina-vnc-symbolic.svg

%if_with gvnc
%files plugins-gvnc
%_libdir/remmina/plugins/remmina-plugin-gvnc.so
%_iconsdir/hicolor/*/emblems/org.remmina.Remmina-gvnc-ssh-symbolic.svg
%_iconsdir/hicolor/*/emblems/org.remmina.Remmina-gvnc-symbolic.svg
%endif

%files plugins-spice
%_libdir/remmina/plugins/remmina-plugin-spice.so
%_iconsdir/hicolor/*/emblems/org.remmina.Remmina-spice-ssh-symbolic.svg
%_iconsdir/hicolor/*/emblems/org.remmina.Remmina-spice-symbolic.svg

%files plugins-www
%_libdir/remmina/plugins/remmina-plugin-www.so
%_iconsdir/hicolor/*/emblems/org.remmina.Remmina-www-symbolic.svg

%if_with x2go
%files plugins-x2go
%_libdir/remmina/plugins/remmina-plugin-x2go.so
%_iconsdir/hicolor/*/emblems/org.remmina.Remmina-x2go-ssh-symbolic.svg
%_iconsdir/hicolor/*/emblems/org.remmina.Remmina-x2go-symbolic.svg
%endif

%files plugins-python
%_libdir/remmina/plugins/remmina-plugin-python_wrapper.so

%files gnome-session
%_bindir/gnome-session-remmina
%_bindir/remmina-gnome
%_datadir/gnome-session/sessions/remmina-gnome.session
%_datadir/xsessions/remmina-gnome.desktop
%_man1dir/gnome-session-remmina.1.*
%_man1dir/remmina-gnome.1.*

%files devel
%_includedir/%name
%_pkgconfigdir/*

%changelog
* Mon Feb 13 2023 Anton Midyukov <antohami@altlinux.org> 1.4.27-alt2
- NMU: build with pkgconfig(ayatana-appindicator3-0.1) instead
  pkgconfig(appindicator3-0.1)

* Thu Sep 08 2022 Alexey Shabalin <shaba@altlinux.org> 1.4.27-alt1
- new version 1.4.27
- build with libsoup-3.0 and webkit2gtk-4.1

* Wed Jun 15 2022 Alexey Shabalin <shaba@altlinux.org> 1.4.26-alt1
- new version 1.4.26.
- new python plugin enabled.

* Wed Apr 13 2022 Alexey Shabalin <shaba@altlinux.org> 1.4.25-alt1
- new version 1.4.25.
- build www plugin.

* Fri Mar 04 2022 Alexey Shabalin <shaba@altlinux.org> 1.4.24-alt1
- new version 1.4.24

* Sat Dec 25 2021 Alexey Shabalin <shaba@altlinux.org> 1.4.23-alt1
- new version 1.4.23.

* Sun Nov 28 2021 Alexey Shabalin <shaba@altlinux.org> 1.4.21-alt1
- new version 1.4.21.
- Remove unmaintained nx, st, xdmcp plugins.
- Add kwallet, gvnc, x2go plugins.

* Tue Feb 09 2021 Alexey Shabalin <shaba@altlinux.org> 1.4.11-alt1
- new version 1.4.11

* Mon Feb 01 2021 Alexey Shabalin <shaba@altlinux.org> 1.4.10-alt2
- fixed load plugins (ALT #39628) (thx iv@)

* Sat Jan 30 2021 Alexey Shabalin <shaba@altlinux.org> 1.4.10-alt1
- new version 1.4.10
- drop fix_plugins_search_v1.2.32.1.patch

* Thu Jul 02 2020 Alexey Shabalin <shaba@altlinux.org> 1.4.7-alt1
- new version 1.4.7

* Thu Jun 18 2020 Alexey Shabalin <shaba@altlinux.org> 1.4.6-alt2
- add -DWITH_NEWS=OFF

* Thu Jun 18 2020 Alexey Shabalin <shaba@altlinux.org> 1.4.6-alt1
- new version 1.4.6

* Sun May 31 2020 Alexey Shabalin <shaba@altlinux.org> 1.4.5-alt1
- new version 1.4.5

* Fri May 08 2020 Alexey Shabalin <shaba@altlinux.org> 1.4.3-alt1
- new version 1.4.3

* Mon Apr 13 2020 Alexey Shabalin <shaba@altlinux.org> 1.4.2-alt1
- new version 1.4.2

* Tue Mar 24 2020 Alexey Shabalin <shaba@altlinux.org> 1.4.1-alt1
- new version 1.4.1

* Mon Jan 27 2020 Alexey Shabalin <shaba@altlinux.org> 1.3.10-alt1
- 1.3.10

* Mon Dec 09 2019 Alexey Shabalin <shaba@altlinux.org> 1.3.7-alt1
- 1.3.7
- drop local localization ru.po

* Thu Nov 21 2019 Ivan A. Melnikov <iv@altlinux.org> 1.3.6-alt2
- package remmina-file-wrapper.sh (closes: #37514)

* Tue Sep 10 2019 Alexey Shabalin <shaba@altlinux.org> 1.3.6-alt1
- 1.3.6

* Tue Apr 30 2019 Pavel Moseev <mars@altlinux.org> 1.3.4-alt2
- update translation

* Mon Mar 25 2019 Alexey Shabalin <shaba@altlinux.org> 1.3.4-alt1
- 1.3.4

* Fri Feb 01 2019 Ivan A. Melnikov <iv@altlinux.org> 1.3.2-alt1
- 1.3.2 (closes: #35993)

* Fri Jan 25 2019 Alexey Shabalin <shaba@altlinux.org> 1.3.0-alt1
- 1.3.0

* Wed Jan 16 2019 Alexey Shabalin <shaba@altlinux.org> 1.2.32.1-alt1
- 1.2.32.1
- split plugins package
- add gnome-session package for kiosk mode

* Wed Aug 29 2018 Sergey V Turchin <zerg@altlinux.org> 1.2.0-alt5.rc21
- fix to build with new libssh

* Wed Jun 27 2018 Andrey Bychkov <mrdrew@altlinux.org> 1.2.0-alt4.rc21
- fix plugins search in version 1.2.0-rc21

* Tue Jun 26 2018 Andrey Bychkov <mrdrew@altlinux.org> 1.2.0-alt3.rc21
- increase release number for allow backport to p8

* Wed Jun 13 2018 Oleg Gadelshin <olegeg@altlinux.ru> 1.2.0-alt2.rc20
- increase release number to alt2
- add remmina-1.2.0-rdp-passwordispin_option.patch for use of smartcard pin as password

* Tue Sep 26 2017 Alexey Shabalin <shaba@altlinux.ru> 1.2.0-alt1.rc20
- 1.2.0-rcgit.20
- increase release number for allow backport to p8

* Wed Jul 26 2017 Alexey Shabalin <shaba@altlinux.ru> 1.2.0-alt0.rc19
- 1.2.0-rcgit.19

* Tue Jan 10 2017 Alexey Shabalin <shaba@altlinux.ru> 1.2.0-alt0.rc17
- 1.2.0-rcgit.17

* Tue Apr 12 2016 Alexey Shabalin <shaba@altlinux.ru> 1.2.0-alt0.rc11.1
- add skip requires for external tools

* Thu Apr 07 2016 Alexey Shabalin <shaba@altlinux.ru> 1.2.0-alt0.rc11
- 1.2.0.rcgit.11

* Tue Aug 04 2015 Michael Shigorin <mike@altlinux.org> 1.1.2-alt2
- fixed plugins path on non-x86_64
- fixed build (closes: #31184)
- added missing R: %%name (closes: #27266)

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

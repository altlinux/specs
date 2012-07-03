%global _internal_version g3e114c9

Name: cinnamon
Version: 1.4.0
Release: alt7

Summary: Window management and application launching for GNOME
License: GPLv2+
Group: Graphical desktop/GNOME

Url: http://cinnamon.linuxmint.com
# To generate tarball
# wget https://github.com/linuxmint/Cinnamon/tarball/1.4 -O cinnamon-1.4.0.tar.gz
Source0: cinnamon-%version.tar.gz
Source1: cinnamon.desktop
Source2: cinnamon.session
Source3: %name-menu.png

# fc patches
# Replace mint favorites with fedora gnome-shell defaults
Patch0: cinnamon-favourite-apps-firefox.patch
Patch2: cinnamon-1.4.0_settings.patch
Patch3: logout_theme.patch
Patch4: window-attention.patch

Patch10: %name-1.4.0-alt-menu.patch

%define clutter_ver 1.7.5
%define gtk_ver 3.0.0
%define gi_ver 0.10.1
%define muffin_ver 1.0.2
%define eds_ver 2.91.6
%define json_glib_ver 0.13.2
%define gjs_ver 1.29.18
%define tp_glib_ver 0.15.5
%define tp_logger_ver 0.2.4
%define polkit_ver 0.100
%define folks_ver 0.5.2
%define bt_ver 3.0.0

Requires: upower
Requires: polkit >= %polkit_ver
# needed for session files
Requires: gnome-session
Requires(post,preun):  GConf
# needed for on-screen keyboard
Requires: caribou

# needed for settings (python.req ignores /usr/share/cinnamon-settings/cinnamon-settings.py)
Requires: python-module-dbus
Requires: python-module-pygnome-gconf
Requires: python-modules-json

# Cinnamon.typelib should be installed in %%_typelibdir for automatic provides,
# but other typelibs (Gvs, St) conflict with gnome-shell
# Provides: typelib(Cinnamon)
# since rpm-build-gir-0.7.1-alt6 we can use
%set_typelibdir %_libdir/%name
# for detection and annihilation internal typelib-dependencies

BuildPreReq: rpm-build-gir >= 0.7.1-alt6
BuildPreReq: libclutter-devel >= %clutter_ver
BuildPreReq: libgtk+3-devel >= %gtk_ver
BuildPreReq: libgjs-devel >= %gjs_ver
BuildPreReq: libjson-glib-devel >= %json_glib_ver
BuildPreReq: evolution-data-server-devel >= %eds_ver
BuildPreReq: libgnome-bluetooth-devel >= %bt_ver
BuildPreReq: libtelepathy-glib-devel >= %tp_glib_ver
BuildPreReq: libtelepathy-logger-devel >= %tp_logger_ver
BuildPreReq: libfolks-devel >= %folks_ver
BuildRequires: libgnome-desktop3-devel libgnome-keyring-devel libgnome-menus-devel libstartup-notification-devel
BuildRequires: libpolkit-devel libupower-devel libgudev-devel libsoup-devel NetworkManager-glib-devel
BuildRequires: libcanberra-gtk3-devel libcroco-devel GConf libGConf-devel
BuildRequires: gobject-introspection >= %gi_ver libupower-gir-devel libgudev-gir-devel libsoup-gir-devel libfolks-gir-devel
BuildRequires: libtelepathy-glib-gir-devel libtelepathy-logger-gir-devel libgnome-menus-gir-devel NetworkManager-glib-gir-devel

# for barriers
BuildRequires: libXfixes-devel >= 5.0
# used in unused BigThemeImage
BuildRequires: librsvg-devel
BuildRequires: libmuffin-devel >= %muffin_ver
BuildRequires: libpulseaudio-devel

BuildRequires: desktop-file-utils
BuildRequires: gtk-doc gnome-common intltool

%description
Cinnamon is a Linux desktop which provides advanced innovative features
and a traditional user experience.

The desktop layout is similar to Gnome 2. The underlying technology is
forked from Gnome Shell. The emphasis is put on making users feel at
home and providing them with an easy to use and comfortable desktop
experience.

%prep
%setup -n linuxmint-Cinnamon-%_internal_version
%patch0 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1

%patch10

# make changes for settings move to /usr/share
mv files/usr/lib/cinnamon-settings files/usr/share
sed -i -e 's@/usr/lib@/usr/share@g' files/usr/bin/cinnamon-settings \
  files/usr/share/cinnamon-settings/cinnamon-settings.py
# make changes for menu-editor move to /usr/share
mv files/usr/lib/cinnamon-menu-editor files/usr/share
rm -rf files/usr/lib
sed -i -e 's@/usr/lib@/usr/share@g' files/usr/bin/cinnamon-menu-editor \
  files/usr/share/cinnamon-menu-editor/Alacarte/MainWindow.py
# replace menu image
rm -f data/theme/menu.png
cp %SOURCE3 data/theme/menu.png
# remove and replace the session files as they don't work with fedora (can't be bothered to patch it)
rm -f files/usr/bin/gnome-session-cinnamon  \
 files/usr/share/xsessions/cinnamon.desktop \
 files/usr/share/gnome-session/sessions/cinnamon.session
cp %SOURCE2 files/usr/share/gnome-session/sessions/
# files replaced with fedora files
rm -f files/usr/share/desktop-directories/cinnamon-menu-applications.directory \
 files/usr/share/desktop-directories/cinnamon-utility.directory                \
 files/usr/share/desktop-directories/cinnamon-utility-accessibility.directory  \
 files/usr/share/desktop-directories/cinnamon-development.directory            \
 files/usr/share/desktop-directories/cinnamon-education.directory              \
 files/usr/share/desktop-directories/cinnamon-game.directory                   \
 files/usr/share/desktop-directories/cinnamon-graphics.directory               \
 files/usr/share/desktop-directories/cinnamon-network.directory                \
 files/usr/share/desktop-directories/cinnamon-audio-video.directory            \
 files/usr/share/desktop-directories/cinnamon-office.directory                 \
 files/usr/share/desktop-directories/cinnamon-system-tools.directory           \
 files/usr/share/desktop-directories/cinnamon-other.directory
# adjust font size
sed -i -e 's,font-size: 9.5pt,font-size: 10pt,g' data/theme/cinnamon.css
sed -i -e 's,font-size: 9pt,font-size: 10pt,g' data/theme/cinnamon.css
sed -i -e 's,font-size: 8.5pt,font-size: 10pt,g' data/theme/cinnamon.css
sed -i -e 's,font-size: 8pt,font-size: 10pt,g' data/theme/cinnamon.css
sed -i -e 's,font-size: 7.5pt,font-size: 10pt,g' data/theme/cinnamon.css

rm -rf debian
rm configure

%build
export CFLAGS="$RPM_OPT_FLAGS -Wno-error=deprecated-declarations"
(if ! test -x configure; then NOCONFIGURE=1 ./autogen.sh; fi;
%configure --disable-static --enable-compile-warnings=yes --without-ca-certificates)

%make_build

%install
export GCONF_DISABLE_MAKEFILE_SCHEMA_INSTALL=1
%makeinstall_std

# Remove .la file
rm -rf $RPM_BUILD_ROOT/%_libdir/cinnamon/libcinnamon.la

# firefox plugin
mv -f $RPM_BUILD_ROOT/%_libdir/mozilla/* $RPM_BUILD_ROOT/%_libdir/browser-plugins

desktop-file-validate $RPM_BUILD_ROOT%_datadir/applications/cinnamon.desktop

desktop-file-install                                 \
 --add-category="Utility"                            \
 --remove-category="DesktopSettings"                 \
 --remove-key="Encoding"                             \
 --add-only-show-in="GNOME"                          \
 --delete-original                                   \
 --dir=$RPM_BUILD_ROOT%_datadir/applications       \
 $RPM_BUILD_ROOT%_datadir/applications/cinnamon-settings.desktop

cat > start%name << _START_
#!/bin/sh
%_bindir/startgnome --session=%name
_START_

install -pD -m755 start%name %buildroot%_bindir/start%name

mkdir -p %buildroot%_x11sysconfdir/wmsession.d
cat > %buildroot%_x11sysconfdir/wmsession.d/02Cinnamon << _WM_
NAME=Cinnamon
ICON=
DESC=This session logs you into Cinnamon
EXEC=/usr/bin/start%name
SCRIPT:
exec /usr/bin/start%name
_WM_

%find_lang %name

%post
%gconf2_install %name

%preun
if [ $1 = 0 ]; then
    %gconf2_uninstall %name
fi

%files -f %name.lang
%doc NEWS README
%_bindir/start%name
%_bindir/cinnamon
%_bindir/cinnamon-menu-editor
%_bindir/cinnamon-settings
%_bindir/cinnamon-extension-tool
%config %_sysconfdir/gconf/schemas/cinnamon.schemas
%config %_sysconfdir/xdg/menus/cinnamon-applications.menu
%config %_sysconfdir/xdg/menus/cinnamon-settings.menu
%_datadir/desktop-directories/cinnamon-*.directory
%_datadir/glib-2.0/schemas/*.xml
%_datadir/applications/cinnamon.desktop
%_datadir/applications/cinnamon-settings.desktop
%_x11sysconfdir/wmsession.d/02Cinnamon
%_datadir/gnome-session/sessions/cinnamon.session
%_datadir/cinnamon/
%_datadir/cinnamon-menu-editor/
%_datadir/cinnamon-settings/
%_datadir/dbus-1/services/org.Cinnamon.CalendarServer.service
%_datadir/dbus-1/services/org.Cinnamon.HotplugSniffer.service
%_libdir/cinnamon/
%_libexecdir/cinnamon-calendar-server
%_libexecdir/cinnamon-perf-helper
%_libexecdir/cinnamon-hotplug-sniffer
%_mandir/man1/%name.1.gz
%_libdir/browser-plugins/libcinnamon*.so
%exclude %_libdir/browser-plugins/libcinnamon*.la

%changelog
* Tue Jun 12 2012 Yuri N. Sedunov <aris@altlinux.org> 1.4.0-alt7
- used %%set_typelibdir macros

* Wed May 30 2012 Michael Shigorin <mike@altlinux.org> 1.4.0-alt6
- rebuilt for Sisyphus (closes: #27381)

* Tue May 29 2012 Vladimir Didenko <vladimir.didenko@gmail.com> 1.4.0-alt5
- update to 1.4-UP3
- window-attention.patch that disables annoying window popups

* Wed May 23 2012 Vladimir Didenko <vladimir.didenko@gmail.com> 1.4.0-alt4
- update to 1.4-UP1

* Thu May 10 2012 Michael Shigorin <mike@altlinux.org> 1.4.0-alt3.1
- changed wmsession priority from 05 to 02 so that
  02Cinnamon comes just before 02Gnome (the rationale
  being that if this GNOME3 extension is installed it's
  likely to have been desired in the first place)

* Sat Apr 14 2012 Yuri N. Sedunov <aris@altlinux.org> 1.4.0-alt3
- removed harmful gir_bluetooth.patch
- removed menu.patch, used system gnome3-applications.menu instead
- DM integration
- updated buildreqs, reqs
- and other small cleanups

* Thu Apr 12 2012 Michael Shigorin <mike@altlinux.org> 1.4.0-alt2
- courtesy of Vladimir Didenko:
  + added missing dependencies for cinnamon-settings to work
  + moved session desktop file to %_x11sysconfdir/sessions/

* Wed Apr 11 2012 Michael Shigorin <mike@altlinux.org> 1.4.0-alt1
- rebuilt for Sisyphus
- minor spec cleanup

* Mon Apr 09 2012 Vyacheslav Dikonov <slava@altlinux.ru> 1.4.0-slava1
- ALTLinux build

* Sat Mar 31 2012 Leigh Scott <leigh123linux@fedoraproject.org> - 1.4.0-3
- rebuild for gnome 3.4.0 changes
- patch so gir can find bluetooth-applet libs

* Tue Mar 13 2012 Leigh Scott <leigh123linux@fedoraproject.org> - 1.4.0-1
- update to 1.4.0

* Mon Feb 20 2012 Leigh Scott <leigh123linux@fedoraproject.org> - 1.3.1-1
- update to 1.3.1
- remove static lib
- remove mozilla plugin

* Fri Feb 17 2012 Leigh Scott <leigh123linux@fedoraproject.org> - 1.3.0-1
- update to 1.3.0 release

* Mon Jan 22 2012 Leigh Scott <leigh123linux@fedoraproject.org> - 1.2.0-1
- update to 1.2.0 release
- add build requires muffin-devel
- add Br libgudev1-devel
- add only-show-in=GNOME to settings desktop file
- make changes for source changes, applets, settings and session added
- delete session files and use my own
- move settings from lib to usr (it had no libs)
- replace menu icon
- change description

* Wed Jan 04 2012 Leigh Scott <leigh123linux@fedoraproject.org> - 1.1.3-2
- add requires gnome-session
- clean up spec file ready for review

* Mon Jan 02 2012 Leigh Scott <leigh123linux@fedoraproject.org> - 1.1.3-1
- update to version 1.1.3

* Sun Jan 01 2012 Leigh Scott <leigh123linux@fedoraproject.org> - 1.1.2-2
- fix firefox launchers

* Fri Dec 30 2011 Leigh Scott <leigh123linux@fedoraproject.org> - 1.1.2-1
- first build based on gnome-shell srpm
- add session files


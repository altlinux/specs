%define _libexecdir %_prefix/libexec
%define _basename mate-screensaver

Name: %{_basename}-pam
Version: 1.20.0
Release: alt2
Epoch: 1
Summary: MATE Screensaver
License: GPLv2+ and LGPLv2+
Group: Graphical desktop/MATE
Url: http://mate-desktop.org/

Requires: pam_gnome-keyring
Provides: %_basename
Conflicts: %_basename
Obsoletes: %_basename

Source: %name-%version.tar
Patch: %{_basename}-%version-%release.patch
Patch1: mate-screensaver-1.9.0-dbus-lock-unescape-path.patch
Patch2: mate-screensaver-1.20.0-alt-pam-auth.patch

BuildRequires: mate-common intltool libSM-devel libXScrnSaver-devel libXxf86misc-devel libXxf86vm-devel
BuildRequires: libdbus-glib-devel libmatekbd-devel libnotify-devel libpam-devel libsystemd-devel
BuildRequires: mate-desktop-devel mate-menus-devel xmlto

%description
mate-screensaver is a screen saver and locker that aims to have
simple, sane, secure defaults and be well integrated with the desktop.

%package devel
Group: Development/C
Summary: Development files for mate-screensaver

%description devel
Development files for mate-screensaver

%prep
%setup -q
%patch -p1
%patch1 -p0
%patch2 -p1

%build
%autoreconf
%configure \
	--disable-schemas-compile \
	--enable-docbook-docs \
	--with-mit-ext \
	--with-xf86gamma-ext \
	--with-libgl \
	--with-shadow \
	--enable-authentication-scheme=pam \
	--enable-locking \
	--with-systemd \
	--without-console-kit

%make_build

%install
%make DESTDIR=%buildroot install

%find_lang %{_basename} --with-gnome --all-name

%files -f %{_basename}.lang
%doc AUTHORS NEWS README COPYING
%_docdir/%{_basename}-%version
%_sysconfdir/pam.d/%{_basename}
%_sysconfdir/xdg/menus/mate-screensavers.menu
%_sysconfdir/xdg/autostart/%{_basename}.desktop
%_bindir/mate-screensaver*
%_libexecdir/mate-screensaver*
%_desktopdir/%{_basename}-preferences.desktop
%_desktopdir/screensavers/*.desktop
%_datadir/%{_basename}
%_datadir/backgrounds/cosmos
%_datadir/pixmaps/mate-logo-white.svg
%_datadir/pixmaps/gnome-logo-white.svg
%_datadir/desktop-directories/mate-screensaver.directory
%_datadir/glib-2.0/schemas/org.mate.screensaver.gschema.xml
%_datadir/mate-background-properties/cosmos.xml
%_datadir/dbus-1/services/org.mate.ScreenSaver.service
%_man1dir/*.1*

%files devel
%_libdir/pkgconfig/*.pc

%changelog
* Wed Oct 24 2018 Paul Wolneykien <manowar@altlinux.org> 1:1.20.0-alt2
- Added PAM-auth patches.

* Thu Mar 15 2018 Valery Inozemtsev <shrek@altlinux.ru> 1:1.20.0-alt1
- initial build from git.mate-desktop.org

* Thu Feb 22 2018 Vladimir D. Seleznev <vseleznv@altlinux.org> 1.20.0-alt1_1
- new fc release

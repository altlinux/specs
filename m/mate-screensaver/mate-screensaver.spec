%define _libexecdir %_prefix/libexec

Name: mate-screensaver
Version: 1.20.3
Release: alt1
Epoch: 2
Summary: MATE Screensaver
License: GPLv2+ and LGPLv2+
Group: Graphical desktop/MATE
Url: http://mate-desktop.org/
Packager: Valery Inozemtsev <shrek@altlinux.ru>

Requires: pam_gnome-keyring

Source: %name-%version.tar
Patch: %name-%version-%release.patch

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

%build
%autoreconf
%configure \
	--disable-schemas-compile \
	--enable-docbook-docs \
	--with-mit-ext \
	--with-xf86gamma-ext \
	--with-libgl \
	--with-shadow \
	--enable-authentication-scheme=helper \
	--with-passwd-helper=%_libexecdir/%name/%name-chkpwd-helper \
	--enable-locking \
	--with-systemd \
	--without-console-kit

%make_build
gcc -o %name-chkpwd-helper $RPM_OPT_FLAGS unix2_chkpwd.c -lpam

%install
%make DESTDIR=%buildroot install
install -m755 %name-chkpwd-helper %buildroot%_libexecdir/%name/
install -m644 -pD doc/mate-screensaver.html %buildroot%_datadir/doc/mate-screensaver/mate-screensaver.html

%find_lang %name --with-gnome --all-name

%files -f %name.lang
%doc AUTHORS NEWS README COPYING
%_docdir/%name
%_sysconfdir/pam.d/%name
%_sysconfdir/xdg/menus/mate-screensavers.menu
%_sysconfdir/xdg/autostart/%name.desktop
%_bindir/mate-screensaver*
%_libexecdir/mate-screensaver*
%attr(2511,root,chkpwd) %_libexecdir/%name/%name-chkpwd-helper
%_desktopdir/%name-preferences.desktop
%_desktopdir/screensavers/*.desktop
%_datadir/%name
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
* Mon Dec 24 2018 Valery Inozemtsev <shrek@altlinux.ru> 2:1.20.3-alt1
- 1.20.3

* Wed Dec 12 2018 Valery Inozemtsev <shrek@altlinux.ru> 2:1.20.2-alt1
- 1.20.2

* Thu Mar 15 2018 Valery Inozemtsev <shrek@altlinux.ru> 1:1.20.0-alt1
- initial build from git.mate-desktop.org

* Thu Feb 22 2018 Vladimir D. Seleznev <vseleznv@altlinux.org> 1.20.0-alt1_1
- new fc release

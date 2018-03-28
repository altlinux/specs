%define rname mate-session-manager

Name: mate-session
Version: 1.20.0
Release: alt2
Epoch: 1
Summary: MATE Desktop session manager
License: GPLv2+
Group: Graphical desktop/MATE
Url: http://mate-desktop.org/
Packager: Valery Inozemtsev <shrek@altlinux.ru>

Requires: mate-control-center mate-polkit mate-desktop polkit

Source: %rname-%version.tar
Patch: %rname-%version-%release.patch

BuildRequires: mate-common intltool libSM-devel libXtst-devel libdbus-glib-devel libgtk+3-devel libsystemd-devel libwrap-devel xmlto xorg-xtrans-devel

%description
This package contains a session that can be started from a display
manager such as MDM. It will load all necessary applications for a
full-featured user session.

%prep
%setup -q -n %rname-%version
%patch -p1

%build
%autoreconf
%configure \
	--enable-ipv6 \
	--with-default-wm=marco \
	--with-systemd \
	--enable-docbook-docs \
	--disable-schemas-compile

%make_build

%install
%make DESTDIR=%buildroot install

mkdir -p %buildroot%_sysconfdir/X11/wmsession.d/
cat << __EOF__ > %buildroot%_sysconfdir/X11/wmsession.d/02Mate
NAME=Mate
ICON=%_iconsdir/hicolor/scalable/apps/mate.svg
DESC=Mate (Gnome 2) Environment
EXEC=%_bindir/mate-session
SCRIPT:
exec %_bindir/mate-session
__EOF__

%find_lang %rname --with-gnome --all-name

%files -f %rname.lang
%doc AUTHORS COPYING README
%_docdir/%rname
%_sysconfdir/X11/wmsession.d/*Mate*
%_bindir/mate-*
%_desktopdir/mate-session-properties.desktop
%_datadir/%rname
%_iconsdir/hicolor/*/apps/*.*
%_datadir/glib-2.0/schemas/org.mate.session.gschema.xml
%_datadir/xsessions/mate.desktop
%_man1dir/*.1*

%changelog
* Wed Mar 28 2018 Valery Inozemtsev <shrek@altlinux.ru> 1:1.20.0-alt2
- mate.desktop: add path to mate-session

* Thu Mar 15 2018 Valery Inozemtsev <shrek@altlinux.ru> 1:1.20.0-alt1
- initial build from git.mate-desktop.org

* Tue Feb 20 2018 Vladimir D. Seleznev <vseleznv@altlinux.org> 1.20.0-alt1_1
- new fc release

Name: mate-media
Version: 1.20.0
Release: alt1
Epoch: 1
Summary: MATE media programs
License: GPLv2+ and LGPLv2+
Group: Graphical desktop/MATE
Url: http://mate-desktop.org/
Packager: Valery Inozemtsev <shrek@altlinux.ru>

Source: %name-%version.tar
Patch: %name-%version-%release.patch

BuildRequires: mate-common intltool libcanberra-gtk3-devel libmatemixer-devel libxml2-devel mate-desktop-devel

%description
This package contains a few media utilities for the MATE desktop,
including a volume control.

%prep
%setup -q
%patch -p1

%build
%autoreconf
%configure \
	--disable-static \
	--disable-schemas-compile

%make_build

%install
%make DESTDIR=%buildroot install

%find_lang %name --with-gnome --all-name

%files -f %{name}.lang
%doc AUTHORS COPYING NEWS README
%_sysconfdir/xdg/autostart/mate-volume-control-applet.desktop
%_bindir/mate-volume-control
%_bindir/mate-volume-control-applet
%_datadir/%name
%_datadir/sounds/mate
%_desktopdir/mate-volume-control.desktop
%_man1dir/*.1*

%changelog
* Tue Mar 13 2018 Valery Inozemtsev <shrek@altlinux.ru> 1:1.20.0-alt1
- initial build from git.mate-desktop.org

* Thu Feb 22 2018 Vladimir D. Seleznev <vseleznv@altlinux.org> 1.20.0-alt1_1
- new fc release

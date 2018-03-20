Name: mate-calc
Version: 1.20.0
Release: alt1
Epoch: 1
Summary: MATE Desktop calculator
License: GPLv2+
Group: Graphical desktop/MATE
Url: http://mate-desktop.org/
Packager: Valery Inozemtsev <shrek@altlinux.ru>

Source: %name-%version.tar
Patch: %name-%version-%release.patch

BuildRequires: mate-common intltool itstool libgtk+3-devel libxml2-devel yelp-tools

%description
mate-calc is a powerful graphical calculator with financial, logical and scientific modes.
It uses a multiple precision package to do its arithmetic to give a high degree of accuracy.

%prep
%setup -q
%patch -p1

%build
%autoreconf
%configure \
	--disable-schemas-compile

%make_build

%install
%make DESTDIR=%buildroot install

%find_lang %name --with-gnome --all-name

%files -f %name.lang
%doc AUTHORS COPYING README
%_bindir/*
%_datadir/appdata/%name.appdata.xml
%_desktopdir/%name.desktop
%_datadir/glib-2.0/schemas/org.mate.calc.gschema.xml
%_datadir/%name
%_man1dir/*.1*

%changelog
* Tue Mar 20 2018 Valery Inozemtsev <shrek@altlinux.ru> 1:1.20.0-alt1
- initial build from git.mate-desktop.org

* Thu Feb 22 2018 Vladimir D. Seleznev <vseleznv@altlinux.org> 1.20.0-alt1_1
- new fc release

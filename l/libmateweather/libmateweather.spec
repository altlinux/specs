Name: libmateweather
Version: 1.26.0
Release: alt4
Epoch: 1
Summary: Libraries to allow MATE Desktop to display weather information
License: GPLv2+ and LGPLv2+
Group: System/Libraries
Url: http://mate-desktop.org/
Packager: Valery Inozemtsev <shrek@altlinux.ru>

Source: %name-%version.tar
Patch: %name-%version-%release.patch

Requires: %name-data = %epoch:%version-%release

BuildRequires: mate-common gtk-doc libgtk+3-devel libsoup-devel libxml2-devel

%description
Libraries to allow MATE Desktop to display weather information

%package data
Group: System/Libraries
Summary: Data files for the libmateweather
BuildArch: noarch

%description data
This package contains shared data needed for libmateweather

%package devel
Group: Development/C
Summary:  Development files for libmateweather

%description devel
Development files for libmateweather

%prep
%setup -q
%patch -p1

%build
%autoreconf
%configure \
	--enable-gtk-doc-html \
	--enable-locations-compression \
	--disable-static \
	--disable-schemas-compile

%make_build

%install
%make DESTDIR=%buildroot install

%find_lang %name --with-gnome --all-name

%files
%doc AUTHORS COPYING README
%_libdir/%name.so.*
%_datadir/glib-2.0/schemas/org.mate.weather.gschema.xml

%files data -f %name.lang
%_iconsdir/hicolor/*/status/*
%_datadir/%name

%files devel
%_includedir/%name
%_libdir/%name.so
%_pkgconfigdir/*.pc

%changelog
* Mon Dec 12 2022 Valery Inozemtsev <shrek@altlinux.ru> 1:1.26.0-alt4
- rebuild

* Wed Oct 26 2022 Valery Inozemtsev <shrek@altlinux.ru> 1:1.26.0-alt3
- merged p10 branch

* Tue Sep 27 2022 Valery Inozemtsev <shrek@altlinux.ru> 1:1.26.0-alt2
- fixed Simferopol location

* Fri Aug 06 2021 Valery Inozemtsev <shrek@altlinux.ru> 1:1.26.0-alt1
- 1.26.0

* Fri Aug 14 2020 Valery Inozemtsev <shrek@altlinux.ru> 1:1.24.1-alt1
- 1.24.1

* Tue Feb 25 2020 Valery Inozemtsev <shrek@altlinux.ru> 1:1.24.0-alt1
- 1.24.0

* Tue Oct 15 2019 Valery Inozemtsev <shrek@altlinux.ru> 1:1.22.1-alt1
- 1.22.1

* Mon Mar 04 2019 Valery Inozemtsev <shrek@altlinux.ru> 1:1.22.0-alt1
- 1.22.0

* Tue Dec 18 2018 Valery Inozemtsev <shrek@altlinux.ru> 1:1.20.2-alt1
- 1.20.2

* Sun Oct 14 2018 Igor Vlasenko <viy@altlinux.ru> 1:1.20.1-alt1.qa1
- NMU: applied repocop patch

* Fri Jun 15 2018 Valery Inozemtsev <shrek@altlinux.ru> 1:1.20.1-alt1
- 1.20.1

* Mon Mar 12 2018 Valery Inozemtsev <shrek@altlinux.ru> 1:1.20.0-alt1
- initial build from git.mate-desktop.org

* Mon Feb 19 2018 Vladimir D. Seleznev <vseleznv@altlinux.org> 1.20.0-alt1_1
- new fc release

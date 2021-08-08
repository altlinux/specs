Name: libmatekbd
Version: 1.26.0
Release: alt1
Epoch: 1
Summary: Libraries for mate kbd
License: GPLv2+
Group: System/Libraries
Url: http://mate-desktop.org/
Packager: Valery Inozemtsev <shrek@altlinux.ru>

Source: %name-%version.tar
Patch: %name-%version-%release.patch

Requires: iso-codes

BuildRequires: mate-common libICE-devel libgtk+3-gir-devel libxklavier-gir-devel

%description
Libraries for matekbd

%package devel
Group: Development/C
Summary: Development libraries for libmatekbd

%description devel
Development libraries for libmatekbd

%prep
%setup -q
%patch -p1

%build
%autoreconf
%configure \
	--disable-static \
	--disable-schemas-compile \
	--enable-introspection

%make_build

%install
%make DESTDIR=%buildroot install

%find_lang %name --with-gnome --all-name

%files -f %name.lang
%doc AUTHORS COPYING README
%_libdir/libmatekbd*.so.*
%_libdir/girepository-1.0/Matekbd-1.0.typelib
%_datadir/glib-2.0/schemas/org.mate.peripherals*.xml

%files devel
%_includedir/%name
%_libdir/libmatekbd*.so
%_pkgconfigdir/libmatekbd*.pc
%_datadir/gir-1.0/Matekbd-1.0.gir

%changelog
* Thu Aug 05 2021 Valery Inozemtsev <shrek@altlinux.ru> 1:1.26.0-alt1
- 1.26.0

* Fri Aug 14 2020 Valery Inozemtsev <shrek@altlinux.ru> 1:1.24.1-alt1
- 1.24.1

* Tue Feb 25 2020 Valery Inozemtsev <shrek@altlinux.ru> 1:1.24.0-alt1
- 1.24.0

* Mon Mar 04 2019 Valery Inozemtsev <shrek@altlinux.ru> 1:1.22.0-alt1
- 1.22.0

* Fri Jun 15 2018 Valery Inozemtsev <shrek@altlinux.ru> 1:1.20.2-alt1
- 1.20.2

* Tue Mar 27 2018 Valery Inozemtsev <shrek@altlinux.ru> 1:1.20.1-alt1
- 1.20.1

* Tue Mar 06 2018 Valery Inozemtsev <shrek@altlinux.ru> 1:1.20.0-alt1
- initial build from git.mate-desktop.org

* Mon Feb 19 2018 Vladimir D. Seleznev <vseleznv@altlinux.org> 1.20.0-alt1_1
- new fc release

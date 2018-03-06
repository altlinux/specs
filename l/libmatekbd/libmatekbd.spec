Name: libmatekbd
Version: 1.20.0
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

BuildRequires: mate-common intltool libICE-devel libgtk+3-gir-devel libxklavier-gir-devel

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
%_datadir/%name
%_datadir/glib-2.0/schemas/org.mate.peripherals-keyboard-xkb.gschema.xml

%files devel
%_includedir/%name
%_libdir/libmatekbd*.so
%_pkgconfigdir/libmatekbd*.pc
%_datadir/gir-1.0/Matekbd-1.0.gir

%changelog
* Tue Mar 06 2018 Valery Inozemtsev <shrek@altlinux.ru> 1:1.20.0-alt1
- initial build from git.mate-desktop.org

* Mon Feb 19 2018 Vladimir D. Seleznev <vseleznv@altlinux.org> 1.20.0-alt1_1
- new fc release

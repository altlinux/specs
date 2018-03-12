Name: libmatemixer
Version: 1.20.0
Release: alt1
Epoch: 1
Summary: Mixer library for MATE desktop
License: GPLv2+
Group: System/Libraries
Url: http://mate-desktop.org/
Packager: Valery Inozemtsev <shrek@altlinux.ru>

Source: %name-%version.tar
Patch: %name-%version-%release.patch

BuildRequires:  mate-common gtk-doc intltool libalsa-devel libpulseaudio-devel

%description
libmatemixer is a mixer library for MATE desktop.
It provides an abstract API allowing access to mixer functionality
available in the PulseAudio and ALSA sound systems.

%package devel
Group: Development/C
Summary:  Development libraries for libmatemixer

%description devel
Development libraries for libmatemixer

%prep
%setup -q
%patch -p1

%build
%autoreconf
%configure \
	--disable-static \
	--enable-pulseaudio \
	--enable-alsa \
	--enable-gtk-doc

%make_build

%install
%make DESTDIR=%buildroot install

%find_lang %name --with-gnome --all-name

%files -f %name.lang
%doc AUTHORS COPYING NEWS README
%_libdir/%name.so.*
%_libdir/%name

%files devel
%_includedir/mate-mixer/
%_libdir/%name.so
%_pkgconfigdir/*.pc
%_datadir/gtk-doc/html/%name

%changelog
* Mon Mar 12 2018 Valery Inozemtsev <shrek@altlinux.ru> 1:1.20.0-alt1
- initial build from git.mate-desktop.org

* Tue Feb 20 2018 Vladimir D. Seleznev <vseleznv@altlinux.org> 1.20.0-alt1_1
- new fc release

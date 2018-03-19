Name: spectrum3d
Version: 2.7.2
Release: alt1
Summary: 3D audio spectrum analyser in real time
Group: Sound
License: GPLv3
Url: http://spectrum3d.sourceforge.net
Source: %name-%version.tar.gz
#:! for N in `grep -rl 'g_build_filename.*"icons"' ~/RPM/BUILD/spectrum3d-2*[0-9]`; do sed -Ei 's/(g_build_filename .*, "icons",)/\1 "spectrum3d",/' $N; done
Patch: spectrum3d-2.7.1-iconspath.patch

# Automatically added by buildreq on Thu Sep 18 2014
# optimized out: at-spi2-atk fontconfig glib2-devel libGL-devel libGLU-devel libX11-devel libat-spi2-core libatk-devel libcairo-devel libcairo-gobject libcairo-gobject-devel libcloog-isl4 libgdk-pixbuf libgdk-pixbuf-devel libgio-devel libpango-devel libwayland-client libwayland-cursor libwayland-server libxml2-devel pkg-config xorg-xproto-devel
BuildRequires: gstreamer-devel libSDL-devel libgtk+3-devel libjack-devel

%description
Spectrum 3D displays a 3D audio spectrogram in real time; the source can
be either the microphone or an audio file; it is also possible to record
a file and to have it analysed; so analysis can be done done on the fly
(harmonics are displayed while the audio file is being played), or
before the file is being played (in that case, the analysis of the whole
will be performed and displayed, then the file can be played
afterwards).

%prep
%setup
%patch -p1

%build
%configure
%make_build icondir=%_iconsdir/%name svgicopndir=%_iconsdir/%name

%install
%makeinstall icondir=%buildroot%_iconsdir/%name svgicondir=%buildroot%_iconsdir/%name
install -D data/spectrum3d.png %buildroot%_liconsdir/spectrum3d.png
install -D data/spectrum3d.svg %buildroot%_iconsdir/hicolor/scalable/apps/spectrum3d.png

%files
%doc README*
%_bindir/*
%_desktopdir/*
%_iconsdir/*/*/*/*
%_iconsdir/%name

%changelog
* Tue Feb 20 2018 Fr. Br. George <george@altlinux.ru> 2.7.2-alt1
- Autobuild version bump to 2.7.2

* Wed Sep 20 2017 Fr. Br. George <george@altlinux.ru> 2.7.1-alt1
- Autobuild version bump to 2.7.1

* Tue Feb 03 2015 Fr. Br. George <george@altlinux.ru> 2.5.0-alt1
- Autobuild version bump to 2.5.0
- Fix icon path patch

* Thu Sep 18 2014 Fr. Br. George <george@altlinux.ru> 2.4.0-alt1
- Autobuild version bump to 2.4.0
- Fix icon path

* Thu Sep 18 2014 Fr. Br. George <george@altlinux.ru> 2.3.0-alt1
- Initial build


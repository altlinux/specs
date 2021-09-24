Name: gqrx
Version: 2.14.4
Release: alt2

Summary: Software defined radio receiver powered by GNU Radio and Qt.
License: GPL-3.0
Group: Other
Url: https://github.com/csete/gqrx

Packager: Anton Midyukov <antohami@altlinux.org>

Source: %name-%version.tar

BuildRequires (pre): rpm-macros-cmake
BuildRequires: gcc-c++
BuildRequires: gnuradio-devel
BuildRequires: gr-osmosdr-devel
BuildRequires: libfftw3-devel
BuildRequires: libalsa-devel
BuildRequires: libjack-devel
BuildRequires: liborc-devel
BuildRequires: qt5-base-devel
BuildRequires: qt5-svg-devel
BuildRequires: libpulseaudio-devel
BuildRequires: pkgconfig(libpulse)
BuildRequires: pkgconfig(libpulse-simple)
BuildRequires: git
BuildRequires: pkgconfig(gnuradio-analog)
BuildRequires: pkgconfig(gnuradio-blocks)
BuildRequires: pkgconfig(gnuradio-digital)
BuildRequires: pkgconfig(gnuradio-filter)
BuildRequires: pkgconfig(gnuradio-fft)
BuildRequires: pkgconfig(gnuradio-runtime)
BuildRequires: pkgconfig(gnuradio-osmosdr)
BuildRequires: pkgconfig(portaudio-2.0)
BuildRequires: boost-devel
BuildRequires: desktop-file-utils
BuildRequires: libappstream-glib
BuildRequires: libsndfile-devel
BuildRequires: libnumpy-py3-devel
BuildRequires: libunwind-devel

# uhd not available for %ix86 %arm
ExcludeArch: %ix86 %arm

%description
%summary

%prep
%setup

%build
%cmake
%cmake_build
sed -i -e 's/Accessories;//g' gqrx.desktop

%install
%cmakeinstall_std

# icon
install -Dpm 644 resources/icons/gqrx.svg \
                 %buildroot%_datadir/icons/hicolor/scalable/apps/gqrx.svg
install -Dpm 644 %name.appdata.xml \
                 %buildroot%_datadir/appdata/%name.appdata.xml

# desktop-file
desktop-file-install \
--dir=%buildroot%_datadir/applications gqrx.desktop

%check
#This appears to be borked
appstream-util validate-relax --nonet \
               %buildroot/%_datadir/appdata/*.appdata.xml

%files
%_bindir/%name
%_datadir/applications/%name.desktop
%_datadir/appdata/%name.appdata.xml
%_datadir/icons/hicolor/scalable/apps/%name.svg
%doc COPYING LICENSE-CTK README.md

%changelog
* Fri Sep 24 2021 Anton Midyukov <antohami@altlinux.org> 2.14.4-alt2
- ExcludeArch: %ix86 %arm

* Sat May 08 2021 Anton Midyukov <antohami@altlinux.org> 2.14.4-alt1
- new version 2.14.4

* Wed Jun 10 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 2.12.1-alt2
- Rebuilt with boost-1.73.0.

* Fri May 22 2020 Anton Midyukov <antohami@altlinux.org> 2.12.1-alt1
- new version 2.12.1

* Tue Nov 26 2019 Anton Midyukov <antohami@altlinux.org> 2.11.5-alt2
- rebuild with gnuradio 3.8

* Sat Dec 29 2018 Anton Midyukov <antohami@altlinux.org> 2.11.5-alt1
- new version 2.11.5

* Thu May 31 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 2.11.4-alt1.1
- NMU: rebuilt with boost-1.67.0

* Mon Apr 23 2018 Anton Midyukov <antohami@altlinux.org> 2.11.4-alt1
- new version 2.11.4

* Tue Mar 27 2018 Anton Midyukov <antohami@altlinux.org> 2.11.2-alt1
- new version 2.11.2

* Sun Oct 22 2017 Anton Midyukov <antohami@altlinux.org> 2.8-alt1
- Initial build for Sisyphus

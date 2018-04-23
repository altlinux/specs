Name: gqrx
Version: 2.11.4
Release: alt1

Summary: Software defined radio receiver powered by GNU Radio and Qt.
License: GPL-3.0
Group: Other
Url: https://github.com/csete/gqrx

Packager: Anton Midyukov <antohami@altlinux.org>

Source: %name-%version.tar

BuildRequires (pre): rpm-macros-cmake
BuildRequires: gcc-c++
BuildRequires: libgnuradio-devel
BuildRequires: qt5-base-devel
BuildRequires: qt5-svg-devel
BuildRequires: libpulseaudio-devel
BuildRequires: pkgconfig(libpulse)
BuildRequires: pkgconfig(libpulse-simple)
BuildRequires: git
BuildRequires: gr-osmosdr-devel
BuildRequires: pkgconfig(gnuradio-analog)
BuildRequires: pkgconfig(gnuradio-blocks)
BuildRequires: pkgconfig(gnuradio-digital)
BuildRequires: pkgconfig(gnuradio-filter)
BuildRequires: pkgconfig(gnuradio-fft)
BuildRequires: pkgconfig(gnuradio-runtime)
BuildRequires: pkgconfig(gnuradio-osmosdr)
BuildRequires: boost-devel
BuildRequires: desktop-file-utils
BuildRequires: libappstream-glib

%description
%summary

%prep
%setup

%build
#qmake_qt5 PREFIX=%_prefix
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
* Mon Apr 23 2018 Anton Midyukov <antohami@altlinux.org> 2.11.4-alt1
- new version 2.11.4

* Tue Mar 27 2018 Anton Midyukov <antohami@altlinux.org> 2.11.2-alt1
- new version 2.11.2

* Sun Oct 22 2017 Anton Midyukov <antohami@altlinux.org> 2.8-alt1
- Initial build for Sisyphus

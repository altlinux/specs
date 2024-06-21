Name: padthv1
Version: 1.0.0
Release: alt1

Summary: Polyphonic additive synthesizer
License: GPL-2.0
Group: Sound
Url: https://padthv1.sourceforge.io/

Source: %name-%version-%release.tar

BuildRequires: cmake gcc-c++
BuildRequires: pkgconfig(alsa)
BuildRequires: pkgconfig(fftw3f)
BuildRequires: pkgconfig(jack)
BuildRequires: pkgconfig(liblo)
BuildRequires: pkgconfig(lv2)
BuildRequires: pkgconfig(Qt6)
BuildRequires: pkgconfig(Qt6Gui)
BuildRequires: pkgconfig(Qt6Svg)
BuildRequires: pkgconfig(Qt6Widgets)
BuildRequires: pkgconfig(Qt6Xml)

%package -n lv2-padthv1-plugin
Summary: Polyphonic additive synthesizer -- LV2 plugin
Group: Sound


%define desc\
An old-school polyphonic additive synthesizer with stereo fx,\
based on the PADsynth algorithm, by Paul Nasca, as a special\
variant of additive synthesis.

%description %desc
%description -n lv2-padthv1-plugin %desc
This package contains LV2 plugin.

%prep
%setup

%build
%cmake
%cmake_build

%install
%cmake_install

%files
%doc LICENSE README
%_bindir/padthv1_jack
%_datadir/padthv1
%_datadir/metainfo/*.xml
%_datadir/mime/packages/*.xml
%_desktopdir/*.desktop
%_iconsdir/*/*/*/*.png
%_iconsdir/*/*/*/*.svg
%_man1dir/*.1*

%files -n lv2-padthv1-plugin
%_libdir/lv2/*
%_datadir/padthv1

%changelog
* Fri Jun 21 2024 Sergey Bolshakov <sbolshakov@altlinux.org> 1.0.0-alt1
- 1.0.0 released

* Fri Apr 12 2024 Sergey Bolshakov <sbolshakov@altlinux.org> 0.9.90-alt1
- 0.9.90 released

* Thu Mar 21 2024 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.9.34-alt1
- initial

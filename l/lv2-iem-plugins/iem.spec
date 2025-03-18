Name: lv2-iem-plugins
Version: 1.14.1
Release: alt1

Summary: Ambisonic plugin suite
License: GPLv3
Group: Sound
Url: https://plugins.iem.at/

ExclusiveArch: aarch64 x86_64

Source0: %name-%version-%release.tar
Source1: deps-%version-%release.tar

BuildRequires: cmake gcc-c++
BuildRequires: pkgconfig(alsa)
BuildRequires: pkgconfig(fftw3)
BuildRequires: pkgconfig(freetype2)
BuildRequires: pkgconfig(gl)
BuildRequires: pkgconfig(jack)
BuildRequires: pkgconfig(xcursor)
BuildRequires: pkgconfig(xext)
BuildRequires: pkgconfig(xinerama)
BuildRequires: pkgconfig(xrandr)
BuildRequires: pkgconfig(xrender)

%description
%summary
The suite provides plug-ins for a full Ambisonic production: encoders, reverbs,
dynamics including limiter and multi-band compression, rotators, and decoders
for both headphones and arbitrary loudspeaker layouts, and many more.

%prep
%setup -a1
sed -ri '/JUCE_LV2_COPY_DIR/ s,"[^"]+","%buildroot%_libdir/lv2",' CMakeLists.txt

%install
%cmake -DIEM_BUILD_LV2=ON -DIEM_BUILD_STANDALONE=OFF -DIEM_POST_BUILD_INSTALL=SYSTEM
%cmake_build

%files
%doc LICENSE README*
%_libdir/lv2/*

%changelog
* Tue Mar 18 2025 Sergey Bolshakov <sbolshakov@altlinux.org> 1.14.1-alt1
- 1.14.1 released


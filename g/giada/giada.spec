Name: giada
Version: 1.0.0
Release: alt1

Summary: Giada - Your Hardcore Loop Machine
License: GPLv3
Group: Sound
Url: https://www.giadamusic.com/

ExclusiveArch: aarch64 x86_64

Source0: %name-%version-%release.tar
Source1: deps-%version-%release.tar

BuildRequires: cmake gcc-c++
BuildRequires: pkgconfig(alsa)
BuildRequires: pkgconfig(flac)
BuildRequires: pkgconfig(fmt)
BuildRequires: pkgconfig(fontconfig)
BuildRequires: pkgconfig(jack)
BuildRequires: pkgconfig(libpulse)
BuildRequires: pkgconfig(nlohmann_json)
BuildRequires: pkgconfig(opus)
BuildRequires: pkgconfig(rtmidi)
BuildRequires: pkgconfig(samplerate)
BuildRequires: pkgconfig(sndfile)
BuildRequires: pkgconfig(xcursor)
BuildRequires: pkgconfig(xfixes)
BuildRequires: pkgconfig(xft)
BuildRequires: pkgconfig(xinerama)
BuildRequires: pkgconfig(xpm)
BuildRequires: pkgconfig(xrandr)
BuildRequires: pkgconfig(xrender)

%description
Giada is an open source, minimalistic and hardcore music production tool.
Designed for DJs, live performers and electronic musicians.

%prep
%setup
tar ixf %SOURCE1

%build
%cmake  -DWITH_VST3=ON \
        -DWITH_ALSA=ON \
        -DWITH_PULSE=ON \
        -DWITH_JACK=ON
%cmake_build

%install
%cmake_install
rm -rf %buildroot%_prefix/{bin,include,lib/cmake}/JUCE*

%files
%doc README*
%_bindir/giada
%_desktopdir/*desktop
%_iconsdir/*/*/*/*.svg
%_datadir/metainfo/*.xml

%changelog
* Wed Mar 20 2024 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.0.0-alt1
- initial

Name: helio
Version: 3.13
Release: alt1

Summary: Music sequencer for desktop and mobile platforms
License: GPLv3
Group: Sound
Url: https://helio.fm/

Source0: %name-%version-%release.tar
Source1: deps-%version-%release.tar

ExclusiveArch: aarch64 x86_64

BuildRequires: cmake gcc-c++
BuildRequires: pkgconfig(alsa)
BuildRequires: pkgconfig(fmt)
BuildRequires: pkgconfig(freetype2)
BuildRequires: pkgconfig(gl)
BuildRequires: pkgconfig(jack)
BuildRequires: pkgconfig(samplerate)
BuildRequires: pkgconfig(xcursor)
BuildRequires: pkgconfig(xinerama)
BuildRequires: pkgconfig(xrandr)
BuildRequires: pkgconfig(xrender)

%description
Helio is an attempt to rethink a music sequencer to create a tool that feels right.
It aims to be a modern music creation software, featuring linear-based/pattern-based
sequencer with clean UI, integrated version control, microtonal temperaments
support, small portable builds and more; mainly targeted at hobbyist composers,
game developers and indie artists.

%prep
%setup
tar ixf %SOURCE1
sed -i '/globalApplicationsDirectory/ s,"/usr","%_libdir",' \
	ThirdParty/JUCE/modules/juce_core/native/juce_linux_Files.cpp

%build
%make_build CFLAGS='%optflags' -C Projects/LinuxMakefile

%install
install -pm0755 -D Projects/LinuxMakefile/build/helio %buildroot%_bindir/helio
cp -av Projects/Deployment/Linux/Debian/x64/usr/share %buildroot%_prefix

%files
%doc CHANGELOG* LICENSE* README* Docs
%_bindir/helio
%_desktopdir/*.desktop
%_iconsdir/*/*/*/*.png

%changelog
* Wed Jul 17 2024 Sergey Bolshakov <sbolshakov@altlinux.org> 3.13-alt1
- initial

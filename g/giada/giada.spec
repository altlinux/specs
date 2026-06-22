Name: giada
Version: 1.5.0
Release: alt2

Summary: Giada - Your Hardcore Loop Machine
License: GPLv3
Group: Sound
URL: https://www.giadamusic.com/
VCS: https://github.com/monocasual/giada

ExclusiveArch: aarch64 x86_64

Source0: %name-%version.tar
Source1: deps-%version.tar

BuildRequires: cmake gcc-c++
BuildRequires: pkgconfig(alsa)
BuildRequires: pkgconfig(flac)
BuildRequires: pkgconfig(fmt)
BuildRequires: pkgconfig(fontconfig)
BuildRequires: pkgconfig(jack)
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
BuildRequires: pkgconfig(gl)
BuildRequires: pkgconfig(libjpeg)

%description
Giada is an open source, minimalistic and hardcore music production tool.
Designed for DJs, live performers and electronic musicians.

%prep
%setup -a1
grep -lr fmt::format src|xargs sed -i '/fmt\/core/ a#include <fmt/format.h>'

%build
%cmake  -DWITH_VST3=ON \
        -DWITH_ALSA=ON \
        -DWITH_PULSE=OFF \
        -DWITH_JACK=ON
%cmake_build

%install
%cmake_install
rm -rf %buildroot%_prefix/{bin,include,lib/cmake}/JUCE*
rm -rf %buildroot{%_includedir/FL,%_datadir/fltk}
rm -vf %buildroot{%_bindir/fltk*,%_libdir/libfltk*,%_mandir/man?/fltk*}

%files
%doc README*
%_bindir/giada
%_desktopdir/*desktop
%_iconsdir/*/*/*/*.svg
%_datadir/metainfo/*.xml

%changelog
* Mon Jun 22 2026 Sergey Bolshakov <sbolshakov@altlinux.org> 1.5.0-alt2
- fixed build with recent fmt

* Wed Jun 17 2026 Sergey Bolshakov <sbolshakov@altlinux.org> 1.5.0-alt1
- 1.5.0 released

* Thu Jun 04 2026 Sergey Bolshakov <sbolshakov@altlinux.org> 1.4.2-alt1
- 1.4.2 released

* Tue May 12 2026 Sergey Bolshakov <sbolshakov@altlinux.org> 1.4.1-alt1
- 1.4.1 released

* Wed Dec 10 2025 Sergey Bolshakov <sbolshakov@altlinux.org> 1.4.0-alt1
- 1.4.0 released

* Wed Oct 29 2025 Sergey Bolshakov <sbolshakov@altlinux.org> 1.3.1-alt1
- 1.3.1 released

* Fri Sep 19 2025 Sergey Bolshakov <sbolshakov@altlinux.org> 1.3.0-alt1
- 1.3.0 released

* Mon Jul 07 2025 Sergey Bolshakov <sbolshakov@altlinux.org> 1.2.1-alt1
- 1.2.1 released

* Tue Apr 22 2025 Sergey Bolshakov <sbolshakov@altlinux.org> 1.2.0-alt1
- 1.2.0 released

* Mon Feb 10 2025 Sergey Bolshakov <sbolshakov@altlinux.org> 1.1.1-alt1
- 1.1.1 released

* Mon Oct 28 2024 Sergey Bolshakov <sbolshakov@altlinux.org> 1.1.0-alt1
- 1.1.0 released

* Wed Mar 20 2024 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.0.0-alt1
- initial

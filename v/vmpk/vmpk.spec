Name: vmpk
Version: 0.9.1
Release: alt1

Summary: Virtual MIDI Piano Keyboard
License: GPLv3
Group: Sound
Url: https://vmpk.sourceforge.net/

Source: %name-%version-%release.tar

BuildRequires: cmake gcc-c++
BuildRequires: pkgconfig(Qt6)
BuildRequires: pkgconfig(Qt6Svg)
BuildRequires: pkgconfig(Qt6Linguist)
BuildRequires: pkgconfig(drumstick-alsa)
BuildRequires: pkgconfig(drumstick-rt)

%description
Virtual MIDI Piano Keyboard is a MIDI events generator and receiver.
It doesn't produce any sound by itself, but can be used to drive a MIDI
synthesizer (either hardware or software, internal or external).
You can use the computer's keyboard to play MIDI notes, and also the
mouse. You can use the Virtual MIDI Piano Keyboard to display the
played MIDI notes from another instrument or MIDI file player. To do
so, connect the other MIDI port to the input port of VMPK.

%prep
%setup

%build
%cmake
%cmake_build

%install
%cmakeinstall_std

%files
%doc AUTHORS COPYING NEWS README* TODO
%_bindir/vmpk
%_datadir/vmpk
%_datadir/metainfo/*.xml
%_iconsdir/*/*/*/*.*
%_desktopdir/*.desktop
%_man1dir/vmpk.1*

%changelog
* Thu Jan 09 2025 Sergey Bolshakov <sbolshakov@altlinux.org> 0.9.1-alt1
- 0.9.1 released

* Thu Nov 14 2024 Sergey Bolshakov <sbolshakov@altlinux.org> 0.9.0-alt1
- 0.9.0 released

* Sun Sep 22 2019 Vladimir D. Seleznev <vseleznv@altlinux.org> 0.7.2-alt1
- 0.7.2.

* Tue Feb 19 2019 Vladimir D. Seleznev <vseleznv@altlinux.org> 0.7.1-alt1
- 0.7.1.

* Fri Dec 16 2016 Vladimir D. Seleznev <vseleznv@altlinux.org> 0.6.2a-alt2
- changed BuildPreReq to BuildRequires(pre) in spec.
- packaged watch file.
- packaged repacked uncompressed tarball.
- added url in spec.

* Sun Jul 31 2016 Vladimir D. Seleznev <vseleznv@altlinux.org> 0.6.2a-alt1
- Initial build.

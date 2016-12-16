Name:           vmpk
Version:        0.6.2a
Release:        alt2

# repacked tarball http://sf.net/vmpk/%name-%version.tar.bz2
Source:         %name-%version.tar
Source1:	%name.watch

Summary:        Virtual MIDI Piano Keyboard
Url:		http://vmpk.sourceforge.net/
License:        GPLv3
Group:          Sound

Packager:       Vladimir D. Seleznev <vseleznv@altlinux.org>

BuildRequires(pre): rpm-macros-cmake
# Automatically added by buildreq on Sat Jul 30 2016
# optimized out: cmake-modules gcc-c++ libEGL-devel libGL-devel libdrumstick-rt1 libgpg-error libqt5-core libqt5-dbus libqt5-gui libqt5-network libqt5-svg libqt5-widgets libqt5-x11extras libqt5-xml libstdc++-devel libxcb-devel pkg-config python-base python-modules qt5-base-devel qt5-tools
BuildRequires: cmake drumstick-devel qt5-svg-devel qt5-tools-devel qt5-x11extras-devel
BuildRequires: xz

%description
Virtual MIDI Piano Keyboard is a MIDI events generator and receiver. It
doesn't produce any sound by itself, but can be used to drive a MIDI
synthesizer (either hardware or software, internal or external). You
can use the computer's keyboard to play MIDI notes, and also the
mouse. You can use the Virtual MIDI Piano Keyboard to display the
played MIDI notes from another instrument or MIDI file player. To do
so, connect the other MIDI port to the input port of VMPK.

%prep
%setup

%build
%cmake
%cmake_build
xz ChangeLog NEWS

%install
%cmakeinstall_std

%files
%doc AUTHORS
%doc ChangeLog*
%doc COPYING
%doc NEWS*
%doc README
%doc TODO

%_bindir/%name
%_man1dir/%name.1.*

%_datadir/%name

%_iconsdir/hicolor/*/apps/*
%_desktopdir/*


%changelog
* Fri Dec 16 2016 Vladimir D. Seleznev <vseleznv@altlinux.org> 0.6.2a-alt2
- changed BuildPreReq to BuildRequires(pre) in spec.
- packaged watch file.
- packaged repacked uncompressed tarball.
- added url in spec.

* Sun Jul 31 2016 Vladimir D. Seleznev <vseleznv@altlinux.org> 0.6.2a-alt1
- Initial build


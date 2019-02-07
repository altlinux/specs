%def_without jack
Name: din
Version: 39.0.1
Release: alt1
License: GPLv2
Summary: Edit waveforms in a GUI, and watch the sound change before your ears
Group: Sound
Source: %name-%version.tar.gz
Url: http://dinisnoise.org/

# Automatically added by buildreq on Wed May 23 2018
# optimized out: fontconfig glibc-kernheaders-generic glibc-kernheaders-x86 libGL-devel libGLU-devel libgpg-error libstdc++-devel perl python-base python-modules
BuildRequires: ImageMagick-tools boost-devel-headers gcc-c++ libSDL-devel libalsa-devel tcl-devel
%if_with jack
BuildRequires: libjack-devel
%endif

%description
If Puredata and Supercollider are two synths, din is a synth of a 3rd kind.
It forgets history, To not repeat it.
It doesnt hide analog music hardware, In digital music software.
You had pulse, sine, triangle and sawtooth,
And went forth and made electronic music.
Now there is just the Bezier curve. Go make your pulse, sine, triangle and sawtooths.
This is nothing new. Some old men did it in the 60s!
Punched numbers into cards. Now you edit waveforms in a GUI,
And watch the sound change before your ears.
Has it got ADSR? It's got DADSARSADS.
Filters? Infinite length delay lines.
With Bezier envelope for feedback and volume.
Modulation? Bezier on Carrier and Modulator. Eat that Chowning.
Notes? Notes! Notes! Notes! Infinite microtones between two tones.
Livecoding? In Tcl. Like LISP, but no ((((:-))))

Collaboration? MIDI. OSC. IRC.

%prep
%setup

%define bmsizes 128 96 64 48 32 24 16
%build
%if_with jack
%autoreconf
%configure --prefix=%prefix CXXFLAGS="-D__UNIX_JACK__"
%make_build
%else
sed -i 's/-ljack//g' src/Makefile.am
%autoreconf
%configure --prefix=%prefix CXXFLAGS="-D__LINUX_ALSA__"
%make_build
%endif
for N in %bmsizes; do convert pixmaps/din.png $N.png; done

%install
%makeinstall
for N in %bmsizes; do
	install -D $N.png %buildroot%_iconsdir/hicolor/${N}x${N}/apps/%name.png
done

%files
%doc README
%_bindir/*
%dir %_datadir/%name
%_datadir/%name/*
%_desktopdir/*
%_iconsdir/hicolor/*/apps/*
%_pixmapsdir/*

%changelog
* Thu Feb 07 2019 Fr. Br. George <george@altlinux.ru> 39.0.1-alt1
- Autobuild version bump to 39.0.1

* Wed May 23 2018 Fr. Br. George <george@altlinux.ru> 34-alt1
- Autobuild version bump to 34
- Provide ALSA build option

* Fri Apr 21 2017 Fr. Br. George <george@altlinux.ru> 10.0.0-alt1
- Autobuild version bump to 10.0.0

* Sat Mar 25 2017 Vladimir D. Seleznev <vseleznv@altlinux.org> 5.2.1-alt2
- Rebuilt against Tcl/Tk 8.6
- Fixed FTBFS

* Thu Jun 20 2013 Andrey Cherepanov <cas@altlinux.org> 5.2.1-alt1.1
- Rebuild with new version liblo

* Sun Mar 31 2013 Fr. Br. George <george@altlinux.ru> 5.2.1-alt1
- Autobuild version bump to 5.2.1
- Fix paths

* Mon Oct 22 2012 Fr. Br. George <george@altlinux.ru> 4.2.1-alt1
- Autobuild version bump to 4.2.1

* Sun Sep 09 2012 Fr. Br. George <george@altlinux.ru> 4.0-alt1
- Initial build from scratch


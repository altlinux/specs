%define		srcname game-music-emu
%def_with player

Summary:	Game Music Emulators library
Name:		libgme
Version:	0.6.1
Release:	alt1
Source0:	http://game-music-emu.googlecode.com/files/%{srcname}-%{version}.tbz2
License:	LGPLv2+
Group:		System/Libraries
#Url:		http://code.google.com/p/game-music-emu/
URL:            https://bitbucket.org/mpyne/game-music-emu/wiki/Home
Packager:	Motsyo Gennadi <drool@altlinux.ru>

# Automatically added by buildreq on Sun Sep 26 2010 (-bi)
BuildRequires: cmake gcc-c++

%description
This is a collection of video game music file emulators that supports a
variety of formats and systems:

 * AY       ZX Spectrum/Amstrad CPC
 * GBS      Nintendo Game Boy
 * GYM      Sega Genesis/Mega Drive
 * HES      NEC TurboGrafx-16/PC Engine
 * KSS      MSX Home Computer/other Z80 systems (does not support FM sound)
 * NSF/NSFE Nintendo NES/Famicom (with VRC 6, Namco 106, and FME-7 sound)
 * SAP      Atari systems using POKEY sound chip
 * SPC      Super Nintendo/Super Famicom
 * VGM/VGZ  Sega Master System/Mark III, Sega Genesis/Mega Drive,BBC Micro

%package -n %name-devel
Group: Development/C++
Summary: Game Music Emulators development library
Requires: %name = %version-%release
Provides: %name-devel = %version-%release

%description -n %name-devel
This is a collection of video game music file emulators that supports a
variety of formats and systems.

%if_with player
%package -n game-music-emu-player
Summary: Demo player utilizing Game_Music_Emu
Group: Sound
License: MIT
BuildRequires: libSDL-devel

%description -n game-music-emu-player
This package contains the demo player for files supported by Game_Music_Emu.
%endif

%prep
%setup -n %srcname-%version
%if_with player
# add install rule for the player
echo -e "\ninstall(TARGETS gme_player RUNTIME DESTINATION %{_bindir})" >> player/CMakeLists.txt
%endif

%build
cmake \
	-DCMAKE_INSTALL_PREFIX=%prefix \
	-DCMAKE_CXX_FLAGS:STRING="%optflags" \
	-DCMAKE_C_FLAGS:STRING="%optflags"
%make_build
%if_with player
# explicitly build the player as it has EXCLUDE_FROM_ALL set
%make_build gme_player
%endif

%install
%makeinstall_std
%if %_lib != lib
mv %buildroot%_prefix/lib/ %buildroot%_libdir
%endif
%if_with player
# explicitly install the player as it has EXCLUDE_FROM_ALL set
cd player
make install DESTDIR=%{buildroot}
cd ..
%endif

%files
%doc readme.txt gme.txt
%_libdir/%name.so.*

%files -n %name-devel
%doc changes.txt design.txt
%_libdir/%name.so
%_includedir/gme
%_pkgconfigdir/*.pc

%if_with player
%files -n game-music-emu-player
%{_bindir}/gme_player
%endif


%changelog
* Sat Mar 17 2018 Igor Vlasenko <viy@altlinux.ru> 0.6.1-alt1
- NMU: updated to 0.6.1, added player

* Thu Nov 17 2016 Motsyo Gennadi <drool@altlinux.ru> 0.6.0-alt1
- 0.6.0 (#32173)

* Sun Apr 14 2013 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 0.5.5-alt1.qa1
- NMU: rebuilt for debuginfo.

* Sun Sep 26 2010 Motsyo Gennadi <drool@altlinux.ru> 0.5.5-alt1
- initial build for ALT Linux from MDV package

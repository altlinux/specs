%def_with bootstrap

Name: SDL2_mixer
Version: 2.6.3
Release: alt1

Summary: Simple DirectMedia Layer - Sample Mixer Library
License: Zlib
Group: System/Libraries

Url: http://www.libsdl.org/projects/SDL_mixer/
Packager: Nazarov Denis <nenderus@altlinux.org>

# https://github.com/libsdl-org/SDL_mixer/archive/release-%version/SDL_mixer-release-%version.tar.gz
Source: SDL_mixer-release-%version.tar

BuildRequires: libSDL2-devel
BuildRequires: libflac-devel
%{?!_with_bootstrap:BuildRequires: libfluidsynth-devel}
BuildRequires: libmodplug-devel
BuildRequires: libmpg123-devel
BuildRequires: libopusfile-devel
BuildRequires: libvorbis-devel

%description
Due to popular demand, here is a simple multi-channel audio mixer.
It supports 8 channels of 16 bit stereo audio, plus a single channel
of music, mixed by the popular MikMod MOD, Timidity MIDI and SMPEG MP3
libraries.

%package -n lib%name
Summary: Simple DirectMedia Layer - Sample Mixer Library
Group: System/Libraries

%description -n lib%name
Due to popular demand, here is a simple multi-channel audio mixer.
It supports 8 channels of 16 bit stereo audio, plus a single channel
of music, mixed by the popular MikMod MOD, Timidity MIDI and SMPEG MP3
libraries.

%package -n lib%name-devel
Summary: Libraries, includes and more to develop SDL applications.
Group: Development/C

%description -n lib%name-devel
Due to popular demand, here is a simple multi-channel audio mixer.
It supports 8 channels of 16 bit stereo audio, plus a single channel
of music, mixed by the popular MikMod MOD, Timidity MIDI and SMPEG MP3
libraries.

%prep
%setup -n SDL_mixer-release-%version

%build
%configure \
	--disable-static \
	--disable-music-ogg-stb \
	--disable-music-flac-drflac \
	--disable-music-mp3-drmp3 \
	--disable-music-mod-modplug \
	--disable-music-mod-xmp-shared \
	--disable-music-midi-fluidsynth-shared \
	--enable-music-ogg-vorbis \
	--enable-music-flac-libflac \
	--enable-music-mp3-mpg123 \
	--enable-music-mod-xmp \
	--enable-music-mp3-mpg123-shared
%make_build

%install
%makeinstall_std
%__rm -f %buildroot%_libdir/lib%name.la

%files -n lib%name
%doc CHANGES.txt README.txt
%_libdir/lib%name-2.0.so.*

%files -n lib%name-devel
%dir %_includedir/SDL2
%_includedir/SDL2/SDL_mixer.h
%_pkgconfigdir/%name.pc
%_libdir/lib%name.so
%_libdir/cmake/%name

%changelog
* Tue Feb 07 2023 Nazarov Denis <nenderus@altlinux.org> 2.6.3-alt1
- Version 2.6.3

* Sat Aug 20 2022 Nazarov Denis <nenderus@altlinux.org> 2.6.2-alt1
- Version 2.6.2

* Wed Jul 20 2022 Nazarov Denis <nenderus@altlinux.org> 2.6.1-alt2
- --disable-*-shared: Link, rather than dlopen

* Wed Jul 13 2022 Nazarov Denis <nenderus@altlinux.org> 2.6.1-alt1
- Version 2.6.1

* Sun Jul 10 2022 Nazarov Denis <nenderus@altlinux.org> 2.6.0-alt1
- Version 2.6.0

* Sat Jan 15 2022 Nazarov Denis <nenderus@altlinux.org> 2.0.4-alt3
- Build with opus support (ALT #41721)

* Sun Apr 07 2019 Nazarov Denis <nenderus@altlinux.org> 2.0.4-alt2
- Remove %ubt macro

* Fri Nov 02 2018 Nazarov Denis <nenderus@altlinux.org> 2.0.4-alt1%ubt
- Version 2.0.4

* Sun Nov 19 2017 Nazarov Denis <nenderus@altlinux.org> 2.0.2-alt2%ubt
- Fix build

* Thu Oct 26 2017 Nazarov Denis <nenderus@altlinux.org> 2.0.2-alt1%ubt
- Version 2.0.2

* Wed Apr 05 2017 Michael Shigorin <mike@altlinux.org> 2.0.1-alt1.1
- avoid libfluidsynth when bootstrapping (hairy BRs)

* Fri Jan 22 2016 Nazarov Denis <nenderus@altlinux.org> 2.0.1-alt1
- Version 2.0.1

* Sun Mar 01 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0.0-alt2.1
- Fixed build

* Wed Feb 05 2014 Nazarov Denis <nenderus@altlinux.org> 2.0.0-alt1.M70T.1
- Build for branch t7

* Fri Nov 01 2013 Nazarov Denis <nenderus@altlinux.org> 2.0.0-alt2
- Add requires for lib%name-devel on lib%name

* Thu Oct 31 2013 Nazarov Denis <nenderus@altlinux.org> 2.0.0-alt1
- Initial build for ALT Linux

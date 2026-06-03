Name: SDL3_mixer
Version: 3.2.4
Release: alt1

Summary: Simple DirectMedia Layer - Sample Mixer Library
License: Zlib
Group: System/Libraries

Url: http://www.libsdl.org/projects/SDL_mixer/
Vcs: https://github.com/libsdl-org/SDL_mixer
Packager: Nazarov Denis <nenderus@altlinux.org>

# https://github.com/libsdl-org/SDL_mixer/archive/release-%version/SDL_mixer-release-%version.tar.gz
Source: SDL_mixer-release-%version.tar

BuildRequires: cmake
BuildRequires: libSDL3-devel
BuildRequires: libe2fs
BuildRequires: libflac-devel
BuildRequires: libfluidsynth-devel
BuildRequires: libgme-devel
BuildRequires: libmodplug-devel
BuildRequires: libmpg123-devel
BuildRequires: libopusfile-devel
BuildRequires: libslang2
BuildRequires: libvorbis-devel
BuildRequires: libwavpack-devel
BuildRequires: libxmp-devel

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
%cmake \
	-DCMAKE_BUILD_TYPE:STRING=RelWithDebInfo \
	-DSDLMIXER_TESTS_INSTALL:BOOL=OFF \
	-DSDLMIXER_EXAMPLES_INSTALL:BOOL=OFF
%cmake_build

%install
%cmake_install
%__rm -rf %buildroot%_datadir/licenses

%files -n lib%name
%doc CHANGES.txt INSTALL.md LICENSE.txt README.md
%_libdir/lib%name.so.*

%files -n lib%name-devel
%dir %_includedir/%name
%_includedir/%name/SDL_mixer.h
%_pkgconfigdir/sdl3-mixer.pc
%_libdir/lib%name.so
%_libdir/cmake/%name

%changelog
* Wed Jun 03 2026 Nazarov Denis <nenderus@altlinux.org> 3.2.4-alt1
- New version 3.2.4.

* Tue May 12 2026 Nazarov Denis <nenderus@altlinux.org> 3.2.2-alt1
- New version 3.2.2.

* Tue Mar 10 2026 Nazarov Denis <nenderus@altlinux.org> 3.2.0-alt1
- Initial build for ALT Linux (ALT #54137)

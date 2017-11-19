%def_with bootstrap

Name: SDL2_mixer
Version: 2.0.2
Release: alt2%ubt

Summary: Simple DirectMedia Layer - Sample Mixer Library
License: zlib
Group: System/Libraries

Url: http://www.libsdl.org/projects/SDL_mixer/
Packager: Nazarov Denis <nenderus@altlinux.org>

Source: http://www.libsdl.org/projects/SDL_mixer/release/%name-%version.tar.gz

BuildRequires(pre): rpm-build-ubt

BuildRequires: libSDL2-devel
BuildRequires: libflac-devel
%{?!_with_bootstrap:BuildRequires: libfluidsynth-devel}
BuildRequires: libmodplug-devel
BuildRequires: libmpg123-devel
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
%setup

%build
%configure --disable-static
%make_build

%install
%makeinstall_std
%__rm -f %buildroot%_libdir/lib%name.la

%files -n lib%name
%doc CHANGES.txt COPYING.txt README.txt
%_libdir/lib%name-2.0.so.*

%files -n lib%name-devel
%dir %_includedir/SDL2
%_includedir/SDL2/SDL_mixer.h
%_pkgconfigdir/%name.pc
%_libdir/lib%name.so

%changelog
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

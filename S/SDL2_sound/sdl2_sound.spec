# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-mageia-compat
BuildRequires: /usr/bin/doxygen gcc-c++
# END SourceDeps(oneline)
%define oldname sdl2_sound
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
# %%oldname is ahead of its definition. Predefining for rpm 4.0 compatibility.
%define name sdl2_sound
%define         hgrev        hg653
%define         srcversion   9262f9205898
%define         srcname      SDL_sound

%define         major        1
%define         libname      lib%{oldname}%{major}
%define         develname    lib%{oldname}-devel
%define         staticname   lib%{oldname}-devel-static

%define         rel 5

Name:           SDL2_sound
Version:        1.0.4
Release:        alt3_%{rel}.%{hgrev}
Summary:        An abstract SDL2 sound-file decoder
License:        zlib
Group:          System/Libraries
Url:            https://hg.icculus.org/icculus/SDL_sound/archive/
Source0:        SDL_sound-%{srcversion}.tar.bz2
Patch0:         sdl2_sound-1.0.4-includedir.patch

BuildRequires:  cmake
BuildRequires:  pkgconfig(sdl2)
BuildRequires:  pkgconfig(flac)
BuildRequires:  pkgconfig(libmikmod)
BuildRequires:  pkgconfig(libmodplug)
BuildRequires:  pkgconfig(vorbis)
BuildRequires:  pkgconfig(speex)
BuildRequires:  pkgconfig(physfs)

Conflicts:      libSDL_sound < 1.0.4
Source44: import.info

%description
SDL2_sound is SDL_sound but with a SDL2 backend. This is a library
that handles the decoding of several popular sound file formats, such
as .WAV and .MP3. It is meant to make the programmer's sound playback
tasks simpler. The programmer gives SDL2_sound a file-name, or feeds it
data directly from one of many sources, and then reads the decoded
waveform data back at her leisure. If resource constraints are a
concern, SDL2_sound can process sound data in programmer-specified
blocks. Alternately, SDL2_sound can decode a whole sound file and hand
back a single pointer to the whole waveform. SDL2_sound can also handle
sample rate, audio format, and channel conversion on-the-fly and
behind-the-scenes.

%package -n %{libname}
Summary:        SDL2_sound main library
Group:          System/Libraries
Obsoletes:      %{_lib}SDL2_sound1 < 1.0.4-0.hg653.2

%description -n %{libname}
%{summary}.


%package -n %{develname}
Summary:        Development files for SDL2_sound applications
Group:          Development/C
Requires:       %{libname} = %{version}-%{release}


%description -n %{develname}
%{summary}.


%package -n %{staticname}
Summary:        Static development files for SDL2_sound libraries
Group:          Development/C
Requires:       %{develname} = %{version}-%{release}
Provides:       %{oldname}-static-devel = %{version}-%{release}
Obsoletes:      %{_lib}SDL2_sound-static-devel < 1.0.4-0.hg653.2

%description -n %{staticname}
%{summary}.



%prep
%setup -q -n %{srcname}-%{srcversion}
%patch0 -p1

pushd %{_builddir}/%{srcname}-%{srcversion}
cp src/SDL_sound.h .
popd

%build
%{?optflags_lto:%global optflags_lto %optflags_lto -ffat-lto-objects}
export CFLAGS="%{optflags} -lm"
%{mageia_cmake} -DCMAKE_STATIC_LIBS:BOOL=ON \
       -DCMAKE_SHARED_LIBS:BOOL=ON
%mageia_cmake_build

%install
%mageia_cmake_install

%files
%doc LICENSE.txt docs/CREDITS.txt
%{_bindir}/*

%files -n %{libname}
%doc docs/README.txt docs/INSTALL.txt
%{_libdir}/libSDL2_sound.so.%{major}*

%files -n %{develname}
%{_libdir}/lib*.so
%{_includedir}/SDL2/SDL_sound.h

%files -n %{staticname}
%{_libdir}/lib*.a


%changelog
* Sat Aug 28 2021 Igor Vlasenko <viy@altlinux.org> 1.0.4-alt3_5.hg653
- fixed build with LTO

* Wed Sep 09 2020 Igor Vlasenko <viy@altlinux.ru> 1.0.4-alt2_5.hg653
- fixed build

* Fri Mar 27 2020 Igor Vlasenko <viy@altlinux.ru> 1.0.4-alt1_5.hg653
- Sisyphus build


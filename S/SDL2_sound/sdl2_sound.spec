# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-mageia-compat
BuildRequires: libsdl2_sound-devel
# END SourceDeps(oneline)
%{?optflags_lto:%global optflags_lto %optflags_lto -ffat-lto-objects}
%define oldname sdl2_sound
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
# %%oldname is ahead of its definition. Predefining for rpm 4.0 compatibility.
%define name sdl2_sound
%define         srcname      SDL2_sound


%define         major        2
%define         libname      lib%{oldname}%{major}
%define         develname    lib%{oldname}-devel
%define         staticname   lib%{oldname}-devel-static

Name:           SDL2_sound
Version:        2.0.4
Release:        alt1_1
Summary:        An abstract SDL2 sound-file decoder
License:        zlib
Group:          System/Libraries
Url:            https://www.icculus.org/SDL_sound/
Source0:        https://github.com/icculus/SDL_sound/releases/download/v%{version}/SDL2_sound-%{version}.tar.gz
#Patch0:         sdl2_sound-1.0.4-includedir.patch

BuildRequires:  ccmake cmake ctest
BuildRequires:  doxygen
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

%description -n %{libname}
SDL2_sound main library.


%package -n %{develname}
Summary:        Development files for SDL2_sound applications
Group:          Development/C
Requires:       %{libname} = %{version}-%{release}

%description -n %{develname}
Development files for SDL2_sound applications.


%package -n %{staticname}
Summary:        Static development files for SDL2_sound libraries
Group:          Development/C
Requires:       %{develname} = %{version}-%{release}
Provides:       %{oldname}-static-devel = %{version}-%{release}

%description -n %{staticname}
Static development files for SDL2_sound libraries.


%prep
%setup -q -n %{srcname}-%{version}


%build
%{mageia_cmake} -DCMAKE_STATIC_LIBS:BOOL=ON \
       -DCMAKE_SHARED_LIBS:BOOL=ON \
       -DSDLSOUND_DECODER_MIDI:BOOL=ON
%mageia_cmake_build

doxygen docs/Doxyfile

%install
%mageia_cmake_install

# Add namespaces to man pages (livna bug #1181)
cp -a docs/man/man3 man3
pushd man3
mv actual.3 Sound_Sample::actual.3
mv author.3 Sound_DecoderInfo::author.3
mv buffer.3 Sound_Sample::buffer.3
mv buffer_size.3 Sound_Sameple::buffer_size.3
mv channels.3 Sound_AudioInfo::channels.3
mv decoder.3 Sound_Sample::decoder.3
mv description.3 Sound_DecoderInfo::description.3
mv desired.3 Sound_Sample::desired.3
mv extensions.3 Sound_DecoderInfo::extensions.3
mv flags.3 Sound_Sample::flags.3
mv format.3 Sound_AudioInfo::format.3
mv major.3 Sound_Version::major.3
mv minor.3 Sound_Version::minor.3
mv opaque.3 Sound_Sample::opaque.3
mv patch.3 Sound_Version::patch.3
mv rate.3 Sound_AudioInfo::rate.3
mv url.3 Sound_DecoderInfo::url.3
popd

mkdir -p %{buildroot}%{_mandir}
mv man3 %{buildroot}%{_mandir}

%files
%doc --no-dereference LICENSE.txt
%doc docs/CREDITS.txt
%{_bindir}/*

%files -n %{libname}
%doc --no-dereference LICENSE.txt
%doc docs/CREDITS.txt README.md
%{_libdir}/libSDL2_sound.so.%{major}
%{_libdir}/libSDL2_sound.so.%{major}.*

%files -n %{develname}
%doc docs/html/
%{_libdir}/lib*.so
%{_includedir}/SDL2/SDL_sound.h
%{_libdir}/cmake/SDL2_sound/
%{_libdir}/pkgconfig/SDL2_sound.pc
%{_mandir}/man3/*.3*

%files -n %{staticname}
%{_libdir}/lib*.a


%changelog
* Tue Apr 08 2025 Igor Vlasenko <viy@altlinux.org> 2.0.4-alt1_1
- update by mgaimport

* Sat Aug 28 2021 Igor Vlasenko <viy@altlinux.org> 1.0.4-alt3_5.hg653
- fixed build with LTO

* Wed Sep 09 2020 Igor Vlasenko <viy@altlinux.ru> 1.0.4-alt2_5.hg653
- fixed build

* Fri Mar 27 2020 Igor Vlasenko <viy@altlinux.ru> 1.0.4-alt1_5.hg653
- Sisyphus build


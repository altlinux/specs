Name: libopenmpt
Version: 0.5.8
Release: alt2
License: BSD
Group: System/Libraries
Summary: C/C++ library to decode tracker music module (MOD) files
Url: https://lib.openmpt.org/libopenmpt/
Packager: Artyom Bystrov <arbars@altlinux.org>

Source: %name-%version.tar

BuildRequires: make
BuildRequires: gcc-c++
BuildRequires: chrpath
BuildRequires: libmpg123-devel
BuildRequires: libogg-devel
BuildRequires: libvorbis-devel
BuildRequires: libsndfile-devel
BuildRequires: libflac-devel
BuildRequires: zlib-devel
BuildRequires: libportaudio2-devel
BuildRequires: libSDL2-devel

# for command-line player audio output

BuildRequires: libpulseaudio-devel

%description
libopenmpt is a cross-platform C++ and C library to decode tracked music
files (modules) into a raw PCM audio stream.
libopenmpt is based on the player code of the OpenMPT project (Open
ModPlug Tracker). In order to avoid code base fragmentation, libopenmpt is
developed in the same source code repository as OpenMPT.

%package -n openmpt123

Summary: Command-line tracker music player based on libopenmpt
Group: Sound

%description -n openmpt123
Openmpt123 is a cross-platform command-line or terminal based player
for tracker music (MOD) module files.

%package devel

Summary: Development files for the libopenmpt library
Group: System/Libraries

%description devel
Files needed when building software which uses libopenmpt.

%prep
%setup
%__subst 's/\r$//' LICENSE

%build
%autoreconf
%configure \
    --docdir=%_docdir/%name-devel \
    --disable-static \
    --disable-silent-rules \
    --disable-doxygen-doc \
    --with-zlib \
    --with-mpg123 \
    --with-ogg \
    --with-vorbis \
    --with-vorbisfile \
    --with-pulseaudio \
    --with-sndfile \
    --with-flac \
    --with-portaudio \
    --with-sdl2

%make_build

%install
install -d %buildroot%_docdir/%name/examples
%makeinstall_std

%files -n openmpt123
%_bindir/openmpt123
%_man1dir/*

%files
%doc LICENSE README.md
%_libdir/*.so.0*
%dir %_docdir/%name/

%files devel
%doc LICENSE README.md
%_includedir/%name/
%_libdir/*.so
%_pkgconfigdir/*.pc
%dir %_docdir/%name-devel/
%exclude %_docdir/%name-devel/examples


%changelog
* Wed Aug 04 2021 Artyom Bystrov <arbars@altlinux.org> 0.5.8-alt2
- fix the loop deps

%changelog
* Mon Aug 02 2021 Artyom Bystrov <arbars@altlinux.org> 0.5.8-alt1
- initial build for ALT Sisyphus

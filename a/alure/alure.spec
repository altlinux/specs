Summary: ALURE is a utility library to help manage common tasks with OpenAL applications
Name: alure
Version: 1.1
Release: alt1
Source0: %name-%version.tar
License: MIT
Packager: Slava Dubrovskiy <dubrsl@altlinux.ru>
Group: System/Libraries
Url: http://kcat.strangesoft.net/alure.html

BuildRequires: cmake gcc-c++ libopenal-devel libsndfile-devel libvorbis-devel libflac-devel libmpg123-devel dumb-devel libmodplug-devel libfluidsynth-devel

%description
The purpose of this library is to provide pre-made functionality that would otherwise be 
repetitive or difficult to (re)code for various projects and platforms, such as loading
a sound file into an OpenAL buffer and streaming an audio file through a buffer queue.
Support for different formats is consistant across platforms, so no special checks are
needed when loading files, and all formats are handled through the same API.

Currently ALURE includes a basic .wav and .aif file reader, and can leverage external
libraries such as libSndFile (for extended wave formats and several others),
VorbisFile (for Ogg Vorbis), FLAC (for FLAC and Ogg FLAC), and others. External libraries
can also be dynamically loaded at run-time, or individually disabled outright at compile time.

%package -n lib%name
Summary: ALURE is a utility library to help manage common tasks with OpenAL applications
Group: System/Libraries

%description -n lib%name
The purpose of this library is to provide pre-made functionality that would otherwise be 
repetitive or difficult to (re)code for various projects and platforms, such as loading
a sound file into an OpenAL buffer and streaming an audio file through a buffer queue.
Support for different formats is consistant across platforms, so no special checks are
needed when loading files, and all formats are handled through the same API.

Currently ALURE includes a basic .wav and .aif file reader, and can leverage external
libraries such as libSndFile (for extended wave formats and several others),
VorbisFile (for Ogg Vorbis), FLAC (for FLAC and Ogg FLAC), and others. External libraries
can also be dynamically loaded at run-time, or individually disabled outright at compile time.

%package -n lib%name-devel
Summary: Development files for %name
Group: Development/C
Requires: lib%name = %version-%release

%description -n lib%name-devel
The %name-devel package contains libraries and header files for
developing applications that use %name.

%package -n lib%name-devel-doc
Summary: Development files for %name
Group: Development/Documentation

%description -n lib%name-devel-doc
The %name-devel package contains development documentation for
developing applications that use %name.

%package examples
Summary: Development files for %name
Group: Sound

%description examples
The %name-examples package contains example program for %name

%prep
%setup -q

%build
%cmake	-DBUILD_STATIC=OFF \
	-DMODPLUG=ON

%make_build -C BUILD VERBOSE=1

%install
%makeinstall_std -C BUILD

mkdir -p %buildroot/usr/bin
cp BUILD/alurecdplay %buildroot/usr/bin/
cp BUILD/alureplay %buildroot/usr/bin/
cp BUILD/alurestream %buildroot/usr/bin/

%files -n lib%name
%_libdir/*.so.*

%files -n lib%name-devel
%_includedir/*
%_libdir/*.so
%_libdir/pkgconfig/*
#_libdir/GG/*.cmake

%files -n lib%name-devel-doc
%doc docs/*

%files examples
%_bindir/*

%changelog
* Sun May 15 2011 Slava Dubrovskiy <dubrsl@altlinux.org> 1.1-alt1
- Build for ALT

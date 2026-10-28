Summary: ALURE is a utility library to help manage common tasks with OpenAL applications
Name: alure
Version: 1.2
Release: alt3
Source0: %name-%version.tar
Patch0: alure-cmake-cflags.patch
License: MIT
Packager: Slava Dubrovskiy <dubrsl@altlinux.ru>
Group: System/Libraries
Url: http://kcat.strangesoft.net/alure.html

BuildRequires: rpm-build-cmake gcc-c++ libopenal-devel libsndfile-devel libvorbis-devel libflac-devel libmpg123-devel dumb-devel libmodplug-devel libfluidsynth-devel

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
%patch -P 0 -p1

%build
%cmake	-DBUILD_STATIC=OFF \
	-DMODPLUG=ON

%cmake_build

%install
%cmake_install

%files -n lib%name
%_libdir/*.so.*

%files -n lib%name-devel
%_includedir/*
%_libdir/*.so
%_libdir/pkgconfig/*

%files -n lib%name-devel-doc
%doc docs/*
%_docdir/%name/html

%files examples
%_bindir/*

%changelog
* Wed Oct 28 2026 Vitaly Lipatov <lav@altlinux.ru> 1.2-alt3
- Fix FTBFS caused by CMake pkg-config flags.
- Replace cmake with rpm-build-cmake in BuildRequires.

* Wed Oct 28 2026 Vitaly Lipatov <lav@altlinux.ru> 1.2-alt2.qa2.1
- Fix CMake handling of pkg-config compiler flags.
- Replace cmake with rpm-build-cmake in BuildRequires.

* Mon May 31 2021 Arseny Maslennikov <arseny@altlinux.org> 1.2-alt2.qa2
- NMU: spec: adapted to new cmake macros.

* Mon Apr 11 2016 Gleb F-Malinovskiy (qa) <qa_glebfm@altlinux.org> 1.2-alt2.qa1
- Rebuilt for gcc5 C++11 ABI.

* Tue Nov 12 2013 Slava Dubrovskiy <dubrsl@altlinux.org> 1.2-alt2
- Fix build

* Sat Oct 26 2013 Slava Dubrovskiy <dubrsl@altlinux.org> 1.2-alt1
- New version. Fix (ALT#29525)

* Sun May 15 2011 Slava Dubrovskiy <dubrsl@altlinux.org> 1.1-alt1
- Build for ALT

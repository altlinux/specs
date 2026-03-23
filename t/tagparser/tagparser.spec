%define _unpackaged_files_terminate_build 1
%define abiversion 12

Name: tagparser
Version: 12.5.2
Release: alt1

Summary: C++ library for reading and writing tags into audio files
Group: Development/C++
License: GPL-2.0-or-later
Url: https://github.com/Martchus/tagparser
Vcs: https://github.com/Martchus/tagparser

Source: %name-%version.tar

BuildRequires(pre): rpm-macros-cmake
BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: libmartchus-c++utilities-devel
BuildRequires: zlib-devel
BuildRequires: iso-codes

%package -n libtagparser%abiversion
Summary: C++ library for reading and writing tags into audio files
Group: Development/C++

%package -n libtagparser-devel
Summary: C++ library for reading and writing tags into audio files
Group: Development/C++
Requires: libtagparser%abiversion = %EVR

%description
C++ library for reading and writing MP4 (iTunes), ID3, Vorbis, Opus, FLAC and
Matroska tags. The library allows you to choose whether tags should be placed
at the beginning or at the end of an MP4/Matroska file.
The tag library can read and write the following tag formats:

* iTunes-style MP4/M4A tags (MP4-DASH is supported)
* ID3v1 and ID3v2 tags
* Conversion between ID3v1 and different versions of ID3v2 is possible
* Mainly for use in MP3 files but can be added to any kind of file
* Vorbis, Opus and FLAC comments in Ogg streams
* Cover art via "METADATA_BLOCK_PICTURE" is supported
* Vorbis comments and "METADATA_BLOCK_PICTURE" in raw FLAC streams
* Matroska/WebM tags and attachments

%description -n libtagparser%abiversion
C++ library for reading and writing MP4 (iTunes), ID3, Vorbis, Opus, FLAC and
Matroska tags. The library allows you to choose whether tags should be placed
at the beginning or at the end of an MP4/Matroska file.
The tag library can read and write the following tag formats:

* iTunes-style MP4/M4A tags (MP4-DASH is supported)
* ID3v1 and ID3v2 tags
* Conversion between ID3v1 and different versions of ID3v2 is possible
* Mainly for use in MP3 files but can be added to any kind of file
* Vorbis, Opus and FLAC comments in Ogg streams
* Cover art via "METADATA_BLOCK_PICTURE" is supported
* Vorbis comments and "METADATA_BLOCK_PICTURE" in raw FLAC streams
* Matroska/WebM tags and attachments

%description -n libtagparser-devel
C++ library for reading and writing MP4 (iTunes), ID3, Vorbis, Opus, FLAC and
Matroska tags. The library allows you to choose whether tags should be placed
at the beginning or at the end of an MP4/Matroska file.
The tag library can read and write the following tag formats:

* iTunes-style MP4/M4A tags (MP4-DASH is supported)
* ID3v1 and ID3v2 tags
* Conversion between ID3v1 and different versions of ID3v2 is possible
* Mainly for use in MP3 files but can be added to any kind of file
* Vorbis, Opus and FLAC comments in Ogg streams
* Cover art via "METADATA_BLOCK_PICTURE" is supported
* Vorbis comments and "METADATA_BLOCK_PICTURE" in raw FLAC streams
* Matroska/WebM tags and attachments

This is the development version of the library. You will need this only if
you intend to compile programs that use this library.

%prep
%setup

%build
%cmake \
  -DCMAKE_BUILD_TYPE=Release \
  -DBUILD_SHARED_LIBS:BOOL=ON \
  -DPACKAGE_NAMESPACE=martchus \
  -DLANGUAGE_FILE_ISO_639_2=%_datadir/iso-codes/json/iso_639-2.json

%cmake_build

%install
%cmake_install

%files -n libtagparser%abiversion
%_libdir/libtagparser.so.%abiversion
%_libdir/libtagparser.so.%version

%files -n libtagparser-devel
%_libdir/libtagparser.so
%_includedir/tagparser/
%_pkgconfigdir/tagparser.pc
%_datadir/tagparser/

%changelog
* Mon Mar 23 2026 Arseniy Kostevich <faux@altlinux.org> 12.5.2-alt1
- Initial build for ALT.

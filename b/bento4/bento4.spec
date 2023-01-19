Name: bento4
Version: 1.6.0.639
Release: alt1

Summary: C++ class library and tools designed to read and write ISO-MP4 files
License: GPLv2
Group: Development/C++
Url: https://www.bento4.com/

Source: %name-%version-%release.tar

BuildRequires: cmake gcc-c++

%package -n libap4-devel-static
Summary: C++ class library designed to read and write ISO-MP4 files
Group: Development/C++

%define desc \
Bento4 is a C++ class library and tools designed to read and write ISO-MP4 files. \
This format is defined in international specifications ISO/IEC 14496-12, 14496-14 \
and 14496-15. The format is a derivative of the Apple Quicktime file format, so \
Bento4 can be used to read and write most Quicktime files as well. In addition to \
supporting ISO-MP4, Bento4 includes support for parsing and multiplexing H.264 \
and H.265 elementary streams, converting ISO-MP4 to MPEG2-TS, packaging HLS and \
MPEG-DASH, CMAF, content encryption, decryption, and much more.

%description %desc

%description -n libap4-devel-static %desc
This package contains bento4 static library.

%define optflags_lto %nil
%add_optflags %optflags_shared

%prep
%setup

%build
%cmake -DBUILD_APPS=OFF
%cmake_build

%install
%cmakeinstall_std

%files -n libap4-devel-static
%_includedir/bento4
%_libdir/cmake/bento4
%_libdir/libap4.a

%changelog
* Tue Nov 15 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.6.0.639-alt1
- 1.6.0.639

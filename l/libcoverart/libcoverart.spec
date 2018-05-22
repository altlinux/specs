Name: libcoverart
Version: 1.0.0
Release: alt2

Summary: Cover Art Archive Client Library
Group: System/Libraries
License: LGPLv2+

Url: http://musicbrainz.org/doc/%name
#VCS: git://github.com/metabrainz/libcoverart.git
Source: http://ftp.musicbrainz.org/pub/musicbrainz/%name/%name-%version.tar

BuildRequires: gcc-c++ cmake libjansson-devel libneon-devel

%description
The Cover Art Archive is a joint project between the Internet Archive
and MusicBrainz, whose goal is to make cover art images available to
everyone on the Internet in an organised and convenient way.

This package provides Cover Art Archive Client Library.

%package devel
Summary: Development files for %name
Group: Development/C++
Requires: %name = %version-%release

%description devel
The %name-devel package contains libraries and header files for
developing applications that use %name.

%prep
%setup


%build
%add_optflags -Wno-error=implicit-fallthrough
%cmake_insource -DCMAKE_BUILD_TYPE=Release
%make_build

%install
%makeinstall_std

%files
%_libdir/*.so.*
%doc NEWS.txt README.md

%files devel
%_includedir/coverart/
%_libdir/*.so
%_libdir/pkgconfig/*.pc

%changelog
* Tue May 22 2018 Yuri N. Sedunov <aris@altlinux.org> 1.0.0-alt2
- rebuilt with -Wno-error=implicit-fallthrough

* Sun Mar 24 2013 Yuri N. Sedunov <aris@altlinux.org> 1.0.0-alt1
- first build for Sisyphus


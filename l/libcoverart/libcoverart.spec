%def_enable snapshot

Name: libcoverart
Version: 1.0.0
Release: alt3

Summary: Cover Art Archive Client Library
Group: System/Libraries
License: LGPLv2+
Url: http://musicbrainz.org/doc/%name

%if_disabled snapshot
Source: http://ftp.musicbrainz.org/pub/musicbrainz/%name/%name-%version.tar.gz
%else
#VCS: git://github.com/metabrainz/libcoverart.git
Source: %name-%version.tar
%endif

BuildRequires(pre): cmake
BuildRequires: gcc-c++ libjansson-devel libneon-devel libxml2-devel

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
%_pkgconfigdir/*.pc

%changelog
* Thu Nov 29 2018 Yuri N. Sedunov <aris@altlinux.org> 1.0.0-alt3
- updated to 1.0.0-37-g86c3d8c
- fixed BR

* Tue May 22 2018 Yuri N. Sedunov <aris@altlinux.org> 1.0.0-alt2
- rebuilt with -Wno-error=implicit-fallthrough

* Sun Mar 24 2013 Yuri N. Sedunov <aris@altlinux.org> 1.0.0-alt1
- first build for Sisyphus


%def_disable snapshot
%define _name musicbrainz
%define api_ver 5

%def_enable check

Name: lib%{_name}%api_ver
Version: 5.1.0
Release: alt2

Summary: A software library for accesing MusicBrainz servers
License: LGPL-2.1-or-later
Group: System/Libraries
Url: http://www.musicbrainz.org/

#Source: ftp://ftp.%_name.org/pub/%_name/lib%_name-%version.tar.gz
Vcs: https://github.com/metabrainz/libmusicbrainz.git
%if_disabled snapshot
Source: https://github.com/metabrainz/lib%_name/releases/download/release-%version/lib%_name-%version.tar.gz
%else
Source: lib%_name-%version.tar
%endif
Patch: lib%_name-5.1.0-up-cmake.patch
# git show f5a31ded..4655b5
Patch1: lib%_name-5.1.0-up-libxml2-2.12.patch

BuildRequires(pre): rpm-macros-cmake
BuildRequires: cmake gcc-c++
BuildRequires: libneon-devel libxml2-devel
%{?_enable_check:BuildRequires: ctest}

%description
The MusicBrainz client library allows applications to make metadata
lookup to a MusicBrainz server, generate signatures from WAV data and
create CD Index Disk ids from audio CD roms.

%package devel
Summary: Headers for developing programs that will use libmusicbrainz
Group: Development/C++
Requires: %name = %EVR

%description devel
This package contains the headers that programmers will need to
develop applications which will use libmusicbrainz.

%prep
%setup -n lib%_name-%version
%patch -p1 -b .cmake
%patch1 -p1 -b .libxml2

%build
%cmake
%cmake_build

%install
%cmake_install

%check
%cmake_build -t tests

%files
%_libdir/%name.so.*
#%_libdir/%{name}cc.so.*
%doc AUTHORS.txt NEWS.txt

%files devel
%_libdir/%name.so
#%_libdir/%{name}cc.so
%_includedir/%_name%api_ver
%_pkgconfigdir/%name.pc
#%_pkgconfigdir/%{name}cc.pc

%changelog
* Sun Dec 17 2023 Yuri N. Sedunov <aris@altlinux.org> 5.1.0-alt2
- fixed build with libxml2-2.12.x

* Mon Dec 01 2014 Yuri N. Sedunov <aris@altlinux.org> 5.1.0-alt1
- 5.1.0

* Sun Sep 09 2012 Yuri N. Sedunov <aris@altlinux.org> 5.0.1-alt1
- first build for Sisyphus



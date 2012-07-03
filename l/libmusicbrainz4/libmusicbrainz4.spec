%define _name musicbrainz
%define api_ver 4

Name: lib%{_name}%api_ver
Version: 4.0.0
Release: alt1

Summary: A software library for accesing MusicBrainz servers
License: LGPLv2+
Group: System/Libraries
Url: http://www.musicbrainz.org/

Source: ftp://ftp.%_name.org/pub/%_name/lib%_name-%version.tar.gz

BuildRequires: ccmake cppunit-devel gcc-c++ libdiscid-devel libneon-devel

%description
The MusicBrainz client library allows applications to make metadata
lookup to a MusicBrainz server, generate signatures from WAV data and
create CD Index Disk ids from audio CD roms.

%package devel
Summary: Headers for developing programs that will use libmusicbrainz
Group: Development/C++
Requires: %name = %version-%release

%description devel
This package contains the headers that programmers will need to
develop applications which will use libmusicbrainz.

%prep
%setup -n lib%_name-%version

%build
cmake . -DCMAKE_INSTALL_PREFIX=%prefix -DCMAKE_VERBOSE_MAKEFILE=1 \
%if "%_lib" == "lib64"
	-DLIB_SUFFIX=64
%endif

%install
%makeinstall_std

%files
%_libdir/%name.so.*
%doc AUTHORS.txt NEWS.txt

%files devel
%_libdir/%name.so
%_includedir/%_name%api_ver
%_pkgconfigdir/%name.pc

%changelog
* Mon Jun 04 2012 Yuri N. Sedunov <aris@altlinux.org> 4.0.0-alt1
- first build for Sisyphus


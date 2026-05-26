%define _unpackaged_files_terminate_build 1

%ifnarch %ix86
%def_with check
%else
%def_without check
%endif

Name:    libosmium
Version: 2.23.1
Release: alt1

Summary: Fast and flexible C++ library for working with OpenStreetMap data
License: BSL-1.0
Group:   System/Libraries
URL:     https://osmcode.org/libosmium/
VCS:     https://github.com/osmcode/libosmium

Source:  %name-%version.tar

BuildRequires(pre): rpm-macros-cmake
BuildRequires: /proc
BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: boost-devel
BuildRequires: protozero-devel
BuildRequires: liblz4-devel
BuildRequires: libexpat-devel
BuildRequires: zlib-devel
BuildRequires: bzlib-devel
BuildRequires: libgeos-devel
BuildRequires: libgdal-devel
%if_with check
BuildRequires: ctest
%endif

%description
The Osmium Library has extensive support for all types of OSM entities:
nodes, ways, relations, and changesets.
It allows reading from and writing to OSM files in XML, PBF, and
several other formats, including change files and full history files.
Osmium can store OSM data in memory and on disk in various formats
and using various indexes. Its easy to use handler interface allows you
to quickly write data filtering and conversion functions. Osmium can create
WKT, WKB, OGR, GEOS and GeoJSON geometries for easy conversion into
many GIS formats and it can assemble multipolygons from ways and relations.

%package devel
Group: Development/C++
Summary: Fast and flexible C++ library for working with OpenStreetMap data

%description devel
%{description %name}

%prep
%setup

%build
%cmake
%cmake_build

%install
%cmake_install

%check
%ctest

%files devel
%_includedir/osmium

%changelog
* Mon May 25 2026 Alexey Volkov <qualimock@altlinux.org> 2.23.1-alt1
- Initial build for ALT

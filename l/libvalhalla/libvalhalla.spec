%define _unpackaged_files_terminate_build 1
%define soname 3

Name: libvalhalla
Version: 3.5.1
Release: alt1

Summary: A routing engine and libraries for use with OpenStreetMap data
License: MIT
Group: Sciences/Geosciences
Url: https://valhalla.github.io/valhalla
Vcs: https://github.com/valhalla/valhalla.git

Source0: %name-%version.tar
Source1: %name-%version-third_party-date.tar
Source2: %name-%version-third_party-tz.tar
Source3: %name-%version-third_party-cpp-statsd-client.tar
Patch0: 0001-Use-system-rapidjson.patch
Patch1: 0002-Make-building-compatible-with-the-C-20.patch

BuildRequires(pre): rpm-macros-cmake
BuildRequires: rpm-build-python3
BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: zlib-devel
BuildRequires: liblz4-devel
BuildRequires: libcurl-devel
BuildRequires: boost-devel
BuildRequires: boost-geometry-devel
BuildRequires: libprotobuf-devel
BuildRequires: protobuf-compiler
BuildRequires: libgdal-devel
BuildRequires: rapidjson-devel
BuildRequires: librobin-hood-hashing-devel
BuildRequires: cxxopts-devel

%description
Valhalla is an open source routing engine and accompanying libraries
for use with OpenStreetMap data. Valhalla also includes tools like
time+distance matrix computation, isochrones, elevation sampling,
map matching and tour optimization (Travelling Salesman).

%package -n libvalhalla%soname
Summary: Routing engine for OpenStreetMap data
Group: Sciences/Geosciences

%description -n libvalhalla%soname
Valhalla is an open source routing engine and accompanying libraries
for use with OpenStreetMap data. Valhalla also includes tools like
time+distance matrix computation, isochrones, elevation sampling,
map matching and tour optimization (Travelling Salesman).

%package devel
Summary: Development libraries and headers for libvalhalla
Group: Development/C++

%description devel
This package provides the development files for libvalhalla, including headers
and libraries needed to build applications that utilize Valhalla's routing
engine.  It is intended for developers who want to integrate Valhalla's
features into their own software.

%package tools
Summary: Command line utils for libvalhalla
Group: Sciences/Geosciences

%description tools
This package includes command-line utilities for working with Valhalla, such as
building configuration files, extracting elevation data, and creating time zone
databases. These tools are useful for setting up and managing Valhalla's
routing data and services.

%prep
%setup -a1 -a2 -a3
%autopatch -p1

%build
%cmake \
  -DENABLE_DATA_TOOLS=OFF \
  -DENABLE_TOOLS=OFF \
  -DENABLE_SERVICES=OFF \
  -DENABLE_PYTHON_BINDINGS=OFF \
  -DENABLE_CCACHE=OFF \
  -DENABLE_TESTS=OFF \
  -DBUILD_SHARED_LIBS=ON \
  -DPREFER_EXTERNAL_DEPS=ON \
  #

%cmake_build

%install
%cmake_install

%files -n libvalhalla%soname
%exclude %_defaultdocdir
%doc COPYING
%_libdir/libvalhalla.so.%soname
%_libdir/libvalhalla.so.%soname.*

%files devel
%_libdir/libvalhalla.so
%_pkgconfigdir/libvalhalla.pc
%_includedir/valhalla/

%files tools
%_bindir/valhalla_build_config
%_bindir/valhalla_build_elevation
%_bindir/valhalla_build_extract
%_bindir/valhalla_build_timezones

%changelog
* Sun Jun 08 2025 Ivan Khanas <xeno@altlinux.org> 3.5.1-alt1
- New version.

* Tue Oct 30 2018 Igor Vlasenko <viy@altlinux.ru> 2.0.0-alt2_16
- update by mgaimport

* Thu Jun 14 2018 Anton Farygin <rider@altlinux.ru> 2.0.0-alt2
- rebuilt for ffmpeg-4.0

* Sun May 06 2018 Igor Vlasenko <viy@altlinux.ru> 2.0.0-alt1_15
- update by mgaimport

* Sun Mar 18 2018 Igor Vlasenko <viy@altlinux.ru> 2.0.0-alt1_14
- new version


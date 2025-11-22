%define __cmake_in_source_build 1
%global __soversion 2.0

Name: biblesync
Version: 2.1.0
Release: alt2
Summary: A Cross-platform library for sharing Bible navigation
Group: System/Libraries
License: Public Domain
Url: http://www.xiphos.org
Source: https://github.com/karlkleinpaste/biblesync/releases/download/%version/biblesync-%version.tar.gz
Source44: %name.watch
Patch0: 4b00f9fd3d0c858947eee18206ef44f9f6bd2283.patch

BuildRequires(pre): rpm-macros-cmake
# Automatically added by buildreq on Wed Sep 13 2017
# optimized out: cmake-modules libstdc++-devel python-base python-modules
BuildRequires: cmake gcc-c++ libuuid-devel

%description
BibleSync is a multicast protocol to support Bible software shared co-
navigation. It uses LAN multicast in either a personal/small team mutual
navigation motif or in a classroom environment where there are Speakers plus
the Audience. It provides a complete yet minimal public interface to support
mode setting, setup for packet reception, transmit on local navigation, and
handling of incoming packets.

This library is not specific to any particular Bible software framework,
completely agnostic as to structure of layers above BibleSync.

%package devel
Group: Development/C++
Summary: Development files for %name
Requires: %name = %version-%release

%description devel
This package contains libraries and header files for developing applications
that use %name.

%prep
%setup
%patch0 -p1

%build
export CFLAGS="$RPM_OPT_FLAGS -fPIC"
export CXXFLAGS="$RPM_OPT_FLAGS -fPIC"
mkdir build
pushd build
%cmake -DLIBDIR=%{_libdir} .. -DBUILD_SHARED_LIBS=TRUE -DCMAKE_SHARED_LINKER_FLAGS="-Wl,--as-needed" -DBIBLESYNC_SOVERSION=%{__soversion}
%cmake_build
popd


%install

pushd build
%cmake_install
popd



%files
%doc AUTHORS COPYING ChangeLog* README* WIRESHARK
%_libdir/libbiblesync.so.%__soversion

%files devel
%_includedir/%name
%_pkgconfigdir/%name.pc
%_libdir/libbiblesync.so
%_man7dir/*

%changelog
* Sun Nov 23 2025 Ilya Mashkin <oddity@altlinux.ru> 2.1.0-alt2
- Add patch

* Sun Nov 23 2025 Ilya Mashkin <oddity@altlinux.ru> 2.1.0-alt1
- 2.1.0

* Tue Apr 27 2021 Arseny Maslennikov <arseny@altlinux.org> 1.2.0-alt2.1
- NMU: spec: adapted to new cmake macros.

* Sun Jun 10 2018 Vitaly Lipatov <lav@altlinux.ru> 1.2.0-alt2
- just rebuild

* Wed May 23 2018 Ildar Mulyukov <ildar@altlinux.ru> 1.2.0-alt1
- new version

* Wed Sep 13 2017 Ildar Mulyukov <ildar@altlinux.ru> 1.1.2-alt1
- converted for ALT Linux by srpmconvert tools


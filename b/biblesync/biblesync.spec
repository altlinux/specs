%global __soversion 1.1

Name: biblesync
Version: 1.2.0
Release: alt1
Summary: A Cross-platform library for sharing Bible navigation
Group: System/Libraries
License: Public Domain
Url: http://www.xiphos.org
Source: https://github.com/karlkleinpaste/biblesync/releases/download/%version/biblesync-%version.tar.gz
Source44: %name.watch

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

%build
%cmake \
	-DBUILD_SHARED_LIBS=TRUE \
	-DLIBDIR=%_libdir \
	-DBIBLESYNC_SOVERSION=%__soversion \

%make_build -C BUILD

%install
%makeinstall_std -C BUILD

%files
%doc AUTHORS COPYING ChangeLog* README* WIRESHARK
%_libdir/libbiblesync.so.%__soversion

%files devel
%_includedir/%name
%_pkgconfigdir/%name.pc
%_libdir/libbiblesync.so
%_man7dir/*

%changelog
* Wed May 23 2018 Ildar Mulyukov <ildar@altlinux.ru> 1.2.0-alt1
- new version

* Wed Sep 13 2017 Ildar Mulyukov <ildar@altlinux.ru> 1.1.2-alt1
- converted for ALT Linux by srpmconvert tools


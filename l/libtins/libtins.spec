#
# spec file for package libtins
#
# Copyright (c) 2015 SUSE LINUX GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

%define soname  3

Name: libtins
Version: 3.2
Release: alt1

Summary: C++ library for manipulating raw network packets
License: BSD-2-Clause
Group: System/Libraries

Url: http://libtins.github.io/
Source: https://github.com/mfontanini/libtins/archive/v3.2.tar.gz#/%name-%version.tar.gz
# PATCH-FIX-UPSTREAM build.patch avvissu@yandex.ru-- Place the package file in LIB_INSTALL_DIR/cmake
Patch: libtins-3.2_build.patch

BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: libpcap-devel
BuildRequires: pkgconfig
BuildRequires: pkgconfig(libcrypto)
BuildRequires: pkgconfig(libssl)

%description
The library's main purpose is to provide the C++ developer an easy,
efficient, platform and endianess-independent way to create tools which
need to send, receive and manipulate specially crafted packets.

%package -n %name%soname
Summary: C++ library for manipulating raw network packets
Group: System/Libraries

%description -n %name%soname
The library's main purpose is to provide the C++ developer an easy,
efficient, platform and endianess-independent way to create tools which
need to send, receive and manipulate specially crafted packets.

%package devel
Summary: Development files for tins
Group: Development/C++
Requires: %name%soname = %version

%description devel
This package contains header files, and libraries needed to develop
application that use libtins.

%prep
%setup
%patch -p1

%build
%cmake_insource -DLIBTINS_ENABLE_CXX11=1
%make_build

%install
%makeinstall_std

%files -n %name%soname
%doc AUTHORS CHANGES LICENSE README*
%_libdir/%name.so.*

%files devel
%_includedir/tins
%_libdir/pkgconfig/%name.pc
%_libdir/%name.so
%_libdir/cmake/tins

%changelog
* Sat May 23 2015 Michael Shigorin <mike@altlinux.org> 3.2-alt1
- built for ALT Linux (based on openSUSE package)

* Thu May  7 2015 avvissu@yandex.ru
- Initial release

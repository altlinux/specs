%define soname 1
Name: srt
Version: 1.5.1
Release: alt1
Summary: Secure Reliable Transport protocol tools
Group: Networking/Other
License: MPL-2.0
Url: https://www.srtalliance.org
# git https://github.com/Haivision/srt
Source0: https://github.com/Haivision/srt/archive/v%version/%name-%version.tar

BuildRequires: cmake gcc-c++
BuildRequires: libgnutls-devel libnettle-devel libp11-kit-devel libidn2-devel libtasn1-devel
BuildRequires: libgmock-devel
BuildRequires: libgtest-devel
BuildRequires: zlib-devel

Requires: libsrt%soname = %EVR

%description
Secure Reliable Transport (SRT) is an open source transport technology that
optimizes streaming performance across unpredictable networks, such as
the Internet.

%package -n libsrt%soname
Group: System/Libraries
Summary: Secure Reliable Transport protocol libraries

%description -n libsrt%soname
Secure Reliable Transport protocol libraries.

%package -n libsrt-devel
Group: Development/Other
Summary: Secure Reliable Transport protocol development libraries and headers
Requires: libsrt%soname = %EVR

%description -n libsrt-devel
Secure Reliable Transport protocol development libraries and header files.

%prep
%setup

%build
# disable network tests in hasher environment
sed -Ei 's,(^TEST_F.*\, )(.*),\1DISABLED_\2,' test/test_ipv6.cpp test/test_muxer.cpp

%cmake \
  -DENABLE_STATIC=OFF \
  -DENABLE_UNITTESTS=ON \
  -DENABLE_TESTING=ON \
  -DENABLE_GETNAMEINFO=ON \
  -DUSE_ENCLIB=gnutls


%cmake_build

%install
%cmake_install
# remove old upstream temporary compatibility pc
rm -f %buildroot/%_libdir/pkgconfig/haisrt.pc

%check
./%_cmake__builddir/test-srt

%files
%doc README.md docs LICENSE
%_bindir/srt-ffplay
%_bindir/srt-file-transmit
%_bindir/srt-live-transmit
%_bindir/srt-tunnel

%files -n libsrt%soname
%doc LICENSE
%_libdir/libsrt.so.%{soname}*

%files -n libsrt-devel
%doc examples
%_includedir/srt
%_libdir/libsrt.so
%_libdir/pkgconfig/srt.pc

%changelog
* Mon Nov 28 2022 Anton Farygin <rider@altlinux.ru> 1.5.1-alt1
- 1.5.1

* Sun Oct 10 2021 Anton Farygin <rider@altlinux.ru> 1.4.4-alt1
- 1.4.4

* Mon Sep 13 2021 Anton Farygin <rider@altlinux.ru> 1.4.3-alt1
- first build for ALT, based on specfile from Fedora

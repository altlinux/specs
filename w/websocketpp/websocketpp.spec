Name: websocketpp
Version: 0.7.0
Release: alt1

Summary: C++ WebSocket Protocol Library

License: BSD
Group: Development/C++
Url: http://www.zaphoyd.com/websocketpp

Packager: Vitaly Lipatov <lav@altlinux.ru>

# Source-url: https://github.com/zaphoyd/websocketpp/archive/%version.tar.gz
Source: %name-%version.tar
Source1: websocketpp.pc

BuildArch: noarch

# put cmake files in share/cmake instead of lib/cmake
Patch1: websocketpp-0.4.0-cmake_noarch.patch

BuildRequires(pre): rpm-macros-cmake
BuildRequires: boost-program_options-devel
BuildRequires: cmake gcc-c++
BuildRequires: pkg-config

%description
WebSocket++ is an open source (BSD license) header only C++ library
that impliments RFC6455 The WebSocket Protocol. It allows integrating
WebSocket client and server functionality into C++ programs. It uses
interchangeable network transport modules including one based on C++
iostreams and one based on Boost Asio.

%package devel
Group: Development/C++
Summary: C++ WebSocket Protocol Library
Requires: boost-program_options-devel

%description devel
WebSocket++ is an open source (BSD license) header only C++ library
that impliments RFC6455 The WebSocket Protocol. It allows integrating
WebSocket client and server functionality into C++ programs. It uses
interchangeable network transport modules including one based on C++
iostreams and one based on Boost Asio.

%prep
%setup

%patch1 -p1 -b .cmake_noarch

%build
%cmake
%cmake_build

%install
%cmakeinstall_std install/fast

%files devel
%doc COPYING changelog.md readme.md roadmap.md
%_includedir/websocketpp/
%dir %_datadir/cmake/
%_datadir/cmake/websocketpp/

%changelog
* Tue May 09 2017 Vitaly Lipatov <lav@altlinux.ru> 0.7.0-alt1
- new version 0.7.0 (with rpmrb script)

* Mon Dec 14 2015 Vitaly Lipatov <lav@altlinux.ru> 0.4.0-alt1
- initial build for ALT Linux Sisyphus

* Thu Aug 27 2015 Jonathan Wakely <jwakely@redhat.com> - 0.4.0-7
- Rebuilt for Boost 1.59

* Wed Jul 29 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.0-6
- Rebuilt for https://fedoraproject.org/wiki/Changes/F23Boost159

* Wed Jul 22 2015 David Tardon <dtardon@redhat.com> - 0.4.0-5
- rebuild for Boost 1.58

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Jan 27 2015 Petr Machata <pmachata@redhat.com> - 0.4.0-3
- Rebuild for boost 1.57.0

* Thu Nov 13 2014 Rex Dieter <rdieter@fedoraproject.org> 0.4.0-2
- use (upstreamable) cmake_noarch.patch instead of manually moving files around

* Wed Nov 05 2014 Rex Dieter <rdieter@fedoraproject.org> 0.4.0-1
- first try

* Mon Mar 17 2014 prusnak@opensuse.org
- created package (based on a Fedora package by Thomas Sailer)

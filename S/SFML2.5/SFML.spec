%define pkgname SFML
%define soversion 2.5

Name: %pkgname%soversion
Version: 2.5.1
Release: alt3

Summary: Simple and Fast Multimedia Library
License: Zlib
Group: System/Legacy libraries

Url: http://www.sfml-dev.org/
Packager: Nazarov Denis <nenderus@altlinux.org>

# Source-url: https://github.com/%pkgname/%pkgname/archive/%version/%pkgname-%version.tar.gz
Source: %pkgname-%version.tar

BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: libGLU-devel
BuildRequires: libXcomposite-devel
BuildRequires: libXcursor-devel
BuildRequires: libXdamage-devel
BuildRequires: libXdmcp-devel
BuildRequires: libXft-devel
BuildRequires: libXi-devel
BuildRequires: libXinerama-devel
BuildRequires: libXmu-devel
BuildRequires: libXrandr-devel
BuildRequires: libXxf86vm-devel
BuildRequires: libflac-devel
BuildRequires: libopenal-devel
BuildRequires: libudev-devel
BuildRequires: libvorbis-devel

%description
SFML is a simple, fast, cross-platform and object-oriented multimedia
API. It provides access to windowing, graphics, audio and network.
It is written in C++, and has bindings for various languages such as C,
.Net, Ruby, Python.

%package -n lib%name
Summary: Simple and Fast Multimedia Library
Group: System/Libraries

%description -n lib%name
SFML is a simple, fast, cross-platform and object-oriented multimedia
API. It provides access to windowing, graphics, audio and network.
It is written in C++, and has bindings for various languages such as C,
.Net, Ruby, Python.

%prep
%setup -n %pkgname-%version

%build
%cmake -Wno-dev
%cmake_build

%install
%cmake_install
%__rm -rf %buildroot%_datadir/%pkgname
%__rm -rf %buildroot%_includedir/%pkgname
%__rm -rf %buildroot%_pkgconfigdir/sfml-*.pc
%__rm -rf %buildroot%_libdir/libsfml-*.so
%__rm -rf %buildroot%_libdir/cmake/%pkgname

%files -n lib%name
%doc changelog.md license.md readme.md
%_libdir/libsfml-*.so.*

%changelog
* Tue Nov 14 2023 Nazarov Denis <nenderus@altlinux.org> 2.5.1-alt3
- Build as legacy library

* Mon May 13 2019 Michael Shigorin <mike@altlinux.org> 2.5.1-alt2
- fixed build on 64-bit platforms
- minor spec cleanup

* Sun Feb 24 2019 Nazarov Denis <nenderus@altlinux.org> 2.5.1-alt1
- Version 2.5.1

* Mon Oct 08 2018 Anton Farygin <rider@altlinux.ru> 2.4.2-alt3
- fixed build on aarch64

* Thu Apr 05 2018 Yuri N. Sedunov <aris@altlinux.org> 2.4.2-alt2
- rebuilt with gcc7 especially for extreme-tuxracer

* Sun Mar 26 2017 Nazarov Denis <nenderus@altlinux.org> 2.4.2-alt1
- Version 2.4.2

* Tue Nov 01 2016 Nazarov Denis <nenderus@altlinux.org> 2.4.0-alt1
- Version 2.4.0

* Sun Jun 12 2016 Igor Vlasenko <viy@altlinux.ru> 2.3.2-alt2
- NMU: added pkgconfig file, fixed cmake

* Sat Nov 07 2015 Nazarov Denis <nenderus@altlinux.org> 2.3.2-alt1
- Version 2.3.2

* Sun Aug 02 2015 Nazarov Denis <nenderus@altlinux.org> 2.3.1-alt1
- Initial release for ALT Linux

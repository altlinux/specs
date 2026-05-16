%define soversion 3.1

Name: SFML
Version: 3.1.0
Release: alt1

Summary: Simple and Fast Multimedia Library
License: Zlib
Group: System/Libraries

Url: http://www.sfml-dev.org/
Vcs: https://github.com/%name/%name
Packager: Nazarov Denis <nenderus@altlinux.org>

# Source-url: https://github.com/%name/%name/archive/%version/%name-%version.tar.gz
Source: %name-%version.tar

Patch0: %name-3.1.0-use-system-SheenBidi-debian.patch

BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: libGLU-devel
BuildRequires: libSheenBidi-devel
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
BuildRequires: libharfbuzz-devel
BuildRequires: libmbedtls-devel
BuildRequires: libssh2-devel
BuildRequires: libudev-devel
BuildRequires: libvorbis-devel

%description
SFML is a simple, fast, cross-platform and object-oriented multimedia
API. It provides access to windowing, graphics, audio and network.
It is written in C++, and has bindings for various languages such as C,
.Net, Ruby, Python.

%package -n lib%name%soversion
Summary: Simple and Fast Multimedia Library
Group: System/Libraries

%description -n lib%name%soversion
SFML is a simple, fast, cross-platform and object-oriented multimedia
API. It provides access to windowing, graphics, audio and network.
It is written in C++, and has bindings for various languages such as C,
.Net, Ruby, Python.

%package -n lib%name-devel
Summary: Development files for SFML
Group: Development/C++
Requires: lib%name%soversion = %EVR
Conflicts: libsfml-devel

%description -n lib%name-devel
Contains libraries and header files for
developing applications that use SFML.

%prep
%setup
%patch0 -p1

%build
%cmake \
	-DBUILD_SHARED_LIBS:BOOL=ON \
	-DSFML_INSTALL_PKGCONFIG_FILES:BOOL=ON \
	-DSFML_PKGCONFIG_INSTALL_DIR:PATH=%_pkgconfigdir \
	-Wno-dev
%cmake_build

%install
%cmake_install

%files -n lib%name%soversion
%doc CONTRIBUTING.md changelog.md migration.md
%_libdir/libsfml-*.so.*

%files -n lib%name-devel
%_defaultdocdir/%name
%_includedir/%name
%_pkgconfigdir/sfml-*.pc
%_libdir/libsfml-*.so
%_libdir/cmake/%name/*.cmake

%changelog
* Sat May 16 2026 Nazarov Denis <nenderus@altlinux.org> 3.1.0-alt1
- New version 3.1.0.

* Thu Sep 18 2025 Nazarov Denis <nenderus@altlinux.org> 3.0.2-alt1
- New version 3.0.2.

* Tue Apr 22 2025 Nazarov Denis <nenderus@altlinux.org> 3.0.1-alt1
- New version 3.0.1.

* Sun Dec 22 2024 Nazarov Denis <nenderus@altlinux.org> 3.0.0-alt1
- New version 3.0.0.

* Tue Nov 12 2024 Nazarov Denis <nenderus@altlinux.org> 2.6.2-alt1
- New version 2.6.2.

* Tue Nov 14 2023 Nazarov Denis <nenderus@altlinux.org> 2.6.1-alt1
- New version 2.6.1.

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

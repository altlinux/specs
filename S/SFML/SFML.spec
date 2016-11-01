%define soversion 2.4

Name: SFML
Version: 2.4.0
Release: alt1

Summary: Simple and Fast Multimedia Library
License: zlib
Group: System/Libraries

Url: http://www.sfml-dev.org/
Packager: Nazarov Denis <nenderus@altlinux.org>
# https://github.com/%name/%name/archive/%version.tar.gz
Source: %name-%version.tar.gz

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
BuildRequires: libjpeg-devel
BuildRequires: libopenal-devel
BuildRequires: libudev-devel
BuildRequires: libvorbis-devel
BuildRequires: libxcbutil-image-devel

%description
SFML is a simple, fast, cross-platform and object-oriented multimedia API. It provides access to windowing, graphics, audio and network.
It is written in C++, and has bindings for various languages such as C, .Net, Ruby, Python.

%package -n lib%name%soversion
Summary: Simple and Fast Multimedia Library
Group: System/Libraries

%description -n lib%name%soversion
SFML is a simple, fast, cross-platform and object-oriented multimedia API. It provides access to windowing, graphics, audio and network.
It is written in C++, and has bindings for various languages such as C, .Net, Ruby, Python.

%package -n lib%name-devel
Summary: Development files for SFML
Group: Development/C++
Requires: lib%name%soversion = %EVR
Conflicts: libsfml-devel

%description -n lib%name-devel
Contains libraries and header files for
developing applications that use SFML

%prep
%setup

%build
%__mkdir_p %_target_platform
pushd %_target_platform

cmake .. \
	-DCMAKE_INSTALL_PREFIX:PATH=%prefix \
	-DCMAKE_C_FLAGS:STRING='%optflags' \
	-DCMAKE_CXX_FLAGS:STRING='%optflags' \
%ifarch x86_64	
	-DLIB_SUFFIX="64" \
%endif
	-DCMAKE_SKIP_RPATH:BOOL=TRUE \
	-DCMAKE_BUILD_TYPE:STRING="Release" \
	-DSFML_INSTALL_PKGCONFIG_FILES:BOOL=TRUE \

popd

%make_build -C %_target_platform

%install
%makeinstall_std -C %_target_platform
%__rm -rf %buildroot%_datadir/%name/{license,readme}.txt

# move FindSFML.cmake to the standard location
%__mkdir_p %buildroot%_datadir/cmake/Modules
%__mv %buildroot%_datadir/%name/cmake/Modules/Find%name.cmake %buildroot%_datadir/cmake/Modules

%files -n lib%name%soversion
%doc changelog.txt license.txt readme.txt
%_libdir/libsfml-*.so.*

%files -n lib%name-devel
%dir %_datadir/%name
%dir %_datadir/cmake
%dir %_datadir/cmake/Modules
%_datadir/cmake/Modules/Find%name.cmake
%_includedir/%name
%_pkgconfigdir/sfml-*.pc
%_libdir/libsfml-*.so

%changelog
* Tue Nov 01 2016 Nazarov Denis <nenderus@altlinux.org> 2.4.0-alt1
- Version 2.4.0

* Sun Jun 12 2016 Igor Vlasenko <viy@altlinux.ru> 2.3.2-alt2
- NMU: added pkgconfig file, fixed cmake

* Sat Nov 07 2015 Nazarov Denis <nenderus@altlinux.org> 2.3.2-alt1
- Version 2.3.2

* Sun Aug 02 2015 Nazarov Denis <nenderus@altlinux.org> 2.3.1-alt1
- Initial release for ALT Linux

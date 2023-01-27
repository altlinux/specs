%define git 3f864cc
%define soname 2

Name: fdk-aac
Version: 2.0.2
Release: alt0.2.g%{git}
Summary: Fraunhofer FDK AAC Codec Library for Android
License: Permissive
Group: System/Libraries
Url: https://github.com/mstorsjo/fdk-aac
Packager: L.A. Kostis <lakostis@altlinux.ru>

Source: %name-%version.tar

BuildRequires(pre): cmake
BuildRequires: gcc-c++

%description
The Fraunhofer FDK AAC Codec Library for Android ("FDK AAC Codec") is software
that implements the MPEG Advanced Audio Coding ("AAC") encoding and decoding
scheme for digital audio. This FDK AAC Codec software is intended to be used on
a wide variety of Android devices.

%package -n lib%{name}%{soname}
Summary: The Fraunhofer FDK AAC Codec Library
Group: System/Libraries

%description -n lib%{name}%{soname}
The Fraunhofer FDK AAC Codec Library for Android ("FDK AAC Codec") is software
that implements the MPEG Advanced Audio Coding ("AAC") encoding and decoding
scheme for digital audio. This FDK AAC Codec software is intended to be used on
a wide variety of Android devices.

%package -n lib%{name}-devel
Summary: The Fraunhofer FDK AAC Codec Library Headers
Group: Development/C++
Requires: lib%{name}%{soname} = %EVR

%description -n lib%{name}-devel
%name-devel contains header files needed to
develop programs which make use of %name

%prep
%setup -q

%build
%cmake
%cmake_build

%install
%cmakeinstall_std

%files -n lib%{name}%{soname}
%_libdir/*.so.*

%files -n lib%{name}-devel
%dir %_includedir/%name
%_includedir/%name/*.h
%_libdir/*.so
%_pkgconfigdir/*.pc
%_libdir/cmake/*

%changelog
* Fri Jan 27 2023 L.A. Kostis <lakostis@altlinux.ru> 2.0.2-alt0.2.g3f864cc
- GIT 3f864cc.

* Mon Jun 14 2021 L.A. Kostis <lakostis@altlinux.ru> 2.0.2-alt0.1
- 2.0.2.
- switch to cmake.

* Sat Mar 21 2020 L.A. Kostis <lakostis@altlinux.ru> 2.0.1-alt0.1
- 2.0.1.

* Mon Sep 16 2019 L.A. Kostis <lakostis@altlinux.ru> 2.0.0-alt0.1.g5ab5496
- GIT 5ab5496.
- Initial build for ALTLinux.

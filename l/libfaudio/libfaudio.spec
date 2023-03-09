%define build_type RelWithDebInfo
%define _cmake %cmake -DCMAKE_BUILD_TYPE=%build_type -DCMAKE_VERBOSE_MAKEFILE:BOOL=ON
%define git %nil
%define sovers 0
%def_disable static

Name: libfaudio
Version: 23.03
Release: alt1
Summary: Accuracy-focused XAudio reimplementation for open platforms

License: Zlib
Group: System/Libraries
Url: https://github.com/FNA-XNA/FAudio

Source: %name-%version.tar
Patch: %name-%version-%release.patch

BuildRequires(pre): cmake pkgconfig
BuildRequires: libSDL2-devel
BuildRequires: gcc-c++ chrpath

Packager: L.A. Kostis <lakostis@altlinux.ru>

%package -n %name%{sovers}
Summary: Accuracy-focused XAudio reimplementation for open platforms
Group: System/Libraries

%package -n %name-devel
Summary: %name development environment
Group: Development/C++
Requires: %name%{sovers} = %EVR

%package -n %name-devel-static
Summary: %name static development environment
Group: Development/C++
Requires: %name-devel = %EVR

%description
This is FAudio, an XAudio reimplementation that focuses solely on developing
fully accurate DirectX Audio runtime libraries for the FNA project, including
XAudio2, X3DAudio, XAPO, and XACT3.

%description -n %name%{sovers}
This is FAudio, an XAudio reimplementation that focuses solely on developing
fully accurate DirectX Audio runtime libraries for the FNA project, including
XAudio2, X3DAudio, XAPO, and XACT3.

%description -n %name-devel
This package contains all files which are needs to compile programs using
the %name library.

%description -n %name-devel-static
This package contains libraries which are needs to compile programs statically
linked against %name library.

%prep
%setup
%patch -p1

%build
%_cmake
%cmake_build

%install
%cmakeinstall_std
chrpath -d %buildroot%{_libdir}/*.so.*.*

%files -n %name%{sovers}
%_libdir/*.so.*
%doc README* LICENSE

%files -n %name-devel
%_includedir/*
%_libdir/*.so
%_datadir/cmake/FAudio
%_pkgconfigdir/*.pc

%if_enabled static
%files -n %name-devel-static
%_libdir/*.a
%endif

%changelog
* Thu Mar 09 2023 L.A. Kostis <lakostis@altlinux.ru> 23.03-alt1
- 23.03.

* Wed Sep 28 2022 L.A. Kostis <lakostis@altlinux.ru> 22.09-alt1.1
- 22.09.01.

* Fri Sep 03 2021 L.A. Kostis <lakostis@altlinux.ru> 21.08-alt0.1
- 21.08.

* Tue Jun 15 2021 L.A. Kostis <lakostis@altlinux.ru> 21.06-alt0.1
- 21.06.
- Fix cmake files location.

* Mon Feb 15 2021 L.A. Kostis <lakostis@altlinux.ru> 21.02-alt0.1
- 21.02.
- Add pkgconfig support.

* Wed Sep 09 2020 L.A. Kostis <lakostis@altlinux.ru> 20.09-alt0.1
- 20.09.
- Update license tag.

* Sun Mar 15 2020 L.A. Kostis <lakostis@altlinux.ru> 20.03-alt0.1
- 20.03.

* Mon Sep 30 2019 L.A. Kostis <lakostis@altlinux.ru> 19.09-alt0.1.g65b787f
- Initial build for ALTLinux.

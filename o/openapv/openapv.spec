%def_disable snapshot

%define _name openapv
%define __name oapv
%define ver_major 0.3
%define sover 3

%def_enable apps
%def_enable check

Name: %_name
Version: %ver_major.0.0
Release: alt1

Summary: OpenAPV (Open Advanced Professional Video Codec)
License: BSD-3-Clause
Group: Video
Url: https://github.com/AcademySoftwareFoundation/openapv

Vcs: https://github.com/AcademySoftwareFoundation/openapv.git

%if_disabled snapshot
Source: https://github.com/AcademySoftwareFoundation/openapv/archive/v%version/%_name-%version.tar.gz
%else
Source: %_name-%version.tar
%endif

BuildRequires(pre): rpm-macros-cmake
BuildRequires: cmake gcc-c++
%{?_enable_check:BuildRequires: ctest}

%description
OpenAPV provides the reference implementation of the APV Codec
(https://datatracker.ietf.org/doc/draft-lim-apv/)
which can be used to record professional-grade video and associated
metadata without quality degradation.

%package -n lib%name
Summary: OpenAPV shared library
Group: System/Libraries
Provides: lib%__name = %EVR

%description -n lib%name
This package provides OpenAPV shared library.

%package -n lib%name-devel
Summary: OpenAPV development files
Group: Development/C
Requires: lib%name = %EVR
Provides: lib%__name-devel = %EVR

%description -n lib%name-devel
This package privides files needed for doing development using OpenAPV.

%package apps
Summary: The OpenAPV apps
Group: Video
Requires: lib%name = %EVR

%description apps
This package provides OpenAPV encoder and decoder command line apps.

%prep
%setup -n %_name-%version

%build
%cmake \
    -DCMAKE_BUILD_TYPE=Release \
    -DOAPV_BUILD_STATIC_LIB=OFF \
    %{?_disable_apps:-DOAPV_BUILD_APPS=OFF} \
    -DOAPV_APP_STATIC_BUILD=OFF \
    %{?_disable_check:-DENABLE_TESTS=OFF}
%nil
%cmake_build

%install
%cmake_install

%check
%cmake_build -t test

%files -n lib%name
%_libdir/lib%__name.so.%{sover}*
%doc README*

%files -n lib%name-devel
%_includedir/%__name/
%_libdir/lib%__name.so
%_pkgconfigdir/%__name.pc

%files apps
%_bindir/%{__name}_app_dec
%_bindir/%{__name}_app_enc

%changelog
* Mon Jun 29 2026 Yuri N. Sedunov <aris@altlinux.org> 0.3.0.0-alt1
- 0.3.0.0

* Wed Apr 29 2026 Yuri N. Sedunov <aris@altlinux.org> 0.2.1.3-alt1
- 0.2.1.3

* Fri Mar 13 2026 Yuri N. Sedunov <aris@altlinux.org> 0.2.1.2-alt1
- 0.2.1.2

* Thu Feb 19 2026 Yuri N. Sedunov <aris@altlinux.org> 0.2.1.1-alt1
- 0.2.1.1

* Fri Jan 30 2026 Yuri N. Sedunov <aris@altlinux.org> 0.2.1.0-alt1
- 0.2.1.0

* Fri Sep 26 2025 Yuri N. Sedunov <aris@altlinux.org> 0.2.0.4-alt1
- 0.2.0.4

* Tue Sep 09 2025 Yuri N. Sedunov <aris@altlinux.org> 0.2.0.3-alt1
- 0.2.0.3

* Wed Sep 03 2025 Yuri N. Sedunov <aris@altlinux.org> 0.2.0.2-alt1
- 0.2.0.2

* Thu Jul 31 2025 Yuri N. Sedunov <aris@altlinux.org> 0.2.0.1-alt1
- 0.2.0.1

* Thu Jul 24 2025 Yuri N. Sedunov <aris@altlinux.org> 0.2.0.0-alt1
- first build for Sisyphus



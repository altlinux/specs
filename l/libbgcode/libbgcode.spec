%define name_orig LibBGCode
%{?optflags_lto:%global optflags_lto %optflags_lto -ffat-lto-objects}

Name:    libbgcode
Version: 0.2.0
Release: alt1
Summary: Prusa Block & Binary G-code reader / writer / converter
License: AGPL-3.0-only
Group:   System/Base
URL:     https://github.com/prusa3d/libbgcode
VCS:     https://github.com/prusa3d/libbgcode
Source:  %name-%version.tar

BuildRequires(pre): rpm-macros-cmake

BuildRequires: libgtkmm3-devel
BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: heatshrink
BuildRequires: heatshrink-devel
BuildRequires: boost-devel
BuildRequires: boost-beast-devel
BuildRequires: catch-devel
BuildRequires: zlib-devel
BuildRequires: libstdc++-devel
BuildRequires: glibc-devel

%description
Prusa Block & Binary G-code reader / writer / converter

%package devel
Summary: Prusa Block & Binary G-code reader / writer / converter
Group: System/Base
Requires: libbgcode_core%version = %EVR
Requires: libbgcode_binarize%version = %EVR
Requires: libbgcode_convert%version = %EVR
Conflicts: libbgcode-devel-static < %EVR

%description devel
Prusa Block & Binary G-code reader / writer / converter

%package -n libbgcode_core%version
Summary: Prusa Block & Binary G-code reader / writer / converter
Group: System/Libraries

%description -n libbgcode_core%version
Prusa Block & Binary G-code reader / writer / converter

%package -n libbgcode_binarize%version
Summary: Prusa Block & Binary G-code reader / writer / converter
Group: System/Libraries

%description -n libbgcode_binarize%version
Prusa Block & Binary G-code reader / writer / converter

%package -n libbgcode_convert%version
Summary: Prusa Block & Binary G-code reader / writer / converter
Group: System/Libraries

%description -n libbgcode_convert%version
Prusa Block & Binary G-code reader / writer / converter

%prep
%setup

%build
%cmake -DBUILD_SHARED_LIBS=ON -DLibBGCode_BUILD_TESTS=OFF
%cmake_build

%install
%cmake_install

%files
%_bindir/bgcode

%files -n libbgcode_core%version
%_libdir/libbgcode_core.so.%version

%files -n libbgcode_binarize%version
%_libdir/libbgcode_binarize.so.%version

%files -n libbgcode_convert%version
%_libdir/libbgcode_convert.so.%version

%files devel
%_includedir/%name_orig/
%_libdir/cmake/%name_orig/
%_libdir/libbgcode_core.so
%_libdir/libbgcode_binarize.so
%_libdir/libbgcode_convert.so

%changelog
* Mon Jan 19 2026 Arseniy Romenskiy <romenskiy@altlinux.org> 0.2.0-alt1
- Build as shared libraries instead static (Closes: 57533)
- Fix license (Closes: 57538).
- Recompiled using dynamic libraries.

* Thu Nov 27 2025 Arseniy Romenskiy <romenskiy@altlinux.org> 0.0-alt1
- Initial build.

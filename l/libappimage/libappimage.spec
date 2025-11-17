%def_with static
%if_with static
%{?optflags_lto:%global optflags_lto %optflags_lto -ffat-lto-objects}
%endif

%define sover 1.0

Name: libappimage
Version: 1.0.4.5.0.29.f8f1
Release: alt1

Summary: Implements functionality for dealing with AppImage files

License: MIT
Group: Networking/File transfer
URL: https://github.com/AppImage/libappimage
VCS: https://github.com/AppImage/libappimage

Source: %name-%version.tar
Patch: %name-%version-%release.patch

BuildRequires(pre): rpm-build-ninja
BuildRequires: gcc-c++ cmake desktop-file-utils glib2-devel libgio-devel zlib-devel libcairo-devel librsvg-devel libgtest-devel liblzma-devel libzstd-devel libfuse-devel squashfuse-devel libarchive-devel boost-devel xdg-utils-cxx-devel

%description
This library is part of the AppImage project. It implements functionality for
dealing with AppImage files. It is written in C++ and is using Boost.

%package common
Summary: Implements functionality for dealing with AppImage files
Group: Documentation
BuildArch: noarch

%description common
This package provides common files for %name.

%package -n %name%sover
Summary: Implements functionality for dealing with AppImage files
Group: System/Libraries

%description -n %name%sover
This library is part of the AppImage project. It implements functionality for
dealing with AppImage files. It is written in C++ and is using Boost.

%package devel
Summary: Development files for %name
Group: Development/C++

%description devel
This package provides development files for %name.

%if_with static
%package devel-static
Summary: Development files for %name
Group: Development/C++

%description devel-static
This package provides development files for %name.
%endif

%prep
%setup
%patch -p1

%build
%cmake \
  -G Ninja \
  -DCMAKE_BUILD_TYPE=RelWithDebInfo \
  -DUSE_SYSTEM_SQUASHFUSE=ON \
  -DUSE_SYSTEM_XDGUTILS=ON
%cmake_build

%install
%cmake_install

%files common
%doc LICENSE README.md

%files -n %name%sover
%_libdir/%name.so.%{sover}*

%files devel
%_libdir/%name.so
%_includedir/appimage
%_pkgconfigdir/%name.pc
%_libdir/cmake/%name/

%if_with static
%files devel-static
%_libdir/%{name}*.a
%endif

%changelog
* Thu Nov 13 2025 Leontiy Volodin <lvol@altlinux.org> 1.0.4.5.0.29.f8f1-alt1
- Initial build for ALT Sisyphus (for deepin-file-manager).

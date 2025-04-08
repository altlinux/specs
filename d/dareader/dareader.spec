%define sover 1

Name: dareader
Version: 0.0.15.933f
Release: alt1

Summary: Reading data from fd provided by deepin-authentication

License: GPL-3.0-only
Group: Graphical desktop/Other
Url: https://github.com/linuxdeepin/dareader
Vcs: https://github.com/linuxdeepin/dareader.git

Source: %url/archive/%version/%name-%version.tar.xz
Patch: %name-%version-%release.patch

BuildRequires(pre): rpm-build-ninja
BuildRequires: gcc-c++ cmake

%description
%summary.

%package common
Summary: Common files for %name
Group: Graphical desktop/Other
BuildArch: noarch

%description common
The package provides common files for %name.

%package -n lib%name%sover
Summary: Library for read image/video from socket file
Group: System/Libraries

%description -n lib%name%sover
The package provides library for %name.

%package -n lib%name-devel
Summary: Development files for %name
Group: Development/C++

%description -n lib%name-devel
The package provides development files for %name.

%prep
%setup
%autopatch -p1

%build
%cmake \
  -G Ninja \
#
%cmake_build

%install
%cmake_install

%files common
%doc LICENSE README*.md

%files -n lib%name%sover
%_libdir/lib%name.so.%{sover}*

%files -n lib%name-devel
%_libdir/lib%name.so
%dir %_includedir/%name/
%_includedir/%name/reader.h
%_pkgconfigdir/%name.pc

%changelog
* Fri Apr 04 2025 Leontiy Volodin <lvol@altlinux.org> 0.0.15.933f-alt1
- Initial build for ALT Sisyphus (for deepin-control-center).

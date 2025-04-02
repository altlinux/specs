%def_without clang

%define sover 1

Name: deepin-pdfium
Version: 1.5.1
Release: alt1

Summary: Development library for pdf on Deepin

License: LGPL-3.0+
Group: Graphical desktop/Other
Url: https://github.com/linuxdeepin/deepin-pdfium
Vcs: https://github.com/linuxdeepin/deepin-pdfium.git

Source: %url/archive/%version/%name-%version.tar.gz
Patch: deepin-pdfium-1.5.1-alt-pkgconfig-dqt6.patch

BuildRequires: dqt6-base-devel libchardet-devel liblcms2-devel libfreetype-devel libopenjpeg2.0-devel libjpeg-devel
%if_with clang
BuildRequires: clang-devel
BuildRequires: lld-devel
BuildRequires: llvm-devel
%else
BuildRequires: gcc-c++
%endif

%description
%summary.

%package -n lib%name%sover
Summary: Library for %name
Group: System/Libraries

%description -n lib%name%sover
%summary.

%package -n lib%name-devel
Summary: Development files for %name
Group: Development/Other

%description -n lib%name-devel
This package provides development files for %name.

%prep
%setup
%autopatch -p1

%build
%if_with clang
%define optflags_lto -flto=thin
export CC=clang
export CXX=clang++
export LDFLAGS="-fuse-ld=lld $LDFLAGS"
%endif

%DQ6build \
  -DVERSION=%version \
  -DCMAKE_INSTALL_LIBDIR=%_lib \
#

%install
%DQ6install

%files -n lib%name%sover
%doc LICENSE
%_libdir/lib%name.so.%{sover}*

%files -n lib%name-devel
%_libdir/lib%name.so
%dir %_includedir/%name/
%_includedir/%name/*.h
%_pkgconfigdir/%name.pc
%_libdir/cmake/%name/

%changelog
* Tue Mar 11 2025 Leontiy Volodin <lvol@altlinux.org> 1.5.1-alt1
- New version 1.5.1.
- Switched to dqt6.
- Added vcs tag.

* Thu May 16 2024 Leontiy Volodin <lvol@altlinux.org> 1.0.2-alt2
- Built via separate qt5 instead system (ALT #48138).

* Tue Oct 24 2023 Leontiy Volodin <lvol@altlinux.org> 1.0.2-alt1
- Initial build for ALT Sisyphus.
- Needed for deepin-file-manager 6.0.13.

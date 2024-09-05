%def_without clang

%define sover 1

Name: deepin-pdfium
Version: 1.0.2
Release: alt2

Summary: Development library for pdf on Deepin

License: LGPL-3.0+
Group: Graphical desktop/Other
Url: https://github.com/linuxdeepin/deepin-pdfium

Source: %url/archive/%version/%name-%version.tar.gz

BuildRequires: dqt5-base-devel libchardet-devel liblcms2-devel libfreetype-devel libopenjpeg2.0-devel libjpeg-devel
%if_with clang
BuildRequires: clang-devel
BuildRequires: lld-devel
BuildRequires: llvm-devel
%else
BuildRequires: gcc-c++
%endif

# find libraries
%add_findprov_lib_path %_dqt5_libdir

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

%build
export PATH=%_dqt5_bindir:$PATH
%if_with clang
%define optflags_lto -flto=thin
export CC=clang
export CXX=clang++
export LDFLAGS="-fuse-ld=lld $LDFLAGS"
%endif

%qmake_dqt5 \
  CONFIG+=nostrip \
  QMAKE_RPATHDIR=%_dqt5_libdir \
  VERSION=%version \
  LIB_INSTALL_DIR=%_libdir \
  unix:LIBS+="-L%_libdir -ljpeg -licuuc" \
  unix:LIBS+="-L/%_lib -lz" \
%if_enabled clang
  QMAKE_STRIP= -spec linux-clang \
%endif
#
%make_build

%install
%makeinstall INSTALL_ROOT=%buildroot

%files -n lib%name%sover
%doc LICENSE
%_libdir/lib%name.so.%{sover}*

%files -n lib%name-devel
%_libdir/lib%name.so
%dir %_includedir/%name/
%_includedir/%name/*.h
%_pkgconfigdir/%name.pc

%changelog
* Thu May 16 2024 Leontiy Volodin <lvol@altlinux.org> 1.0.2-alt2
- Built via separate qt5 instead system (ALT #48138).

* Tue Oct 24 2023 Leontiy Volodin <lvol@altlinux.org> 1.0.2-alt1
- Initial build for ALT Sisyphus.
- Needed for deepin-file-manager 6.0.13.

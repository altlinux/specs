%define repo image-editor
%define repoiv imageviewer
%define repoivr imagevisualresult
%define sonameiv 0
%define sonameivr 0
%define llvm_ver 15

%def_disable clang
%def_enable cmake

Name: deepin-image-editor
Version: 1.0.25
Release: alt1
Summary: Image editor libraries for Deepin
License: GPL-3.0+
Group: System/Libraries
Url: https://github.com/linuxdeepin/image-editor

Source: %url/archive/%version/%repo-%version.tar.gz

%if_enabled clang
ExcludeArch: armh
%endif

%if_enabled clang
#BuildRequires(pre): rpm-macros-llvm-common
BuildRequires: clang%llvm_ver.0-devel
BuildRequires: lld%llvm_ver.0-devel
BuildRequires: llvm%llvm_ver.0-devel
%else
BuildRequires: gcc-c++
%endif
%if_enabled cmake
BuildRequires(pre): cmake rpm-build-ninja
%endif
BuildRequires: qt5-base-devel qt5-svg-devel qt5-tools-devel dtk5-widget-devel libopencv-devel libfreeimage-devel glib2-devel libmediainfo-devel libtiff-devel libffmpegthumbnailer-devel

%description
Image editor is a public library for deepin-image-viewer
and deepin-album developed by Deepin Technology.

%package -n lib%repoiv-data
Summary: Data files for lib%repoiv
Group: Development/Other
BuildArch: noarch

%description -n lib%repoiv-data
Data files for libimageviewer.

%package -n lib%repoivr-data
Summary: Data files for lib%repoivr
Group: Development/Other
BuildArch: noarch

%description -n lib%repoivr-data
Data files for libimagevisualresult.

%package -n lib%repoiv%sonameiv
Summary: Image editor library for deepin-image-viewer
Group: System/Libraries
Requires: lib%repoiv-data

%description -n lib%repoiv%sonameiv
Image editor is a public library for deepin-image-viewer
by Deepin Technology.

%package -n lib%repoiv-devel
Summary: Development package for deepin-image-viewer
Group: Development/C++

%description -n lib%repoiv-devel
Development libraries for deepin-image-viewer.

%package -n lib%repoivr%sonameivr
Summary: Image editor library for deepin-album
Group: System/Libraries

%description -n lib%repoivr%sonameivr
Image editor is a public library for deepin-image-viewer
by Deepin Technology.

%package -n lib%repoivr-devel
Summary: Development package for deepin-album
Group: Development/C++

%description -n lib%repoivr-devel
Development libraries for deepin-album.

%prep
%setup -n %repo-%version
sed -i 's|/usr/lib/|%_libdir/|' \
    libimageviewer/CMakeLists.txt \
    libimageviewer/libimageviewer.pro \
    libimagevisualresult/CMakeLists.txt
sed -i 's|3rdparty/tiff-tools/converttiff.h|../../3rdparty/tiff-tools/converttiff.h|' \
    libimageviewer/unionimage/unionimage.cpp
sed -i 's|libimageviewer|libimagevisualresult|' \
    libimagevisualresult/libimagevisualresult.pc.in

%build
export PATH=%_qt5_bindir:$PATH
%if_enabled cmake
%if_enabled clang
%define optflags_lto -flto=thin
export CC=clang-%llvm_ver
export CXX=clang++-%llvm_ver
export LDFLAGS="-fuse-ld=lld-%llvm_ver $LDFLAGS"
%else
%define optflags_lto %nil
%endif
%cmake \
    -GNinja \
    -DCMAKE_BUILD_TYPE=RelWithDebInfo \
    -DAPP_VERSION=%version \
    -DVERSION=%version \
    -DLIB_INSTALL_DIR=%_libdir \
    -DCMAKE_INSTALL_LIBDIR=%_lib \
    %nil
cmake --build "%_cmake__builddir"
%else
%qmake_qt5 \
%if_enabled clang
    QMAKE_STRIP= -spec linux-clang \
%endif
    CONFIG+=nostrip \
    PREFIX=%prefix \
    DAPP_VERSION=%version \
    DVERSION=%version \
    LIB_INSTALL_DIR=%_libdir \
    %nil
%make
%endif

%install
%if_enabled cmake
%cmake_install
%else
%makeinstall INSTALL_ROOT=%buildroot
%endif

%files -n lib%repoiv-data
%doc LICENSE.txt README.md
%dir %_datadir/lib%repoiv/
%_datadir/lib%repoiv/*

%files -n lib%repoivr-data
%dir %_datadir/lib%repoivr/
%_datadir/lib%repoivr/filter*

%files -n lib%repoiv%sonameiv
%_libdir/lib%repoiv.so.%{sonameiv}*

%files -n lib%repoiv-devel
%_libdir/lib%repoiv.so
%_includedir/lib%repoiv/
%_pkgconfigdir/lib%repoiv.pc

%files -n lib%repoivr%sonameivr
%_libdir/lib%repoivr.so.%{sonameivr}*

%files -n lib%repoivr-devel
%_libdir/lib%repoivr.so
%_includedir/lib%repoivr/
%_pkgconfigdir/lib%repoivr.pc

%changelog
* Tue Mar 07 2023 Leontiy Volodin <lvol@altlinux.org> 1.0.25-alt1
- New version.

* Fri Feb 03 2023 Leontiy Volodin <lvol@altlinux.org> 1.0.24-alt2
- Enabled build on armh.

* Tue Jan 17 2023 Leontiy Volodin <lvol@altlinux.org> 1.0.24-alt1
- New version.

* Thu Jul 21 2022 Leontiy Volodin <lvol@altlinux.org> 1.0.18-alt1
- New version.

* Wed May 11 2022 Leontiy Volodin <lvol@altlinux.org> 1.0.13-alt1
- Initial build for ALT Sisyphus.
- Built as require for deepin-image-viewer.

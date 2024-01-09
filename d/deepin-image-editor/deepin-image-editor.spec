%define repo image-editor
%define repoiv imageviewer
%define repoivr imagevisualresult
%define sonameiv 0
%define sonameivr 0

%def_without clang
%def_with cmake

Name: deepin-image-editor
Version: 1.0.40.0.1.7088
Release: alt1

Summary: Image editor libraries for Deepin

License: GPL-3.0+
Group: System/Libraries
Url: https://github.com/linuxdeepin/image-editor

Source: %url/archive/%version/%repo-%version.tar.gz
# Applied the patch by archlinux:
# https://gitlab.archlinux.org/archlinux/packaging/packages/deepin-image-editor/-/raw/main/remove-broken-flags.patch
Patch: %name-%version-%release.patch

%if_with clang
ExcludeArch: armh
%endif

# Automatically added by buildreq on Sat Oct 28 2023
# optimized out: cmake cmake-modules gcc-c++ glibc-kernheaders-generic glibc-kernheaders-x86 libdouble-conversion3 libdtkcore-devel libdtkgui-devel libglvnd-devel libgpg-error libp11-kit libqt5-concurrent libqt5-core libqt5-dbus libqt5-gui libqt5-network libqt5-printsupport libqt5-svg libqt5-widgets libsasl2-3 libssl-devel libstdc++-devel libzen-devel pkg-config python3 python3-base python3-dev python3-module-setuptools qt5-base-devel qt5-tools sh5 tbb-devel zlib-devel
BuildRequires: glib2-devel libdtkwidget-devel libffmpegthumbnailer-devel libfreeimage-devel libmediainfo-devel libtiff-devel qt5-svg-devel qt5-tools-devel libdfm-io-devel

%if_with clang
BuildRequires: clang-devel
%else
BuildRequires: gcc-c++
%endif

%if_with cmake
BuildRequires: cmake rpm-build-ninja
%endif

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
%patch -p1

%build
export PATH=%_qt5_bindir:$PATH
%if_with cmake
%if_with clang
%define optflags_lto -flto=thin
export CC=clang
export CXX=clang++
export LDFLAGS="-fuse-ld=lld $LDFLAGS"
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
%if_with clang
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
%if_with cmake
%cmake_install
%else
%makeinstall INSTALL_ROOT=%buildroot
%endif
%find_lang --with-qt lib%repoiv

%files -n lib%repoiv-data -f lib%repoiv.lang
%doc LICENSE.txt README.md
%dir %_datadir/lib%repoiv/
%dir %_datadir/lib%repoiv/translations/
%_datadir/lib%repoiv/translations/libimageviewer.qm

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
* Tue Jan 09 2024 Leontiy Volodin <lvol@altlinux.org> 1.0.40.0.1.7088-alt1
- New version 1.0.40.0.1.7088.
- Removed broken build flags (thanks archlinux for the patch).

* Fri Dec 22 2023 Leontiy Volodin <lvol@altlinux.org> 1.0.39-alt1
- New version 1.0.39.

* Thu Jun 29 2023 Leontiy Volodin <lvol@altlinux.org> 1.0.33-alt1
- New version.

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

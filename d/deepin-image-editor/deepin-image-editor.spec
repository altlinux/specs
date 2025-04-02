%define repo image-editor
%define repoiv imageviewer6
%define repoivr imagevisualresult6
%define sonameiv 0.1
%define sonameivr 0.1

%def_without clang

Name: deepin-image-editor
Version: 6.5.0
Release: alt1

Summary: Image editor libraries for Deepin

License: GPL-3.0+
Group: System/Libraries
Url: https://github.com/linuxdeepin/image-editor
Vcs: https://github.com/linuxdeepin/image-editor.git

Source: %url/archive/%version/%repo-%version.tar.gz
Patch0: %name-%version-%release.patch
Patch1: deepin-image-editor-6.5.0-alt-fix-broken-pkgconfig.patch
Patch2: deepin-image-editor-6.5.0-alt-fix-dqt6-pkgconfig.patch

%if_with clang
ExcludeArch: armh
%endif

BuildRequires: cmake glib2-devel dtk6-common-devel libdtk6widget-devel libffmpegthumbnailer-devel libfreeimage-devel libmediainfo-devel libtiff-devel dqt6-svg-devel dqt6-tools-devel libdfm6-io-devel libcups-devel

%if_with clang
BuildRequires: clang-devel
%else
BuildRequires: gcc-c++
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

%package -n lib%{repoiv}_%sonameiv
Summary: Image editor library for deepin-image-viewer
Group: System/Libraries
Requires: lib%repoiv-data

%description -n lib%{repoiv}_%sonameiv
Image editor is a public library for deepin-image-viewer
by Deepin Technology.

%package -n lib%repoiv-devel
Summary: Development package for deepin-image-viewer
Group: Development/C++

%description -n lib%repoiv-devel
Development libraries for deepin-image-viewer.

%package -n lib%{repoivr}_%sonameivr
Summary: Image editor library for deepin-album
Group: System/Libraries

%description -n lib%{repoivr}_%sonameivr
Image editor is a public library for deepin-image-viewer
by Deepin Technology.

%package -n lib%repoivr-devel
Summary: Development package for deepin-album
Group: Development/C++

%description -n lib%repoivr-devel
Development libraries for deepin-album.

%prep
%setup -n %repo-%version
%autopatch -p1
sed '/qt5.cmake/d' \
  -i libimageviewer/CMakeLists.txt \
  -i libimagevisualresult/CMakeLists.txt

%build
%if_with clang
%define optflags_lto -flto=thin
export CC=clang
export CXX=clang++
export LDFLAGS="-fuse-ld=lld $LDFLAGS"
%else
%define optflags_lto %nil
%endif
%DQ6build \
  -DCMAKE_INSTALL_LIBDIR=%_lib \
#

%install
%DQ6install
%find_lang --with-qt lib%repoiv

%files -n lib%repoiv-data -f lib%repoiv.lang
%doc LICENSE.txt README.md
%dir %_datadir/lib%repoiv/
%dir %_datadir/lib%repoiv/translations/
%_datadir/lib%repoiv/translations/libimageviewer.qm

%files -n lib%repoivr-data
%dir %_datadir/lib%repoivr/
%_datadir/lib%repoivr/filter*

%files -n lib%{repoiv}_%sonameiv
%_libdir/lib%repoiv.so.%{sonameiv}*

%files -n lib%repoiv-devel
%_libdir/lib%repoiv.so
%_includedir/lib%repoiv/
%_pkgconfigdir/lib%repoiv.pc

%files -n lib%{repoivr}_%sonameivr
%_libdir/lib%repoivr.so.%{sonameivr}*

%files -n lib%repoivr-devel
%_libdir/lib%repoivr.so
%_includedir/lib%repoivr/
%_pkgconfigdir/lib%repoivr.pc

%changelog
* Wed Mar 26 2025 Leontiy Volodin <lvol@altlinux.org> 6.5.0-alt1
- New version 6.5.0.
- Added vcs tag.
- Switched to dqt6.

* Wed May 29 2024 Leontiy Volodin <lvol@altlinux.org> 1.0.41-alt2
- Built via separate qt5 instead system (ALT #48138).

* Tue Jan 30 2024 Leontiy Volodin <lvol@altlinux.org> 1.0.41-alt1
- New version 1.0.41.

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

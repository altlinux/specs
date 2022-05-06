%def_enable clang

%if_enabled clang
%define optflags_lto -flto=thin
%endif

Name: deepin-movie
Version: 5.9.14
Release: alt1
Summary: Deepin movie is Deepin Desktop Environment Movie Player
License: GPL-3.0+ and OpenSSL-exception
Group: Video
Url: https://github.com/linuxdeepin/deepin-movie-reborn
Packager: Leontiy Volodin <lvol@altlinux.org>

Source: %url/archive/%version/%name-reborn-%version.tar.gz
Patch: deepin-movie-5.9.8-alt-fix-build.patch

ExcludeArch: armh

%if_enabled clang
BuildRequires(pre): clang-devel
%else
BuildRequires(pre): gcc-c++
%endif
BuildRequires(pre): rpm-build-ninja
BuildRequires: cmake
BuildRequires: qt5-base-devel
BuildRequires: qt5-x11extras-devel
BuildRequires: qt5-tools-devel
BuildRequires: qt5-svg-devel
BuildRequires: dtk5-widget-devel
BuildRequires: libmpv-devel
BuildRequires: libxcb-devel
BuildRequires: libxcbutil-devel
BuildRequires: libxcbutil-icccm-devel
BuildRequires: xorg-xcbproto-devel
BuildRequires: libavformat-devel
BuildRequires: libavutil-devel
BuildRequires: libavcodec-devel
BuildRequires: libffmpegthumbnailer-devel
BuildRequires: libpulseaudio-devel
BuildRequires: libdvdnav-devel
BuildRequires: gsettings-qt-devel
BuildRequires: libswresample-devel
BuildRequires: mpris-qt5-devel
BuildRequires: dbusextended-qt5-devel
BuildRequires: libva-devel
Requires: libdmr libdvdnav libgsettings-qt libmpv1

%description
%summary.

%package -n libdmr
Summary: Library for %name
Group: System/Libraries

%description -n libdmr
This package provides Library for %name.

%package -n libdmr-devel
Summary: Development files for libdmr
Group: Development/Other

%description -n libdmr-devel
This package provides development files for libdmr.

%prep
%setup -n %name-reborn-%version
%patch -p1

%build
%if_enabled clang
export CC="clang"
export CXX="clang++"
export AR="llvm-ar"
%endif

%cmake \
    -GNinja \
    -DCMAKE_BUILD_TYPE=RelWithDebInfo \
    -DCMAKE_INSTALL_PREFIX=%_prefix \
    -DCMAKE_INSTALL_LIBDIR=%_libdir \
    -DAPP_VERSION=%version \
    -DVERSION=%version
cmake --build "%_cmake__builddir" -j%__nprocs

%install
%cmake_install
%find_lang %name

%files -f %name.lang
%doc CHANGELOG.md HACKING.md LICENSE LICENSE.OpenSSL README.md
%_bindir/%name
%_datadir/%name/
%_desktopdir/%name.desktop
%_datadir/glib-2.0/schemas/com.deepin.deepin-movie.gschema.xml
%_iconsdir/hicolor/scalable/apps/%name.svg
%dir %_datadir/deepin-manual/
%dir %_datadir/deepin-manual/manual-assets/
%dir %_datadir/deepin-manual/manual-assets/application/
%dir %_datadir/deepin-manual/manual-assets/application/%name/
%_datadir/deepin-manual/manual-assets/application/%name/movie/

%files -n libdmr
%_libdir/libdmr.so.*

%files -n libdmr-devel
%_libdir/libdmr.so
%dir %_includedir/libdmr/
%_includedir/libdmr/*.h
%_pkgconfigdir/libdmr.pc

%changelog
* Fri May 06 2022 Leontiy Volodin <lvol@altlinux.org> 5.9.14-alt1
- New version (5.9.14).

* Wed Feb 09 2022 Leontiy Volodin <lvol@altlinux.org> 5.9.8-alt1
- New version (5.9.8).

* Thu Jun 10 2021 Leontiy Volodin <lvol@altlinux.org> 5.7.15-alt1.gitfe98519
- New version (5.7.15).
- Updated to git commit fe98519031e8482cba72bfca4ad67269cd98a1de.

* Mon Apr 26 2021 Leontiy Volodin <lvol@altlinux.org> 5.7.11-alt1
- New version (5.7.11) with rpmgs script.

* Thu Mar 25 2021 Leontiy Volodin <lvol@altlinux.org> 5.7.6.165-alt2
- Fixed version tag.

* Mon Jan 11 2021 Leontiy Volodin <lvol@altlinux.org> 5.7.6.165-alt1
- New version (5.7.6.165) with rpmgs script.

* Thu Dec 10 2020 Leontiy Volodin <lvol@altlinux.org> 5.7.6.164-alt1
- New version (5.7.6.164) with rpmgs script.
- Fixed build with mpv (thanks archlinux for the patches).

* Mon Nov 30 2020 Leontiy Volodin <lvol@altlinux.org> 5.7.6.157-alt1.git1ad288f
- Built from git.

* Fri Nov 13 2020 Leontiy Volodin <lvol@altlinux.org> 5.7.6.88-alt1
- New version (5.7.6.88) with rpmgs script.

* Thu Nov 05 2020 Leontiy Volodin <lvol@altlinux.org> 5.7.6.74-alt1
- New version (5.7.6.74) with rpmgs script.

* Mon Oct 26 2020 Leontiy Volodin <lvol@altlinux.org> 5.7.6.61-alt1
- New version (5.7.6.61) with rpmgs script.

* Mon Oct 19 2020 Leontiy Volodin <lvol@altlinux.org> 5.7.6.51-alt1
- New version (5.7.6.51) with rpmgs script.

* Fri Oct 16 2020 Leontiy Volodin <lvol@altlinux.org> 5.7.6.48-alt1
- New version (5.7.6.48) with rpmgs script.

* Thu Oct 15 2020 Leontiy Volodin <lvol@altlinux.org> 5.7.6.47-alt1
- New version (5.7.6.47) with rpmgs script.

* Sat Oct 03 2020 Leontiy Volodin <lvol@altlinux.org> 5.7.6.37-alt1
- New version (5.7.6.37) with rpmgs script.

* Fri Sep 11 2020 Leontiy Volodin <lvol@altlinux.org> 5.7.6.29-alt1
- Initial build for ALT Sisyphus.

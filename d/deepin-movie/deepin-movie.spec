%def_disable clang

Name: deepin-movie
Version: 5.7.6.165
Release: alt1
Summary: Deepin movie is Deepin Desktop Environment Movie Player
License: GPL-3.0+ and LGPL-2.1+
Group: Video
Url: https://github.com/linuxdeepin/deepin-movie-reborn
Packager: Leontiy Volodin <lvol@altlinux.org>

Source: %url/archive/%version/%name-reborn-%version.tar.gz
# archlinux patches
Patch: deepin-movie_5.7.6.164_archlinux_mpv-qthelper.patch
Patch1: deepin-movie_5.7.6.164_archlinux_libavformat-version-check.patch

ExcludeArch: armh

%if_enabled clang
BuildRequires(pre): clang11.0-devel
%else
BuildRequires(pre): gcc-c++
%endif
BuildRequires(pre): rpm-build-ninja
BuildRequires: cmake
BuildRequires: qt5-base-devel
BuildRequires: qt5-x11extras-devel
BuildRequires: qt5-tools-devel
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
%patch1 -p1

sed -i '/#include <DPalette>/a #include <QPainterPath>' src/widgets/{tip,toolbutton}.h

%build
%if_enabled clang
export CC="clang"
export CXX="clang++"
export AR="llvm-ar"
%endif

%cmake_insource \
    -GNinja \
    -DCMAKE_BUILD_TYPE=Release
%ninja_build

%install
%ninja_install
%find_lang %name

%files -f %name.lang
%doc CHANGELOG.md HACKING.md LICENSE LICENSE.OpenSSL README.md
%_bindir/%name
%_datadir/%name/
%_desktopdir/%name.desktop
%_datadir/glib-2.0/schemas/com.deepin.deepin-movie.gschema.xml
%_iconsdir/hicolor/scalable/apps/%name.svg

%files -n libdmr
%_libdir/libdmr.so.*

%files -n libdmr-devel
%_libdir/libdmr.so
%dir %_includedir/libdmr/
%_includedir/libdmr/*.h
%_pkgconfigdir/libdmr.pc

%changelog
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

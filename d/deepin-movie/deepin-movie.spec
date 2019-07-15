%add_findprov_lib_path %_libdir/libdvdnav.so.4 %_libdir/libgsettings-qt.so.1

Name: deepin-movie
Version: 5.7.6.29
Release: alt1
Summary: Deepin movie is Deepin Desktop Environment Movie Player
License: GPL-3.0+ and LGPL-2.1+
Group: Video
Url: https://github.com/linuxdeepin/deepin-movie-reborn
Packager: Leontiy Volodin <lvol@altlinux.org>

Source: %url/archive/%version/%name-reborn-%version.tar.gz
Patch: deepin-movie_5.7.6.29_alt_qt5.15.patch

ExcludeArch: armh

BuildRequires(pre): rpm-build-ninja
BuildRequires: gcc-c++ cmake qt5-base-devel qt5-x11extras-devel qt5-tools-devel dtk5-widget-devel libmpv-devel libxcb-devel libxcbutil-devel libxcbutil-icccm-devel xorg-xcbproto-devel libavformat-devel libavutil-devel libavcodec-devel libffmpegthumbnailer-devel libpulseaudio-devel libdvdnav-devel gsettings-qt-devel libswresample-devel

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
%patch -p2

%build
%cmake \
    -GNinja \
    -DCMAKE_BUILD_TYPE=Debug
%ninja_build -C BUILD

%install
%ninja_install -C BUILD

%files
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
* Fri Sep 11 2020 Leontiy Volodin <lvol@altlinux.org> 5.7.6.29-alt1
- Initial build for ALT Sisyphus.

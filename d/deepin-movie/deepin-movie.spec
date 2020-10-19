Name: deepin-movie
Version: 5.7.6.51
Release: alt1
Summary: Deepin movie is Deepin Desktop Environment Movie Player
License: GPL-3.0+ and LGPL-2.1+
Group: Video
Url: https://github.com/linuxdeepin/deepin-movie-reborn
Packager: Leontiy Volodin <lvol@altlinux.org>

Source: %url/archive/%version/%name-reborn-%version.tar.gz

ExcludeArch: armh

BuildRequires(pre): rpm-build-ninja
BuildRequires: gcc-c++ cmake qt5-base-devel qt5-x11extras-devel qt5-tools-devel dtk5-widget-devel libmpv-devel libxcb-devel libxcbutil-devel libxcbutil-icccm-devel xorg-xcbproto-devel libavformat-devel libavutil-devel libavcodec-devel libffmpegthumbnailer-devel libpulseaudio-devel libdvdnav-devel gsettings-qt-devel libswresample-devel
Requires: libdmr libdvdnav libgsettings-qt

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
sed -i '/#include <DPalette>/a #include <QPainterPath>' src/widgets/{tip,toolbutton}.h

%build
%cmake \
    -GNinja \
    -DCMAKE_BUILD_TYPE=Release
%ninja_build -C BUILD

%install
%ninja_install -C BUILD
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

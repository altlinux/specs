%global repo dde-control-center

Name: deepin-control-center
Version: 5.3.0.68
Release: alt1
Summary: New control center for Linux Deepin
License: GPL-3.0+
Group: Graphical desktop/Other
Url: https://github.com/linuxdeepin/dde-control-center
Packager: Leontiy Volodin <lvol@altlinux.org>

Source: %url/archive/%version/%repo-%version.tar.gz

BuildRequires(pre): rpm-build-ninja desktop-file-utils rpm-build-kf5
BuildRequires: gcc-c++ cmake deepin-dock-devel pkgconfig(dde-network-utils) pkgconfig(dtkwidget) pkgconfig(dframeworkdbus) pkgconfig(gsettings-qt) pkgconfig(geoip) pkgconfig(libnm) pkgconfig(Qt5Core) pkgconfig(Qt5Concurrent) pkgconfig(Qt5DBus) pkgconfig(Qt5Multimedia) pkgconfig(Qt5Svg) pkgconfig(Qt5Sql) pkgconfig(Qt5Xml) pkgconfig(Qt5X11Extras) pkgconfig(xcb-ewmh) pkgconfig(xext) qt5-linguist pkgconfig(udisks2-qt5)
BuildRequires: kf5-networkmanager-qt-devel libpwquality-devel
BuildRequires: pkgconfig(libpcre) pkgconfig(libffi) pkgconfig(zlib) pkgconfig(mount) pkgconfig(blkid) pkgconfig(libselinux) pkgconfig(gio-2.0)
# Requires: deepin-account-faces deepin-api deepin-daemon deepin-qt5integration deepin-network-utils GeoIP-GeoLite-data GeoIP-GeoLite-data-extra gtk-murrine-engine proxychains-ng redshift startdde

%description
New control center for Linux Deepin.

%package devel
Summary: %summary
Group: Development/Other

%description devel
%summary.

%prep
%setup -n %repo-%version

sed -i 's|lrelease|lrelease-qt5|' translate_generation.sh
sed -i -E '/add_compile_definitions/d' CMakeLists.txt
# sed -i '/%repo/s|\.\./lib|%_libdir|' src/frame/pluginscontroller.cpp
# Qt next version fixes
sed -i '/#include <QPainter>/a #include <QPainterPath>' \
    src/frame/modules/display/recognizedialog.cpp
sed -i '/#include <QRect>/a #include <QPainterPath>' \
    src/frame/window/modules/personalization/personalizationgeneral.cpp

sed -i 's|/bin/deepin-recovery-tool|/usr/bin/deepin-recovery-tool|' \
    src/frame/window/modules/systeminfo/backupandrestoreworker.cpp

# remove after they obey -DDISABLE_SYS_UPDATE properly
sed -i '/new UpdateModule/d' src/frame/window/mainwindow.cpp

sed -i 's|/lib/|/%_lib/|' \
    com.deepin.controlcenter.develop.policy \
    src/frame/window/mainwindow.cpp \
    src/frame/window/insertplugin.cpp \
    src/frame/plugins/weather/weather.pro \
    src/frame/plugins/example/example.pro \
    src/frame/plugins/calculator/calculator.pro

%build
%K5cmake \
    -GNinja \
    -DDCC_DISABLE_GRUB=YES \
    -DDISABLE_SYS_UPDATE=YES
%ninja_build -C BUILD

%install
%ninja_install -C BUILD
# place holder plugins dir
mkdir -p %buildroot%_libdir/%repo/plugins

mkdir -p %buildroot%_libdir/cmake/DdeControlCenter
mv %buildroot/cmake/DdeControlCenter/DdeControlCenterConfig.cmake %buildroot%_libdir/cmake/DdeControlCenter

%ifarch aarch64 ppc64le x86_64
mv %buildroot/usr/lib/libdccwidgets.so %buildroot%_libdir/
%endif

# mkdir -p %%buildroot%%_libdir/%%repo/
# mv %%buildroot/usr/lib/%%repo/* %%buildroot%%_libdir/%%repo/

install -Dm644 com.deepin.controlcenter.addomain.policy %buildroot%_datadir/polkit-1/actions/

%check
desktop-file-validate %buildroot%_desktopdir/%repo.desktop ||:

%files
%doc README.md
%doc LICENSE
%_bindir/%repo
%_bindir/abrecovery
%_desktopdir/%repo.desktop
%_datadir/dbus-1/services/*.service
%_datadir/polkit-1/actions/*.policy
%_datadir/%repo/
%_datadir/dict/MainEnglishDictionary_ProbWL.txt
%_sysconfdir/xdg/autostart/deepin-ab-recovery.desktop
# %%_libdir/%%repo/
%_libdir/libdccwidgets.so

%files devel
%_libdir/cmake/DdeControlCenter/
%_includedir/%repo/

%changelog
* Mon Nov 30 2020 Leontiy Volodin <lvol@altlinux.org> 5.3.0.68-alt1
- New version (5.3.0.68) with rpmgs script.

* Fri Oct 09 2020 Leontiy Volodin <lvol@altlinux.org> 5.3.0.44-alt1
- New version (5.3.0.44) with rpmgs script.

* Mon Aug 31 2020 Leontiy Volodin <lvol@altlinux.org> 5.3.0.18-alt1
- Initial build for ALT Sisyphus (thanks fedora and archlinux for this spec).

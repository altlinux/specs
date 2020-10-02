%set_verify_elf_method unresolved=no
%global repo dde-control-center

Name: deepin-control-center
Version: 5.3.0.18
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

%__subst 's|lrelease|lrelease-qt5|' translate_generation.sh
%__subst '/%repo/s|\.\./lib|%_libdir|' src/frame/pluginscontroller.cpp
# Qt next version fixes
%__subst '/#include <QPainter>/a #include <QPainterPath>' src/frame/widgets/basiclistdelegate.cpp src/frame/window/modules/update/updatehistorybutton.cpp \
                                                          src/frame/window/modules/commoninfo/commonbackgrounditem.cpp src/frame/modules/accounts/useroptionitem.cpp \
                                                          src/frame/window/modules/sync/pages/avatarwidget.cpp src/frame/window/modules/accounts/avataritemdelegate.cpp \
                                                          src/frame/modules/accounts/avatarwidget.cpp src/frame/window/modules/accounts/accountswidget.cpp \
                                                          src/frame/modules/datetime/timezone_dialog/popup_menu.cpp src/frame/modules/display/recognizedialog.cpp \
                                                          src/frame/window/modules/personalization/roundcolorwidget.cpp src/frame/window/modules/unionid/pages/avatarwidget.cpp
%__subst '/#include <QRect>/a #include <QPainterPath>' src/frame/window/modules/personalization/personalizationgeneral.cpp

%__subst 's|/bin/deepin-recovery-tool|/usr/bin/deepin-recovery-tool|' src/frame/window/modules/systeminfo/backupandrestoreworker.cpp

# remove after they obey -DDISABLE_SYS_UPDATE properly
%__subst '/new UpdateModule/d' src/frame/window/mainwindow.cpp

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
# %%_libdir/%%repo/
%_datadir/dict/MainEnglishDictionary_ProbWL.txt
%_sysconfdir/xdg/autostart/deepin-ab-recovery.desktop

%files devel
%_libdir/cmake/DdeControlCenter/
%_includedir/%repo/
%_libdir/libdccwidgets.so

%changelog
* Mon Aug 31 2020 Leontiy Volodin <lvol@altlinux.org> 5.3.0.18-alt1
- Initial build for ALT Sisyphus (thanks fedora and archlinux for this spec).

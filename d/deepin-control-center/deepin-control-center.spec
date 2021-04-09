%global repo dde-control-center

Name: deepin-control-center
Version: 5.4.17
Release: alt2
Summary: New control center for Linux Deepin
License: GPL-3.0+
Group: Graphical desktop/Other
Url: https://github.com/linuxdeepin/dde-control-center
Packager: Leontiy Volodin <lvol@altlinux.org>

Source: %url/archive/%version/%repo-%version.tar.gz
# archlinux patches
Patch: deepin-control-center-no-user-experience.patch

BuildRequires(pre): rpm-build-ninja desktop-file-utils rpm-build-kf5
BuildRequires: gcc-c++
BuildRequires: cmake
BuildRequires: deepin-dock-devel
BuildRequires: deepin-network-utils-devel
BuildRequires: dtk5-widget-devel
BuildRequires: deepin-qt-dbus-factory-devel
BuildRequires: gsettings-qt-devel
BuildRequires: libGeoIP-devel
BuildRequires: libnm-devel
BuildRequires: qt5-base-devel
BuildRequires: qt5-multimedia-devel
BuildRequires: qt5-svg-devel
BuildRequires: qt5-x11extras-devel
BuildRequires: libxcbutil-icccm-devel
BuildRequires: libXext-devel
BuildRequires: qt5-linguist
BuildRequires: udisks2-qt5-devel
BuildRequires: kf5-networkmanager-qt-devel
BuildRequires: libpwquality-devel
BuildRequires: libgtest-devel
BuildRequires: libpolkitqt5-qt5-devel
BuildRequires: deepin-pw-check-devel
BuildRequires: deepin-desktop-base
BuildRequires: dtk5-common
# ---
BuildRequires: libpcre-devel
BuildRequires: libffi-devel
BuildRequires: zlib-devel
BuildRequires: libmount-devel
BuildRequires: libblkid-devel
BuildRequires: libselinux-devel
BuildRequires: libgio-devel
# ---
# Requires: deepin-account-faces deepin-api deepin-daemon deepin-qt5integration deepin-network-utils GeoIP-GeoLite-data GeoIP-GeoLite-data-extra gtk-murrine-engine proxychains-ng redshift startdde
# Requires: libdeepin-pw-check

%description
New control center for Linux Deepin.

%package devel
Summary: %summary
Group: Development/Other

%description devel
%summary.

%prep
%setup -n %repo-%version
%patch -p2

sed -i 's|lrelease|lrelease-qt5|' translate_generation.sh
sed -i -E '/add_compile_definitions/d' CMakeLists.txt
# sed -i '/%repo/s|\.\./lib|%_libdir|' src/frame/pluginscontroller.cpp

# remove after they obey -DDISABLE_SYS_UPDATE properly
sed -i '/new UpdateModule/d' src/frame/window/mainwindow.cpp

sed -i 's|/lib/|/%_lib/|' \
    com.deepin.controlcenter.develop.policy \
    src/frame/window/mainwindow.cpp \
    src/frame/window/insertplugin.cpp \
    src/frame/modules/update/updatework.cpp \
    src/frame/plugins/battery-health/battery-health.pro \
    src/frame/plugins/weather/weather.pro \
    src/frame/plugins/example/example.pro \
    src/frame/plugins/calculator/calculator.pro \
    src/frame/plugins/privacy/privacy.pro

sed -i 's|/etc/deepin/dde-session-ui.conf|/usr/share/dde-session-ui/dde-session-ui.conf|' \
	src/frame/modules/accounts/accountsworker.cpp

%build
export SYSTYPE=Desktop
# export SYSTYPE=$(cat /etc/deepin-version | grep Type= | awk -F'=' '{print $$2}')
%K5cmake \
    -GNinja \
    -DDCC_DISABLE_GRUB=YES \
    -DDISABLE_SYS_UPDATE=YES \
    -DCMAKE_INSTALL_LIBDIR=%_libdir \
    -DDISABLE_RECOVERY=YES \
    -DCVERSION=%version \
    -DAPP_VERSION=%version \
    -DVERSION=%version
%ninja_build -C BUILD

%install
%ninja_install -C BUILD
# place holder plugins dir
mkdir -p %buildroot%_libdir/%repo/plugins

# mkdir -p %buildroot%_libdir/cmake/DdeControlCenter
# mv %buildroot/cmake/DdeControlCenter/DdeControlCenterConfig.cmake %buildroot%_libdir/cmake/DdeControlCenter

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
%_bindir/%repo-wapper
# %%_bindir/abrecovery
%_desktopdir/%repo.desktop
%_datadir/dbus-1/services/*.service
%_datadir/polkit-1/actions/*.policy
%_datadir/%repo/
%_datadir/dict/MainEnglishDictionary_ProbWL.txt
# %%_sysconfdir/xdg/autostart/deepin-ab-recovery.desktop
%_datadir/glib-2.0/schemas/com.deepin.dde.control-center.gschema.xml
# %%_libdir/%%repo/
%_libdir/libdccwidgets.so

%files devel
%_libdir/cmake/DdeControlCenter/
%_includedir/%repo/

%changelog
* Fri Apr 09 2021 Leontiy Volodin <lvol@altlinux.org> 5.4.17-alt2
- Fixed build with dtk 5.4.13.

* Tue Apr 06 2021 Leontiy Volodin <lvol@altlinux.org> 5.4.17-alt1
- New version (5.4.17) with rpmgs script (thanks archlinux for the patch).

* Wed Mar 24 2021 Leontiy Volodin <lvol@altlinux.org> 5.4.9-alt1
- New version (5.4.9) with rpmgs script.

* Tue Jan 12 2021 Leontiy Volodin <lvol@altlinux.org> 5.3.0.82-alt1
- New version (5.3.0.82) with rpmgs script.

* Mon Nov 30 2020 Leontiy Volodin <lvol@altlinux.org> 5.3.0.68-alt1
- New version (5.3.0.68) with rpmgs script.

* Fri Oct 09 2020 Leontiy Volodin <lvol@altlinux.org> 5.3.0.44-alt1
- New version (5.3.0.44) with rpmgs script.

* Mon Aug 31 2020 Leontiy Volodin <lvol@altlinux.org> 5.3.0.18-alt1
- Initial build for ALT Sisyphus (thanks fedora and archlinux for this spec).

%def_disable clang

%define _cmake__builddir BUILD
%define repo dde-control-center

Name: deepin-control-center
Version: 5.5.16.2
Release: alt1
Summary: New control center for Linux Deepin
License: GPL-3.0+
Group: Graphical desktop/Other
Url: https://github.com/linuxdeepin/dde-control-center
Packager: Leontiy Volodin <lvol@altlinux.org>

Source: %url/archive/%version/%repo-%version.tar.gz
# archlinux patches
Patch: deepin-control-center-no-user-experience.patch
# alt patches
Patch1: deepin-control-center-fix-build-deepinid-syncdaemon.patch
Patch2: deepin-control-center-fix-build-gcc10.patch
Patch4: deepin-control-center-lightdm-lockscreen.patch
Patch5: deepin-control-center-hide-lockscreen-slide-widget.patch
Patch6: deepin-control-center-remove-pw-check-support.patch
# upstream patches
Patch10: deepin-control-center-pull407-disable-biometric-auth.patch

BuildRequires(pre): rpm-build-ninja desktop-file-utils rpm-build-kf5
%if_enabled clang
BuildRequires(pre): clang-devel
%else
BuildRequires(pre): gcc-c++
%endif
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
BuildRequires: libgmock-devel
BuildRequires: libpolkitqt5-qt5-devel
BuildRequires: libdeepin-pw-check-devel
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
#patch -p2
#patch1 -p1
#patch2 -p1
%patch4 -p1
%patch5 -p1
#patch6 -p1
%patch10 -p1

# remove after they obey -DDISABLE_SYS_UPDATE properly
sed -i '/new UpdateModule/d' src/frame/window/mainwindow.cpp
# remove General Settings
sed -i '/new CommonInfoModule/d' src/frame/window/mainwindow.cpp
# remove Accounts module
sed -i '/new AccountsModule/d' src/frame/window/mainwindow.cpp
# remove Deepin ID Sync module
sed -i '/new SyncModule/d' src/frame/window/mainwindow.cpp
# disable non-working modules that switch to the lock screen
# sed -i '/Wakeup Settings/d' \
#     src/frame/window/modules/power/generalwidget.cpp \
#     src/frame/window/search/searchwidget.cpp

sed -i '/m_wakeComputerNeedPassword/d' src/frame/window/modules/power/generalwidget.{cpp,h}
sed -i '/(GSettingWatcher::instance()->getStatus("systemSuspend") != "Hidden"));/d' src/frame/window/modules/power/generalwidget.cpp
sed -i '/m_wakeDisplayNeedPassword/d' src/frame/window/modules/power/generalwidget.{cpp,h}
sed -i '/m_monitorSleepOnPower/d' src/frame/window/modules/power/generalwidget.h
# sed -i '/void CommonInfoWork::setUeProgram/s|enabled|disabled|' src/frame/window/modules/commoninfo/commoninfowork.cpp

sed -i 's|/lib/|/%_lib/|' \
    com.deepin.controlcenter.develop.policy \
    src/frame/window/mainwindow.cpp \
    src/frame/window/insertplugin.cpp

sed -i 's|/etc/deepin/dde-session-ui.conf|/usr/share/dde-session-ui/dde-session-ui.conf|' \
	src/frame/modules/accounts/accountsworker.cpp

sed -i '/dde-grand-search-daemon/s|lib/|%_lib/|' CMakeLists.txt

%build
export PATH=%_qt5_bindir:$PATH
export SYSTYPE=Desktop
# export SYSTYPE=$(cat /etc/deepin-version | grep Type= | awk -F'=' '{print $$2}')
%if_enabled clang
export CC="clang"
export CXX="clang++"
export AR="llvm-ar"
export NM="llvm-nm"
export READELF="llvm-readelf"
%endif
# src/frame/CMakeLists.txt
%K5cmake \
    -GNinja \
    -DCMAKE_BUILD_TYPE=RelWithDebInfo \
    -DDCC_DISABLE_GRUB=YES \
    -DDISABLE_SYS_UPDATE=YES \
    -DCMAKE_INSTALL_LIBDIR=%_libdir \
    -DDISABLE_RECOVERY=YES \
    -DCVERSION=%version \
    -DAPP_VERSION=%version \
    -DVERSION=%version \
    -DDISABLE_CLOUD_SYNC=YES \
    -DDISABLE_AUTHENTICATION=YES \
    -DDISABLE_ACCOUNT=YES \
    -DDISABLE_SYS_UPDATE_SOURCE_CHECK=YES \
    -DDISABLE_SYS_UPDATE_MIRRORS=YES \
    -DDCC_DISABLE_FEEDBACK=YES \
%nil
cmake --build "%_cmake__builddir" -j%__nprocs

%install
%cmake_install
# place holder plugins dir
mkdir -p %buildroot%_libdir/%repo/plugins

%ifarch aarch64 ppc64le x86_64
mv %buildroot/usr/lib/libdccwidgets.so %buildroot%_libdir/
%endif

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
%dir %_libdir/dde-grand-search-daemon/
%dir %_libdir/dde-grand-search-daemon/plugins/
%dir %_libdir/dde-grand-search-daemon/plugins/searcher/
%_libdir/dde-grand-search-daemon/plugins/searcher/com.deepin.dde-grand-search.dde-control-center-setting.conf
%_libdir/libdccwidgets.so
%dir %_datadir/dsg/apps/dde-control-center/
%dir %_datadir/dsg/apps/dde-control-center/configs/
%_datadir/dsg/apps/dde-control-center/configs/dde.control-center.*.json

%files devel
%_libdir/cmake/DdeControlCenter/
%_includedir/%repo/

%changelog
* Fri Apr 22 2022 Leontiy Volodin <lvol@altlinux.org> 5.5.16.2-alt1
- New version (5.5.16.2).
- Built with deepin-pw-check again (without cracklib).

* Wed Aug 25 2021 Leontiy Volodin <lvol@altlinux.org> 5.4.70-alt1
- New version (5.4.70).
- Remove deepin-pw-check from BuildRequires.

* Thu Jul 08 2021 Leontiy Volodin <lvol@altlinux.org> 5.4.47-alt2.git1362dfe
- Fixed build with libgmock.so.1.11.0.

* Wed Jun 30 2021 Leontiy Volodin <lvol@altlinux.org> 5.4.47-alt1.git1362dfe
- Fixed version tag.

* Fri Jun 25 2021 Leontiy Volodin <lvol@altlinux.org> 5.4.23-alt3.git1362dfe
- Temporarily hidden the widget to set the lockscreen timeout.

* Thu Jun 24 2021 Leontiy Volodin <lvol@altlinux.org> 5.4.23-alt2.git1362dfe
- Build git snapshot.
- Disabled General Settings.

* Tue May 18 2021 Leontiy Volodin <lvol@altlinux.org> 5.4.23-alt1
- New version (5.4.23) with rpmgs script.

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

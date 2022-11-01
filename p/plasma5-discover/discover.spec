%define rname discover

%ifarch armh
%def_disable fwupd
%else
%def_enable fwupd
%endif
#
%def_enable snap
#
%ifarch %qt5_qtwebengine_arches
%def_enable qtwebengine
%else
%def_disable qtwebengine
%endif

%define sover 0
%define libdiscovercommon libdiscovercommon%sover
%define libdiscovernotifiers libdiscovernotifiers%sover

Name: plasma5-%rname
Version: 5.26.2
Release: alt1
%K5init no_altplace appdata

Group: System/Configuration/Packaging
Summary: KDE Software Center
Url: http://www.kde.org
License: GPL-2.0-or-later

Requires: %name-core
Requires: %name-kns

Source: %rname-%version.tar
Source1: env-flatpak.sh
Source2: env-snap.sh
Patch1: alt-offline-updates.patch
Patch2: alt-skip-obsoleted-and-removed-from-upgrade.patch
Patch3: alt-discover-update-all-packages-from-appstream.patch
#
Patch5: alt-soversion.patch
Patch6: alt-fix-status-after-transaction.patch
Patch7: alt-pk-disable-launch.patch
Patch8: alt-dont-crash-if-flatpak-not-initialized.patch
Patch9: alt-show-reboot-avail.patch
Patch10: alt-keep-focus.patch
Patch11: alt-hide-autoreboot.patch
Patch12: alt-send-interactive.patch
Patch13: alt-fix-notifications.patch

# Automatically added by buildreq on Tue Aug 07 2018 (-bi)
# optimized out: appstream appstream-qt cmake cmake-modules elfutils fontconfig gcc-c++ glib2-devel glibc-kernheaders-generic glibc-kernheaders-x86 gtk-update-icon-cache kf5-attica-devel kf5-kauth-devel kf5-kbookmarks-devel kf5-kcodecs-devel kf5-kcompletion-devel kf5-kconfig-devel kf5-kconfigwidgets-devel kf5-kcoreaddons-common kf5-kcoreaddons-devel kf5-kitemviews-devel kf5-kjobwidgets-common kf5-kjobwidgets-devel kf5-kservice-devel kf5-kwidgetsaddons-common kf5-kwidgetsaddons-devel kf5-kwindowsystem-devel kf5-kxmlgui-devel kf5-solid-devel libEGL-devel libGL-devel libdbusmenu-qt52 libgio-devel libgpg-error libjson-glib libqt5-concurrent libqt5-core libqt5-dbus libqt5-gui libqt5-network libqt5-printsupport libqt5-qml libqt5-quick libqt5-svg libqt5-test libqt5-widgets libqt5-x11extras libqt5-xml libstdc++-devel libxcbutil-keysyms perl pkg-config python-base python-modules python3 python3-base qt5-base-common qt5-base-devel rpm-build-python3 rpm-build-qml ruby ruby-stdlibs sh3
#BuildRequires: appstream-qt-devel extra-cmake-modules kf5-karchive-devel kf5-kcrash-devel kf5-kdbusaddons-devel kf5-ki18n-devel kf5-kio-devel kf5-kirigami-devel kf5-kitemmodels-devel kf5-knewstuff-devel kf5-knotifications-devel kf5-kpackage-devel kf5-plasma-framework-devel libflatpak-devel libssl-devel packagekit-qt-devel python3-dev qt5-declarative-devel qt5-translations rpm-build-ruby
BuildRequires(pre): rpm-build-kf5 rpm-macros-qt5-webengine
BuildRequires: libssl-devel qt5-declarative-devel qt5-x11extras-devel
BuildRequires: desktop-file-utils
BuildRequires: pkgconfig(libmarkdown)
%if_enabled qtwebengine
#BuildRequires: qt5-webengine-devel
BuildRequires: qt5-webview-devel
%endif
%if_enabled fwupd
BuildRequires: pkgconfig(fwupd)
%endif
%if_enabled snap
BuildRequires: snapd-qt-devel
%endif
BuildRequires: packagekit-qt-devel
BuildRequires: appstream-qt-devel
BuildRequires: libflatpak-devel
BuildRequires: extra-cmake-modules kf5-karchive-devel kf5-kcrash-devel kf5-kdbusaddons-devel kf5-ki18n-devel kf5-kio-devel
BuildRequires: kf5-kirigami-devel kf5-kitemmodels-devel kf5-knewstuff-devel kf5-knotifications-devel kf5-kpackage-devel
BuildRequires: kf5-kdeclarative-devel kf5-kcmutils-devel kf5-kidletime-devel
BuildRequires: kf5-plasma-framework-devel kf5-purpose-devel

%description
KDE and Plasma resources management GUI.

%package maxi
Summary: Plasma Discover maximum package
Group: System/Configuration/Packaging
Requires: %name-kns
Requires: %name-packagekit
Requires: %name-flatpak
%if_enabled fwupd
Requires: %name-fwupd
%endif
%if_enabled snap
Requires: %name-snap
%endif
%description maxi
Plasma Discover maximum package.

%package core
Summary: Plasma Discover core files
Group: System/Configuration/Packaging
Requires: %name-common
Requires: kf5-kirigami appstream-data
%description core
Plasma Discover core files.

%package common
Summary: %name common package
Group: System/Configuration/Other
#BuildArch: noarch
Requires: kf5-filesystem
%description common
%name common package

%package devel
Group: Development/KDE and QT
Summary: Development files for %name
Requires: %name-common
%description devel
The %name-devel package contains libraries and header files for
developing applications that use %name.
%package kns
Summary: Plasma Discover KDE New Stuff support
Group: System/Configuration/Packaging
Requires: %name-core
#Requires: plasma5-workspace
%description kns
Integrates  KDE New Stuff into Discover.

%package flatpak
Summary: Plasma Discover flatpak support
Group: System/Configuration/Packaging
Requires: %name-core
Requires: flatpak
%description flatpak
Integrates Flatpak applications into Discover.

%if_enabled snap
%package snap
Summary: Plasma Discover flatpak support
Group: System/Configuration/Packaging
Requires: %name-core
Requires: snapd
%description snap
Integrates Snap applications into Discover.
%endif

%package fwupd
Summary: Plasma Discover fwupd support
Group: System/Configuration/Packaging
Requires: %name-core
Requires: fwupd
%description fwupd
Integrates Fwupd firmware updater into Discover.

%package packagekit
Summary: Plasma Discover PackageKit support
Group: System/Configuration/Packaging
Requires: %name-core
Requires: packagekit
%description packagekit
Integrates PackageKit package manager into Discover.

%package -n %libdiscovercommon
Group: System/Libraries
Summary: KF5 library
Requires: %name-common
%description -n %libdiscovercommon
KF5 library

%package -n %libdiscovernotifiers
Group: System/Libraries
Summary: KF5 library
Requires: %name-common
%description -n %libdiscovernotifiers
KF5 library


%prep
%setup -n %rname-%version
%patch1 -p1
%patch2 -p2
#%patch3 -p2 -b .upd-appstream
#
%patch5 -p1
%patch6 -p1
%patch7 -p1
%patch8 -p2
%patch9 -p1
%patch10 -p2
%patch11 -p1
%patch12 -p1
%patch13 -p1

%build
%if "%(%__kf5_if_have_opt altplace yes no)" == "no"
    %undefine _K5start
    %define _K5start %_sysconfdir/xdg/autostart
%endif
%K5build

%install
%K5install
mv %buildroot/%_libdir/plasma-discover/lib*.so* %buildroot/%_libdir/

%K5install_move data libdiscover kpackage

mkdir -p %buildroot/%_K5xdgconf/plasma-workspace/env/
install -m 0755 %SOURCE1 %buildroot/%_K5xdgconf/plasma-workspace/env/%{name}-flatpak.sh
install -m 0755 %SOURCE2 %buildroot/%_K5xdgconf/plasma-workspace/env/%{name}-snap.sh

for f in %buildroot/%_K5xdgapp/org.kde.discover*.desktop ; do
    desktop-file-install --mode=0755 --dir %buildroot/%_K5xdgapp \
	--remove-key="X-DocPath" \
	$f
done
desktop-file-install --mode=0644 --dir %buildroot/%_K5start \
	--add-only-show-in="KDE;XFCE;" \
	--remove-key="X-KDE-autostart-phase" \
	%buildroot/%_K5start/org.kde.discover.notifier.desktop

%find_lang %name --with-kde --all-name

%files
%files maxi

%files common -f %name.lang
%doc LICENSES/*
%dir %_K5data/libdiscover/
%dir %_K5data/libdiscover/categories/
%dir %_K5plug/discover-notifier/
%dir %_K5plug/discover/
%_datadir/qlogging-categories5/*.*categories
%_K5icon/*/*/apps/plasmadiscover.*

%files core
%_K5bin/*
%_K5libexecdir/DiscoverNotifier
%_K5exec/discover/runservice
%_K5xdgapp/org.kde.discover.desktop
%_K5xdgapp/org.kde.discover.urlhandler.desktop
%_K5xdgapp/org.kde.discover.notifier.desktop
%_K5xdgapp/kcm_updates.desktop
%_K5start/org.kde.discover.notifier.desktop
%_K5xmlgui/*
%_K5notif/*.notifyrc
%_datadir/metainfo/org.kde.discover.appdata.xml
#
%_K5plug/plasma/kcms/systemsettings/kcm_updates.so
%_K5data/kpackage/kcms/kcm_updates/

%files kns
%_K5plug/discover/kns-backend.so

%files packagekit
%_K5plug/discover/packagekit-backend.so
%_K5plug/discover-notifier/DiscoverPackageKitNotifier.so
%_K5data/libdiscover/categories/packagekit-backend-categories.xml
%_datadir/metainfo/org.kde.discover.packagekit.appdata.xml

%files flatpak
%config(noreplace) %_K5xdgconf/plasma-workspace/env/*flatpak*.sh
%_K5plug/discover/flatpak-backend.so
%_datadir/metainfo/org.kde.discover.flatpak.appdata.xml
%_K5plug/discover-notifier/FlatpakNotifier.so
%_K5data/libdiscover/categories/flatpak-backend-categories.xml
%_K5xdgapp/org.kde.discover-flatpak.desktop
%_K5icon/*/*/apps/*flatpak*.*

%if_enabled snap
%files snap
%config(noreplace) %_K5xdgconf/plasma-workspace/env/*snap*.sh
%_K5plug/discover/snap-backend.so
%_K5libexecdir/discover/SnapMacaroonDialog
%_K5libexecdir/kauth/libsnap_helper
%_K5dbus_sys_srv/org.kde.discover.libsnapclient.service
%_K5xdgapp/org.kde.discover.snap.desktop
%_K5dbus/system.d/org.kde.discover.libsnapclient.conf
%_datadir/metainfo/org.kde.discover.snap.appdata.xml
#%_K5data/libdiscover/categories/snap-backend-categories.xml
%_datadir/polkit-1/actions/org.kde.discover.libsnapclient.policy
%endif

%if_enabled fwupd
%files fwupd
%_K5plug/discover/fwupd-backend.so
%endif

%files -n %libdiscovercommon
%_K5lib/libDiscoverCommon.so.%sover
%_K5lib/libDiscoverCommon.so.*
%files -n %libdiscovernotifiers
%_K5lib/libDiscoverNotifiers.so.%sover
%_K5lib/libDiscoverNotifiers.so.*


%changelog
* Thu Oct 27 2022 Sergey V Turchin <zerg@altlinux.org> 5.26.2-alt1
- new version

* Thu Oct 06 2022 Oleg Solovyov <mcpain@altlinux.org> 5.25.5-alt5
- fix repair failed offline update notifications

* Thu Oct 06 2022 Sergey V Turchin <zerg@altlinux.org> 5.25.5-alt4
- update russian translation

* Fri Sep 23 2022 Sergey V Turchin <zerg@altlinux.org> 5.25.5-alt3
- fix autostart DiscoverNotifier (closes: 43782)

* Thu Sep 22 2022 Sergey V Turchin <zerg@altlinux.org> 5.25.5-alt2
- allow to autostart DiscoverNotifier in XFCE

* Wed Sep 07 2022 Sergey V Turchin <zerg@altlinux.org> 5.25.5-alt1
- new version

* Wed Aug 17 2022 Sergey V Turchin <zerg@altlinux.org> 5.25.4-alt1
- new version

* Wed Aug 17 2022 Oleg Solovyov <mcpain@altlinux.org> 5.24.6-alt2
- packagekit backend: fix "Repair System" button

* Mon Jul 11 2022 Sergey V Turchin <zerg@altlinux.org> 5.24.6-alt1
- new version

* Wed May 04 2022 Sergey V Turchin <zerg@altlinux.org> 5.24.5-alt1
- new version

* Mon Apr 11 2022 Sergey V Turchin <zerg@altlinux.org> 5.24.4-alt2
- don't apply alt-discover-update-all-packages-from-appstream.patch

* Fri Apr 01 2022 Sergey V Turchin <zerg@altlinux.org> 5.24.4-alt1
- bump release

* Wed Mar 30 2022 Sergey V Turchin <zerg@altlinux.org> 5.24.4-alt0.1
- new version

* Tue Mar 29 2022 Oleg Solovyov <mcpain@altlinux.org> 5.24.3-alt0.2
- re-apply appstream patch from darktemplar

* Wed Mar 23 2022 Sergey V Turchin <zerg@altlinux.org> 5.24.3-alt0.1
- new version

* Fri Mar 04 2022 Slava Aseev <ptrnine@altlinux.org> 5.23.5-alt5
- keep focus on the search field

* Fri Mar 04 2022 Sergey V Turchin <zerg@altlinux.org> 5.23.5-alt4
- show reboot when available to system update

* Fri Feb 11 2022 Aleksei Nikiforov <darktemplar@altlinux.org> 5.23.5-alt3
- fixed crash on flatpak initialization failure

* Wed Jan 19 2022 Sergey V Turchin <zerg@altlinux.org> 5.23.5-alt2
- temporary disable launch button for packagekit apps

* Mon Jan 10 2022 Sergey V Turchin <zerg@altlinux.org> 5.23.5-alt1
- new version

* Tue Dec 28 2021 Sergey V Turchin <zerg@altlinux.org> 5.23.4-alt7
- add workaround to setup  XDG_DATA_DIRS for snap

* Sun Dec 26 2021 Sergey V Turchin <zerg@altlinux.org> 5.23.4-alt6
- always enable SNAP backend by default

* Fri Dec 24 2021 Oleg Solovyov <mcpain@altlinux.org> 5.23.4-alt5
- fix updating packages status after succesful transaction (Closes: #41532)

* Fri Dec 24 2021 Sergey V Turchin <zerg@altlinux.org> 5.23.4-alt4
- turn off SNAP support for sisyphus branch

* Thu Dec 23 2021 Sergey V Turchin <zerg@altlinux.org> 5.23.4-alt3
- build with SNAP support

* Sat Dec 04 2021 Sergey V Turchin <zerg@altlinux.org> 5.23.4-alt2
- fix setup XDG_DATA_DIRS for flatpak

* Wed Dec 01 2021 Sergey V Turchin <zerg@altlinux.org> 5.23.4-alt1
- new version

* Mon Nov 15 2021 Sergey V Turchin <zerg@altlinux.org> 5.23.3.1-alt1
- new version

* Wed Nov 10 2021 Sergey V Turchin <zerg@altlinux.org> 5.23.3-alt1
- new version

* Mon Nov 01 2021 Sergey V Turchin <zerg@altlinux.org> 5.23.2-alt1
- new version

* Fri Sep 17 2021 Sergey V Turchin <zerg@altlinux.org> 5.22.5-alt2
- remove entry from khelpcenter

* Wed Sep 01 2021 Sergey V Turchin <zerg@altlinux.org> 5.22.5-alt1
- new version

* Tue Jul 27 2021 Sergey V Turchin <zerg@altlinux.org> 5.22.4-alt1
- new version

* Wed Jul 07 2021 Sergey V Turchin <zerg@altlinux.org> 5.22.3-alt1
- new version

* Thu Jul 01 2021 Sergey V Turchin <zerg@altlinux.org> 5.22.2-alt1
- new version

* Mon Jun 28 2021 Oleg Solovyov <mcpain@altlinux.org> 5.21.5-alt2
- enable offline updates by default (discoverrc)

* Thu May 13 2021 Sergey V Turchin <zerg@altlinux.org> 5.21.5-alt1
- new version

* Tue Apr 06 2021 Sergey V Turchin <zerg@altlinux.org> 5.21.4-alt1
- new version

* Wed Mar 31 2021 Sergey V Turchin <zerg@altlinux.org> 5.21.3-alt2
- fix package

* Fri Mar 19 2021 Sergey V Turchin <zerg@altlinux.org> 5.21.3-alt1
- new version

* Mon Jan 11 2021 Sergey V Turchin <zerg@altlinux.org> 5.20.5-alt1
- new version

* Wed Dec 02 2020 Sergey V Turchin <zerg@altlinux.org> 5.20.4-alt1
- new version

* Wed Oct 28 2020 Sergey V Turchin <zerg@altlinux.org> 5.20.2-alt1
- new version

* Thu Sep 17 2020 Sergey V Turchin <zerg@altlinux.org> 5.19.5-alt1
- new version

* Tue Jul 28 2020 Sergey V Turchin <zerg@altlinux.org> 5.19.4-alt1
- new version

* Tue Jul 07 2020 Sergey V Turchin <zerg@altlinux.org> 5.19.3-alt1
- new version

* Fri May 15 2020 Sergey V Turchin <zerg@altlinux.org> 5.18.5-alt2
- disable fwupd support on armh

* Thu May 07 2020 Sergey V Turchin <zerg@altlinux.org> 5.18.5-alt1
- new version

* Wed Apr 15 2020 Sergey V Turchin <zerg@altlinux.org> 5.18.4-alt2
- remove unnecessary X-DocPath from desktop-files

* Thu Apr 02 2020 Sergey V Turchin <zerg@altlinux.org> 5.18.4-alt1
- new version

* Wed Mar 11 2020 Sergey V Turchin <zerg@altlinux.org> 5.18.3-alt1
- new version

* Wed Feb 19 2020 Sergey V Turchin <zerg@altlinux.org> 5.18.1-alt1
- new version
- separate backands into subpackages
- add version to library sonames

* Thu Jan 09 2020 Sergey V Turchin <zerg@altlinux.org> 5.17.5-alt1
- new version

* Tue Dec 24 2019 Sergey V Turchin <zerg@altlinux.org> 5.17.4-alt3
- fix launch of packagekit applications

* Wed Dec 11 2019 Sergey V Turchin <zerg@altlinux.org> 5.17.4-alt2
- fix fwupd subpackage summary
- update requires

* Thu Dec 05 2019 Sergey V Turchin <zerg@altlinux.org> 5.17.4-alt1
- new version

* Wed Nov 13 2019 Sergey V Turchin <zerg@altlinux.org> 5.17.3-alt1
- new version

* Fri Nov 01 2019 Sergey V Turchin <zerg@altlinux.org> 5.17.2-alt1
- new version

* Fri Nov 01 2019 Aleksei Nikiforov <darktemplar@altlinux.org> 5.17.1-alt2
- Fixed use-after-free bug introduced by last patch.

* Mon Oct 28 2019 Sergey V Turchin <zerg@altlinux.org> 5.17.1-alt1
- new version

* Thu Oct 17 2019 Sergey V Turchin <zerg@altlinux.org> 5.17.0-alt1
- new version

* Tue Oct 01 2019 Aleksei Nikiforov <darktemplar@altlinux.org> 5.16.5-alt4
- Fixed issue with update if one appstream component corresponds to
  multiple packages without strict dependency between those packages.

* Mon Sep 30 2019 Aleksei Nikiforov <darktemplar@altlinux.org> 5.16.5-alt3
- Fixed updates via discover with patched packagekit.

* Tue Sep 24 2019 Sergey V Turchin <zerg@altlinux.org> 5.16.5-alt2
- using PackageKit offline updates by default

* Mon Sep 09 2019 Sergey V Turchin <zerg@altlinux.org> 5.16.5-alt1
- new version

* Thu Aug 01 2019 Sergey V Turchin <zerg@altlinux.org> 5.16.4-alt1
- new version

* Thu Jul 11 2019 Sergey V Turchin <zerg@altlinux.org> 5.16.3-alt1
- new version

* Thu Jun 27 2019 Sergey V Turchin <zerg@altlinux.org> 5.16.2-alt2
- move files to more standard place

* Wed Jun 26 2019 Sergey V Turchin <zerg@altlinux.org> 5.16.2-alt1
- new version

* Tue Jun 18 2019 Sergey V Turchin <zerg@altlinux.org> 5.16.1-alt1
- new version

* Fri Jun 07 2019 Sergey V Turchin <zerg@altlinux.org> 5.15.5-alt3
- export environment variable to add flatpak apps to menu

* Thu Jun 06 2019 Sergey V Turchin <zerg@altlinux.org> 5.15.5-alt2
- new version

* Tue Jun 04 2019 Sergey V Turchin <zerg@altlinux.org> 5.15.5-alt1
- new version

* Wed Apr 24 2019 Sergey V Turchin <zerg@altlinux.org> 5.15.4-alt1
- new version

* Tue Mar 05 2019 Sergey V Turchin <zerg@altlinux.org> 5.12.8-alt1
- new version

* Thu Jan 31 2019 Sergey V Turchin <zerg@altlinux.org> 5.12.7-alt4
- require packagekit
- require flatpak for flatpak-backend

* Thu Jan 10 2019 Sergey V Turchin <zerg@altlinux.org> 5.12.7-alt3
- require appstream-data

* Thu Dec 27 2018 Sergey V Turchin <zerg@altlinux.org> 5.12.7-alt2
- rebuild

* Thu Sep 27 2018 Sergey V Turchin <zerg@altlinux.org> 5.12.7-alt1
- new version
- build flatpak support in separate package

* Tue Aug 07 2018 Sergey V Turchin <zerg@altlinux.org> 5.12.6-alt2
- build without flatpak

* Tue Aug 07 2018 Sergey V Turchin <zerg@altlinux.org> 5.12.6-alt1
- initial build

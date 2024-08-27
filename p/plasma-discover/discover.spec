%define rname discover

%ifarch armh
%def_disable fwupd
%else
%def_enable fwupd
%endif
#
%def_enable snap
%def_disable ostree
#
%ifarch %qt6_qtwebengine_arches
%def_enable qtwebengine
%else
%def_disable qtwebengine
%endif

%define sover 6
%define libdiscovercommon libdiscovercommon%sover
%define libdiscovernotifiers libdiscovernotifiers%sover

Name: plasma-%rname
Version: 6.1.4
Release: alt2
%K6init no_altplace

Group: System/Configuration/Packaging
Summary: KDE Software Center
Url: http://www.kde.org
License: GPL-2.0-or-later

Provides: plasma5-discover = %EVR
Obsoletes: plasma5-discover < %EVR

Requires: %name-core
Requires: %name-packagekit

Source: %rname-%version.tar
Source1: env-flatpak.sh
Source2: env-snap.sh
# ALT
Patch1: alt-offline-updates.patch
Patch2: alt-pk-refresh-timer.patch
Patch3: alt-discover-update-all-packages-from-appstream.patch
Patch4: alt-hide-reviews.patch
Patch5: alt-soversion.patch
Patch6: alt-fix-status-after-transaction.patch
Patch7: alt-pk-disable-launch.patch
Patch8: alt-dont-crash-if-flatpak-not-initialized.patch
Patch9: alt-show-reboot-avail.patch
Patch10: alt-keep-focus.patch
Patch11: alt-hide-autoreboot.patch
Patch12: alt-send-interactive.patch
Patch13: alt-ghns-auth.patch

BuildRequires(pre): rpm-build-kf6 rpm-macros-qt6-webengine
BuildRequires: libvulkan-devel
BuildRequires: libssl-devel qt6-declarative-devel
BuildRequires: qcoro6-devel
BuildRequires: desktop-file-utils
BuildRequires: pkgconfig(libmarkdown)
%if_enabled qtwebengine
#BuildRequires: qt6-webengine-devel
BuildRequires: qt6-webview-devel
%endif
%if_enabled fwupd
BuildRequires: pkgconfig(fwupd)
%endif
%if_enabled snap
BuildRequires: snapd-qt-2-devel
%endif
%if_enabled ostree
BuildRequires: libostree-devel rpm-ostree-devel
%endif
BuildRequires: packagekit-qt6-devel
BuildRequires: libappstream-qt6-devel
BuildRequires: libflatpak-devel
BuildRequires: extra-cmake-modules kf6-karchive-devel kf6-kcrash-devel kf6-kdbusaddons-devel kf6-ki18n-devel kf6-kio-devel
BuildRequires: kf6-kirigami-devel kf6-kirigami-addons-devel
BuildRequires: kf6-kitemmodels-devel kf6-knewstuff-devel kf6-knotifications-devel kf6-kpackage-devel
BuildRequires: kf6-kdeclarative-devel kf6-kcmutils-devel kf6-kidletime-devel
BuildRequires: kf6-purpose-devel kf6-kstatusnotifieritem-devel kf6-kiconthemes-devel

%description
KDE and Plasma resources management GUI.

%package maxi
Summary: Plasma Discover maximum package
Group: System/Configuration/Packaging
Requires: %name
Requires: %name-kns
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
Requires: kf6-kirigami appstream-data
#Requires: plasma-runtime
Provides: plasma5-discover-core = %EVR
Obsoletes: plasma5-discover-core < %EVR
%description core
Plasma Discover core files.

%package common
Summary: %name common package
Group: System/Configuration/Other
#BuildArch: noarch
Requires: kde-common
Provides: plasma5-discover-common = %EVR
Obsoletes: plasma5-discover-common < %EVR
%description common
%name common package

%package devel
Group: Development/KDE and QT
Summary: Development files for %name
Requires: %name-common >= %EVR
Conflicts: plasma5-discover-devel < %EVR
%description devel
The %name-devel package contains libraries and header files for
developing applications that use %name.

%package kns
Summary: Plasma Discover KDE New Stuff support
Group: System/Configuration/Packaging
Requires: %name-core
Provides: plasma5-discover-kns = %EVR
Obsoletes: plasma5-discover-kns < %EVR
%description kns
Integrates  KDE New Stuff into Discover.

%package flatpak
Summary: Plasma Discover flatpak support
Group: System/Configuration/Packaging
Requires: %name-core
Requires: flatpak xdg-desktop-portal-kde flatpak-kcm
Provides: plasma5-discover-flatpak = %EVR
Obsoletes: plasma5-discover-flatpak < %EVR
%description flatpak
Integrates Flatpak applications into Discover.

%if_enabled snap
%package snap
Summary: Plasma Discover flatpak support
Group: System/Configuration/Packaging
Requires: %name-core
Requires: snapd
Provides: plasma5-discover-snap = %EVR
Obsoletes: plasma5-discover-snap < %EVR
%description snap
Integrates Snap applications into Discover.
%endif

%package fwupd
Summary: Plasma Discover fwupd support
Group: System/Configuration/Packaging
Requires: %name-core
Requires: fwupd
Provides: plasma5-discover-fwupd = %EVR
Obsoletes: plasma5-discover-fwupd < %EVR
%description fwupd
Integrates Fwupd firmware updater into Discover.

%package packagekit
Summary: Plasma Discover PackageKit support
Group: System/Configuration/Packaging
Requires: %name-core
Requires: packagekit
Provides: plasma5-discover-packagekit = %EVR
Obsoletes: plasma5-discover-packagekit < %EVR
%description packagekit
Integrates PackageKit package manager into Discover.

%package -n %libdiscovercommon
Group: System/Libraries
Summary: KF6 library
Requires: %name-common >= %EVR
%description -n %libdiscovercommon
KF6 library

%package -n %libdiscovernotifiers
Group: System/Libraries
Summary: KF6 library
Requires: %name-common >= %EVR
%description -n %libdiscovernotifiers
KF6 library


%prep
%setup -n %rname-%version
%patch1 -p1
%patch2 -p1
#%patch3 -p2 -b .upd-appstream
%patch4 -p1
%patch5 -p1
%patch6 -p1
#%patch7 -p1 -b .pk-disable-launch
%patch8 -p2
#patch9 -p1 -b .show-reboot-checkbox
%patch10 -p2
#%patch11 -p1 -b .autoreboot
%patch12 -p1
%patch13 -p1

if [ -d %_libdir/cmake/AppStreamQt6 -a ! -d %_libdir/cmake/AppStreamQt ] ; then
    mkdir -p cmake/AppStreamQt/
    for f in %_libdir/cmake/AppStreamQt6/*.cmake ; do
	ln -s $f cmake/AppStreamQt/`basename "$f" | sed 's|6||'`
    done
    ln -s %_includedir/AppStreamQt6 libdiscover/AppStreamQt
fi

# fix missing header
for d in libdiscover/backends/SnapBackend libdiscover/backends/SnapBackend/libsnapclient
do
    mkdir -p $d/Snapd/
    cat >$d/Snapd/Notice <<__EOF__
#include <Snapd/notice.h>
__EOF__
done

%build
%K6build \
    -DAppStreamQt_DIR:PATH=$PWD/cmake/AppStreamQt \
    -DSnapd_DIR:PATH=%_libdir/cmake/Snapd2 \
    #

%install
%K6install
mv %buildroot/%_libdir/plasma-discover/lib*.so* %buildroot/%_libdir/

%K6install_move data libdiscover kpackage

mkdir -p %buildroot/%_K6xdgconf/plasma-workspace/env/
install -m 0755 %SOURCE1 %buildroot/%_K6xdgconf/plasma-workspace/env/%{name}-flatpak.sh
install -m 0755 %SOURCE2 %buildroot/%_K6xdgconf/plasma-workspace/env/%{name}-snap.sh

for f in %buildroot/%_K6xdgapp/org.kde.discover*.desktop ; do
    desktop-file-install --mode=0755 --dir %buildroot/%_K6xdgapp \
	--remove-key="X-DocPath" \
	$f
done
desktop-file-install --mode=0644 --dir %buildroot/%_K6start \
	--add-only-show-in="KDE;XFCE;" \
	--remove-key="X-KDE-autostart-phase" \
	%buildroot/%_K6start/org.kde.discover.notifier.desktop

%find_lang %name --with-kde --all-name

%files
%files maxi

%files common -f %name.lang
%doc LICENSES/*
%dir %_K6data/libdiscover/
%dir %_K6data/libdiscover/categories/
%dir %_K6plug/discover-notifier/
%dir %_K6plug/discover/
%_datadir/qlogging-categories6/*.*categories
%_K6icon/*/*/apps/plasmadiscover.*

%files core
%_K6bin/*
%_K6libexecdir/DiscoverNotifier
%_K6xdgapp/org.kde.discover.desktop
%_K6xdgapp/org.kde.discover.urlhandler.desktop
%_K6xdgapp/org.kde.discover.notifier.desktop
%_K6xdgapp/kcm_updates.desktop
%_K6start/org.kde.discover.notifier.desktop
%_K6notif/*.notifyrc
%_datadir/metainfo/org.kde.discover.appdata.xml
#
%_K6plug/plasma/kcms/systemsettings/kcm_updates.so
#%_K6data/kpackage/kcms/kcm_updates/

%files kns
%_K6plug/discover/kns-backend.so

%files packagekit
%_K6plug/discover/packagekit-backend.so
%_K6plug/discover-notifier/DiscoverPackageKitNotifier.so
%_K6data/libdiscover/categories/packagekit-backend-categories.xml
%_datadir/metainfo/org.kde.discover.packagekit.appdata.xml

%files flatpak
%config(noreplace) %_K6xdgconf/plasma-workspace/env/*flatpak*.sh
%_K6plug/discover/flatpak-backend.so
%_datadir/metainfo/org.kde.discover.flatpak.appdata.xml
%_K6plug/discover-notifier/FlatpakNotifier.so
%_K6data/libdiscover/categories/flatpak-backend-categories.xml
%_K6xdgapp/org.kde.discover-flatpak.desktop
%_K6icon/*/*/apps/*flatpak*.*

%if_enabled snap
%files snap
%config(noreplace) %_K6xdgconf/plasma-workspace/env/*snap*.sh
%_K6plug/discover/snap-backend.so
%_K6libexecdir/discover/SnapMacaroonDialog
%_K6exec/kauth/libsnap_helper
%_K6dbus_sys_srv/org.kde.discover.libsnapclient.service
%_K6xdgapp/org.kde.discover.snap.desktop
%_K6dbus/system.d/org.kde.discover.libsnapclient.conf
%_datadir/metainfo/org.kde.discover.snap.appdata.xml
#%_K6data/libdiscover/categories/snap-backend-categories.xml
%_datadir/polkit-1/actions/org.kde.discover.libsnapclient.policy
%endif

%if_enabled fwupd
%files fwupd
%_K6plug/discover/fwupd-backend.so
%endif

%files -n %libdiscovercommon
%_K6lib/libDiscoverCommon.so.%sover
%_K6lib/libDiscoverCommon.so.*
%files -n %libdiscovernotifiers
%_K6lib/libDiscoverNotifiers.so.%sover
%_K6lib/libDiscoverNotifiers.so.*




%changelog
* Tue Aug 27 2024 Sergey V Turchin <zerg@altlinux.org> 6.1.4-alt2
- hide reviews preview

* Thu Aug 15 2024 Sergey V Turchin <zerg@altlinux.org> 6.1.4-alt1
- new version

* Thu Jul 11 2024 Sergey V Turchin <zerg@altlinux.org> 6.1.2-alt1
- new version

* Wed Jun 26 2024 Sergey V Turchin <zerg@altlinux.org> 6.1.1-alt1
- new version

* Tue Jun 25 2024 Sergey V Turchin <zerg@altlinux.org> 6.1.0-alt1
- initial build


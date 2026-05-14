%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1

Name: syncthingtray
Version: 2.1.0
Release: alt1

Summary: Desktop integration for Syncthing
License: GPL-2.0-or-later
Group: Networking/File transfer
Url: https://github.com/Martchus/syncthingtray

Source: %name-%version.tar

BuildRequires(pre): rpm-macros-cmake

BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: pkgconfig(martchus-c++utilities)
BuildRequires: pkgconfig(martchus-qtutilities)
BuildRequires: pkgconfig(martchus-qtquickforkawesome)
BuildRequires: boost-devel
BuildRequires: boost-filesystem-devel
BuildRequires: boost-asio-devel
BuildRequires: pkgconfig(Qt6Qml)
BuildRequires: qt6-tools-devel
BuildRequires: pkgconfig(Qt6Svg)
BuildRequires: plasma6-lib-devel
BuildRequires: kf6-kpackage-devel
BuildRequires: kf6-kcoreaddons-devel
BuildRequires: extra-cmake-modules
BuildRequires: kf6-kwindowsystem-devel
BuildRequires: kf6-kconfig-devel
BuildRequires: kf6-kio-devel

%description
Syncthing Tray is a user-friendly frontend for Syncthing.  The tray applet
contains a dashboard and remote controls for Syncthing.

This package makes Syncthing easier to use because it provides desktop
integration; The familiarity of a desktop interface makes it easier to
add shared folders and remote nodes, as well as to associate them with
each other.  It also provides quick access to the Device ID QR code so
that phones can be more easily added to the mesh network.

Syncthing Tray is also typically used to enable, monitor, and control the
Syncthing systemd service.  Finally, a program called "syncthingctl" is
provided as an additional remote control; it may be useful in scripts.

Syncthing is an application for decentralised file synchronisation and p2p
folder sharing.  It is an alternative solution to Dropbox, Google Drive,
and WebDav.  Syncthing also fulfills (or exceeds) the requirements for
file synchronisation that users of iCloud, ownCloud, or Nextcloud expect.

This package contains the tray applet, and syncthingctl.  Users of KDE
Plasma will benefit from superior integration as well as addition features
provided in the "syncthingtray-kde-plasma" package.

%package kde-plasma
Summary: KDE Plasma Desktop and Dolphin integration for Syncthing
Group: Graphical desktop/KDE
Requires: %name = %version-%release
Requires: /usr/bin/dolphin

%description kde-plasma
Syncthing Tray is a user-friendly frontend for Syncthing.

This package makes Syncthing easier to use because it provides desktop
integration; The familiarity of a desktop interface makes it easier to
add shared folders and remote nodes, as well as to associate them with
each other.  It also provides quick access to the Device ID QR code so
that phones can be more easily added to the mesh network.

Syncthing Tray is also typically used to enable, monitor, and control the
Syncthing systemd service.  Finally, a program called "syncthingctl" is
provided as an additional remote control; it may be useful in scripts.

Syncthing is an application for decentralised file synchronisation and p2p
folder sharing.  It is an alternative solution to Dropbox, Google Drive,
and WebDav.  Syncthing also fulfills (or exceeds) the requirements for
file synchronisation that users of iCloud, ownCloud, or Nextcloud expect.

This package contains the plasmoid for the KDE Plasma Desktop as well as a
KIO plugin.  The KIO plugin is typically appreciated for enabling Syncthing
awareness in the Dolphin file manager, and the plasmoid provides superior
integration with KDE Plasma when compared to the multidesktop tray applet.

%prep
%setup

%build
%cmake \
       -DCMAKE_BUILD_TYPE=Release \
       -DBUILD_SHARED_LIBS=ON \
       -DPACKAGE_NAMESPACE=martchus \
       -DNO_LIBSYNCTHING=ON \
       -DQT_PACKAGE_PREFIX=Qt6 \
       -DKF_PACKAGE_PREFIX=KF6
%cmake_build

%install
%cmake_install

%find_lang syncthingconnector --with-qt
%find_lang syncthingmodel --with-qt
%find_lang syncthingtray --with-qt
%find_lang syncthingwidgets --with-qt

cat syncthingconnector.lang syncthingmodel.lang syncthingtray.lang syncthingwidgets.lang  > %{name}-main.lang

%find_lang syncthingfileitemaction --with-qt
%find_lang syncthingplasmoid --with-qt

cat syncthingfileitemaction.lang syncthingplasmoid.lang > %{name}-kde.lang

%files -f %{name}-main.lang
%doc README.md
%_bindir/syncthingctl
%_bindir/syncthingtray
%_libdir/libsyncthingconnector.so.*
%_libdir/libsyncthingmodel.so.*
%_libdir/libsyncthingwidgets.so.*
%_desktopdir/syncthingtray.desktop
%_datadir/bash-completion/completions/syncthingctl
%_datadir/bash-completion/completions/syncthingtray
%_iconsdir/hicolor/scalable/apps/syncthingtray.svg
%_datadir/metainfo/io.github.martchus.syncthingtray.metainfo.xml
%dir %_datadir/syncthingconnector
%dir %_datadir/syncthingconnector/translations
%dir %_datadir/syncthingmodel
%dir %_datadir/syncthingmodel/translations
%dir %_datadir/syncthingtray
%dir %_datadir/syncthingtray/translations
%dir %_datadir/syncthingwidgets
%dir %_datadir/syncthingwidgets/translations

# devel files are excluded as done in Debian
%exclude %_includedir/syncthingconnector/global.h
%exclude %_includedir/syncthingconnector/qstringhash.h
%exclude %_includedir/syncthingconnector/syncthingcompletion.h
%exclude %_includedir/syncthingconnector/syncthingconfig.h
%exclude %_includedir/syncthingconnector/syncthingconnection.h
%exclude %_includedir/syncthingconnector/syncthingconnectionenums.h
%exclude %_includedir/syncthingconnector/syncthingconnectionsettings.h
%exclude %_includedir/syncthingconnector/syncthingconnectionstatus.h
%exclude %_includedir/syncthingconnector/syncthingconnector-definitions.h
%exclude %_includedir/syncthingconnector/syncthingdev.h
%exclude %_includedir/syncthingconnector/syncthingdir.h
%exclude %_includedir/syncthingconnector/syncthingignorepattern.h
%exclude %_includedir/syncthingconnector/syncthingnotifier.h
%exclude %_includedir/syncthingconnector/syncthingprocess.h
%exclude %_includedir/syncthingconnector/syncthingservice.h
%exclude %_includedir/syncthingconnector/utils.h
%exclude %_includedir/syncthingconnector/version.h
%exclude %_includedir/syncthingmodel/colors.h
%exclude %_includedir/syncthingmodel/global.h
%exclude %_includedir/syncthingmodel/syncthingdevicemodel.h
%exclude %_includedir/syncthingmodel/syncthingdirectorymodel.h
%exclude %_includedir/syncthingmodel/syncthingdownloadmodel.h
%exclude %_includedir/syncthingmodel/syncthingerrormodel.h
%exclude %_includedir/syncthingmodel/syncthingfilemodel.h
%exclude %_includedir/syncthingmodel/syncthingicons.h
%exclude %_includedir/syncthingmodel/syncthingmodel-definitions.h
%exclude %_includedir/syncthingmodel/syncthingmodel.h
%exclude %_includedir/syncthingmodel/syncthingrecentchangesmodel.h
%exclude %_includedir/syncthingmodel/syncthingsortfiltermodel.h
%exclude %_includedir/syncthingmodel/syncthingstatuscomputionmodel.h
%exclude %_includedir/syncthingmodel/syncthingstatusselectionmodel.h
%exclude %_includedir/syncthingmodel/version.h
%exclude %_includedir/syncthingwidgets/global.h
%exclude %_includedir/syncthingwidgets/misc/dbusstatusnotifier.h
%exclude %_includedir/syncthingwidgets/misc/diffhighlighter.h
%exclude %_includedir/syncthingwidgets/misc/direrrorsdialog.h
%exclude %_includedir/syncthingwidgets/misc/internalerror.h
%exclude %_includedir/syncthingwidgets/misc/internalerrorsdialog.h
%exclude %_includedir/syncthingwidgets/misc/otherdialogs.h
%exclude %_includedir/syncthingwidgets/misc/statusinfo.h
%exclude %_includedir/syncthingwidgets/misc/syncthingkiller.h
%exclude %_includedir/syncthingwidgets/misc/syncthinglauncher.h
%exclude %_includedir/syncthingwidgets/misc/textviewdialog.h
%exclude %_includedir/syncthingwidgets/misc/utils.h
%exclude %_includedir/syncthingwidgets/misc/syncthingdata.h
%exclude %_includedir/syncthingwidgets/misc/syncthingmodels.h
%exclude %_includedir/syncthingwidgets/settings/settings.h
%exclude %_includedir/syncthingwidgets/settings/settingsdialog.h
%exclude %_includedir/syncthingwidgets/settings/wizard.h
%exclude %_includedir/syncthingwidgets/settings/wizardenums.h
%exclude %_includedir/syncthingwidgets/syncthingwidgets-definitions.h
%exclude %_includedir/syncthingwidgets/version.h
%exclude %_includedir/syncthingwidgets/webview/webpage.h
%exclude %_includedir/syncthingwidgets/webview/webviewdialog.h
%exclude %_libdir/libsyncthingconnector.so
%exclude %_libdir/libsyncthingmodel.so
%exclude %_libdir/libsyncthingwidgets.so
%exclude %_pkgconfigdir/syncthingconnector.pc
%exclude %_pkgconfigdir/syncthingfileitemaction.pc
%exclude %_pkgconfigdir/syncthingmodel.pc
%exclude %_pkgconfigdir/syncthingplasmoid.pc
%exclude %_pkgconfigdir/syncthingwidgets.pc
%exclude %_datadir/syncthingconnector/cmake/syncthingconnectorConfig.cmake
%exclude %_datadir/syncthingconnector/cmake/syncthingconnectorConfigVersion.cmake
%exclude %_datadir/syncthingconnector/cmake/syncthingconnectorTargets-release.cmake
%exclude %_datadir/syncthingconnector/cmake/syncthingconnectorTargets.cmake
%exclude %_datadir/syncthingfileitemaction/cmake/syncthingfileitemactionConfig.cmake
%exclude %_datadir/syncthingfileitemaction/cmake/syncthingfileitemactionConfigVersion.cmake
%exclude %_datadir/syncthingfileitemaction/cmake/syncthingfileitemactionTargets-release.cmake
%exclude %_datadir/syncthingfileitemaction/cmake/syncthingfileitemactionTargets.cmake
%exclude %_datadir/syncthingmodel/cmake/syncthingmodelConfig.cmake
%exclude %_datadir/syncthingmodel/cmake/syncthingmodelConfigVersion.cmake
%exclude %_datadir/syncthingmodel/cmake/syncthingmodelTargets-release.cmake
%exclude %_datadir/syncthingmodel/cmake/syncthingmodelTargets.cmake
%exclude %_datadir/syncthingplasmoid/cmake/syncthingplasmoidConfig.cmake
%exclude %_datadir/syncthingplasmoid/cmake/syncthingplasmoidConfigVersion.cmake
%exclude %_datadir/syncthingplasmoid/cmake/syncthingplasmoidTargets-release.cmake
%exclude %_datadir/syncthingplasmoid/cmake/syncthingplasmoidTargets.cmake
%exclude %_datadir/syncthingwidgets/cmake/syncthingwidgetsConfig.cmake
%exclude %_datadir/syncthingwidgets/cmake/syncthingwidgetsConfigVersion.cmake
%exclude %_datadir/syncthingwidgets/cmake/syncthingwidgetsTargets-release.cmake
%exclude %_datadir/syncthingwidgets/cmake/syncthingwidgetsTargets.cmake

%files kde-plasma -f %{name}-kde.lang
%_libdir/qt6/plugins/kf6/kfileitemaction/libsyncthingfileitemaction.so
%_libdir/qt6/plugins/plasma/applets/martchus.syncthingplasmoid.so
%_datadir/metainfo/io.github.martchus.syncthingfileitemaction.metainfo.xml
%_datadir/metainfo/io.github.martchus.syncthingplasmoid.metainfo.xml
%dir %_datadir/plasma/plasmoids/martchus.syncthingplasmoid
%dir %_datadir/plasma/plasmoids/martchus.syncthingplasmoid/contents
%dir %_datadir/plasma/plasmoids/martchus.syncthingplasmoid/contents/ui
%_datadir/plasma/plasmoids/martchus.syncthingplasmoid/contents/ui/CompactRepresentation.qml
%_datadir/plasma/plasmoids/martchus.syncthingplasmoid/contents/ui/DetailItem.qml
%_datadir/plasma/plasmoids/martchus.syncthingplasmoid/contents/ui/DetailView.qml
%_datadir/plasma/plasmoids/martchus.syncthingplasmoid/contents/ui/DevicesPage.qml
%_datadir/plasma/plasmoids/martchus.syncthingplasmoid/contents/ui/DirectoriesPage.qml
%_datadir/plasma/plasmoids/martchus.syncthingplasmoid/contents/ui/DownloadsPage.qml
%_datadir/plasma/plasmoids/martchus.syncthingplasmoid/contents/ui/FullRepresentation.qml
%_datadir/plasma/plasmoids/martchus.syncthingplasmoid/contents/ui/IconLabel.qml
%_datadir/plasma/plasmoids/martchus.syncthingplasmoid/contents/ui/RecentChangesPage.qml
%_datadir/plasma/plasmoids/martchus.syncthingplasmoid/contents/ui/StatisticsView.qml
%_datadir/plasma/plasmoids/martchus.syncthingplasmoid/contents/ui/TabButton.qml
%_datadir/plasma/plasmoids/martchus.syncthingplasmoid/contents/ui/TinyButton.qml
%_datadir/plasma/plasmoids/martchus.syncthingplasmoid/contents/ui/ToolBar.qml
%_datadir/plasma/plasmoids/martchus.syncthingplasmoid/contents/ui/ToolButton.qml
%_datadir/plasma/plasmoids/martchus.syncthingplasmoid/contents/ui/ToolTipTrigger.qml
%_datadir/plasma/plasmoids/martchus.syncthingplasmoid/contents/ui/ToolTipView.qml
%_datadir/plasma/plasmoids/martchus.syncthingplasmoid/contents/ui/TopLevelItem.qml
%_datadir/plasma/plasmoids/martchus.syncthingplasmoid/contents/ui/TopLevelView.qml
%_datadir/plasma/plasmoids/martchus.syncthingplasmoid/contents/ui/main.qml
%_datadir/plasma/plasmoids/martchus.syncthingplasmoid/metadata.json
%dir %_datadir/syncthingfileitemaction
%dir %_datadir/syncthingfileitemaction/translations
%dir %_datadir/syncthingplasmoid
%dir %_datadir/syncthingplasmoid/translations

%changelog
* Thu May 14 2026 Nikolay Strelkov <snk@altlinux.org> 2.1.0-alt1
- New version 2.1.0.

* Wed Apr 08 2026 Nikolay Strelkov <snk@altlinux.org> 2.0.10-alt1
- New version 2.0.10.

* Sun Mar 15 2026 Nikolay Strelkov <snk@altlinux.org> 2.0.9-alt1
- New version 2.0.9.

* Wed Mar 04 2026 Nikolay Strelkov <snk@altlinux.org> 2.0.8-alt1
- New version 2.0.8.

* Thu Feb 05 2026 Nikolay Strelkov <snk@altlinux.org> 2.0.7-alt1
- New version 2.0.7.

* Wed Jan 07 2026 Nikolay Strelkov <snk@altlinux.org> 2.0.6-alt1
- New version 2.0.6.

* Sat Dec 13 2025 Nikolay Strelkov <snk@altlinux.org> 2.0.5-alt1
- New version 2.0.5.

* Thu Dec 04 2025 Nikolay Strelkov <snk@altlinux.org> 2.0.4-alt1
- New version 2.0.4.

* Sat Nov 22 2025 Nikolay Strelkov <snk@altlinux.org> 2.0.3-alt1
- Initial build for Sisyphus

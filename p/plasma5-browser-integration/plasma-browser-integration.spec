%define rname plasma-browser-integration

Name: plasma5-browser-integration
Version: 5.27.2
Release: alt1
%K5init altplace

Group: Graphical desktop/KDE
Summary: KDE Plasma 5 integration of web browsers
Url: http://www.kde.org
License: GPL-3.0-or-later

Source: %rname-%version.tar
Patch2: alt-detect-more-browsers.patch

# Automatically added by buildreq on Thu Feb 27 2020 (-bi)
# optimized out: clang7.0 cmake cmake-modules elfutils gcc-c++ glibc-kernheaders-generic glibc-kernheaders-x86 kf5-kauth-devel kf5-kbookmarks-devel kf5-kcodecs-devel kf5-kcompletion-devel kf5-kconfig-devel kf5-kconfigwidgets-devel kf5-kcoreaddons-devel kf5-kitemviews-devel kf5-kjobwidgets-devel kf5-kservice-devel kf5-kwidgetsaddons-devel kf5-kwindowsystem-devel kf5-kxmlgui-devel kf5-plasma-framework-devel kf5-solid-devel libdbusmenu-qt52 libglvnd-devel libgpg-error libqt5-concurrent libqt5-core libqt5-dbus libqt5-gui libqt5-network libqt5-printsupport libqt5-qml libqt5-sql libqt5-svg libqt5-texttospeech libqt5-widgets libqt5-x11extras libqt5-xml libsasl2-3 libstdc++-devel libxcbutil-keysyms python-modules python2-base python3 python3-base qt5-base-common qt5-base-devel rpm-build-python3 sh4
#BuildRequires: appstream extra-cmake-modules kf5-kactivities-devel kf5-kcrash-devel kf5-kdbusaddons-devel kf5-kded kf5-kfilemetadata-devel kf5-ki18n-devel kf5-kio-devel kf5-knotifications-devel kf5-kpackage-devel kf5-krunner-devel kf5-purpose-devel libssl-devel python-modules-compiler python3-dev qt5-wayland-devel
BuildRequires(pre): rpm-build-kf5
BuildRequires: extra-cmake-modules qt5-base-devel qt5-declarative-devel
BuildRequires: kf5-kactivities-devel kf5-kcrash-devel kf5-kdbusaddons-devel kf5-kded kf5-kfilemetadata-devel
BuildRequires: kf5-ki18n-devel kf5-kio-devel kf5-knotifications-devel kf5-kpackage-devel kf5-krunner-devel
BuildRequires: kf5-purpose-devel kf5-kitemmodels-devel
BuildRequires: plasma5-workspace-devel

%description
This package aims to provide better integration of web browsers with the KDE Plasma desktop.

%package common
Summary: %name common package
Group: System/Configuration/Other
BuildArch: noarch
Requires: kf5-filesystem
%description common
%name common package

%package devel
Group: Development/KDE and QT
Summary: Development files for %name
%description devel
The %name-devel package contains libraries and header files for
developing applications that use %name.

%package -n libplasma-browser-integration
Group: System/Libraries
Summary: %name library
Requires: %name-common
%description -n libplasma-browser-integration
%name library


%prep
%setup -n %rname-%version
%patch2 -p1

# disable krunners by default
for f in host/*.desktop ; do
    sed -i 's|^X-KDE-PluginInfo-EnabledByDefault=.*$|X-KDE-PluginInfo-EnabledByDefault=false|' $f
done


%build
%K5build \
    -DMOZILLA_DIR:PATH=%_libdir/mozilla \
    #
#    -DINSTALL_CHROME_MANIFEST=ON \

%install
%K5install
%K5install_move data krunner
%find_lang %name --all-name

#%files common -f %name.lang

%files -f %name.lang
%doc LICENSES/*
%config %_sysconfdir/chromium/native-messaging-hosts/org.kde.plasma.browser_integration.json
%config %_sysconfdir/opt/chrome/native-messaging-hosts/org.kde.plasma.browser_integration.json
%config %_sysconfdir/opt/edge/native-messaging-hosts/org.kde.plasma.browser_integration.json
%_libdir/mozilla/native-messaging-hosts/org.kde.plasma.browser_integration.json
%_K5bin/plasma-browser-integration-host
%_K5plug/kf5/kded/browserintegrationreminder.so
#%_K5plug/kf5/krunner/*.so
%_K5data/krunner/dbusplugins/plasma-runner-*.desktop
%_K5xdgapp/*browser_integration*.desktop

#%files devel
#%_K5inc/plasma-browser-integration_version.h
#%_K5inc/plasma-browser-integration/
#%_K5link/lib*.so
#%_K5lib/cmake/plasma-browser-integration
#%_K5archdata/mkspecs/modules/qt_plasma-browser-integration.pri

#%files -n libplasma-browser-integration
#%_K5lib/libplasma-browser-integration.so.*

%changelog
* Tue Feb 28 2023 Sergey V Turchin <zerg@altlinux.org> 5.27.2-alt1
- new version

* Mon Jan 09 2023 Sergey V Turchin <zerg@altlinux.org> 5.26.5-alt1
- new version

* Tue Nov 29 2022 Sergey V Turchin <zerg@altlinux.org> 5.26.4-alt1
- new version

* Tue Nov 08 2022 Sergey V Turchin <zerg@altlinux.org> 5.26.3-alt1
- new version

* Thu Oct 27 2022 Sergey V Turchin <zerg@altlinux.org> 5.26.2-alt1
- new version

* Wed Sep 07 2022 Sergey V Turchin <zerg@altlinux.org> 5.25.5-alt1
- new version

* Wed Aug 17 2022 Sergey V Turchin <zerg@altlinux.org> 5.25.4-alt1
- new version

* Mon Jul 11 2022 Sergey V Turchin <zerg@altlinux.org> 5.24.6-alt1
- new version

* Wed May 04 2022 Sergey V Turchin <zerg@altlinux.org> 5.24.5-alt1
- new version

* Wed Mar 30 2022 Sergey V Turchin <zerg@altlinux.org> 5.24.4-alt1
- new version

* Mon Jan 10 2022 Sergey V Turchin <zerg@altlinux.org> 5.23.5-alt1
- new version

* Wed Dec 01 2021 Sergey V Turchin <zerg@altlinux.org> 5.23.4-alt1
- new version

* Wed Nov 10 2021 Sergey V Turchin <zerg@altlinux.org> 5.23.3-alt1
- new version

* Mon Nov 01 2021 Sergey V Turchin <zerg@altlinux.org> 5.23.2-alt1
- new version

* Wed Sep 01 2021 Sergey V Turchin <zerg@altlinux.org> 5.22.5-alt1
- new version

* Tue Jul 27 2021 Sergey V Turchin <zerg@altlinux.org> 5.22.4-alt1
- new version

* Wed Jul 07 2021 Sergey V Turchin <zerg@altlinux.org> 5.22.3-alt1
- new version

* Thu Jul 01 2021 Sergey V Turchin <zerg@altlinux.org> 5.22.2-alt1
- new version

* Thu May 13 2021 Sergey V Turchin <zerg@altlinux.org> 5.21.5-alt1
- new version

* Tue Apr 06 2021 Sergey V Turchin <zerg@altlinux.org> 5.21.4-alt1
- new version

* Thu Apr 01 2021 Sergey V Turchin <zerg@altlinux.org> 5.21.3-alt2
- fix detect chromium and chromium-gost

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

* Thu May 07 2020 Sergey V Turchin <zerg@altlinux.org> 5.18.5-alt1
- new version

* Thu Apr 02 2020 Sergey V Turchin <zerg@altlinux.org> 5.18.4-alt1
- new version

* Wed Apr 01 2020 Sergey V Turchin <zerg@altlinux.org> 5.18.3-alt2
- turn off krunner plugin by default

* Wed Mar 11 2020 Sergey V Turchin <zerg@altlinux.org> 5.18.3-alt1
- new version

* Thu Feb 27 2020 Sergey V Turchin <zerg@altlinux.org> 5.18.1-alt1
- new version

%define rname layer-shell-qt

%define sover 5
%define liblayershellqtinterface liblayershellqtinterface%sover

Name: plasma5-%rname
Version: 5.26.5
Release: alt1
%K5init altplace

Group: Graphical desktop/KDE
Summary: KDE Plasma 5 Wayland shell component
Url: http://www.kde.org
License: GPL-2.0-or-later

Source: %rname-%version.tar

# Automatically added by buildreq on Fri Jul 02 2021 (-bi)
# optimized out: cmake cmake-modules debugedit elfutils fontconfig gcc-c++ glibc-kernheaders-generic glibc-kernheaders-x86 libctf-nobfd0 libglvnd-devel libgpg-error libqt5-core libqt5-dbus libqt5-gui libqt5-network libqt5-qml libqt5-waylandclient libsasl2-3 libssl-devel libstdc++-devel libwayland-client libwayland-client-devel libwayland-cursor libwayland-server-devel libxkbcommon-devel pkg-config python-modules python2-base python3 python3-base python3-module-paste qt5-base-devel qt5-declarative-devel rpm-build-python3 rpm-macros-python sh4 wayland-devel
#BuildRequires: appstream extra-cmake-modules git-core python-modules-compiler python3-dev python3-module-mpl_toolkits qt5-base-devel-static qt5-svg-devel qt5-wayland-devel tbb-devel wayland-protocols
BuildRequires(pre): rpm-build-kf5
BuildRequires: qt5-base-devel
BuildRequires: extra-cmake-modules
BuildRequires: qt5-base-devel-static qt5-svg-devel qt5-wayland-devel wayland-protocols

%description
This component is meant for applications to be able to easily use clients based on wlr-layer-shell.

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

%package -n %liblayershellqtinterface
Group: System/Libraries
Summary: %name library
Requires: %name-common
%description -n %liblayershellqtinterface
%name library


%prep
%setup -n %rname-%version

%build
%K5build \
    -DKDE_INSTALL_INCLUDEDIR=%_K5inc \
    #

%install
%K5install
%find_lang %name --all-name

%files common -f %name.lang
%doc LICENSES/*

%files
%_K5plug/wayland-shell-integration/liblayer-shell.so

%files devel
%_K5inc/LayerShellQt/
%_K5link/lib*.so
%_K5lib/cmake/LayerShellQt/

%files -n %liblayershellqtinterface
%_K5lib/libLayerShellQtInterface.so.%sover
%_K5lib/libLayerShellQtInterface.so.*

%changelog
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

* Fri Jul 02 2021 Sergey V Turchin <zerg@altlinux.org> 5.22.2-alt1
- initial build

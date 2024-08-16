%define rname layer-shell-qt

%define sover 6
%define liblayershellqtinterface liblayershellqtinterface%sover

Name: plasma6-%rname
Version: 6.1.4
Release: alt1
%K6init

Group: Graphical desktop/KDE
Summary: KDE Plasma 6 Wayland shell component
Url: http://www.kde.org
License: GPL-2.0-or-later

Source: %rname-%version.tar

BuildRequires(pre): rpm-build-kf6
BuildRequires: libvulkan-devel
BuildRequires: qt6-base-devel
BuildRequires: extra-cmake-modules
BuildRequires: qt6-base-devel qt6-svg-devel qt6-wayland-devel wayland-protocols

%description
This component is meant for applications to be able to easily use clients based on wlr-layer-shell.

%package common
Summary: %name common package
Group: System/Configuration/Other
BuildArch: noarch
Requires: kde-common
%description common
%name common package

%package devel
Group: Development/KDE and QT
Summary: Development files for %name
Conflicts: plasma5-layer-shell-qt-devel
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
%K6build \
    -DKDE_INSTALL_INCLUDEDIR=%_K6inc \
    #

%install
%K6install
%find_lang %name --all-name

%files common -f %name.lang
%doc LICENSES/*

%files
%_K6plug/wayland-shell-integration/liblayer-shell.so
%_K6qml/org/kde/layershell/

%files devel
%_K6inc/LayerShellQt/
%_K6link/lib*.so
%_K6lib/cmake/LayerShellQt/

%files -n %liblayershellqtinterface
%_K6lib/libLayerShellQtInterface.so.%sover
%_K6lib/libLayerShellQtInterface.so.*

%changelog
* Thu Aug 15 2024 Sergey V Turchin <zerg@altlinux.org> 6.1.4-alt1
- new version

* Thu Jul 11 2024 Sergey V Turchin <zerg@altlinux.org> 6.1.2-alt1
- new version

* Wed Jun 26 2024 Sergey V Turchin <zerg@altlinux.org> 6.1.1-alt1
- new version

* Tue Jun 25 2024 Sergey V Turchin <zerg@altlinux.org> 6.1.0-alt1
- initial build


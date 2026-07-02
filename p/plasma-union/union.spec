%define rname union

%define sover 6
%define libunion libunion%sover
%define libunionquickimpl libunionquickimpl%sover
%define libunionquickstyle libunionquickstyle%sover

Name: plasma-%rname
Version: 6.7.2
Release: alt1
%K6init

Group: Graphical desktop/KDE
Summary: KDE Plasma style engine
Url: http://www.kde.org
License: GPL-2.0-or-later

Source: %rname-%version.tar

BuildRequires(pre): rpm-build-kf6
# Automatically added by buildreq on Thu Jul 02 2026 (-bi)
# optimized out: cmake cmake-modules debugedit elfutils gcc-c++ git-core glibc-kernheaders-generic glibc-kernheaders-x86 libctf-nobfd0 libdouble-conversion3 libgcc15-devel libglvnd-devel libgpg-error libp11-kit libqt6-core libqt6-dbus libqt6-gui libqt6-network libqt6-opengl libqt6-pdf libqt6-qml libqt6-qmlcompiler libqt6-qmlmeta libqt6-qmlmodels libqt6-qmlworkerscript libqt6-quick libqt6-quickcontrols2 libqt6-quicktemplates2 libqt6-shadertools libqt6-svg libqt6-waylandclient libqt6-waylandcompositor libqt6-widgets libqt6-wlshellintegration libsasl2-3 libssl-devel libstdc++-devel libwayland-client libwayland-cursor perl python-modules python2-base python3 python3-base python3-dev python3-module-setuptools qt6-base-common qt6-base-devel qt6-declarative-devel qt6-shadertools-devel qt6-svg-devel qt6-tools rpm-build-file rpm-build-python3 rpm-build-qml6 rpm-macros-python sh5 tzdata vulkan-headers
#BuildRequires: appstream clang-tools extra-cmake-modules glslang kf6-kcolorscheme-devel kf6-kconfig-devel kf6-kcoreaddons-devel kf6-kguiaddons-devel kf6-kiconthemes-devel kf6-kirigami-devel libGLU-devel libvulkan-devel plasma6-breeze-devel python-modules-compiler qt6-quick3d-devel qt6-tools-devel qt6-virtualkeyboard qt6-virtualkeyboard-devel qt6-wayland-devel qt6-webengine-devel rpm-build-qml tbb-devel
BuildRequires: extra-cmake-modules qt6-declarative-devel qt6-shadertools-devel qt6-tools-devel
BuildRequires: kf6-kcolorscheme-devel kf6-kconfig-devel kf6-kcoreaddons-devel kf6-kguiaddons-devel
BuildRequires: kf6-kiconthemes-devel kf6-kirigami-devel
BuildRequires: libvulkan-devel
BuildRequires: plasma6-breeze-devel
#qt6-quick3d-devel  qt6-virtualkeyboard-devel qt6-webengine-devel
#BuildRequires: libryml-devel
#BuildRequires: cxx-rust-cssparser

%description
Union is a style engine designed to provide a unified style description to a set
of separate output styles.

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
Requires: %name-common >= %EVR
%description devel
The %name-devel package contains libraries and header files for
developing applications that use %name.

%package -n %libunion
Group: System/Libraries
Summary: %name library
Requires: %name-common >= %EVR
%description -n %libunion
%name library

%package -n %libunionquickimpl
Group: System/Libraries
Summary: %name library
Requires: %name-common >= %EVR
%description -n %libunionquickimpl
%name library

%package -n %libunionquickstyle
Group: System/Libraries
Summary: %name library
Requires: %name-common >= %EVR
%description -n %libunionquickstyle
%name library

%prep
%setup -n %rname-%version

%build
%K6build \
    -DKDE_INSTALL_INCLUDEDIR=%_K6inc \
    -DBUILD_INPUT_CSS:BOOL=OFF \
    -DBUILD_INPUT_PLASMASVG:BOOL=OFF \
    #

%install
%K6install
%find_lang %name --all-name

%files common  -f %name.lang
%doc LICENSES/*

%files
%_K6bin/*union*
%_K6plug/union/
%_K6qml/org/kde/kirigami/styles/org.kde.union/
%_K6qml/org/kde/union/
%_K6data/kstyle/themes/union.themerc
%_datadir/qlogging-categories6/*.*categories
%_K6plug/kf6/kirigami/platform/*union*.so
%_K6plug/styles/*nion*.so

%files devel
%_K6inc/union/
%_K6link/lib*.so
%_libdir/cmake/Union/

%files -n %libunion
%_K6lib/libUnion.so.%sover
%_K6lib/libUnion.so.*
%files -n %libunionquickimpl
%_K6lib/libUnionQuickImpl.so.%sover
%_K6lib/libUnionQuickImpl.so.*
%files -n %libunionquickstyle
%_K6lib/libUnionQuickStyle.so.%sover
%_K6lib/libUnionQuickStyle.so.*

%changelog
* Thu Jul 02 2026 Sergey V Turchin <zerg@altlinux.org> 6.7.2-alt1
- initial build

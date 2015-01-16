%define rname kguiaddons

Name: kf5-%rname
Version: 5.6.0
Release: alt0.1
%K5init altplace

Group: System/Libraries
Summary: KDE Frameworks 5 utilities for graphical user interfaces
Url: http://www.kde.org
License: GPLv2+ / LGPLv2+

Source: %rname-%version.tar

# Automatically added by buildreq on Fri Dec 26 2014 (-bi)
# optimized out: cmake cmake-modules elfutils libEGL-devel libGL-devel libICE-devel libSM-devel libX11-devel libXau-devel libXext-devel libXfixes-devel libXi-devel libXrender-devel libXt-devel libcloog-isl4 libqt5-core libqt5-gui libqt5-test libqt5-widgets libqt5-x11extras libstdc++-devel libxcb-devel pkg-config python-base qt5-base-devel ruby ruby-stdlibs xorg-kbproto-devel xorg-xf86miscproto-devel xorg-xproto-devel
#BuildRequires: extra-cmake-modules gcc-c++ libXScrnSaver-devel libXcomposite-devel libXcursor-devel libXdamage-devel libXdmcp-devel libXft-devel libXinerama-devel libXmu-devel libXpm-devel libXrandr-devel libXtst-devel libXv-devel libXxf86misc-devel libXxf86vm-devel libxkbfile-devel python-module-google qt5-x11extras-devel rpm-build-ruby
BuildRequires(pre): rpm-build-kf5
BuildRequires: extra-cmake-modules gcc-c++ qt5-x11extras-devel
BuildRequires: libXScrnSaver-devel libXcomposite-devel libXcursor-devel libXdamage-devel libXdmcp-devel
BuildRequires: libXft-devel libXinerama-devel libXmu-devel libXpm-devel libXrandr-devel libXtst-devel
BuildRequires: libXv-devel libXxf86misc-devel libXxf86vm-devel libxkbfile-devel

%description
The KDE GUI addons provide utilities for graphical user interfaces in the areas
of colors, fonts, text, images, keyboard input.

%package common
Summary: %name common package
Group: Graphical desktop/KDE
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

%package -n libkf5guiaddons
Group: System/Libraries
Summary: KF5 library
Requires: %name-common = %version-%release
%description -n libkf5guiaddons
KF5 library


%prep
%setup -n %rname-%version

%build
%K5build

%install
%K5install
%find_lang %name --with-qt --all-name

%files common -f %name.lang
%doc COPYING.LIB README.md

%files devel
%_K5inc/kguiaddons_version.h
%_K5inc/KGuiAddons/
%_K5link/lib*.so
%_K5lib/cmake/KF5GuiAddons
%_K5archdata/mkspecs/modules/qt_KGuiAddons.pri

%files -n libkf5guiaddons
%_K5lib/libKF5GuiAddons.so.*

%changelog
* Fri Jan 16 2015 Sergey V Turchin <zerg@altlinux.org> 5.6.0-alt0.1
- initial build

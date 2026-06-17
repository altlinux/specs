%define rname kguiaddons
%def_disable python
%if_enabled python
%define sipver2 %(rpm -q --qf '%%{VERSION}' python-module-sip)
%define sipver3 %(rpm -q --qf '%%{VERSION}' python3-module-sip)
%endif

Name: kf6-%rname
Version: 6.27.0
Release: alt1
%K6init no_altplace

Group: System/Libraries
Summary: KDE Frameworks 6 utilities for graphical user interfaces
Url: http://www.kde.org
License: GPL-2.0-or-later and LGPL-2.0-or-later

Requires: %name-common >= %EVR
Provides: kf5-kguiaddons = %EVR
Obsoletes: kf5-kguiaddons < %EVR

Source: %rname-%version.tar
Source10: yandex-maps-geo-handler.desktop
#Patch1: fix-modifierless-grabs.patch
Patch2: alt-fix-multiple-clipboard-images.patch

# Automatically added by buildreq on Fri Dec 26 2014 (-bi)
# optimized out: cmake cmake-modules elfutils libEGL-devel libGL-devel libICE-devel libSM-devel libX11-devel libXau-devel libXext-devel libXfixes-devel libXi-devel libXrender-devel libXt-devel libcloog-isl4 libqt6-core libqt6-gui libqt6-test libqt6-widgets libqt6-x11extras libstdc++-devel libxcb-devel pkg-config python-base qt6-base-devel ruby ruby-stdlibs xorg-kbproto-devel xorg-xf86miscproto-devel xorg-xproto-devel
#BuildRequires: extra-cmake-modules gcc-c++ libXScrnSaver-devel libXcomposite-devel libXcursor-devel libXdamage-devel libXdmcp-devel libXft-devel libXinerama-devel libXmu-devel libXpm-devel libXrandr-devel libXtst-devel libXv-devel libXxf86misc-devel libXxf86vm-devel libxkbfile-devel python-module-google  rpm-build-ruby
BuildRequires(pre): rpm-build-kf6
%if_enabled python
BuildRequires(pre): python3-module-sip-devel
BuildRequires: python3-module-PyQt6-devel
%endif
BuildRequires: extra-cmake-modules qt6-wayland-devel qt6-tools-devel
# 
BuildRequires: libXScrnSaver-devel libXcomposite-devel libXcursor-devel libXdamage-devel libXdmcp-devel
BuildRequires: libXft-devel libXinerama-devel libXmu-devel libXpm-devel libXrandr-devel libXtst-devel
BuildRequires: libXv-devel libXxf86misc-devel libXxf86vm-devel libxkbfile-devel
BuildRequires: libwayland-cursor-devel
BuildRequires: plasma-wayland-protocols

%description
The KDE GUI addons provide utilities for graphical user interfaces in the areas
of colors, fonts, text, images, keyboard input.

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
%description devel
The %name-devel package contains libraries and header files for
developing applications that use %name.

%package -n libkf6guiaddons
Group: System/Libraries
Summary: KF6 library
Requires: %name-common >= %EVR
%description -n libkf6guiaddons
KF6 library

%if_enabled python
%package -n python-module-%rname
Summary: Python bindings for KGuiAddons
License: GPLv2+ / LGPLv2+
Group: Development/Python
Requires: %name-common >= %EVR
Requires: python-module-pykf6
Requires: python-module-sip = %sipver2
%description -n python-module-%rname
Python bindings for KGuiAddons

%package -n python-module-%rname-devel
Summary: Sip files for python-module-%rname
Group: Development/Python
BuildArch: noarch
%description -n python-module-%rname-devel
Sip files for python-module-%rname

%package -n python3-module-%rname
Summary: Python3 bindings for KGuiAddons
License: GPLv2+ / LGPLv2+
Group: Development/Python3
Requires: %name-common >= %EVR
Requires: python3-module-pykf6
Requires: python3-module-sip = %sipver3
%description -n python3-module-%rname
Python3 bindings for KGuiAddons

%package -n python3-module-%rname-devel
Summary: Sip files for python3-module-%rname
Group: Development/Python3
BuildArch: noarch
%description -n python3-module-%rname-devel
Sip files for python3-module-%rname
%endif

%prep
%setup -n %rname-%version
#%patch1 -p1
%patch2 -p1

%build
%K6build \
    -DBUILD_PYTHON_BINDINGS:BOOL=OFF \
    #

%install
%K6install
install -m 0644 %SOURCE10 %buildroot/%_K6xdgapp/
%find_lang %name --all-name
%K6find_qtlang %name --all-name
rm -rf %buildroot%_libdir/*/*/*/__*


%files common -f %name.lang
%doc LICENSES/* README.md
%_datadir/qlogging-categories6/*.*categories

%files
%_K6bin/*geo*handler*
%_K6xdgapp/*geo*handler*.desktop

%files devel
%_K6inc/KGuiAddons/
%_K6link/lib*.so
%_K6lib/cmake/KF6GuiAddons/
%_K6archdata/metatypes/*.json
%_pkgconfigdir/KF6GuiAddons.pc

%files -n libkf6guiaddons
%_K6lib/libKF6GuiAddons.so.*
%_K6qml/org/kde/guiaddons/

%if_enabled python
#%files -n python-module-%rname
#%python_sitelibdir/PyKF6/*.so
#%files -n python-module-%rname-devel
#%_datadir/sip/PyKF6/KGuiAddons/
%files -n python3-module-%rname
%python3_sitelibdir/PyKF6/*.so
%files -n python3-module-%rname-devel
%_datadir/sip3/PyKF6/KGuiAddons/
%endif


%changelog
* Tue Jun 16 2026 Sergey V Turchin <zerg@altlinux.org> 6.27.0-alt1
- new version

* Mon May 11 2026 Sergey V Turchin <zerg@altlinux.org> 6.26.0-alt1
- new version

* Mon Apr 13 2026 Sergey V Turchin <zerg@altlinux.org> 6.25.0-alt1
- new version

* Fri Apr 03 2026 Dmitrii Fomchenkov <sirius@altlinux.org> 6.24.0-alt2
- fix corrupted screenshots on paste (closes: 58423)
- fix reinserting image into clipboard error

* Fri Mar 20 2026 Sergey V Turchin <zerg@altlinux.org> 6.24.0-alt1
- new version

* Fri Mar 06 2026 Sergey V Turchin <zerg@altlinux.org> 6.23.1-alt3
- add Yandex Maps

* Tue Mar 03 2026 Dmitrii Fomchenkov <sirius@altlinux.org> 6.23.1-alt2
- fix delay when pasting text from Klipper wdiget (closes: 57926)

* Tue Mar 03 2026 Sergey V Turchin <zerg@altlinux.org> 6.23.1-alt1
- new version

* Mon Feb 16 2026 Sergey V Turchin <zerg@altlinux.org> 6.23.0-alt1
- new version

* Fri Jan 30 2026 Dmitrii Fomchenkov <sirius@altlinux.org> 6.22.1-alt3
- update (closes: 57621)

* Tue Jan 20 2026 Dmitrii Fomchenkov <sirius@altlinux.org> 6.22.1-alt2
- fix issue with multiple clibpboard copies

* Wed Jan 14 2026 Sergey V Turchin <zerg@altlinux.org> 6.22.1-alt1
- new version

* Wed Jan 14 2026 Sergey V Turchin <zerg@altlinux.org> 6.22.0-alt1
- new version

* Mon Dec 22 2025 Sergey V Turchin <zerg@altlinux.org> 6.21.0-alt1
- new version

* Thu Nov 20 2025 Sergey V Turchin <zerg@altlinux.org> 6.20.0-alt1
- new version

* Fri Oct 17 2025 Sergey V Turchin <zerg@altlinux.org> 6.19.0-alt1
- new version

* Mon Sep 15 2025 Sergey V Turchin <zerg@altlinux.org> 6.18.0-alt1
- new version

* Mon Aug 25 2025 Sergey V Turchin <zerg@altlinux.org> 6.17.0-alt1
- new version

* Mon Aug 04 2025 Sergey V Turchin <zerg@altlinux.org> 6.16.0-alt1
- new version

* Mon Jul 07 2025 Sergey V Turchin <zerg@altlinux.org> 6.15.0-alt1
- new version

* Wed May 14 2025 Sergey V Turchin <zerg@altlinux.org> 6.14.0-alt1
- new version

* Mon Apr 14 2025 Sergey V Turchin <zerg@altlinux.org> 6.13.0-alt1
- new version

* Mon Mar 17 2025 Sergey V Turchin <zerg@altlinux.org> 6.12.0-alt1
- new version

* Fri Feb 14 2025 Sergey V Turchin <zerg@altlinux.org> 6.11.0-alt1
- new version

* Mon Jan 13 2025 Sergey V Turchin <zerg@altlinux.org> 6.10.0-alt1
- new version

* Mon Dec 16 2024 Sergey V Turchin <zerg@altlinux.org> 6.9.0-alt1
- new version

* Mon Nov 11 2024 Sergey V Turchin <zerg@altlinux.org> 6.8.0-alt1
- new version

* Fri Oct 11 2024 Sergey V Turchin <zerg@altlinux.org> 6.7.0-alt1
- new version

* Fri Oct 11 2024 Sergey V Turchin <zerg@altlinux.org> 6.6.0-alt1
- new version

* Wed Sep 04 2024 Sergey V Turchin <zerg@altlinux.org> 6.5.0-alt1
- new version

* Tue Aug 13 2024 Sergey V Turchin <zerg@altlinux.org> 6.4.0-alt1
- new version

* Tue Jul 23 2024 Sergey V Turchin <zerg@altlinux.org> 6.3.0-alt3
- obsolete kf5-kguiaddons

* Thu Jul 18 2024 Sergey V Turchin <zerg@altlinux.org> 6.3.0-alt2
- add conflict with kf5-kguiaddons

* Tue Jun 11 2024 Sergey V Turchin <zerg@altlinux.org> 6.3.0-alt1
- new version

* Mon May 13 2024 Sergey V Turchin <zerg@altlinux.org> 6.2.0-alt1
- new version

* Mon Apr 15 2024 Sergey V Turchin <zerg@altlinux.org> 6.1.0-alt1
- bump release

* Mon Apr 15 2024 Sergey V Turchin <zerg@altlinux.org> 6.1.0-alt0
- initial build


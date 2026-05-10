%define rname krfb

%define sover 5
%define libkrfbprivate libkrfbprivate%sover

Name: %rname
Version: 26.04.1
Release: alt1
%K6init

Group: Graphical desktop/KDE
Summary: KDE Desktop Sharing
Url: http://www.kde.org
License: GPL-2.0-or-later

Provides: kde5-krfb = %EVR
Obsoletes: kde5-krfb < %EVR

Source: %rname-%version.tar

BuildRequires(pre): rpm-build-kf6
BuildRequires: extra-cmake-modules qt6-declarative-devel
BuildRequires: libvulkan-devel
BuildRequires: libvncserver-devel
BuildRequires: libxcbutil-image-devel libXdamage-devel libXext-devel libXtst-devel
BuildRequires: libgbm-devel libepoxy-devel
BuildRequires: liblzo2-devel libjpeg-devel libpng-devel libgcrypt-devel libgnutls-devel libsystemd-devel
BuildRequires: pipewire-libs-devel plasma6-kpipewire-devel
BuildRequires: kf6-kauth-devel kf6-kcodecs-devel kf6-kcompletion-devel kf6-kconfig-devel kf6-kconfigwidgets-devel
BuildRequires: kf6-kcoreaddons-devel kf6-kcrash-devel kf6-kdbusaddons-devel  kf6-kdnssd-devel
BuildRequires: kf6-kdoctools kf6-kdoctools-devel kf6-ki18n-devel kf6-knotifications-devel kf6-kwallet-devel
BuildRequires: kf6-kwidgetsaddons-devel kf6-kxmlgui-devel kf6-kwindowsystem-devel kf6-kcolorscheme-devel
BuildRequires: kf6-kstatusnotifieritem-devel
BuildRequires: libwayland-client-devel qt6-wayland-devel plasma6-kwayland-devel plasma-wayland-protocols

%description
KDE Desktop Sharing (krfb) is a small server for the RFB protocol, better known as VNC.
Unlike most other Unix/Linux RFB servers, KRfb allows you to share your X11 session
instead of creating a new X11 session.

%package common
Summary: %name common package
Group: System/Configuration/Other
BuildArch: noarch
Requires: kde-common
Provides: kde5-krfb-common = %EVR
Obsoletes: kde5-krfb-common < %EVR
%description common
%name common package

%package devel
Group: Development/KDE and QT
Summary: Development files for %name
%description devel
The %name-devel package contains libraries and header files for
developing applications that use %name.

%package -n %libkrfbprivate
Group: System/Libraries
Summary: %name library
Requires: %name-common
%description -n %libkrfbprivate
%name library


%prep
%setup -n %rname-%version

%build
%K6build

%install
%K6install
%K6install_move data krfb
%find_lang %name --with-kde --all-name

%files common -f %name.lang
%doc COPYING*
%_datadir/qlogging-categories6/*.*categories

%files
%_K6bin/krfb*
%_K6plug/krfb/
%_K6xdgapp/*krfb*.desktop
%_K6data/krfb/
%_K6icon/*/*/apps/krfb.*
%_datadir/metainfo/*.xml

#%files devel
#%_K6inc/krfb_version.h
#%_K6inc/krfb/
#%_K6link/lib*.so
#%_K6lib/cmake/krfb

%files -n %libkrfbprivate
%_K6lib/libkrfbprivate.so.%sover
%_K6lib/libkrfbprivate.so.*


%changelog
* Fri May 08 2026 Sergey V Turchin <zerg@altlinux.org> 26.04.1-alt1
- new version

* Fri Mar 06 2026 Sergey V Turchin <zerg@altlinux.org> 25.12.3-alt1
- new version

* Fri Feb 06 2026 Sergey V Turchin <zerg@altlinux.org> 25.12.2-alt1
- new version

* Mon Jan 19 2026 Sergey V Turchin <zerg@altlinux.org> 25.12.1-alt1
- new version

* Tue Nov 18 2025 Sergey V Turchin <zerg@altlinux.org> 25.08.3-alt1
- new version

* Mon Oct 13 2025 Sergey V Turchin <zerg@altlinux.org> 25.08.2-alt1
- new version

* Mon Sep 22 2025 Sergey V Turchin <zerg@altlinux.org> 25.08.1-alt1
- new version

* Thu Jul 24 2025 Sergey V Turchin <zerg@altlinux.org> 25.04.3-alt1
- new version

* Tue Jun 10 2025 Sergey V Turchin <zerg@altlinux.org> 25.04.2-alt1
- new version

* Mon May 12 2025 Sergey V Turchin <zerg@altlinux.org> 25.04.1-alt1
- new version

* Mon Apr 21 2025 Sergey V Turchin <zerg@altlinux.org> 25.04.0-alt1
- new version

* Tue Mar 11 2025 Sergey V Turchin <zerg@altlinux.org> 24.12.3-alt1
- new version

* Tue Feb 18 2025 Sergey V Turchin <zerg@altlinux.org> 24.12.2-alt1
- new version

* Mon Jan 20 2025 Sergey V Turchin <zerg@altlinux.org> 24.12.1-alt1
- new version

* Wed Nov 13 2024 Sergey V Turchin <zerg@altlinux.org> 24.08.3-alt1
- new version

* Fri Oct 25 2024 Sergey V Turchin <zerg@altlinux.org> 24.08.2-alt1
- new version

* Wed Sep 25 2024 Sergey V Turchin <zerg@altlinux.org> 24.08.1-alt1
- initial build


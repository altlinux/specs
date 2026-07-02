%ifndef _userunitdir
%define _userunitdir %prefix/lib/systemd/user
%endif

%define sover 6
%define libkpipewire libkpipewire%sover
%define libkpipewirerecord libkpipewirerecord%sover
%define libkpipewiredmabuf libkpipewiredmabuf%sover


%define rname kpipewire
Name: plasma6-%rname
Version: 6.7.2
Release: alt1
%K6init

Group: System/Libraries
Summary: Set of convenient classes to use PipeWire
Url: http://www.kde.org
License: LGPL-2.0-only AND LGPL-3.0-only

Source: %rname-%version.tar
Patch1: alt-format-buffer.patch

BuildRequires(pre): rpm-build-kf6
BuildRequires: qt6-wayland-devel rpm-build-qml
BuildRequires: extra-cmake-modules
BuildRequires: libavformat-devel libswscale-devel libavfilter-devel
BuildRequires: libdrm-devel libepoxy-devel libgbm-devel
BuildRequires: libvulkan-devel
BuildRequires: pipewire-libs-devel
BuildRequires: kf6-kcoreaddons-devel kf6-ki18n-devel
BuildRequires: plasma-wayland-protocols

%description
Offers a set of convenient classes to use PipeWire (https://pipewire.org/) in Qt projects.

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
Requires: pipewire-libs-devel
Conflicts: plasma5-kpipewire-devel < %EVR
%description devel
The %name-devel package contains libraries and header files for
developing applications that use %name.

%package -n %libkpipewirerecord
Group: System/Libraries
Summary: %name library
Requires: %name-common
%description -n %libkpipewirerecord
%name library

%package -n %libkpipewire
Group: System/Libraries
Summary: %name library
Requires: %name-common
%description -n %libkpipewire
%name library

%package -n %libkpipewiredmabuf
Group: System/Libraries
Summary: %name library
Requires: %name-common
%description -n %libkpipewiredmabuf
%name library

%prep
%setup -n %rname-%version
%patch1 -p1

%build
%K6build \
    -DKDE_INSTALL_INCLUDEDIR=%_K6inc \
    #

%install
%K6install
%K6install_move data locale
%find_lang %name --all-name
%K6find_qtlang %name --append --all-name

%files
%_K6qml/org/kde/pipewire/

%files common -f %name.lang
%doc LICENSES/*
%_datadir/qlogging-categories6/*.*categories

%files devel
%_K6inc/KPipeWire/
%_K6link/lib*.so
%_K6lib/cmake/KPipeWire/
#%_pkgconfigdir/*.pc

%files -n %libkpipewire
%_K6lib/libKPipeWire.so.%sover
%_K6lib/libKPipeWire.so.*
%files -n %libkpipewirerecord
%_K6lib/libKPipeWireRecord.so.%sover
%_K6lib/libKPipeWireRecord.so.*
%files -n %libkpipewiredmabuf
%_K6lib/libKPipeWireDmaBuf.so.%sover
%_K6lib/libKPipeWireDmaBuf.so.*



%changelog
* Wed Jul 01 2026 Sergey V Turchin <zerg@altlinux.org> 6.7.2-alt1
- new version

* Mon Jun 29 2026 Sergey V Turchin <zerg@altlinux.org> 6.7.1-alt1
- new version

* Tue May 12 2026 Sergey V Turchin <zerg@altlinux.org> 6.6.5-alt1
- new version

* Thu Apr 09 2026 Sergey V Turchin <zerg@altlinux.org> 6.6.4-alt1
- new version

* Mon Mar 30 2026 Sergey V Turchin <zerg@altlinux.org> 6.6.3-alt1
- new version

* Wed Mar 11 2026 Sergey V Turchin <zerg@altlinux.org> 6.5.6-alt1
- new version

* Thu Jan 15 2026 Sergey V Turchin <zerg@altlinux.org> 6.5.5-alt1
- new version

* Wed Dec 10 2025 Sergey V Turchin <zerg@altlinux.org> 6.5.4-alt1
- new version

* Tue Nov 18 2025 Sergey V Turchin <zerg@altlinux.org> 6.5.3-alt1
- new version

* Thu Nov 13 2025 Sergey V Turchin <zerg@altlinux.org> 6.5.2-alt1
- new version

* Wed Nov 12 2025 Sergey V Turchin <zerg@altlinux.org> 6.4.6-alt1
- new version

* Tue Sep 16 2025 Sergey V Turchin <zerg@altlinux.org> 6.4.5-alt1
- new version

* Fri Aug 22 2025 Sergey V Turchin <zerg@altlinux.org> 6.4.4-alt1
- new version

* Tue Jul 15 2025 Sergey V Turchin <zerg@altlinux.org> 6.4.3-alt1
- new version

* Tue Jul 08 2025 Sergey V Turchin <zerg@altlinux.org> 6.4.2-alt1
- new version

* Wed May 07 2025 Sergey V Turchin <zerg@altlinux.org> 6.3.5-alt1
- new version

* Wed Apr 02 2025 Sergey V Turchin <zerg@altlinux.org> 6.3.4-alt1
- new version

* Wed Mar 12 2025 Sergey V Turchin <zerg@altlinux.org> 6.3.3-alt1
- new version

* Wed Feb 26 2025 Sergey V Turchin <zerg@altlinux.org> 6.3.2-alt1
- new version

* Wed Feb 19 2025 Sergey V Turchin <zerg@altlinux.org> 6.3.1-alt1
- new version

* Fri Feb 14 2025 Sergey V Turchin <zerg@altlinux.org> 6.3.0-alt1
- new version

* Thu Jan 09 2025 Sergey V Turchin <zerg@altlinux.org> 6.2.5-alt1
- new version

* Tue Nov 26 2024 Sergey V Turchin <zerg@altlinux.org> 6.2.4-alt1
- new version

* Wed Nov 06 2024 Sergey V Turchin <zerg@altlinux.org> 6.2.3-alt1
- new version

* Mon Oct 28 2024 Sergey V Turchin <zerg@altlinux.org> 6.2.2-alt1
- new version

* Tue Sep 10 2024 Sergey V Turchin <zerg@altlinux.org> 6.1.5-alt1
- new version

* Thu Aug 15 2024 Sergey V Turchin <zerg@altlinux.org> 6.1.4-alt1
- new version

* Thu Jul 11 2024 Sergey V Turchin <zerg@altlinux.org> 6.1.2-alt1
- new version

* Wed Jun 26 2024 Sergey V Turchin <zerg@altlinux.org> 6.1.1-alt1
- new version

* Tue Jun 25 2024 Sergey V Turchin <zerg@altlinux.org> 6.1.0-alt1
- initial build


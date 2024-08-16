%ifndef _userunitdir
%define _userunitdir %prefix/lib/systemd/user
%endif

%define sover 6
%define libkpipewire libkpipewire%sover
%define libkpipewirerecord libkpipewirerecord%sover
%define libkpipewiredmabuf libkpipewiredmabuf%sover


%define rname kpipewire
Name: plasma6-%rname
Version: 6.1.4
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
* Thu Aug 15 2024 Sergey V Turchin <zerg@altlinux.org> 6.1.4-alt1
- new version

* Thu Jul 11 2024 Sergey V Turchin <zerg@altlinux.org> 6.1.2-alt1
- new version

* Wed Jun 26 2024 Sergey V Turchin <zerg@altlinux.org> 6.1.1-alt1
- new version

* Tue Jun 25 2024 Sergey V Turchin <zerg@altlinux.org> 6.1.0-alt1
- initial build


Name: libkgeomap
Version: 2.0.0
Release: alt2

Summary: Libkgeomap is a wrapper around different world-map components
License: GPL2
Group: System/Libraries

Url: https://projects.kde.org/projects/extragear/libs/libkgeomap
Source: %name-%version.tar

BuildRequires(pre): kde-common-devel
BuildRequires: gcc-c++ kde4libs-devel kde4graphics-devel kde4edu-devel
Conflicts: libkmap

%description
Libkgeomap is a wrapper around different world-map components, to browse and arrange photos over a map.
Currently supported map engine are:
- Marble,
- OpenstreetMap (via Marble),
- GoogleMap.

%package devel
Group: Development/KDE and QT
Summary: Devel files for %name
%description devel
Devel files for %name

%prep
%setup

%build
%K4build

%install
%K4install

%files
%_K4bindir/*
%_K4libdir/%name.so*
%_K4apps/%name

%files devel
%_pkgconfigdir/%name.pc
%_K4includedir/*
%_K4link/*.so
%_K4apps/cmake/modules/FindKGeoMap.cmake


%changelog
* Fri Jan 27 2012 Sergey V Turchin <zerg@altlinux.org> 2.0.0-alt2
- rebuilt with new kde

* Tue Oct 04 2011 Aeliya Grevnyov <gray_graff@altlinux.org> 2.0.0-alt1
- Update to 2.0.0
  + Rename to libkgeomap

* Thu Jun 30 2011 Aeliya Grevnyov <gray_graff@altlinux.org> 1.0.0-alt1
- Initial build for sysiphus


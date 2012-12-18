Name: libkgeomap
Version: 2.0.0
Release: alt4

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
#%_K4bindir/*
%_K4libdir/%name.so*
%_K4apps/%name

%files devel
%_pkgconfigdir/%name.pc
%_K4includedir/*
%_K4link/*.so
%_K4apps/cmake/modules/FindKGeoMap.cmake


%changelog
* Tue Dec 18 2012 Sergey V Turchin <zerg@altlinux.org> 2.0.0-alt4
- update from digikam-3.0.0-beta3

* Fri Oct 05 2012 Sergey V Turchin <zerg@altlinux.org> 2.0.0-alt3
- rebuilt with KDE-4.9

* Sat Apr 07 2012 Sergey V Turchin <zerg@altlinux.org> 2.0.0-alt0.M60P.3
- rebuilt with KDE-4.8

* Fri Jan 27 2012 Sergey V Turchin <zerg@altlinux.org> 2.0.0-alt2
- rebuilt with new kde

* Thu Nov 03 2011 Sergey V Turchin <zerg@altlinux.org> 2.0.0-alt0.M60P.2
- rebuilt with KDE-4.7

* Tue Oct 18 2011 Aeliya Grevnyov <gray_graff@altlinux.org> 2.0.0-alt0.M60P.1
- backport to ALTLinux 6.0P (by rpmbph script)

* Tue Oct 04 2011 Aeliya Grevnyov <gray_graff@altlinux.org> 2.0.0-alt1
- Update to 2.0.0
  + Rename to libkgeomap

* Thu Jun 30 2011 Aeliya Grevnyov <gray_graff@altlinux.org> 1.0.0-alt1
- Initial build for sysiphus


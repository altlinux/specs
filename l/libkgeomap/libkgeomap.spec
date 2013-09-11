Name: libkgeomap
Version: 2.0.0
Release: alt7

Group: System/Libraries
Summary: Libkgeomap is a wrapper around different world-map components
Url: https://projects.kde.org/projects/extragear/libs/libkgeomap
License: GPL2

Requires: %name-common >= %EVR

Source: %name-%version.tar
Source1: po.tar

BuildRequires(pre): kde-common-devel
BuildRequires: gcc-c++ kde4libs-devel kde4graphics-devel kde4edu-devel
Conflicts: libkmap

%description
Libkgeomap is a wrapper around different world-map components, to browse and arrange photos over a map.
Currently supported map engine are:
- Marble,
- OpenstreetMap (via Marble),
- GoogleMap.

%package common
BuildArch: noarch
Group: Graphical desktop/KDE
Summary: Common files for %name package
%description common
Common files for %name package

%package devel
Group: Development/KDE and QT
Summary: Devel files for %name
%description devel
Devel files for %name

%prep
%setup -a1
if ! grep -qe '^add_subdirectory([[:space:]]*po[[:space:]]*)' CMakeLists.txt
then
cat >> CMakeLists.txt <<__EOF__
find_package(Msgfmt REQUIRED)
find_package(Gettext REQUIRED)
add_subdirectory( po )
__EOF__
fi

%build
%K4build

%install
%K4install

rm -rf %buildroot/%_K4i18n/*/*/*kipi*
rm -rf %buildroot/%_K4i18n/*/*/digikam*
%K4find_lang %name

%files common -f %name.lang
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
* Tue Sep 10 2013 Sergey V Turchin <zerg@altlinux.org> 2.0.0-alt7
- update from digikam-3.4.0

* Tue May 21 2013 Sergey V Turchin <zerg@altlinux.org> 2.0.0-alt6
- update from digikam-3.2.0

* Thu Apr 18 2013 Sergey V Turchin <zerg@altlinux.org> 2.0.0-alt5
- update from digikam-3.1.0
- package translatons (ALT#26565)

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


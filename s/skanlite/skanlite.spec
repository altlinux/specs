
Name: skanlite
Version: 0.8
Release: alt1

Group: Graphics
Summary: Image scanning application
Url: http://www.kde.org/
License: GPLv2

Requires: kde4libs >= %{get_version kde4libs}

Source0: %name-%version.tar
Source1: FindKSane.cmake

# Automatically added by buildreq on Mon Dec 22 2008 (-bi)
#BuildRequires: gcc-c++ kde4base-runtime kde4graphics-devel libXScrnSaver-devel libXau-devel libXcomposite-devel libXdamage-devel libXdmcp-devel libXpm-devel libXt-devel libXtst-devel libXv-devel libXxf86misc-devel libqt3-devel libxkbfile-devel xorg-xf86vidmodeproto-devel
BuildRequires(pre): kde4libs-devel
BuildRequires: gcc-c++ kde4base-runtime-devel kde4graphics-devel


%description
Skanlite is a simple image scanning application that does nothing more
than scan and save images. It can open a save dialog for every image
scanned or save the images immediately in a specified directory
with auto-generated names and format.


%prep
%setup -q -n %name-%version
mkdir -p cmake/modules/
install -m 0644 %SOURCE1 cmake/modules/
sed -i \
    's|\(^find_package.*\)$|set(CMAKE_MODULE_PATH ${CMAKE_MODULE_PATH} ${CMAKE_CURRENT_SOURCE_DIR}/cmake/modules )\n\1|' \
    CMakeLists.txt

%build
%K4cmake
%K4make

%install
%K4install
%K4find_lang --with-kde %name

%files -f %name.lang
%doc src/TODO
%_K4bindir/%name
%_K4xdg_apps/%name.desktop
%doc %_K4doc/*/%name

%changelog
* Thu Apr 05 2012 Sergey V Turchin <zerg@altlinux.org> 0.8-alt1
- new version

* Tue Jan 24 2012 Sergey V Turchin <zerg@altlinux.org> 0.5-alt1.M60P.1
- built for M60P

* Fri Oct 07 2011 Sergey V Turchin <zerg@altlinux.org> 0.5-alt2
- fix find libksane

* Fri Nov 19 2010 Sergey V Turchin <zerg@altlinux.org> 0.5-alt0.M51.1
- built for M51

* Fri Nov 19 2010 Sergey V Turchin <zerg@altlinux.org> 0.5-alt1
- new version

* Thu Apr 22 2010 Sergey V Turchin <zerg@altlinux.org> 0.4-alt0.M51.1
- build for M51

* Fri Feb 12 2010 Sergey V Turchin <zerg@altlinux.org> 0.4-alt1
- new version

* Fri Sep 11 2009 Sergey V Turchin <zerg@altlinux.org> 0.3-alt2
- updated translations

* Mon Apr 06 2009 Sergey V Turchin <zerg@altlinux.org> 0.3-alt1
- new version

* Mon Jan 26 2009 Sergey V Turchin <zerg at altlinux dot org> 0.2-alt2
- updated translations

* Mon Dec 22 2008 Sergey V Turchin <zerg at altlinux dot org> 0.2-alt1
- initial specfile


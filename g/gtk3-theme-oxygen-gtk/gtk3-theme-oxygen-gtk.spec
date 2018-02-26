%define real_name oxygen-gtk
%define gtk3_prefix gtk3-theme

Name: %gtk3_prefix-%real_name
Version: 1.0.5
Release: alt1
Serial: 1

Group: Graphical desktop/GNOME
Summary: Oxygen GTK3 theme
Summary(ru_RU.UTF8): Тема Oxygen для GTK3
URL: http://kde.org/
License: LGPLv2.1

Provides: %real_name = %version-%release

Source0: %{real_name}-%{version}.tar

# Automatically added by buildreq on Mon Aug 29 2011 (-bi)
# optimized out: cmake-modules elfutils fontconfig fontconfig-devel glib2-devel libICE-devel libSM-devel libX11-devel libXau-devel libXext-devel libXfixes-devel libXft-devel libXi-devel libXrender-devel libatk-devel libcairo-devel libcairo-gobject libcairo-gobject-devel libdbus-devel libdbus-glib libfreetype-devel libgdk-pixbuf libgdk-pixbuf-devel libgio-devel libpango-devel libstdc++-devel pkg-config python-base ruby xorg-kbproto-devel xorg-xf86miscproto-devel xorg-xproto-devel
#BuildRequires: cmake gcc-c++ libXScrnSaver-devel libXcomposite-devel libXcursor-devel libXdamage-devel libXdmcp-devel libXinerama-devel libXpm-devel libXrandr-devel libXt-devel libXtst-devel libXv-devel libXxf86misc-devel libXxf86vm-devel libdbus-glib-devel libgtk+3-devel libxkbfile-devel rpm-build-ruby
BuildRequires: cmake gcc-c++ libdbus-glib-devel libgtk+3-devel
BuildRequires: kde-common-devel
BuildRequires: libXScrnSaver-devel libXcomposite-devel libXcursor-devel libXdamage-devel libXdmcp-devel libXinerama-devel
BuildRequires: libXpm-devel libXrandr-devel libXt-devel libXtst-devel libXv-devel libXxf86misc-devel libXxf86vm-devel
BuildRequires: libxkbfile-devel

%description
This is GTK3 port of default KDE4 Oxygen style.

%description -l ru_RU.UTF8
Данная тема представляет собой порт на GTK3 стандартного
стиля графических элементов KDE4 - Oxygen.

%prep
%setup -qn %{real_name}-%{version}

%build
%Kcmake
%Kmake

%install
%Kinstall

%files
%_bindir/oxygen-gtk3-*
%_libdir/gtk-3.*/*/theming-engines/*oxygen*.so
%_datadir/themes/%real_name

%changelog
* Tue Jun 19 2012 Sergey V Turchin <zerg@altlinux.org> 1:1.0.5-alt1
- new version

* Mon May 14 2012 Sergey V Turchin <zerg@altlinux.org> 1:1.0.4-alt0.M60P.1
- build for M60P

* Mon May 14 2012 Sergey V Turchin <zerg@altlinux.org> 1:1.0.4-alt1
- new version

* Mon Apr 16 2012 Sergey V Turchin <zerg@altlinux.org> 1:1.0.3-alt0.M60P.1
- built for M60P

* Mon Apr 16 2012 Sergey V Turchin <zerg@altlinux.org> 1:1.0.3-alt1
- new version

* Tue Mar 13 2012 Sergey V Turchin <zerg@altlinux.org> 1:1.0.2-alt0.M60P.1
- built for M60P

* Tue Mar 13 2012 Sergey V Turchin <zerg@altlinux.org> 1:1.0.2-alt1
- new version

* Sun Mar 11 2012 Sergey V Turchin <zerg@altlinux.org> 1:1.0.1-alt0.M60P.1
- built for M60P

* Sun Mar 11 2012 Sergey V Turchin <zerg@altlinux.org> 1:1.0.1-alt1
- new version

* Tue Jan 17 2012 Sergey V Turchin <zerg@altlinux.org> 1:1.0.0-alt1
- 1.0.0 release

* Tue Nov 22 2011 Sergey V Turchin <zerg@altlinux.org> 1.1.50-alt3
- update from gtk3 branch

* Fri Sep 16 2011 Sergey V Turchin <zerg@altlinux.org> 1.1.50-alt1.M60P.1
- built for M60P

* Fri Sep 16 2011 Sergey V Turchin <zerg@altlinux.org> 1.1.50-alt2
- update from gtk3 branch

* Thu Sep 01 2011 Sergey V Turchin <zerg@altlinux.org> 1.1.50-alt0.M60P.1
- built for M60P

* Mon Aug 29 2011 Sergey V Turchin <zerg@altlinux.org> 1.1.50-alt1
- initial build

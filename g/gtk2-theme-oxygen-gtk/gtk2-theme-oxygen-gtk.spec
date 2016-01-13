%define real_name oxygen-gtk
%define gtk2_prefix gtk2-theme

Name: %gtk2_prefix-%real_name
Version: 1.4.6
Release: alt2

Group: Graphical desktop/GNOME
Summary: Oxygen GTK2 theme
Summary(ru_RU.UTF8): Тема Oxygen для GTK2
URL: http://kde.org/
License: LGPLv2.1

Provides: %real_name = %version-%release

Source0: %{real_name}-%{version}.tar

# Automatically added by buildreq on Tue Apr 12 2011 (-bi)
# optimized out: cmake-modules elfutils fontconfig fontconfig-devel glib2-devel libICE-devel libSM-devel libX11-devel libXau-devel libXext-devel libXfixes-devel libXft-devel libXi-devel libXrender-devel libatk-devel libcairo-devel libfreetype-devel libgdk-pixbuf libgdk-pixbuf-devel libgio-devel libpango-devel libstdc++-devel pkg-config python-base ruby xorg-kbproto-devel xorg-xf86miscproto-devel xorg-xproto-devel
#BuildRequires: cmake gcc-c++ libXScrnSaver-devel libXcomposite-devel libXcursor-devel libXdamage-devel libXdmcp-devel libXinerama-devel libXpm-devel libXrandr-devel libXt-devel libXtst-devel libXv-devel libXxf86misc-devel libXxf86vm-devel libgtk+2-devel libxkbfile-devel rpm-build-ruby
BuildRequires: cmake gcc-c++ libgtk+2-devel libdbus-glib-devel
BuildRequires: kde-common-devel
BuildRequires: libXScrnSaver-devel libXcomposite-devel libXcursor-devel libXdamage-devel
BuildRequires: libXdmcp-devel libXinerama-devel libXpm-devel libXrandr-devel libXt-devel
BuildRequires: libXtst-devel libXv-devel libXxf86vm-devel libxkbfile-devel

%description
This is GTK2 port of default KDE4 Oxygen style.

%description -l ru_RU.UTF8
Данная тема представляет собой порт на GTK2 стандартного
стиля графических элементов KDE4 - Oxygen.

%prep
%setup -qn %{real_name}-%{version}

%build
%Kbuild \
    -DENABLE_DEMO=OFF \
    #

%install
%Kinstall

%files
%_libdir/gtk-2.*/*/engines/*.so
%_datadir/themes/%real_name

%changelog
* Wed Jan 13 2016 Sergey V Turchin <zerg@altlinux.org> 1.4.6-alt2
- update from 1.4 branch (ALT#31703)

* Mon Oct 27 2014 Sergey V Turchin <zerg@altlinux.org> 1.4.6-alt0.M70P.1
- built for M70P

* Mon Oct 27 2014 Sergey V Turchin <zerg@altlinux.org> 1.4.6-alt1
- new version

* Thu Apr 10 2014 Sergey V Turchin <zerg@altlinux.org> 1.4.5-alt0.M70P.1
- built for M70P

* Thu Apr 10 2014 Sergey V Turchin <zerg@altlinux.org> 1.4.5-alt1
- new version

* Thu Mar 27 2014 Sergey V Turchin <zerg@altlinux.org> 1.4.4-alt0.M70P.1
- built for M70P

* Thu Mar 27 2014 Sergey V Turchin <zerg@altlinux.org> 1.4.4-alt1
- new version

* Mon Jan 27 2014 Sergey V Turchin <zerg@altlinux.org> 1.4.3-alt0.M70P.1
- built for M70P

* Mon Jan 27 2014 Sergey V Turchin <zerg@altlinux.org> 1.4.3-alt1
- new version

* Fri Jan 24 2014 Sergey V Turchin <zerg@altlinux.org> 1.4.2-alt0.M70P.1
- built for M70P

* Fri Jan 24 2014 Sergey V Turchin <zerg@altlinux.org> 1.4.2-alt1
- new version

* Thu Dec 12 2013 Sergey V Turchin <zerg@altlinux.org> 1.4.1-alt0.M70P.1
- built for M70P

* Thu Dec 12 2013 Sergey V Turchin <zerg@altlinux.org> 1.4.1-alt1
- new version

* Mon Sep 02 2013 Sergey V Turchin <zerg@altlinux.org> 1.4.0-alt1
- new version

* Mon Jun 03 2013 Sergey V Turchin <zerg@altlinux.org> 1.3.4-alt1
- new version

* Mon Apr 29 2013 Sergey V Turchin <zerg@altlinux.org> 1.3.3-alt1
- new version

* Thu Feb 14 2013 Sergey V Turchin <zerg@altlinux.org> 1.3.2.1-alt1
- new version

* Thu Jan 31 2013 Sergey V Turchin <zerg@altlinux.org> 1.3.2-alt1
- new version

* Mon Oct 08 2012 Sergey V Turchin <zerg@altlinux.org> 1.3.1-alt1
- new version

* Wed Jul 18 2012 Sergey V Turchin <zerg@altlinux.org> 1.3.0-alt1
- new version

* Tue Jun 19 2012 Sergey V Turchin <zerg@altlinux.org> 1.2.5-alt0.M60P.1
- built for M60P

* Tue Jun 19 2012 Sergey V Turchin <zerg@altlinux.org> 1.2.5-alt1
- new version

* Mon May 14 2012 Sergey V Turchin <zerg@altlinux.org> 1.2.4-alt0.M60P.1
- build for M60P

* Mon May 14 2012 Sergey V Turchin <zerg@altlinux.org> 1.2.4-alt1
- new version

* Mon Apr 16 2012 Sergey V Turchin <zerg@altlinux.org> 1.2.3-alt0.M60P.1
- built for M60P

* Mon Apr 16 2012 Sergey V Turchin <zerg@altlinux.org> 1.2.3-alt1
- new version

* Tue Mar 13 2012 Sergey V Turchin <zerg@altlinux.org> 1.2.2-alt1
- new version

* Sun Mar 11 2012 Sergey V Turchin <zerg@altlinux.org> 1.2.1-alt1
- new version

* Tue Jan 17 2012 Sergey V Turchin <zerg@altlinux.org> 1.2.0-alt1
- new version

* Wed Dec 28 2011 Sergey V Turchin <zerg@altlinux.org> 1.1.6-alt0.M60P.1
- built for M60P

* Thu Dec 15 2011 Sergey V Turchin <zerg@altlinux.org> 1.1.6-alt1
- new version

* Tue Nov 22 2011 Sergey V Turchin <zerg@altlinux.org> 1.1.5-alt1
- new version

* Fri Oct 21 2011 Sergey V Turchin <zerg@altlinux.org> 1.1.4-alt0.M60T.1
- built for M60T

* Tue Oct 18 2011 Sergey V Turchin <zerg@altlinux.org> 1.1.4-alt1
- new version

* Fri Sep 16 2011 Sergey V Turchin <zerg@altlinux.org> 1.1.3-alt1
- new version

* Mon Aug 29 2011 Sergey V Turchin <zerg@altlinux.org> 1.1.2-alt1
- new version

* Wed Aug 03 2011 Sergey V Turchin <zerg@altlinux.org> 1.1.1-alt1
- new version

* Wed Jun 15 2011 Sergey V Turchin <zerg@altlinux.org> 1.1.0-alt1
- new version

* Thu May 12 2011 Sergey V Turchin <zerg@altlinux.org> 1.0.5-alt1
- new version

* Tue Apr 12 2011 Sergey V Turchin <zerg@altlinux.org> 1.0.4-alt1
- new version

* Fri Mar 25 2011 Sergey V Turchin <zerg@altlinux.org> 1.0.3-alt2
- using sources from anongit.kde.org

* Tue Mar 15 2011 Sergey V Turchin <zerg@altlinux.org> 1.0.3-alt1
- new version

* Mon Feb 14 2011 Sergey V Turchin <zerg@altlinux.org> 1.0.2-alt1
- new version

* Mon Jan 17 2011 Sergey V Turchin <zerg@altlinux.org> 1.0.1-alt1
- initial build

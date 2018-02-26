%define _iskde 1
%define rname yawp
#define svnversion 
%define naplet plasma_applet_yawp

Name: kde4plasma-addon-yawp
Version: 0.4.0
Release: alt1

Group: Graphical desktop/KDE
Summary: Yet Another Weather Plasmoid
License: GPLv2
Url: http://yawp.sourceforge.net/



Source: %rname-%version.tar.bz2
Patch: yawp-0.3.2-russia.patch
Patch2: yawp-0.3.4-alt-fix-compile.patch



# Automatically added by buildreq on Mon Feb 22 2010
BuildRequires: gcc-c++ glib2-devel glibc-devel-static kde4base-workspace-devel
BuildRequires: libXScrnSaver-devel libXau-devel libXcomposite-devel
BuildRequires: libXdamage-devel libXdmcp-devel libXpm-devel libXt-devel
BuildRequires: libXtst-devel libXv-devel libXxf86misc-devel
BuildRequires: libxkbfile-devel qt4-assistant xorg-xf86vidmodeproto-devel

BuildRequires: libXcomposite-devel libXdamage-devel libXdmcp-devel libXpm-devel
BuildRequires: libXt-devel libXtst-devel libXv-devel libXxf86misc-devel
BuildRequires: libqt4-devel libxkbfile-devel xorg-xf86vidmodeproto-devel
 
%description
Yet Another Weather Plasmoid.
This is not complete I am putting it out there for some help.
There is nothing wrong with the ones that exist, I just wanted something more 



%prep
%setup -q -n %rname-%version
#%patch -p1
#%patch2 -p1


%build
%K4cmake
%K4make

%install
%K4install
#install -D -m 644  themes/*.svgz %buildroot%_K4apps/desktoptheme/default/widgets/

# i18n
%K4find_lang %naplet

%files -f %naplet.lang
%_K4libdir/kde4/*.so
%_K4srv/*.desktop
%_K4apps/desktoptheme/default/widgets/*
%_K4apps/ion_accuweather/

%changelog
* Tue Nov 15 2011 Sergey V Turchin <zerg@altlinux.org> 0.4.0-alt1
- new version

* Thu Feb 03 2011 Sergey V Turchin <zerg@altlinux.org> 0.3.6-alt1
- new version

* Wed Nov 03 2010 Sergey V Turchin <zerg@altlinux.org> 0.3.5-alt2
- rebuilt

* Mon Oct 18 2010 Sergey V Turchin <zerg@altlinux.org> 0.3.5-alt1
- new version (ALT#24325)

* Fri Oct 08 2010 Sergey V Turchin <zerg@altlinux.org> 0.3.4-alt1
- new version
- fix compile with new kde

* Thu Apr 22 2010 Sergey V Turchin <zerg@altlinux.org> 0.3.2-alt0.M51.2
- rebuilt with KDE-4.4

* Sun Mar 07 2010 Hihin Ruslan <ruslandh@altlinux.ru> 0.3.2-alt0.M51.1
- backport to branch 5.1

* Mon Feb 22 2010 Hihin Ruslan <ruslandh@altlinux.ru> 0.3.2-alt1
- new version

* Mon Feb 16 2009 Hihin Ruslan <ruslandh@altlinux.ru> 0.1-alt1.svn20090216.1
- new version

* Sun Dec 28 2008 Hihin Ruslan <ruslandh@altlinux.ru> 0.1-alt1.svn20081228.3
- fixed background

* Sun Dec 28 2008 Hihin Ruslan <ruslandh@altlinux.ru> 0.1-alt1.svn20081228.1
- first build

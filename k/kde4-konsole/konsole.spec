
%add_findpackage_path %_kde4_bindir

%define rname konsole
%define major 4
%define minor 14
%define bugfix 3
Name: kde4-konsole
Version: %major.%minor.%bugfix
Release: alt3

Group: Terminals
Summary: Terminal emulator for KDE
Url: http://www.kde.org/
License: GPLv2

PreReq(post,preun): alternatives >= 0.2
Requires: fonts-bitmap-terminus
Provides: xvt, %_x11bindir/xvt
Provides: kde4base-konsole = %version-%release
Obsoletes: kde4base-konsole < %version-%release
Conflicts: kdebase-wm <= 3.5.12-alt2

Source0: ftp://ftp.kde.org/pub/kde/stable/%version/src/%rname-%version.tar
Patch1: kdebase-4.8.0-alt-konsole-allow-sgid.patch
Patch2: kdebase-4.10.0-alt-konsole-profiles.patch
Patch3: kdebase-4.14.3-alt-no-transparency.patch
Patch4: kdebase-4.14.3-alt-def-font.patch
# Dmitry Prokoptsev
Patch1000: BR59256fixed.diff
# upstream

# Automatically added by buildreq on Tue Mar 01 2011 (-bi)
#BuildRequires: gcc-c++ glib2-devel kde4libs-devel libXScrnSaver-devel libXau-devel libXcomposite-devel libXdamage-devel libXdmcp-devel libXpm-devel libXt-devel libXtst-devel libXv-devel libXxf86misc-devel libXxf86vm-devel libqt3-devel libxkbfile-devel qt4-designer rpm-build-ruby zlib-devel-static
BuildRequires: gcc-c++ glib2-devel kde4libs-devel kde4base-devel
BuildRequires: libalternatives-devel

%description
As well as being a standalone program, it is also used by other KDE programs
such as the Kate editor and KDevelop development environment to provide easy
access to a terminal window. Konsole's features and usage are explained and
illustrated in the Konsole handbook, which can be accessed by browsing to
"help:/konsole" in Konqueror.

%prep
%setup -q -n %rname-%version
%patch1 -p3
%patch2 -p2
%patch3 -p1
%patch4 -p1
pushd src
#%patch1000 -p0
popd

%build
%K4build \
    -DKDE4_ENABLE_FPIE:BOOL=ON \
    -DKDE4_ENABLE_FINAL:BOOL=ON

%install
%K4install

# install alternatives
install -d %buildroot/%_sysconfdir/alternatives/packages.d
cat > %buildroot/%_sysconfdir/alternatives/packages.d/kde4-konsole <<__EOF__
%ifdef _kde4_alternate_placement
%_x11bindir/xvt %_kde4_bindir/konsole        14
%else
%_x11bindir/xvt %_K4bindir/konsole        60
%endif
__EOF__


%files
%config %_sysconfdir/alternatives/packages.d/kde4-konsole
# adding to utmp don't work because dbus checking for saved guid
#attr(2711,root,utempter) %_K4bindir/konsole
%_K4bindir/konsole
#
%_K4bindir/konsoleprofile
%_K4libdir/libkdeinit4_konsole.so
%_K4libdir/libkonsoleprivate.so
%_K4lib/libkonsolepart.so*
%_K4xdg_apps/konsole.desktop
%_K4apps/konsole/
%_K4conf_update/*
%_K4srv/konsolepart.desktop
%_K4srv/ServiceMenus/konsole*.desktop
%_K4srvtyp/terminalemulator.desktop
%_K4doc/en/konsole/


%changelog
* Tue Dec 29 2015 Sergey V Turchin <zerg@altlinux.org> 4.14.3-alt3
- set Terminus font by default

* Mon Jul 27 2015 Sergey V Turchin <zerg@altlinux.org> 4.14.3-alt2
- allow transparent backgroungs

* Fri Nov 14 2014 Sergey V Turchin <zerg@altlinux.org> 4.14.3-alt1
- new version

* Thu Sep 18 2014 Sergey V Turchin <zerg@altlinux.org> 4.14.1-alt1
- new version

* Wed Aug 13 2014 Sergey V Turchin <zerg@altlinux.org> 4.14.0-alt1
- new version

* Wed Jun 18 2014 Sergey V Turchin <zerg@altlinux.org> 4.13.2-alt1
- new version

* Tue May 13 2014 Sergey V Turchin <zerg@altlinux.org> 4.13.1-alt1
- new version

* Fri Apr 18 2014 Sergey V Turchin <zerg@altlinux.org> 4.13.0-alt1
- new version

* Thu Mar 13 2014 Sergey V Turchin <zerg@altlinux.org> 4.12.3-alt0.M70P.1
- built for M70P

* Tue Mar 11 2014 Sergey V Turchin <zerg@altlinux.org> 4.12.3-alt1
- new version

* Thu Jan 30 2014 Sergey V Turchin <zerg@altlinux.org> 4.12.2-alt1
- new version

* Fri Oct 04 2013 Sergey V Turchin <zerg@altlinux.org> 4.11.2-alt0.M70P.1
- built for M70P

* Thu Oct 03 2013 Sergey V Turchin <zerg@altlinux.org> 4.11.2-alt1
- new version

* Thu Sep 05 2013 Sergey V Turchin <zerg@altlinux.org> 4.11.1-alt1
- new version

* Wed Jul 03 2013 Sergey V Turchin <zerg@altlinux.org> 4.10.5-alt1
- new version

* Tue Jun 25 2013 Sergey V Turchin <zerg@altlinux.org> 4.10.4-alt2
- remove sgid(adding to utmp don't work because dbus checking for saved guid)

* Tue Jun 04 2013 Sergey V Turchin <zerg@altlinux.org> 4.10.4-alt1
- new version

* Tue May 14 2013 Sergey V Turchin <zerg@altlinux.org> 4.10.3-alt1
- new version

* Fri Apr 05 2013 Sergey V Turchin <zerg@altlinux.org> 4.10.2-alt1
- new version

* Tue Mar 05 2013 Sergey V Turchin <zerg@altlinux.org> 4.10.1-alt1
- new version

* Mon Jan 14 2013 Sergey V Turchin <zerg@altlinux.org> 4.10.0-alt0.2
- update from 4.10 branch

* Tue Dec 11 2012 Sergey V Turchin <zerg@altlinux.org> 4.10.0-alt0.1
- new beta version

* Thu Dec 06 2012 Sergey V Turchin <zerg@altlinux.org> 4.9.4-alt1
- new version

* Fri Nov 09 2012 Sergey V Turchin <zerg@altlinux.org> 4.9.3-alt1
- new version

* Mon Oct 01 2012 Sergey V Turchin <zerg@altlinux.org> 4.9.1-alt1
- new version

* Fri Aug 03 2012 Sergey V Turchin <zerg@altlinux.org> 4.8.5-alt0.M60P.1
- built for M60P

* Thu Aug 02 2012 Sergey V Turchin <zerg@altlinux.org> 4.8.5-alt1
- new version

* Mon Jun 18 2012 Sergey V Turchin <zerg@altlinux.org> 4.8.4-alt0.M60P.1
- built for M60P

* Tue Jun 05 2012 Sergey V Turchin <zerg@altlinux.org> 4.8.4-alt1
- new version

* Thu May 10 2012 Sergey V Turchin <zerg@altlinux.org> 4.8.3-alt0.M60P.1
- build for M60P

* Wed May 02 2012 Sergey V Turchin <zerg@altlinux.org> 4.8.3-alt1
- new version

* Tue Apr 10 2012 Sergey V Turchin <zerg@altlinux.org> 4.8.2-alt0.M60P.1
- built for M60P

* Tue Apr 10 2012 Sergey V Turchin <zerg@altlinux.org> 4.8.2-alt1
- new version

* Wed Apr 04 2012 Sergey V Turchin <zerg@altlinux.org> 4.8.1-alt0.M60P.1
- built for M60P

* Tue Mar 06 2012 Sergey V Turchin <zerg@altlinux.org> 4.8.1-alt1
- new version

* Fri Jan 20 2012 Sergey V Turchin <zerg@altlinux.org> 4.8.0-alt1
- new version

* Mon Dec 05 2011 Sergey V Turchin <zerg@altlinux.org> 4.7.4-alt0.M60P.1
- build for M60P

* Fri Dec 02 2011 Sergey V Turchin <zerg@altlinux.org> 4.7.4-alt1
- new version

* Thu Nov 03 2011 Sergey V Turchin <zerg@altlinux.org> 4.7.3-alt0.M60P.1
- built for M60P

* Sun Oct 30 2011 Sergey V Turchin <zerg@altlinux.org> 4.7.3-alt1
- new version

* Tue Oct 18 2011 Sergey V Turchin <zerg@altlinux.org> 4.7.2-alt0.M60T.1
- built for M60T

* Tue Oct 04 2011 Sergey V Turchin <zerg@altlinux.org> 4.7.2-alt1
- new version

* Thu Sep 08 2011 Sergey V Turchin <zerg@altlinux.org> 4.7.1-alt1
- new version

* Tue Jun 07 2011 Sergey V Turchin <zerg@altlinux.org> 4.6.4-alt1
- new version

* Mon May 16 2011 Sergey V Turchin <zerg@altlinux.org> 4.6.3-alt2
- disable background transparency by default

* Wed May 04 2011 Sergey V Turchin <zerg@altlinux.org> 4.6.3-alt1
- new version

* Tue Apr 05 2011 Sergey V Turchin <zerg@altlinux.org> 4.6.2-alt1
- new version

* Fri Mar 04 2011 Sergey V Turchin <zerg@altlinux.org> 4.6.1-alt1
- split from kde4base

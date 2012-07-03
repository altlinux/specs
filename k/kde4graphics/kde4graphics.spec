
%add_findpackage_path %_kde4_bindir

%define rname kdegraphics
Name: kde4graphics
%define major 4
%define minor 8
%define bugfix 0
Version: %major.%minor.%bugfix
Release: alt2

Group: Graphical desktop/KDE
Summary: K Desktop Environment - Graphics Applications
License: GPL
Url: http://www.kde.org

BuildArch: noarch
#Provides: %name-common = %version-%release
#Obsoletes: %name-common < %version-%release

Requires: kde4base-runtime-core
Requires: kde4-kgamma
Requires: kde4-kamera
Requires: kde4-okular
Requires: kde4-gwenview
Requires: kde4-kcolorchooser
Requires: kde4-kolourpaint
Requires: kde4-kruler
Requires: kde4-ksnapshot
#
Requires: kde4-ksaneplugin
Requires: kde4-graphics-strigi-analyzer
Requires: kde4-svgpart
Requires: kde4-graphics-thumbnailers

%description
Graphical tools for the K Desktop Environment.
Collection of graphic oriented applications

%package devel
Summary: Devel stuff for %name
Group: Development/KDE and QT
Requires: kde4libs-devel
Requires: libkipi4-devel libkdcraw4-devel libkexiv24-devel libksane4-devel
Requires: kde4-ksnapshot-devel kde4-okular-devel
%description devel
This package contains header files needed if you wish to build applications
based on %name.

%prep
%setup -Tc %name-%version

%build

%files
%files devel

%changelog
* Fri Feb 03 2012 Sergey V Turchin <zerg@altlinux.org> 4.8.0-alt2
- fix requires

* Tue Jan 24 2012 Sergey V Turchin <zerg@altlinux.org> 4.8.0-alt1
- new version

* Thu Nov 03 2011 Sergey V Turchin <zerg@altlinux.org> 4.7.1-alt0.M60P.1
- built for M60P

* Tue Oct 18 2011 Sergey V Turchin <zerg@altlinux.org> 4.7.1-alt0.M60T.1
- built for M60T

* Tue Sep 13 2011 Sergey V Turchin <zerg@altlinux.org> 4.7.1-alt1
- make an empty package with requires

* Mon Aug 22 2011 Sergey V Turchin <zerg@altlinux.org> 4.6.5-alt1.M60P.1
- built for M60P

* Fri Aug 12 2011 Sergey V Turchin <zerg@altlinux.org> 4.6.5-alt2
- fix compile with new cmake

* Tue Jul 05 2011 Sergey V Turchin <zerg@altlinux.org> 4.6.5-alt1
- new version

* Tue Jun 07 2011 Sergey V Turchin <zerg@altlinux.org> 4.6.4-alt1
- new version

* Thu May 05 2011 Sergey V Turchin <zerg@altlinux.org> 4.6.3-alt1
- new version

* Wed Apr 06 2011 Sergey V Turchin <zerg@altlinux.org> 4.6.2-alt1
- new version

* Wed Mar 02 2011 Sergey V Turchin <zerg@altlinux.org> 4.6.1-alt1
- new version

* Fri Feb 18 2011 Sergey V Turchin <zerg@altlinux.org> 4.6.0-alt2
- move to standart place

* Fri Jan 28 2011 Sergey V Turchin <zerg@altlinux.org> 4.6.0-alt1
- new version

* Wed Jan 19 2011 Sergey V Turchin <zerg@altlinux.org> 4.5.5-alt1
- new version

* Wed Dec 01 2010 Sergey V Turchin <zerg@altlinux.org> 4.5.4-alt1
- new version

* Tue Nov 02 2010 Sergey V Turchin <zerg@altlinux.org> 4.5.3-alt1
- new version

* Wed Oct 06 2010 Sergey V Turchin <zerg@altlinux.org> 4.5.2-alt1
- new version

* Mon Aug 30 2010 Sergey V Turchin <zerg@altlinux.org> 4.5.1-alt1
- new version

* Thu Aug 05 2010 Sergey V Turchin <zerg@altlinux.org> 4.5.0-alt1
- new version

* Thu Jul 08 2010 Sergey V Turchin <zerg@altlinux.org> 4.4.5-alt0.M51.1
- built for M51

* Mon Jul 05 2010 Sergey V Turchin <zerg@altlinux.org> 4.4.5-alt1
- new version

* Mon Jun 07 2010 Sergey V Turchin <zerg@altlinux.org> 4.4.4-alt2
- rebuilt with new exiv2

* Thu Jun 03 2010 Sergey V Turchin <zerg@altlinux.org> 4.4.4-alt0.M51.1
- built for M51

* Tue Jun 01 2010 Sergey V Turchin <zerg@altlinux.org> 4.4.4-alt1
- new version

* Thu May 13 2010 Sergey V Turchin <zerg@altlinux.org> 4.4.3-alt0.M51.1
- built for M51

* Mon May 03 2010 Sergey V Turchin <zerg@altlinux.org> 4.4.3-alt1
- new version

* Wed Apr 21 2010 Sergey V Turchin <zerg@altlinux.org> 4.4.2-alt0.M51.1
- built for M51

* Tue Mar 30 2010 Sergey V Turchin <zerg@altlinux.org> 4.4.2-alt1
- new version

* Mon Mar 01 2010 Sergey V Turchin <zerg@altlinux.org> 4.4.1-alt1
- new version

* Thu Feb 11 2010 Sergey V Turchin <zerg@altlinux.org> 4.4.0-alt1
- new version

* Thu Jan 28 2010 Sergey V Turchin <zerg@altlinux.org> 4.3.95-alt1
- new version

* Thu Jan 21 2010 Sergey V Turchin <zerg@altlinux.org> 4.3.90-alt1
- new version

* Mon Jan 11 2010 Sergey V Turchin <zerg@altlinux.org> 4.3.4-alt2
- rebuilt with new exiv

* Tue Dec 15 2009 Sergey V Turchin <zerg@altlinux.org> 4.3.4-alt0.M51.1
- built for M51

* Mon Nov 30 2009 Sergey V Turchin <zerg@altlinux.org> 4.3.4-alt1
- new version

* Mon Nov 09 2009 Sergey V Turchin <zerg@altlinux.org> 4.3.3-alt0.M51.1
- built for M51

* Mon Nov 02 2009 Sergey V Turchin <zerg@altlinux.org> 4.3.3-alt1
- new version

* Fri Oct 09 2009 Sergey V Turchin <zerg@altlinux.org> 4.3.2-alt1
- new version

* Mon Aug 31 2009 Sergey V Turchin <zerg@altlinux.org> 4.3.1-alt1
- new version

* Wed Aug 05 2009 Sergey V Turchin <zerg@altlinux.org> 4.3.0-alt1
- 4.3.0

* Fri Jul 24 2009 Sergey V Turchin <zerg@altlinux.org> 4.2.98-alt2
- rebuilt with new exiv2

* Wed Jul 22 2009 Sergey V Turchin <zerg@altlinux.org> 4.2.98-alt1
- 4.2.98

* Thu Jul 16 2009 Sergey V Turchin <zerg@altlinux.org> 4.2.96-alt1
- 4.2.96

* Mon Jun 22 2009 Sergey V Turchin <zerg@altlinux.org> 4.2.4-alt0.M50.1
- built for M50

* Fri Jun 05 2009 Sergey V Turchin <zerg@altlinux.org> 4.2.4-alt1
- new version

* Tue May 05 2009 Sergey V Turchin <zerg@altlinux.org> 4.2.3-alt1
- new version

* Fri Apr 03 2009 Sergey V Turchin <zerg@altlinux.org> 4.2.2-alt1
- new version

* Mon Mar 16 2009 Sergey V Turchin <zerg@altlinux.org> 4.2.1-alt0.M50.1
- built for M50

* Wed Mar 04 2009 Sergey V Turchin <zerg at altlinux dot org> 4.2.1-alt1
- new version

* Wed Jan 28 2009 Sergey V Turchin <zerg at altlinux dot org> 4.2.0-alt1
- new version

* Tue Jan 20 2009 Sergey V Turchin <zerg at altlinux dot org> 4.1.96-alt1
- new version
- remove deprecated macroses from specfile

* Thu Nov 06 2008 Sergey V Turchin <zerg at altlinux dot org> 4.1.3-alt1
- new version
- built okular without msits:/ (.chm) support

* Tue Oct 07 2008 Sergey V Turchin <zerg at altlinux dot org> 4.1.2-alt1
- new version

* Thu Sep 04 2008 Sergey V Turchin <zerg at altlinux dot org> 4.1.1-alt1
- new version

* Sat Aug 02 2008 Sergey V Turchin <zerg at altlinux dot org> 4.1.0-alt1
- new version

* Mon Jun 02 2008 Sergey V Turchin <zerg at altlinux dot org> 4.0.80-alt1
- 4.1 beta1

* Mon May 12 2008 Sergey V Turchin <zerg at altlinux dot org> 4.0.72-alt2
- okular built with libspectre

* Wed May 07 2008 Sergey V Turchin <zerg at altlinux dot org> 4.0.72-alt1
- new version

* Wed Apr 02 2008 Sergey V Turchin <zerg at altlinux dot org> 4.0.3-alt1
- new version

* Fri Mar 21 2008 Sergey V Turchin <zerg at altlinux dot org> 4.0.2-alt1
- initial specfile


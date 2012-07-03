%define _kde_alternate_placement 1
%define ical_req 0.33
%define akonadi_req 1.5

%add_findpackage_path %_kde4_bindir

%define rname kdepimlibs
Name: kde4pimlibs
Version: 4.8.4
Release: alt2

Group: System/Libraries
Summary: K Desktop Environment 4 - PIM Libraries
License: LGPLv2
Url: http://www.kde.org/

Source: %rname-%version.tar
# upstream
# FC
# ALT
Patch10: kdepimlibs-4.3.95-alt-test-akonadi-resources.patch
Patch11: kdepimlibs-4.4.92-alt-no-report-akonadi-old-log.patch
Patch12: kdepimlibs-4.4.2-alt-nepomuk-only-warn.patch

BuildRequires(pre): akonadi-devel kde4libs-devel
BuildRequires: boost-devel bzlib-devel gcc-c++ shared-mime-info xsltproc
BuildRequires: libgpg-error-devel libgpgme-devel libassuan-devel libpth-devel
BuildRequires: libldap-devel libstrigi-devel prison-devel
BuildRequires: libgpgme-devel libsasl2-devel libical-devel >= %ical_req
BuildRequires: libsoprano-devel soprano-backend-redland soprano shared-desktop-ontologies-devel
BuildRequires: akonadi-devel >= %akonadi_req
BuildRequires: kde4libs-devel >= %version

%description
Personal Information Management (PIM) libraries for the
K Desktop Environment 4.

%package devel
Group: Development/KDE and QT
Summary: Header files for %name
Requires: kde-common boost-devel
Requires: kde4libs-devel => %version
Requires: %name = %version-%release

%description devel
Header files for developing applications using %name.

%prep
%setup -q -n %rname-%version
%patch10 -p1
%patch11 -p1
%patch12 -p1

%build
%add_optflags -D_FILE_OFFSET_BITS=64
#    -DKDE4_ENABLE_FINAL:BOOL=ON \
%K4build \
    -DKDE4_ENABLE_FPIE:BOOL=ON

%install
%K4install


%files
%_K4datadir/apps/akonadi-kde/
%_K4libdir/lib*.so.*
#%_K4libdir/libkdeinit4_*.so
%_K4lib/*.so*
%dir %_K4libdir/gpgmepp/
%_K4apps/kabc/
#%_K4apps/libical/
%_K4conf_update/*
%_K4cfg/*
%_K4srv/*
%_K4srvtyp/*
%_K4apps/libkholidays
%_K4apps/akonadi
%_K4xdg_mime/kdepimlibs-mime.xml
%doc %_K4doc/en/*

%files devel
%_K4link/lib*.so
%_K4lib/plugins/designer/*.so
%_K4dbus_interfaces/*
%_K4apps/cmake/modules/*
%_K4libdir/cmake/KdepimLibs*/
%_K4includedir/*
%_K4libdir/gpgmepp/*.cmake


%changelog
* Fri Jun 08 2012 Sergey V Turchin <zerg@altlinux.org> 4.8.4-alt2
- update from 4.8 branch

* Tue Jun 05 2012 Sergey V Turchin <zerg@altlinux.org> 4.8.4-alt1
- new version

* Wed May 30 2012 Sergey V Turchin <zerg@altlinux.org> 4.8.3-alt2.M60P.1
- build for M60P

* Mon May 21 2012 Sergey V Turchin <zerg@altlinux.org> 4.8.3-alt3
- update from 4.8 branch

* Thu May 10 2012 Sergey V Turchin <zerg@altlinux.org> 4.8.3-alt1.M60P.1
- build for M60P

* Sat May 05 2012 Sergey V Turchin <zerg@altlinux.org> 4.8.3-alt2
- update from 4.8 branch

* Wed May 02 2012 Sergey V Turchin <zerg@altlinux.org> 4.8.3-alt1
- new version

* Wed Apr 11 2012 Sergey V Turchin <zerg@altlinux.org> 4.8.2-alt0.M60P.1
- built for M60P

* Tue Apr 10 2012 Sergey V Turchin <zerg@altlinux.org> 4.8.2-alt1
- new version

* Wed Apr 04 2012 Sergey V Turchin <zerg@altlinux.org> 4.8.1-alt1.M60P.1
- built for M60P

* Mon Mar 26 2012 Sergey V Turchin <zerg@altlinux.org> 4.8.1-alt2
- update from 4.8 branch

* Mon Mar 05 2012 Sergey V Turchin <zerg@altlinux.org> 4.8.1-alt1
- new version

* Wed Feb 08 2012 Sergey V Turchin <zerg@altlinux.org> 4.8.0-alt3
- update from 4.8 branch

* Tue Jan 31 2012 Sergey V Turchin <zerg@altlinux.org> 4.8.0-alt2
- update from 4.8 branch

* Wed Jan 18 2012 Sergey V Turchin <zerg@altlinux.org> 4.8.0-alt1
- new version

* Mon Dec 05 2011 Sergey V Turchin <zerg@altlinux.org> 4.7.4-alt0.M60P.1
- build for M60P

* Fri Dec 02 2011 Sergey V Turchin <zerg@altlinux.org> 4.7.4-alt1
- new version

* Sun Nov 27 2011 Sergey V Turchin <zerg@altlinux.org> 4.7.3-alt1.M60P.1
- built for M60P

* Fri Nov 25 2011 Sergey V Turchin <zerg@altlinux.org> 4.7.3-alt2
- update from 4.7 branch

* Thu Nov 03 2011 Sergey V Turchin <zerg@altlinux.org> 4.7.3-alt0.M60P.1
- built for M60P

* Sat Oct 29 2011 Sergey V Turchin <zerg@altlinux.org> 4.7.3-alt1
- new version

* Tue Oct 18 2011 Sergey V Turchin <zerg@altlinux.org> 4.7.2-alt2.M60T.1
- built for M60T

* Mon Oct 17 2011 Sergey V Turchin <zerg@altlinux.org> 4.7.2-alt3
- update from 4.7 branch (ALT#26456)

* Wed Oct 12 2011 Sergey V Turchin <zerg@altlinux.org> 4.7.2-alt2
- built with prison

* Tue Oct 04 2011 Sergey V Turchin <zerg@altlinux.org> 4.7.2-alt1
- new version

* Tue Sep 27 2011 Sergey V Turchin <zerg@altlinux.org> 4.7.1-alt2
- update from 4.7 branch

* Wed Aug 31 2011 Sergey V Turchin <zerg@altlinux.org> 4.7.1-alt1
- new version

* Wed Jul 06 2011 Sergey V Turchin <zerg@altlinux.org> 4.6.5-alt0.M60P.1
- built for M60P

* Fri Jul 01 2011 Sergey V Turchin <zerg@altlinux.org> 4.6.5-alt1
- new version

* Tue Jun 07 2011 Sergey V Turchin <zerg@altlinux.org> 4.6.4-alt0.M60P.1
- built for M60P

* Fri Jun 03 2011 Sergey V Turchin <zerg@altlinux.org> 4.6.4-alt1
- new version

* Wed May 04 2011 Sergey V Turchin <zerg@altlinux.org> 4.6.3-alt1
- new version

* Tue Apr 05 2011 Sergey V Turchin <zerg@altlinux.org> 4.6.2-alt1
- new version

* Mon Feb 28 2011 Sergey V Turchin <zerg@altlinux.org> 4.6.1-alt1
- new version

* Fri Feb 04 2011 Sergey V Turchin <zerg@altlinux.org> 4.6.0-alt2
- add patch from FC to fix memory overlap in kio-imap4

* Thu Jan 27 2011 Sergey V Turchin <zerg@altlinux.org> 4.6.0-alt1
- new version

* Wed Jan 19 2011 Sergey V Turchin <zerg@altlinux.org> 4.5.5-alt1
- new version

* Wed Dec 01 2010 Sergey V Turchin <zerg@altlinux.org> 4.5.4-alt1
- new version

* Mon Nov 01 2010 Sergey V Turchin <zerg@altlinux.org> 4.5.3-alt1
- new version

* Tue Oct 05 2010 Sergey V Turchin <zerg@altlinux.org> 4.5.2-alt1
- new version

* Mon Aug 30 2010 Sergey V Turchin <zerg@altlinux.org> 4.5.1-alt1
- new version

* Tue Aug 03 2010 Sergey V Turchin <zerg@altlinux.org> 4.5.0-alt1
- new version

* Thu Jul 22 2010 Sergey V Turchin <zerg@altlinux.org> 4.4.92-alt1
- new version

* Thu Jul 08 2010 Sergey V Turchin <zerg@altlinux.org> 4.4.5-alt0.M51.1
- built for M51

* Mon Jul 05 2010 Sergey V Turchin <zerg@altlinux.org> 4.4.5-alt1
- new version

* Thu Jun 03 2010 Sergey V Turchin <zerg@altlinux.org> 4.4.4-alt0.M51.1
- built for M51

* Mon May 31 2010 Sergey V Turchin <zerg@altlinux.org> 4.4.4-alt1
- built for M51

* Thu May 13 2010 Sergey V Turchin <zerg@altlinux.org> 4.4.3-alt0.M51.1
- built for M51

* Fri Apr 30 2010 Sergey V Turchin <zerg@altlinux.org> 4.4.3-alt1
- new version

* Wed Apr 21 2010 Sergey V Turchin <zerg@altlinux.org> 4.4.2-alt2.M51.1
- built for M51

* Thu Apr 15 2010 Sergey V Turchin <zerg@altlinux.org> 4.4.2-alt3
- report only warning when nemomuk don't registared in dbus

* Wed Apr 14 2010 Sergey V Turchin <zerg@altlinux.org> 4.4.2-alt2
- don't report when old akonadi server error log found

* Mon Mar 29 2010 Sergey V Turchin <zerg@altlinux.org> 4.4.2-alt1
- new version

* Fri Mar 05 2010 Sergey V Turchin <zerg@altlinux.org> 4.4.1-alt2
- don't report when old akonadi_control error log found

* Mon Mar 01 2010 Sergey V Turchin <zerg@altlinux.org> 4.4.1-alt1
- new version

* Fri Feb 26 2010 Sergey V Turchin <zerg@altlinux.org> 4.4.0-alt2
- add patch to fix attachment names (ALT#21327)

* Wed Feb 10 2010 Sergey V Turchin <zerg@altlinux.org> 4.4.0-alt1
- new version

* Tue Feb 02 2010 Sergey V Turchin <zerg@altlinux.org> 4.3.95-alt2
- fix test akonadi resources at startup

* Thu Jan 28 2010 Sergey V Turchin <zerg@altlinux.org> 4.3.95-alt1
- new version

* Mon Jan 18 2010 Sergey V Turchin <zerg@altlinux.org> 4.3.90-alt1
- new version

* Tue Dec 15 2009 Sergey V Turchin <zerg@altlinux.org> 4.3.4-alt0.M51.1
- built for M51

* Mon Nov 30 2009 Sergey V Turchin <zerg@altlinux.org> 4.3.4-alt1
- new version

* Mon Nov 09 2009 Sergey V Turchin <zerg@altlinux.org> 4.3.3-alt0.M51.1
- built for M51

* Fri Oct 30 2009 Sergey V Turchin <zerg@altlinux.org> 4.3.3-alt1
- new version

* Thu Oct 08 2009 Sergey V Turchin <zerg@altlinux.org> 4.3.2-alt1
- new version

* Mon Aug 31 2009 Sergey V Turchin <zerg@altlinux.org> 4.3.1-alt1
- new version

* Tue Aug 04 2009 Sergey V Turchin <zerg@altlinux.org> 4.3.0-alt1
- 4.3.0

* Wed Jul 22 2009 Sergey V Turchin <zerg@altlinux.org> 4.2.98-alt1
- 4.2.98

* Wed Jul 15 2009 Sergey V Turchin <zerg@altlinux.org> 4.2.96-alt1
- 4.2.96

* Wed Jul 08 2009 Sergey V Turchin <zerg@altlinux.org> 4.2.4-alt4
- fix to compile with new gpgme (ALT#20708)

* Tue Jul 07 2009 Sergey V Turchin <zerg@altlinux.org> 4.2.4-alt3
- fix to add branches/4.2 changes

* Mon Jul 06 2009 Sergey V Turchin <zerg@altlinux.org> 4.2.4-alt2
- update from branches/4.2

* Mon Jun 22 2009 Sergey V Turchin <zerg@altlinux.org> 4.2.4-alt0.M50.1
- built for M50

* Fri Jun 05 2009 Sergey V Turchin <zerg@altlinux.org> 4.2.4-alt1
- new version

* Mon May 04 2009 Sergey V Turchin <zerg@altlinux.org> 4.2.3-alt1
- new version

* Thu Apr 02 2009 Sergey V Turchin <zerg@altlinux.org> 4.2.2-alt1
- new version

* Mon Mar 02 2009 Sergey V Turchin <zerg at altlinux dot org> 4.2.1-alt1
- new version

* Tue Feb 17 2009 Sergey V Turchin <zerg at altlinux dot org> 4.2.0-alt2
- require libical >= 0.33

* Wed Jan 28 2009 Sergey V Turchin <zerg at altlinux dot org> 4.2.0-alt1
- new version

* Wed Jan 14 2009 Sergey V Turchin <zerg at altlinux dot org> 4.1.96-alt1
- new version
- remove deprecated macroses from specfile

* Thu Nov 06 2008 Sergey V Turchin <zerg at altlinux dot org> 4.1.3-alt1
- new version

* Thu Oct 09 2008 Sergey V Turchin <zerg at altlinux dot org> 4.1.2-alt1
- new version

* Mon Sep 01 2008 Sergey V Turchin <zerg at altlinux dot org> 4.1.1-alt1
- new version

* Wed Jul 30 2008 Sergey V Turchin <zerg at altlinux dot org> 4.1.0-alt1
- new version

* Tue May 27 2008 Sergey V Turchin <zerg at altlinux dot org> 4.0.80-alt1
- 4.1 beta1

* Tue May 06 2008 Sergey V Turchin <zerg at altlinux dot org> 4.0.72-alt1
- new version

* Sun May 04 2008 Sergey V Turchin <zerg at altlinux dot org> 4.0.71-alt1
- new version

* Tue Apr 01 2008 Sergey V Turchin <zerg at altlinux dot org> 4.0.3-alt1
- new version

* Thu Mar 06 2008 Sergey V Turchin <zerg at altlinux dot org> 4.0.2-alt1
- new version

* Fri Feb 15 2008 Sergey V Turchin <zerg at altlinux dot org> 4.0.1-alt1
- built for ALT


%define _kde_alternate_placement 1
%define ical_req 0.33
%define akonadi_req 1.12.90

%add_findpackage_path %_kde4_bindir

%define rname kdepimlibs
Name: kde4pimlibs
Version: 4.14.11
Release: alt7

Group: System/Libraries
Summary: K Desktop Environment 4 - PIM Libraries
License: LGPLv2
Url: http://www.kde.org/

# until KDE-4.11
Requires: libakonadi4-calendar libakonadi4-contact libakonadi4-kabc libakonadi4-kcal libakonadi4-kmime
Requires: libakonadi4-notes libgpgmexx4-pthread libgpgmexx4 libkalarmcal4 libkblog4 libkcalcore4
Requires: libkcalutils4 libkholidays4 libkmbox4 libkontactinterface4 libkpimidentities4 libkpimtextedit4
Requires: libktnef4 libkxmlrpcclient4 libmicroblog4 libqgpgme4 libsyndication4
# end until KDE-4.11

Source: %rname-%version.tar
# upstream
# FC
# ALT
Patch10: kdepimlibs-4.14.0-alt-test-akonadi-resources.patch
Patch11: kdepimlibs-4.14.0-alt-warn-akonadi-old-log.patch
Patch12: kdepimlibs-4.4.2-alt-nepomuk-only-warn.patch

BuildRequires(pre): akonadi-devel kde4libs-devel
BuildRequires: boost-devel bzlib-devel gcc-c++ shared-mime-info xsltproc libxslt-devel
BuildRequires: libgpg-error-devel libgpgme-devel libassuan-devel libpth-devel libicu-devel
BuildRequires: libldap-devel libstrigi-devel prison-devel qjson-devel
BuildRequires: libgpgme-devel libsasl2-devel libical-devel >= %ical_req
#BuildRequires: libsoprano-devel soprano-backend-redland soprano shared-desktop-ontologies-devel
BuildRequires: akonadi-devel >= %akonadi_req
BuildRequires: kde4libs-devel >= %version

%description
Personal Information Management (PIM) libraries for the
K Desktop Environment 4.

%package common
Summary: %name common package
Group: System/Configuration/Other
BuildArch: noarch
Requires: kde-common
Conflicts: kde4pimlibs < 4.12
%description common
%name common package

%package devel
Group: Development/KDE and QT
Summary: Header files for %name
Requires: boost-devel libgpgme-devel
Requires: kde4libs-devel => %version
Requires: %name-common = %version-%release
Requires: %name = %version-%release
%description devel
Header files for developing applications using %name.

%package -n libakonadi4-xml
Summary: %name libraries
Group: System/Libraries
Requires: %name-common = %version-%release
%description -n libakonadi4-xml
%name library

%package -n libakonadi4-calendar
Summary: %name libraries
Group: System/Libraries
Requires: %name-common = %version-%release
%description -n libakonadi4-calendar
%name library

%package -n libakonadi4-contact
Summary: %name libraries
Group: System/Libraries
Requires: %name-common = %version-%release
%description -n libakonadi4-contact
%name library

%package -n libakonadi4-kabc
Summary: %name libraries
Group: System/Libraries
Requires: %name-common = %version-%release
%description -n libakonadi4-kabc
%name library

%package -n libakonadi4-kcal
Summary: %name libraries
Group: System/Libraries
Requires: %name-common = %version-%release
%description -n libakonadi4-kcal
%name library

%package -n libakonadi4-kde
Summary: %name libraries
Group: System/Libraries
Requires: %name-common = %version-%release
%description -n libakonadi4-kde
%name library

%package -n libakonadi4-kmime
Summary: %name libraries
Group: System/Libraries
Requires: %name-common = %version-%release
%description -n libakonadi4-kmime
%name library

%package -n libakonadi4-notes
Summary: %name libraries
Group: System/Libraries
Requires: %name-common = %version-%release
%description -n libakonadi4-notes
%name library

%package -n libakonadi4-socialutils
Summary: %name libraries
Group: System/Libraries
Requires: %name-common = %version-%release
%description -n libakonadi4-socialutils
%name library

%package -n libgpgmexx4-pthread
Summary: %name libraries
Group: System/Libraries
Requires: %name-common = %version-%release
%description -n libgpgmexx4-pthread
%name library

%package -n libgpgmexx4
Summary: %name libraries
Group: System/Libraries
Requires: %name-common = %version-%release
%description -n libgpgmexx4
%name library

%package -n libkabc4
Summary: %name libraries
Group: System/Libraries
Requires: %name-common = %version-%release
%description -n libkabc4
%name library

%package -n libkabc4_file_core
Summary: %name libraries
Group: System/Libraries
Requires: %name-common = %version-%release
%description -n libkabc4_file_core
%name library

%package -n libkalarmcal4
Summary: %name libraries
Group: System/Libraries
Requires: %name-common = %version-%release
%description -n libkalarmcal4
%name library

%package -n libkblog4
Summary: %name libraries
Group: System/Libraries
Requires: %name-common = %version-%release
%description -n libkblog4
%name library

%package -n libkcal4
Summary: %name libraries
Group: System/Libraries
Requires: %name-common = %version-%release
%description -n libkcal4
%name library

%package -n libkcalcore4
Summary: %name libraries
Group: System/Libraries
Requires: %name-common = %version-%release
%description -n libkcalcore4
%name library

%package -n libkcalutils4
Summary: %name libraries
Group: System/Libraries
Requires: %name-common = %version-%release
%description -n libkcalutils4
%name library

%package -n libkholidays4
Summary: %name libraries
Group: System/Libraries
Requires: %name-common = %version-%release
%description -n libkholidays4
%name library

%package -n libkimap4
Summary: %name libraries
Group: System/Libraries
Requires: %name-common = %version-%release
%description -n libkimap4
%name library

%package -n libkldap4
Summary: %name libraries
Group: System/Libraries
Requires: %name-common = %version-%release
%description -n libkldap4
%name library

%package -n libkmbox4
Summary: %name libraries
Group: System/Libraries
Requires: %name-common = %version-%release
%description -n libkmbox4
%name library

%package -n libkmime4
Summary: %name libraries
Group: System/Libraries
Requires: %name-common = %version-%release
%description -n libkmime4
%name library

%package -n libkontactinterface4
Summary: %name libraries
Group: System/Libraries
Requires: %name-common = %version-%release
%description -n libkontactinterface4
%name library

%package -n libkpimidentities4
Summary: %name libraries
Group: System/Libraries
Requires: %name-common = %version-%release
%description -n libkpimidentities4
%name library

%package -n libkpimtextedit4
Summary: %name libraries
Group: System/Libraries
Requires: %name-common = %version-%release
%description -n libkpimtextedit4
%name library

%package -n libkpimutils4
Summary: %name libraries
Group: System/Libraries
Requires: %name-common = %version-%release
%description -n libkpimutils4
%name library

%package -n libkresources4
Summary: %name libraries
Group: System/Libraries
Requires: %name-common = %version-%release
%description -n libkresources4
%name library

%package -n libktnef4
Summary: %name libraries
Group: System/Libraries
Requires: %name-common = %version-%release
%description -n libktnef4
%name library

%package -n libkxmlrpcclient4
Summary: %name libraries
Group: System/Libraries
Requires: %name-common = %version-%release
%description -n libkxmlrpcclient4
%name library

%package -n libmailtransport4
Summary: %name libraries
Group: System/Libraries
Requires: %name-common = %version-%release
%description -n libmailtransport4
%name library

%package -n libmicroblog4
Summary: %name libraries
Group: System/Libraries
Requires: %name-common = %version-%release
%description -n libmicroblog4
%name library

%package -n libqgpgme4
Summary: %name libraries
Group: System/Libraries
Requires: %name-common = %version-%release
%description -n libqgpgme4
%name library

%package -n libsyndication4
Summary: %name libraries
Group: System/Libraries
Requires: %name-common = %version-%release
%description -n libsyndication4
%name library

%prep
%setup -q -n %rname-%version
%patch10 -p1
%patch11 -p1
#%patch12 -p1

%build
%add_optflags -D_FILE_OFFSET_BITS=64
#    -DKDE4_ENABLE_FINAL:BOOL=ON \
%K4build \
    -DKDE4_BUILD_TESTS=OFF \
    -DKDE4_ENABLE_FPIE:BOOL=ON \
    #

%install
%K4install
mkdir -p %buildroot/%_datadir/akonadi/agents/

%files common

%files
%_kde4_bindir/akonadi*
%_K4apps/akonadi-kde/
%_K4lib/*.so
%dir %_K4libdir/gpgmepp/
%_K4apps/kabc/
%_K4conf_update/*
%_K4cfg/*
%_K4srv/*
%_K4srvtyp/*
%_K4apps/libkholidays/
%_K4apps/akonadi/
%_K4apps/akonadi_knut_resource/
%_K4xdg_mime/kdepimlibs-mime.xml
%_K4xdg_mime/x-vnd.akonadi.socialfeeditem.xml
%_datadir/akonadi/
%doc %_K4doc/en/*

%files devel
%_K4link/lib*.so
%_K4lib/plugins/designer/*.so
%_K4dbus_interfaces/*
%_K4apps/cmake/modules/*
%_K4libdir/cmake/KdepimLibs*/
%_K4includedir/*
%_K4libdir/gpgmepp/*.cmake

%files -n libakonadi4-xml
%_K4libdir/libakonadi-xml.so.*
%files -n libakonadi4-calendar
%_K4libdir/libakonadi-calendar.so.*
%files -n libakonadi4-contact
%_K4libdir/libakonadi-contact.so.*
%files -n libakonadi4-kabc
%_K4libdir/libakonadi-kabc.so.*
%files -n libakonadi4-kcal
%_K4libdir/libakonadi-kcal.so.*
%files -n libakonadi4-kde
%_K4libdir/libakonadi-kde.so.*
%files -n libakonadi4-kmime
%_K4libdir/libakonadi-kmime.so.*
%files -n libakonadi4-notes
%_K4libdir/libakonadi-notes.so.*
%files -n libakonadi4-socialutils
%_K4libdir/libakonadi-socialutils.so.*
%files -n libgpgmexx4-pthread
%_K4libdir/libgpgme++-pthread.so.*
%files -n libgpgmexx4
%_K4libdir/libgpgme++.so.*
%files -n libkabc4
%_K4libdir/libkabc.so.*
%files -n libkabc4_file_core
%_K4libdir/libkabc_file_core.so.*
%files -n libkalarmcal4
%_K4libdir/libkalarmcal.so.*
%files -n libkblog4
%_K4libdir/libkblog.so.*
%files -n libkcal4
%_K4libdir/libkcal.so.*
%files -n libkcalcore4
%_K4libdir/libkcalcore.so.*
%files -n libkcalutils4
%_K4libdir/libkcalutils.so.*
%files -n libkholidays4
%_K4libdir/libkholidays.so.*
%files -n libkimap4
%_K4libdir/libkimap.so.*
%files -n libkldap4
%_K4libdir/libkldap.so.*
%files -n libkmbox4
%_K4libdir/libkmbox.so.*
%files -n libkmime4
%_K4libdir/libkmime.so.*
%files -n libkontactinterface4
%_K4libdir/libkontactinterface.so.*
%files -n libkpimidentities4
%_K4libdir/libkpimidentities.so.*
%files -n libkpimtextedit4
%_K4libdir/libkpimtextedit.so.*
%files -n libkpimutils4
%_K4libdir/libkpimutils.so.*
%files -n libkresources4
%_K4libdir/libkresources.so.*
%files -n libktnef4
%_K4libdir/libktnef.so.*
%files -n libkxmlrpcclient4
%_K4libdir/libkxmlrpcclient.so.*
%files -n libmailtransport4
%_K4libdir/libmailtransport.so.*
%files -n libmicroblog4
%_K4libdir/libmicroblog.so.*
%files -n libqgpgme4
%_K4libdir/libqgpgme.so.*
%files -n libsyndication4
%_K4libdir/libsyndication.so.*

%changelog
* Wed Feb 24 2016 Sergey V Turchin <zerg@altlinux.org> 4.14.11-alt7
- update from 4.14 branch

* Mon Jan 25 2016 Sergey V Turchin <zerg@altlinux.org> 4.14.11-alt6
- update build requires

* Mon Jan 18 2016 Sergey V Turchin <zerg@altlinux.org> 4.14.11-alt5
- update from 4.14 branch

* Mon Oct 19 2015 Sergey V Turchin <zerg@altlinux.org> 4.14.11-alt4
- update from 4.14 branch

* Mon Sep 28 2015 Sergey V Turchin <zerg@altlinux.org> 4.14.11-alt3
- update from 4.14 branch

* Fri Sep 11 2015 Sergey V Turchin <zerg@altlinux.org> 4.14.11-alt2
- update from 4.14 branch

* Fri Aug 28 2015 Sergey V Turchin <zerg@altlinux.org> 4.14.11-alt1
- new version

* Wed Jul 15 2015 Sergey V Turchin <zerg@altlinux.org> 4.14.10-alt1
- new version

* Mon Jun 08 2015 Sergey V Turchin <zerg@altlinux.org> 4.14.9-alt1
- new version

* Thu May 14 2015 Sergey V Turchin <zerg@altlinux.org> 4.14.8-alt1
- new version

* Tue Apr 21 2015 Sergey V Turchin <zerg@altlinux.org> 4.14.7-alt1
- new version

* Wed Mar 11 2015 Sergey V Turchin <zerg@altlinux.org> 4.14.6-alt1
- new version

* Thu Feb 05 2015 Sergey V Turchin <zerg@altlinux.org> 4.14.5-alt1
- new version

* Mon Jan 26 2015 Sergey V Turchin <zerg@altlinux.org> 4.14.4-alt1
- new version

* Thu Nov 13 2014 Sergey V Turchin <zerg@altlinux.org> 4.14.3-alt1
- new version

* Mon Oct 13 2014 Sergey V Turchin <zerg@altlinux.org> 4.14.2-alt1
- new version

* Wed Sep 17 2014 Sergey V Turchin <zerg@altlinux.org> 4.14.1-alt1
- new version

* Tue Aug 12 2014 Sergey V Turchin <zerg@altlinux.org> 4.14.0-alt1
- new version

* Mon Jul 14 2014 Sergey V Turchin <zerg@altlinux.org> 4.13.3-alt1
- new version

* Tue Jun 17 2014 Sergey V Turchin <zerg@altlinux.org> 4.13.2-alt1
- new version

* Mon May 12 2014 Sergey V Turchin <zerg@altlinux.org> 4.13.1-alt1
- new version

* Thu Apr 17 2014 Sergey V Turchin <zerg@altlinux.org> 4.13.0-alt1
- new version

* Mon Mar 31 2014 Sergey V Turchin <zerg@altlinux.org> 4.12.4-alt0.M70P.1
- built for M70P

* Fri Mar 28 2014 Sergey V Turchin <zerg@altlinux.org> 4.12.4-alt1
- new version

* Thu Mar 13 2014 Sergey V Turchin <zerg@altlinux.org> 4.12.3-alt0.M70P.1
- built for M70P

* Wed Mar 05 2014 Sergey V Turchin <zerg@altlinux.org> 4.12.3-alt1
- new version

* Thu Feb 13 2014 Sergey V Turchin <zerg@altlinux.org> 4.12.2-alt2
- fix requires

* Thu Jan 30 2014 Sergey V Turchin <zerg@altlinux.org> 4.12.2-alt1
- new version

* Sat Jan 11 2014 Sergey V Turchin <zerg@altlinux.org> 4.11.5-alt0.M70P.1
- built for M70P

* Thu Jan 09 2014 Sergey V Turchin <zerg@altlinux.org> 4.11.5-alt1
- new version

* Wed Dec 18 2013 Sergey V Turchin <zerg@altlinux.org> 4.11.4-alt1.M70P.1
- built for M70P

* Wed Dec 18 2013 Sergey V Turchin <zerg@altlinux.org> 4.11.4-alt2
- update from 4.11 branch

* Wed Dec 04 2013 Sergey V Turchin <zerg@altlinux.org> 4.11.4-alt0.M70P.1
- built for M70P

* Wed Dec 04 2013 Sergey V Turchin <zerg@altlinux.org> 4.11.4-alt1
- new version

* Wed Nov 20 2013 Sergey V Turchin <zerg@altlinux.org> 4.11.3-alt3
- rebuilt with fixed libical

* Tue Nov 19 2013 Sergey V Turchin <zerg@altlinux.org> 4.11.3-alt2
- rebuilt with new libical

* Thu Nov 07 2013 Sergey V Turchin <zerg@altlinux.org> 4.11.3-alt0.M70P.1
- built for M70P

* Wed Nov 06 2013 Sergey V Turchin <zerg@altlinux.org> 4.11.3-alt1
- new version

* Fri Oct 04 2013 Sergey V Turchin <zerg@altlinux.org> 4.11.2-alt0.M70P.1
- built for M70P

* Wed Oct 02 2013 Sergey V Turchin <zerg@altlinux.org> 4.11.2-alt1
- new version

* Tue Sep 03 2013 Sergey V Turchin <zerg@altlinux.org> 4.11.1-alt1
- new version

* Mon Jul 01 2013 Sergey V Turchin <zerg@altlinux.org> 4.10.5-alt1
- new version

* Mon Jun 03 2013 Sergey V Turchin <zerg@altlinux.org> 4.10.4-alt1
- new version

* Tue May 07 2013 Sergey V Turchin <zerg@altlinux.org> 4.10.3-alt1
- new version

* Wed Apr 03 2013 Sergey V Turchin <zerg@altlinux.org> 4.10.2-alt1
- new version

* Tue Mar 05 2013 Sergey V Turchin <zerg@altlinux.org> 4.10.1-alt1
- new version

* Mon Feb 25 2013 Sergey V Turchin <zerg@altlinux.org> 4.10.0-alt3
- update from 4.10 branch

* Fri Feb 01 2013 Sergey V Turchin <zerg@altlinux.org> 4.10.0-alt2
- update from 4.10 branch

* Thu Jan 31 2013 Sergey V Turchin <zerg@altlinux.org> 4.10.0-alt1
- update from 4.10 branch

* Tue Jan 29 2013 Sergey V Turchin <zerg@altlinux.org> 4.10.0-alt0.6
- update from 4.10 branch

* Thu Jan 24 2013 Sergey V Turchin <zerg@altlinux.org> 4.10.0-alt0.5
- update from 4.10 branch

* Fri Jan 11 2013 Sergey V Turchin <zerg@altlinux.org> 4.10.0-alt0.4
- update from 4.10 branch

* Thu Jan 10 2013 Sergey V Turchin <zerg@altlinux.org> 4.10.0-alt0.3
- update from 4.10 branch

* Thu Dec 20 2012 Sergey V Turchin <zerg@altlinux.org> 4.10.0-alt0.2
- update from 4.10 branch

* Fri Dec 07 2012 Sergey V Turchin <zerg@altlinux.org> 4.10.0-alt0.1
- new beta version

* Wed Dec 05 2012 Sergey V Turchin <zerg@altlinux.org> 4.9.4-alt1
- new version

* Wed Dec 05 2012 Sergey V Turchin <zerg@altlinux.org> 4.9.3-alt3
- rebuilt with new gpgme

* Thu Nov 22 2012 Sergey V Turchin <zerg@altlinux.org> 4.9.3-alt2
- update code from KDE/4.9 branch

* Wed Nov 07 2012 Sergey V Turchin <zerg@altlinux.org> 4.9.3-alt1
- new version

* Fri Oct 12 2012 Sergey V Turchin <zerg@altlinux.org> 4.9.2-alt1
- new version

* Mon Oct 01 2012 Sergey V Turchin <zerg@altlinux.org> 4.9.1-alt1
- new version

* Mon Sep 24 2012 Sergey V Turchin <zerg@altlinux.org> 4.9.0-alt1
- new version

* Thu Aug 02 2012 Sergey V Turchin <zerg@altlinux.org> 4.8.5-alt0.M60P.1
- built for M60P

* Wed Aug 01 2012 Sergey V Turchin <zerg@altlinux.org> 4.8.5-alt1
- new version

* Mon Jun 18 2012 Sergey V Turchin <zerg@altlinux.org> 4.8.4-alt0.M60P.1
- built for M60P

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



Name: akonadi
Version: 1.13.1
Release: alt0.3

Group: Databases
Summary: An extensible cross-desktop storage service for PIM
Url: http://pim.kde.org/akonadi/
License: LGPLv2+

Requires: %name-database tar bzip2

Source: %name-%version.tar
Source10: mysql_install_db
# RH
Patch10: akonadi-1.7.0-mysql_conf.patch
# ALT
Patch101: akonadi-1.1.1-alt-alt-kdebindir.patch
Patch102: akonadi-1.3.81-alt-mysql-paths.patch
Patch103: akonadi-1.11.0-alt-pluginsdir.patch
#
Patch105: akonadi-1.11.0-alt-start-mysqlcheck.patch
Patch106: akonadi-1.6.2-alt-own-mysql_install_db.patch
Patch107: akonadi-1.6.2-alt-check-nepomuk.patch

BuildRequires(pre): libqt4-devel
BuildRequires: gcc-c++ automoc
BuildRequires: libqt4-devel >= 4.4 kde-common-devel >= 4
BuildRequires: shared-mime-info >=  0.20
BuildRequires: pkg-config cmake xsltproc xml-utils
BuildRequires: boost-devel boost-program_options-devel libsqlite3-devel

%description
An extensible cross-desktop storage service for PIM data and meta data providing
concurrent read, write, and query access.


%package common
Summary: %name common mime and dbus calls
Group: System/Libraries
%description common
%name common mime and dbus calls.

%package -n libqt4-sql-sqlite3
Summary: SQLite3 driver for Qt4 SQL classes
Group: System/Libraries
Requires: qt4-common
Provides: libqt4-plugin-sql = 4.7
%description -n libqt4-sql-sqlite3
SQLite3 driver for Qt's SQL classes (QSQLITE3)

%package database-1-sqlite
Group: Databases
Summary: %name Qt sqlite database
BuildArch: noarch
Requires: %name-common = %EVR
Requires: libqt4-sql-sqlite
Provides: %name-database = %EVR
Provides: %name-database-sqlite = %EVR
Provides: akonadi-database0 = %EVR
Obsoletes: akonadi-database0 < %EVR
%description database-1-sqlite
%name Qt sqlite database

%package database-3-sqlite3
Group: Databases
Summary: %name sqlite database
BuildArch: noarch
Requires: %name-common = %EVR
Requires: libqt4-sql-sqlite3
Provides: %name-database = %EVR
Provides: %name-database-sqlite3 = %EVR
Provides: akonadi-database1 = %EVR
Obsoletes: akonadi-database1 < %EVR
%description database-3-sqlite3
%name sqlite database

%package database-5-postgresql
Group: Databases
Summary: %name postgresql database
BuildArch: noarch
Requires: %name-common = %EVR
Requires: libqt4-sql-postgresql postgresql /usr/bin/pg_dump /usr/bin/pg_restore
Provides: %name-database = %EVR
Provides: %name-database-postgresql = %EVR
Provides: akonadi-database2 = %EVR
Obsoletes: akonadi-database2 < %EVR
%description database-5-postgresql
%name postgresql database

%package database-8-mysql
Group: Databases
Summary: %name mysql database
BuildArch: noarch
Requires: %name-common = %EVR
Requires: libqt4-sql-mysql mariadb-server mariadb-client
Provides: %name-database = %EVR
Provides: %name-database-mysql = %EVR
Provides: akonadi-database3 = %EVR
Obsoletes: akonadi-database3 < %EVR
Provides: akonadi-database-7-mysql = %EVR
Obsoletes: akonadi-database-7-mysql < %EVR
%description database-8-mysql
%name mysql database

%package -n libakonadiprotocolinternals
Group: System/Libraries
Summary: %name library
Requires: %name-common = %EVR
%description -n libakonadiprotocolinternals
%name library

%package -n libakonadiprivate
Group: System/Libraries
Summary: %name library
Requires: %name-common = %EVR
%description -n libakonadiprivate
%name library

%package devel
Group: Development/KDE and QT
Summary: Development files for %name
Requires: libqt4-devel libxml2-devel dbus
Conflicts: kde4pimlibs-devel < 4.0.70
Conflicts: kde4pim-devel < 4.0.70
%description devel
Development files for %name


%prep
%setup -q
#
%patch10 -p1
#
%patch101 -p1
%patch102 -p1
%patch103 -p1
#
%patch105 -p1
%patch106 -p1
%patch107 -p1

%build
#export PATH=%_libdir/kde4bin:$PATH
export CMAKE_LIBRARY_PATH=%_libdir
%Kcmake \
    -DQT5_BUILD=OFF \
    -DAKONADI_BUILD_TESTS=OFF \
    -DBIN_INSTALL_DIR2=%_kde4_bindir \
    -DCONFIG_INSTALL_DIR=%_sysconfdir \
    -DINCLUDE_INSTALL_DIR=%_includedir \
    -DMYSQLD_EXECUTABLE:FILEPATH=%_sbindir/mysqld \
    -DINSTALL_QSQLITE_IN_QT_PREFIX=ON \
    -DWITH_SOPRANO=FALSE \
    #
%Kmake


%install
%Kinstall
mkdir -p %buildroot/%_libdir/akonadi/contact/editorpageplugins/
install -m 0755 %SOURCE10 %buildroot/%_bindir/akonadi_mysql_install_db

%files common
%_K4xdg_mime/akonadi-mime.xml
%dir %_sysconfdir/akonadi/
%dir %_libdir/akonadi/
%dir %_libdir/akonadi/*/
%dir %_libdir/akonadi/*/*/

%files
%_bindir/akonadi_rds
%_bindir/akonadi_control
%_bindir/akonadictl
%_bindir/akonadiserver
%_bindir/akonadi_agent_launcher
%_bindir/akonadi_agent_server
%config(noreplace) %_sysconfdir/akonadi/*
%_K4dbus_services/org.freedesktop.Akonadi.Control.service

%files -n libqt4-sql-sqlite3
%_qt4dir/plugins/sqldrivers/libqsqlite3.so

%files database-1-sqlite
%files database-3-sqlite3
%files database-5-postgresql
%files database-8-mysql
%_bindir/akonadi_mysql_install_db

#%files -n libakonadiprivate
#%_libdir/libakonadiprivate.so.*

%files -n libakonadiprotocolinternals
%_libdir/libakonadiprotocolinternals.so.*

%files devel
%_K4dbus_interfaces/*.xml
%_includedir/*
%_libdir/cmake/Akonadi/
%_libdir/*.so
%_libdir/pkgconfig/*

%changelog
* Wed Feb 24 2016 Sergey V Turchin <zerg@altlinux.org> 1.13.1-alt0.3
- fix requires

* Thu Feb 18 2016 Sergey V Turchin <zerg@altlinux.org> 1.13.1-alt0.2
- fix package dbus service file

* Thu Sep 10 2015 Sergey V Turchin <zerg@altlinux.org> 1.13.1-alt0.1
- update from 1.13 branch

* Thu Jun 18 2015 Sergey V Turchin <zerg@altlinux.org> 1.13.0-alt3
- add upstream fixes

* Fri Jan 23 2015 Sergey V Turchin <zerg@altlinux.org> 1.13.0-alt2
- rebuild with new boost

* Tue Aug 19 2014 Sergey V Turchin <zerg@altlinux.org> 1.13.0-alt1
- new version

* Tue Aug 12 2014 Sergey V Turchin <zerg@altlinux.org> 1.12.91-alt1
- new version

* Mon May 12 2014 Sergey V Turchin <zerg@altlinux.org> 1.12.1-alt2
- update from 1.12 branch

* Thu Apr 17 2014 Sergey V Turchin <zerg@altlinux.org> 1.12.1-alt1
- new version

* Wed Mar 26 2014 Sergey V Turchin <zerg@altlinux.org> 1.12.0-alt0.M70P.1
- built for M70P

* Wed Mar 26 2014 Sergey V Turchin <zerg@altlinux.org> 1.12.0-alt1
- new version

* Thu Jan 30 2014 Sergey V Turchin <zerg@altlinux.org> 1.11.0-alt4.M70P.1
- built for M70P

* Fri Jan 24 2014 Sergey V Turchin <zerg@altlinux.org> 1.11.0-alt5
- update from 1.11 branch

* Sun Dec 22 2013 Sergey V Turchin <zerg@altlinux.org> 1.11.0-alt3.M70P.1
- built for M70P

* Sun Dec 22 2013 Sergey V Turchin <zerg@altlinux.org> 1.11.0-alt4
- fix find plugins

* Wed Dec 18 2013 Sergey V Turchin <zerg@altlinux.org> 1.11.0-alt2.M70P.1
- built for M70P

* Wed Dec 18 2013 Sergey V Turchin <zerg@altlinux.org> 1.11.0-alt3
- update from 1.11 branch

* Fri Dec 06 2013 Sergey V Turchin <zerg@altlinux.org> 1.11.0-alt1.M70P.1
- built for M70P

* Fri Dec 06 2013 Sergey V Turchin <zerg@altlinux.org> 1.11.0-alt2
- don't start mysqlcheck detached only first time
- update from 1.11 branch

* Wed Dec 04 2013 Sergey V Turchin <zerg@altlinux.org> 1.11.0-alt0.M70P.1
- built for M70P

* Wed Dec 04 2013 Sergey V Turchin <zerg@altlinux.org> 1.11.0-alt1
- new version
- don't start mysqlcheck detached

* Thu Oct 17 2013 Sergey V Turchin <zerg at altlinux dot org> 1.10.3-alt1.M70P.1
- built for M70P

* Thu Oct 17 2013 Sergey V Turchin <zerg at altlinux dot org> 1.10.3-alt2
- require mariadb directly

* Wed Oct 09 2013 Sergey V Turchin <zerg@altlinux.org> 1.10.3-alt0.M70P.1
- built for M70P

* Mon Oct 07 2013 Sergey V Turchin <zerg@altlinux.org> 1.10.3-alt1
- new version

* Mon Sep 23 2013 Sergey V Turchin <zerg@altlinux.org> 1.10.2-alt2
- fix requires to mysql-server and mysql-client

* Mon Jul 29 2013 Sergey V Turchin <zerg@altlinux.org> 1.10.2-alt1
- new version

* Wed Jul 24 2013 Sergey V Turchin <zerg@altlinux.org> 1.10.1-alt1
- new version

* Thu Jul 11 2013 Sergey V Turchin <zerg at altlinux dot org> 1.10.0-alt2
- fix requires

* Wed Jul 10 2013 Sergey V Turchin <zerg@altlinux.org> 1.10.0-alt1
- new version

* Tue May 07 2013 Sergey V Turchin <zerg@altlinux.org> 1.9.2-alt1
- new version

* Wed Mar 13 2013 Sergey V Turchin <zerg@altlinux.org> 1.9.1-alt3
- update provides for database subpackages

* Tue Mar 12 2013 Sergey V Turchin <zerg@altlinux.org> 1.9.1-alt2
- rename database subpackages

* Tue Mar 05 2013 Sergey V Turchin <zerg@altlinux.org> 1.9.1-alt1
- new version

* Mon Feb 11 2013 Sergey V Turchin <zerg@altlinux.org> 1.9.0-alt2
- rebuilt with new boost

* Thu Jan 10 2013 Sergey V Turchin <zerg@altlinux.org> 1.9.0-alt1
- new version

* Fri Dec 07 2012 Sergey V Turchin <zerg@altlinux.org> 1.8.80-alt1
- new beta version

* Wed Nov 28 2012 Sergey V Turchin <zerg@altlinux.org> 1.8.1-alt2
- rebuilt with new boost

* Mon Oct 15 2012 Sergey V Turchin <zerg@altlinux.org> 1.8.1-alt1
- new version

* Tue Sep 25 2012 Sergey V Turchin <zerg@altlinux.org> 1.8.0-alt2
- rebuilt with new boost

* Mon Aug 06 2012 Sergey V Turchin <zerg@altlinux.org> 1.8.0-alt1
- new version

* Wed Apr 04 2012 Sergey V Turchin <zerg@altlinux.org> 1.7.2-alt0.M60P.1
- built for M60P

* Wed Apr 04 2012 Sergey V Turchin <zerg@altlinux.org> 1.7.2-alt1
- new version

* Tue Mar 13 2012 Sergey V Turchin <zerg@altlinux.org> 1.7.1-alt1
- new version

* Fri Mar 02 2012 Sergey V Turchin <zerg@altlinux.org> 1.7.0-alt2
- update code from 1.7 branch

* Thu Jan 26 2012 Sergey V Turchin <zerg@altlinux.org> 1.7.0-alt1
- new version

* Fri Dec 02 2011 Sergey V Turchin <zerg@altlinux.org> 1.6.2-alt9
- rebuilt with new boost

* Mon Nov 21 2011 Sergey V Turchin <zerg@altlinux.org> 1.6.2-alt7.M60P.1
- built for M60P

* Mon Nov 21 2011 Sergey V Turchin <zerg@altlinux.org> 1.6.2-alt8
- don't start nepomuk agents if nepomukserver is off

* Wed Nov 02 2011 Sergey V Turchin <zerg@altlinux.org> 1.6.2-alt6.M60P.1
- built for M60P

* Wed Nov 02 2011 Sergey V Turchin <zerg@altlinux.org> 1.6.2-alt7
- using own mysql_install_db (ALT#26541)

* Tue Nov 01 2011 Sergey V Turchin <zerg@altlinux.org> 1.6.2-alt5.M60P.1
- built for M60P

* Tue Nov 01 2011 Sergey V Turchin <zerg@altlinux.org> 1.6.2-alt6
- fix startup mysqlcheck and mysql_upgrade

* Mon Oct 31 2011 Sergey V Turchin <zerg@altlinux.org> 1.6.2-alt4.M60P.1
- built for M60P

* Mon Oct 31 2011 Sergey V Turchin <zerg@altlinux.org> 1.6.2-alt5
- start mysql_upgrade after connection

* Thu Oct 20 2011 Sergey V Turchin <zerg@altlinux.org> 1.6.2-alt3.M60T.1
- built for M60T

* Thu Oct 20 2011 Sergey V Turchin <zerg@altlinux.org> 1.6.2-alt3.M60P.1
- built for M60P

* Thu Oct 20 2011 Sergey V Turchin <zerg@altlinux.org> 1.6.2-alt4
- start mysqlcheck detached

* Thu Oct 13 2011 Sergey V Turchin <zerg@altlinux.org> 1.6.2-alt2.M60P.1
- built for M60P

* Thu Oct 13 2011 Sergey V Turchin <zerg@altlinux.org> 1.6.2-alt3
- fix requires

* Fri Oct 07 2011 Sergey V Turchin <zerg@altlinux.org> 1.6.2-alt1.M60P.1
- built for M60P

* Fri Oct 07 2011 Sergey V Turchin <zerg@altlinux.org> 1.6.2-alt2
- add database0 subpackage with native qt sqlite driver dependency

* Thu Oct 06 2011 Sergey V Turchin <zerg@altlinux.org> 1.6.2-alt0.M60P.1
- built for M60P

* Thu Oct 06 2011 Sergey V Turchin <zerg@altlinux.org> 1.6.2-alt1
- new version

* Thu Oct 06 2011 Sergey V Turchin <zerg@altlinux.org> 1.6.1-alt1
- new version

* Tue Sep 20 2011 Sergey V Turchin <zerg@altlinux.org> 1.6.1-alt0.M60P.1
- built for M60P

* Tue Sep 20 2011 Sergey V Turchin <zerg@altlinux.org> 1.6.1-alt1
- new version

* Fri Aug 05 2011 Sergey V Turchin <zerg@altlinux.org> 1.6.0-alt0.M60P.1
- built for M60P

* Fri Jul 15 2011 Sergey V Turchin <zerg@altlinux.org> 1.6.0-alt1
- new version

* Tue May 10 2011 Sergey V Turchin <zerg@altlinux.org> 1.5.3-alt1
- new version

* Fri Apr 08 2011 Sergey V Turchin <zerg@altlinux.org> 1.5.2-alt1
- new version

* Thu Mar 24 2011 Sergey V Turchin <zerg@altlinux.org> 1.5.1-alt2
- rebuilt with new boost

* Fri Mar 11 2011 Sergey V Turchin <zerg@altlinux.org> 1.5.1-alt1
- new version

* Thu Jan 27 2011 Sergey V Turchin <zerg@altlinux.org> 1.5.0-alt1
- new version

* Fri Jan 14 2011 Sergey V Turchin <zerg@altlinux.org> 1.4.3-alt1
- new version

* Wed Dec 15 2010 Sergey V Turchin <zerg@altlinux.org> 1.4.1-alt2
- rebuilt with new boost

* Mon Nov 08 2010 Sergey V Turchin <zerg@altlinux.org> 1.4.1-alt1
- new version

* Wed Aug 11 2010 Sergey V Turchin <zerg@altlinux.org> 1.4.0-alt1
- new version

* Tue Aug 10 2010 Sergey V Turchin <zerg@altlinux.org> 1.3.90-alt1
- new version

* Thu Jul 22 2010 Sergey V Turchin <zerg@altlinux.org> 1.3.81-alt1
- new version

* Tue Apr 20 2010 Sergey V Turchin <zerg@altlinux.org> 1.3.1-alt4.M51.1
- build for M51

* Thu Apr 15 2010 Sergey V Turchin <zerg@altlinux.org> 1.3.1-alt5
- fix mysql database initialization

* Wed Apr 14 2010 Sergey V Turchin <zerg@altlinux.org> 1.3.1-alt4
- don't use mysql_install_db because incompatible with user data

* Fri Apr 09 2010 Sergey V Turchin <zerg@altlinux.org> 1.3.1-alt3
- add upstream mysw and dbus fixes
- fix mysql ulils search paths

* Wed Mar 03 2010 Sergey V Turchin <zerg@altlinux.org> 1.3.1-alt2
- add common plugin dirs

* Fri Feb 12 2010 Sergey V Turchin <zerg@altlinux.org> 1.3.1-alt1
- new version

* Tue Feb 02 2010 Sergey V Turchin <zerg@altlinux.org> 1.3.0-alt2
- add requires to database packages (default mysql because qslite don't work)

* Fri Jan 22 2010 Sergey V Turchin <zerg@altlinux.org> 1.3.0-alt1
- new version

* Mon Jan 18 2010 Sergey V Turchin <zerg@altlinux.org> 1.2.90.1070828-alt1
- svn r1070828

* Mon Aug 31 2009 Sergey V Turchin <zerg@altlinux.org> 1.2.1-alt1
- new version

* Tue Aug 04 2009 Sergey V Turchin <zerg@altlinux.org> 1.2.0-alt1
- new version

* Wed Jul 15 2009 Sergey V Turchin <zerg@altlinux.org> 1.1.95-alt1
- new version

* Tue Jun 30 2009 Sergey V Turchin <zerg@altlinux.org> 1.1.1-alt3
- rebuilt with new boost

* Mon Mar 16 2009 Sergey V Turchin <zerg@altlinux.org> 1.1.1-alt2
- fix to find agents executables

* Wed Jan 28 2009 Sergey V Turchin <zerg at altlinux dot org> 1.1.1-alt1
- new version

* Tue Jan 13 2009 Sergey V Turchin <zerg at altlinux dot org> 1.1.0-alt1
- new version
- removed deprecated macroses from specfile

* Wed Jul 30 2008 Sergey V Turchin <zerg at altlinux dot org> 1.0.0-alt1
- new version

* Tue May 27 2008 Sergey V Turchin <zerg at altlinux dot org> 0.81.0-alt1
- new version

* Tue May 06 2008 Sergey V Turchin <zerg at altlinux dot org> 0.80.0-alt1
- initial spec

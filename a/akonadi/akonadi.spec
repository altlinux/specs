
Name: akonadi
Version: 1.7.2
Release: alt1

Group: Databases
Summary: An extensible cross-desktop storage service for PIM
Url: http://pim.kde.org/akonadi/
License: LGPLv2+

Requires: %name-database tar bzip2

Source: %name-%version.tar
Source10: mysql_install_db
# Upstream
# RH
Patch10: akonadi-1.7.0-mysql_conf.patch
# ALT
Patch101: akonadi-1.1.1-alt-alt-kdebindir.patch
Patch102: akonadi-1.3.81-alt-mysql-paths.patch
Patch103: akonadi-1.4.1-alt-disable-mysql_install_db.patch
Patch104: akonadi-1.6.2-alt-mysql-db-create.patch
Patch105: akonadi-1.6.2-alt-start-mysqlcheck.patch
Patch106: akonadi-1.6.2-alt-own-mysql_install_db.patch
Patch107: akonadi-1.6.2-alt-check-nepomuk.patch

BuildRequires(pre): libqt4-devel
BuildRequires: gcc-c++ automoc libsoprano-devel soprano
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

%package database0
Group: Databases
Summary: %name Qt sqlite database
BuildArch: noarch
Requires: %name-common = %version-%release
Requires: libqt4-sql-sqlite
Provides: %name-database = %version-%release
%description database0
%name Qt sqlite database

%package database1
Group: Databases
Summary: %name sqlite database
BuildArch: noarch
Requires: %name-common = %version-%release
Requires: libqt4-sql-sqlite3
Provides: %name-database = %version-%release
%description database1
%name sqlite database

%package database2
Group: Databases
Summary: %name postgresql database
BuildArch: noarch
Requires: %name-common = %version-%release
Requires: libqt4-sql-postgresql postgresql /usr/bin/pg_dump /usr/bin/pg_restore
Provides: %name-database = %version-%release
%description database2
%name postgresql database

%package database3
Group: Databases
Summary: %name mysql database
BuildArch: noarch
Requires: %name-common = %version-%release
Requires: libqt4-sql-mysql MySQL-server  MySQL-client
Provides: %name-database = %version-%release
%description database3
%name mysql database

%package -n libakonadiprotocolinternals
Group: System/Libraries
Summary: %name library
Requires: %name-common = %version-%release
Requires: %{get_dep libqt4-core}
%description -n libakonadiprotocolinternals
%name library

%package -n libakonadiprivate
Group: System/Libraries
Summary: %name library
Requires: %name-common = %version-%release
Requires: %{get_dep libqt4-core}
%description -n libakonadiprivate
%name library

%package devel
Group: Development/KDE and QT
Summary: Development files for %name
Requires: libqt4-devel libxml2-devel
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
#%patch103 -p1
#%patch104 -p1
%patch105 -p1
%patch106 -p1
%patch107 -p1

%build
#export PATH=%_libdir/kde4bin:$PATH
export CMAKE_LIBRARY_PATH=%_libdir
%Kcmake \
    -DBIN_INSTALL_DIR2=%_kde4_bindir \
    -DCONFIG_INSTALL_DIR=%_sysconfdir \
    -DINCLUDE_INSTALL_DIR=%_includedir \
    -DMYSQLD_EXECUTABLE:FILEPATH=%_sbindir/mysqld
#    -DAKONADI_BUILD_QSQLITE:BOOL=TRUE \
#    -DINSTALL_QSQLITE_IN_QT_PREFIX:BOOL=TRUE \
#    -DAUTOMOC4_EXECUTABLE:FILEPATH=%_libdir/kde4bin/kde4automoc
#    -DBOOST_ROOT:STRING=%_prefix \
#    -DBOOST_INCLUDEDIR:STRING=%_includedir/boost \
#    -DBOOST_LIBRARYDIR:STRING=%_libdir \
#    -DBoost_MINIMUM_VERSION=1.34 \
%Kmake


%install
%Kinstall
mkdir -p %buildroot/%_libdir/akonadi/contact/editorpageplugins/
install -m 0755 %SOURCE10 %buildroot/%_bindir/akonadi_mysql_install_db

%files
%_bindir/akonadi_rds
%_bindir/akonadi_control
%_bindir/akonadictl
%_bindir/akonadiserver
%_bindir/akonadi_agent_launcher
%_bindir/akonadi_agent_server
%dir %_sysconfdir/akonadi/
%config(noreplace) %_sysconfdir/akonadi/*

%files -n libqt4-sql-sqlite3
%_qt4dir/plugins/sqldrivers/libqsqlite3.so

%files database0
%files database1
%files database2
%files database3
%_bindir/akonadi_mysql_install_db

%files common
%_K4dbus_services/org.freedesktop.Akonadi.Control.service
%_K4xdg_mime/akonadi-mime.xml
%_libdir/akonadi

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

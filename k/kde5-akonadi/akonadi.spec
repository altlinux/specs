%define rname akonadi

Name: kde5-%rname
Version: 15.12.1
Release: alt1
%K5init altplace

Group: Databases
Summary: An extensible cross-desktop storage service for PIM
Url: http://www.kde.org
License: GPLv2+ / LGPLv2+

Requires: %name-database tar bzip2

Source: %rname-%version.tar
Source10: mysql_install_db
Patch1: alt-find-exe.patch
Patch2: alt-mysql-conf.patch
Patch3: alt-mysql-paths.patch
Patch4: alt-mysqlcheck-detached.patch
Patch5: alt-own-mysql-install-db.patch
Patch6: alt-find-resources.patch

# Automatically added by buildreq on Thu Aug 06 2015 (-bi)
# optimized out: cmake cmake-modules elfutils libEGL-devel libGL-devel libgpg-error libqt5-core libqt5-dbus libqt5-gui libqt5-network libqt5-sql libqt5-test libqt5-widgets libqt5-xml libstdc++-devel pkg-config python-base python3 python3-base ruby ruby-stdlibs shared-mime-info
#BuildRequires: extra-cmake-modules gcc-c++ libdb4-devel libsqlite3-devel python-module-google qt5-base-devel rpm-build-python3 rpm-build-ruby xml-utils xsltproc
BuildRequires(pre): rpm-build-kf5
BuildRequires: extra-cmake-modules gcc-c++ qt5-base-devel
BuildRequires: libsqlite3-devel xml-utils xsltproc shared-mime-info

%description
An extensible cross-desktop storage service for PIM data and meta data providing
concurrent read, write, and query access.

%package common
Summary: %name common package
Group: System/Configuration/Other
Requires: kf5-filesystem
%description common
%name common package

%package -n qt5-sql-sqlite3
Summary: SQLite3 driver for Qt5 SQL classes
Group: System/Libraries
Provides: qt5-plugin-sql = 5.5
%description -n qt5-sql-sqlite3
SQLite3 driver for Qt's SQL classes (QSQLITE3)

%package database-1-sqlite
Group: Databases
Summary: %name Qt sqlite database
BuildArch: noarch
Requires: %name-common = %EVR
Requires: qt5-sql-sqlite
Provides: %name-database = %EVR
Provides: %name-database-sqlite = %EVR
%description database-1-sqlite
%name Qt sqlite database

%package database-3-sqlite3
Group: Databases
Summary: %name sqlite database
BuildArch: noarch
Requires: %name-common = %EVR
Requires: qt5-sql-sqlite3
Provides: %name-database = %EVR
Provides: %name-database-sqlite3 = %EVR
%description database-3-sqlite3
%name Akonadi sqlite database

%package database-5-postgresql
Group: Databases
Summary: %name postgresql database
BuildArch: noarch
Requires: %name-common = %EVR
Requires: qt5-sql-postgresql postgresql /usr/bin/pg_dump /usr/bin/pg_restore
Provides: %name-database = %EVR
Provides: %name-database-postgresql = %EVR
%description database-5-postgresql
%name postgresql database

%package database-8-mysql
Group: Databases
Summary: %name mysql database
BuildArch: noarch
Requires: %name-common = %EVR
Requires: qt5-sql-mysql mariadb-server mariadb-client
Provides: %name-database = %EVR
Provides: %name-database-mysql = %EVR
%description database-8-mysql
%name mysql database

%package devel
Group: Development/KDE and QT
Summary: Development files for %name
%description devel
The %name-devel package contains libraries and header files for
developing applications that use %name.

%package -n libkf5akonadiprivate
Group: System/Libraries
Summary: KF5 library
Requires: %name-common = %version-%release
%description -n libkf5akonadiprivate
KF5 library


%prep
%setup -n %rname-%version
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1

%build
%K5build \
    -DMYSQLD_EXECUTABLE:FILEPATH=%_sbindir/mysqld \
    #

%install
%K5install

install -m 0755 %SOURCE10 %buildroot/%_K5bin/akonadi5_mysql_install_db
mv %buildroot/%_K5xdgmime/akonadi{,5}-mime.xml

mkdir -p %buildroot/%_K5srv/akonadi/contact
mkdir -p %buildroot/%_K5lib/akonadi5/contact
mkdir -p %buildroot/%_datadir/akonadi5/{agents,contact,plugins,accountwizard}

%files
%_K5dbus_srv/org.freedesktop.Akonadi.Control.service
%_K5bin/akonadi_agent_launcher
%_K5bin/akonadi_agent_server
%_K5bin/akonadi_rds
%_K5bin/akonadi_control
%_K5bin/akonadictl
%_K5bin/akonadiserver

%files -n qt5-sql-sqlite3
%_qt5_plugindir/sqldrivers/libqsqlite3.so

%files database-1-sqlite
%files database-3-sqlite3
%files database-5-postgresql
%files database-8-mysql
%config(noreplace) %_K5xdgconf/akonadi/mysql-*.conf
%_K5bin/akonadi5_mysql_install_db

%files common
%dir %_K5lib/akonadi5/
%dir %_K5lib/akonadi5/contact/
%dir %_K5xdgconf/akonadi/
%dir %_K5srv/akonadi/
%dir %_K5srv/akonadi/contact/
%dir %_datadir/akonadi5/
%dir %_datadir/akonadi5/accountwizard/
%dir %_datadir/akonadi5/agents/
%dir %_datadir/akonadi5/contact/
%dir %_datadir/akonadi5/plugins/
%config(noreplace) %_K5xdgconf/akonadi.categories
%_K5xdgmime/akonadi5-mime.xml

%files devel
%_K5bin/asapcat
#%_K5inc/akonadi_version.h
%_K5inc/akonadi/
%_K5link/lib*.so
%_K5lib/cmake/KF5AkonadiServer
%_K5dbus_iface/*.Akonadi.*.xml
#%_K5archdata/mkspecs/modules/qt_akonadi.pri

%files -n libkf5akonadiprivate
%_K5lib/libKF5AkonadiPrivate.so.*

%changelog
* Tue Jan 19 2016 Sergey V Turchin <zerg@altlinux.org> 15.12.1-alt1
- new version

* Mon Dec 21 2015 Sergey V Turchin <zerg@altlinux.org> 15.12.0-alt1
- new version

* Thu Nov 12 2015 Sergey V Turchin <zerg@altlinux.org> 15.08.3-alt1
- new version

* Wed Oct 14 2015 Sergey V Turchin <zerg@altlinux.org> 15.08.2-alt1
- new version

* Wed Sep 16 2015 Sergey V Turchin <zerg@altlinux.org> 15.08.1-alt1
- new version

* Wed Sep 09 2015 Sergey V Turchin <zerg@altlinux.org> 15.08.0-alt3
- not't search for resources in KDE4 place

* Tue Sep 01 2015 Sergey V Turchin <zerg@altlinux.org> 15.08.0-alt2
- add plugins dir

* Thu Aug 20 2015 Sergey V Turchin <zerg@altlinux.org> 15.08.0-alt1
- new version

* Mon Aug 10 2015 Sergey V Turchin <zerg@altlinux.org> 15.7.90-alt1
- new version

* Mon Aug 03 2015 Sergey V Turchin <zerg@altlinux.org> 15.7.80-alt1
- initial build

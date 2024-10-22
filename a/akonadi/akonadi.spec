%define rname akonadi

%def_enable tools

Name: %rname
Version: 24.08.1
Release: alt1
%K6init

Group: Databases
Summary: An extensible cross-desktop storage service for PIM
Url: http://www.kde.org
License: GPL-2.0-or-later or LGPL-2.1-or-later

Provides: kde5-akonadi = %EVR
Obsoletes: kde5-akonadi < %EVR
Requires: %name-database tar bzip2

Source: %rname-%version.tar
Source10: mysql_install_db
Patch1: alt-find-exe.patch
Patch2: alt-mysql-conf.patch
Patch3: alt-mysqlcheck-detached.patch
Patch4: alt-own-mysql-install-db.patch
Patch5: alt-find-mysql-global-conf.patch

BuildRequires(pre): rpm-build-kf6
BuildRequires: boost-devel extra-cmake-modules qt6-declarative-devel qt6-tools-devel
BuildRequires: xsltproc xml-utils shared-mime-info
BuildRequires: libsqlite3-devel libxslt-devel liblzma-devel
BuildRequires: signon-devel libaccounts-glib-devel accounts-qt6-devel kaccounts-integration-devel
BuildRequires: kf6-kauth-devel kf6-kbookmarks-devel kf6-kcodecs-devel kf6-kcompletion-devel kf6-kconfig-devel kf6-kconfigwidgets-devel
BuildRequires: kf6-kcoreaddons-devel kf6-kdbusaddons-devel  kf6-kguiaddons-devel kf6-ki18n-devel
BuildRequires: kf6-kiconthemes-devel kf6-kio-devel kf6-kitemmodels-devel kf6-kitemviews-devel kf6-kjobwidgets-devel kf6-kservice-devel
BuildRequires: kf6-kwidgetsaddons-devel kf6-kwindowsystem-devel kf6-kxmlgui-devel kf6-solid-devel
BuildRequires: kf6-kcrash-devel

%description
An extensible cross-desktop storage service for PIM data and meta data providing
concurrent read, write, and query access.

%package common
Summary: %name common package
Group: System/Configuration/Other
Requires: kf6-filesystem
Provides: kde5-akonadi-common = %EVR
Obsoletes: kde5-akonadi-common < %EVR
%description common
%name common package

%package database-1-sqlite
Group: Databases
Summary: %name Qt sqlite database
BuildArch: noarch
Requires: %name-common >= %EVR
Requires: qt6-sql-sqlite
Provides: %name-database = %EVR
Provides: %name-database-sqlite = %EVR
Provides: kde5-akonadi-database-3-sqlite3 = %EVR
Obsoletes: kde5-akonadi-database-3-sqlite3 < %EVR
Provides: kde5-akonadi-database-1-sqlite = %EVR
Obsoletes: kde5-akonadi-database-1-sqlite < %EVR
%description database-1-sqlite
%name Qt sqlite database

%package database-5-postgresql
Group: Databases
Summary: %name postgresql database
BuildArch: noarch
Requires: %name-common >= %EVR
Requires: qt6-sql-postgresql postgresql /usr/bin/pg_dump /usr/bin/pg_restore
Provides: %name-database = %EVR
Provides: %name-database-postgresql = %EVR
Provides: kde5-akonadi-database-5-postgresql = %EVR
Obsoletes: kde5-akonadi-database-5-postgresql < %EVR
%description database-5-postgresql
%name postgresql database

%package database-10-mysql
Group: Databases
Summary: %name mysql database
BuildArch: noarch
Conflicts: %name-database-9-mariadb
Requires: %name-common >= %EVR
Requires: qt6-sql-mysql MySQL-server MySQL-client
Provides: %name-database = %EVR
Provides: %name-database-mysql = %EVR
Provides: kde5-akonadi-database-10-mysql = %EVR
Obsoletes: kde5-akonadi-database-10-mysql < %EVR
%description database-10-mysql
%name mysql database

%package database-9-mariadb
Group: Databases
Summary: %name mariadb database
BuildArch: noarch
Conflicts: %name-database-10-mysql
Requires: %name-common >= %EVR
Requires: qt6-sql-mysql mariadb-server mariadb-client
Provides: %name-database = %EVR
Provides: %name-database-mariadb = %EVR
Provides: kde5-akonadi-database-9-mariadb = %EVR
Obsoletes: kde5-akonadi-database-9-mariadb < %EVR
%description database-9-mariadb
%name mysql database

%package devel
Group: Development/KDE and QT
Summary: Development files for %name
Requires: boost-devel
%description devel
The %name-devel package contains libraries and header files for
developing applications that use %name.

%package -n libkpim6akonadiprivate
Group: System/Libraries
Summary: %name library
Requires: %name-common >= %EVR
%description -n libkpim6akonadiprivate
%name library

%package -n libkpim6akonadiagentbase
Group: System/Libraries
Summary: %name library
Requires: %name-common >= %EVR
%description -n libkpim6akonadiagentbase
%name library

%package -n libkpim6akonadicore
Group: System/Libraries
Summary: %name library
Requires: %name-common >= %EVR
%description -n libkpim6akonadicore
%name library

%package -n libkpim6akonadiwidgets
Group: System/Libraries
Summary: %name library
Requires: %name-common >= %EVR
%description -n libkpim6akonadiwidgets
%name library

%package -n libkpim6akonadixml
Group: System/Libraries
Summary: %name library
Requires: %name-common >= %EVR
%description -n libkpim6akonadixml
%name library

%prep
%setup -n %rname-%version
%patch1 -p1
%patch2 -p1
#%patch3 -p1 -b .mysqlcheck-detached
%patch4 -p1
%patch5 -p1

%build
%K6build \
    -DKDE_INSTALL_INCLUDEDIR=%_K6inc \
    -DMYSQLD_EXECUTABLE:FILEPATH=%_sbindir/mysqld \
    -DBUILD_TESTING=OFF \
    -DBUILD_TOOLS=%{?_enable_tools:ON}%{!?_enable_tools:OFF} \
    -DMYSQLD_SCRIPTS_PATH:FILEPATH="%_K6bin" \
    #
#    -DDATABASE_BACKEND=MYSQL \

%install
%K6install
%K6install_move data kdevappwizard

install -m 0755 %SOURCE10 %buildroot/%_bindir/akonadi6_mysql_install_db
mv %buildroot/%_K6xdgmime/akonadi{,6}-mime.xml

mkdir -p %buildroot/%_K6srv/akonadi/contact
mkdir -p %buildroot/%_K6plug/akonadi/contacts/plugins/

mkdir -p %buildroot/%_datadir/akonadi/{agents,contact,plugins,accountwizard}

#mkdir -p %buildroot/%_kf6_data/akonadi/
cp -ar %buildroot/%_kf6_data/akonadi/*.xs* %buildroot/%_datadir/akonadi/ ||:

# cleanup
rm -rf %buildroot/%_sysconfdir/apparmor.d/

%find_lang %name --with-kde --all-name


%files
%config(noreplace) %_K6xdgconf/akonadi/mysql-*.conf
%_bindir/akonadi6_mysql_install_db
%_K6bin/akonadi_agent_launcher
%_K6bin/akonadi_agent_server
%_K6bin/akonadi_rds
%_K6bin/akonadi_control
%_K6bin/akonadi-db-migrator
%_K6bin/akonadictl
%_K6bin/akonadiserver
%_K6bin/akonadiselftest
%_K6dbus_srv/org.freedesktop.Akonadi.Control.service
%if_enabled tools
%_K6bin/akonadi2xml
%_K6bin/akonaditest
%_K6bin/akonadi_knut_resource
%_K6plug/pim6/akonadi/*.so
%_datadir/akonadi/agents/knutresource.desktop
%_kf6_data/akonadi_knut_resource/
%endif

%files database-1-sqlite
%files database-5-postgresql
%files database-9-mariadb
%files database-10-mysql

%files common -f %name.lang
%doc LICENSES/*
%dir %_K6plug/akonadi/
%dir %_K6plug/akonadi/contacts/
%dir %_K6plug/akonadi/contacts/plugins/
#%dir %_K6lib/akonadi/
#%dir %_K6lib/akonadi/contact/
%dir %_K6xdgconf/akonadi/
%dir %_K6srv/akonadi/
%dir %_K6srv/akonadi/contact/
%dir %_kf6_data/akonadi/
%dir %_datadir/akonadi/
%dir %_datadir/akonadi/accountwizard/
%dir %_datadir/akonadi/agents/
%dir %_datadir/akonadi/contact/
%dir %_datadir/akonadi/plugins/
#%config(noreplace) %_K6xdgconf/akonadi.*categories
%_datadir/qlogging-categories6/*.*categories
%_K6cfg/resourcebase.kcfg
%_K6xdgmime/akonadi6-mime.xml
%_K6icon/*/*/apps/*akonadi*.*

%files devel
%_K6bin/asapcat
%_K6plug/designer/*akonadi*.so
%_K6inc/KPim6/Akonadi*/
%_K6link/lib*.so
%_K6lib/cmake/K*6Akonadi/
%_K6dbus_iface/*.Akonadi.*.xml
%_datadir/akonadi/*.xs*
%_kf6_data/akonadi/*.xs*
%_K6data/kdevappwizard/templates/*akonadi*

%files -n libkpim6akonadiprivate
%_K6lib/libKPim6AkonadiPrivate.so.*
%files -n libkpim6akonadiagentbase
%_K6lib/libKPim6AkonadiAgentBase.so.*
%files -n libkpim6akonadicore
%_K6lib/libKPim6AkonadiCore.so.*
%files -n libkpim6akonadiwidgets
%_K6lib/libKPim6AkonadiWidgets.so.*

%if_enabled tools
%files -n libkpim6akonadixml
%_K6lib/libKPim6AkonadiXml.so.*
%endif


%changelog
* Wed Sep 25 2024 Sergey V Turchin <zerg@altlinux.org> 24.08.1-alt1
- new version

* Mon Sep 09 2024 Sergey V Turchin <zerg@altlinux.org> 24.08.0-alt1
- new version

* Wed Aug 21 2024 Sergey V Turchin <zerg@altlinux.org> 24.05.2-alt1
- initial build


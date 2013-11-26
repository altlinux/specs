
#def_enable qtchooser
%def_disable bootstrap
%def_enable sql_pgsql
%def_enable sql_odbc
%def_enable sql_ibase
%def_disable sql_tds
%def_disable sql_sqlite2

%define platform linux-g++
%define graphicssystem raster
%ifarch %arm
%define opengl_type es2
%else
%define opengl_type desktop
%endif

%define rname  qtbase
%define gname  qt5
%define libname  lib%gname
%define major  5
%define minor  1
%define bugfix 1
Name: qt5-base
Version: %major.%minor.%bugfix
Release: alt4

Group: System/Libraries
Summary: Qt%major - QtBase components
License: LGPLv2 with exceptions / GPLv3 with exceptions
Url: http://qt-project.org/

Source: %rname-opensource-src-%version.tar
Source1: rpm-macros-addon
# FC
Patch1: qtbase-opensource-src-5.0.2-lowmem.patch
# upstream
Patch10: xcb-1.9.3.patch
# ALT
Patch1000: alt-sql-ibase-firebird.patch
Patch1001: alt-enable-ft-lcdfilter.patch

# macros
%define _qt5 %gname
%define _qt5_prefix %_datadir/qt5
%define _qt5_datadir %_datadir/qt5
%define _qt5_archdatadir %_libdir/qt5
#
%define _qt5_bindir %_qt5_prefix/bin
%define _qt5_docdir %_defaultdocdir/qt5
%define _qt5_examplesdir %_qt5_archdatadir/examples
%define _qt5_headerdir %_includedir/qt5
%define _qt5_importdir %_qt5_archdatadir/imports
%define _qt5_libdir %_libdir
%define _qt5_libexecdir %_qt5_archdatadir/libexec
%define _qt5_libdatadir %_qt5_prefix/lib
%define _qt5_plugindir %_qt5_archdatadir/plugins
%define _qt5_settingsdir %_sysconfdir/xdg
%define _qt5_sysconfdir %_qt5_settingsdir
%define _qt5_translationdir %_qt5_datadir/translations

# Automatically added by buildreq on Fri Sep 20 2013 (-bi)
# optimized out: elfutils fontconfig fontconfig-devel glib2-devel glibc-devel-static gstreamer-devel libEGL-devel libGL-devel libX11-devel libXext-devel libXfixes-devel libXrender-devel libatk-devel libcairo-devel libcom_err-devel libfreetype-devel libgdk-pixbuf libgdk-pixbuf-devel libgio-devel libgst-plugins libkrb5-devel libpango-devel libpng-devel libpq-devel libssl-devel libstdc++-devel libwayland-client libwayland-server libxcb-devel libxcb-render-util libxcbutil-icccm libxcbutil-image libxcbutil-keysyms libxml2-devel pkg-config python-base python3 python3-base ruby ruby-stdlibs xorg-fixesproto-devel xorg-inputproto-devel xorg-renderproto-devel xorg-xproto-devel zlib-devel
#BuildRequires: firebird-devel gcc-c++ gst-plugins-devel libXi-devel libalsa-devel libcups-devel libdbus-devel libfreetds-devel libgtk+2-devel libicu-devel libjpeg-devel libmysqlclient-devel libpcre-devel libpulseaudio-devel libsqlite3-devel libudev-devel libunixODBC-devel libxcb-render-util-devel libxcbutil-icccm-devel libxcbutil-image-devel libxcbutil-keysyms-devel postgresql-devel python-module-distribute rpm-build-python3 rpm-build-ruby zlib-devel-static
BuildRequires: gcc-c++ libcups-devel libdbus-devel libicu-devel libjpeg-devel
BuildRequires: libpcre-devel libudev-devel libdrm-devel libgbm-devel zlib-devel libgtk+2-devel
BuildRequires: pkgconfig(gl) pkgconfig(glesv2)
BuildRequires: libX11-devel libXi-devel libxkbcommon-devel
BuildRequires: libxcb-render-util-devel libxcbutil-icccm-devel libxcbutil-image-devel libxcbutil-keysyms-devel
BuildRequires: gst-plugins-devel libalsa-devel libpulseaudio-devel
%{?_enable_sql_tds:BuildRequires: libfreetds-devel}
%{?_enable_sql_ibase:BuildRequires: firebird-devel}
%{?_enable_sql_odbc:BuildRequires: libunixODBC-devel}
%{?_enable_sql_pgsql:BuildRequires: postgresql-devel libpq-devel libecpg-devel-static}
%{?_enable_sql_sqlite2:BuildRequires: libsqlite-devel}
BuildRequires: libmysqlclient-devel
BuildRequires: libsqlite3-devel
%if_disabled bootstrap
BuildRequires: qt5-base-devel qt5-tools
%endif

%description
Qt is a software toolkit for developing applications.

This package contains base tools, like string, xml, and network
handling.

%package common
Summary: Common package for Qt%major
Group: System/Configuration/Other
Requires: common-licenses
%description common
Common package for Qt%major

%package devel
Group: Development/KDE and QT
Summary: Development files for %name
Requires: %name-common = %EVR
Requires: pkgconfig(gl)
Requires: rpm-macros-%gname = %EVR
%description devel
%summary.

%package devel-static
Group: Development/KDE and QT
Summary: Development files for %name
Requires: %name-common = %EVR
Requires: %name-devel
%description devel-static
%summary.

%package -n rpm-macros-%gname
Summary: Set of RPM macros for packaging Qt%major-based applications
Group: Development/KDE and QT
Requires: %name-common = %version-%release
%description -n rpm-macros-%gname
Set of RPM macros for packaging Qt%major-based applications for %distribution
Install this package if you want to create RPM packages that use Qt%major

%package static
Group: Development/KDE and QT
Summary: Static library files for %name
Requires: %name-devel = %EVR
Requires: pkgconfig(fontconfig)
Requires: pkgconfig(glib-2.0)
Requires: pkgconfig(zlib)
%description static
%summary.

%package doc
BuildArch: noarch
Summary: Document for developing apps which will use Qt%{major}
Group: Development/KDE and QT
Requires: %name-common = %EVR
#Requires: %gname-assistant
%description doc
This package contains documentation and sources for example programs.

%package -n %gname-sql
BuildArch: noarch
Group: System/Libraries
Summary: Meta-package for SQL support of Qt%major GUI toolkit
Requires: %name-common = %EVR
Requires: %gname-sql-mysql = %EVR
Requires: %gname-sql-sqlite = %EVR
%if_enabled sql_ibase
Requires: %gname-sql-interbase = %EVR
%endif
%if_enabled sql_pgsql
Requires: %gname-sql-postgresql = %EVR
%endif
%if_enabled sql_odbc
Requires: %gname-sql-odbc = %EVR
%endif
%if_enabled sql_tds
Requires: %gname-sql-tds = %EVR
%endif
%if_enabled sql_sqlite2
Requires: %gname-sql-sqlite2 = %EVR
%endif
%description -n %gname-sql
Meta-package for SQL support of Qt%major GUI toolkit

%package -n %gname-sql-odbc
Summary: ODBC drivers for Qt%major SQL classes
Group: System/Libraries
Requires: %name-common = %EVR
Provides: %gname-plugin-sql = %EVR
%description -n %gname-sql-odbc
ODBC driver for Qt's SQL classes (QODBC)

%package -n %gname-sql-tds
Summary: FreeTDS(Sybase) driver for Qt%major SQL classes
Group: System/Libraries
Requires: %name-common = %EVR
Provides: %gname-plugin-sql = %EVR
%description -n %gname-sql-tds
FreeTDS(Sybase) driver for Qt's SQL classes (QTDS)

%package -n %gname-sql-mysql
Summary: MySQL driver for Qt%major SQL classes
Group: System/Libraries
Requires: %name-common = %EVR
Provides: %gname-plugin-sql = %EVR
%description -n %gname-sql-mysql
MySQL driver for Qt's SQL classes (QMYSQL)

%package -n %gname-sql-postgresql
Summary: PostgreSQL drivers for Qt%major SQL classes
Group: System/Libraries
Requires: %name-common = %EVR
Provides: %gname-plugin-sql = %EVR
%description -n %gname-sql-postgresql
PostgreSQL driver for Qt's SQL classes (QPSQL)

%package -n %gname-sql-interbase
Summary: InterBase drivers for Qt%major SQL classes
Group: System/Libraries
Requires: %name-common = %EVR
Provides: %gname-plugin-sql = %EVR
%description -n %gname-sql-interbase
InterBase driver for Qt's SQL classes (QIBASE)

%package -n %gname-sql-sqlite
Summary: SQLite driver for Qt%major SQL classes
Group: System/Libraries
Requires: %name-common = %EVR
Provides: %gname-plugin-sql = %EVR
%description -n %gname-sql-sqlite
SQLite driver for Qt's SQL classes (QSQLITE2)

%package -n %gname-sql-sqlite2
Summary: SQLite2 driver for Qt%major SQL classes
Group: System/Libraries
Requires: %name-common = %EVR
Provides: %gname-plugin-sql = %EVR
%description -n %gname-sql-sqlite2
SQLite2 driver for Qt's SQL classes (QSQLITE2)

%package -n lib%{gname}-sql
Summary: SQL support library for the Qt%major toolkit
Group: System/Libraries
Requires: %name-common = %EVR
# sqlite plugin included
Provides: %gname-plugin-sql = %EVR
Provides: %gname-sql-sqlite = %EVR
%description -n lib%{gname}-sql
SQL support library for the Qt%major toolkit

%package -n lib%{gname}-core
Summary: Core library for the Qt%major toolkit
Group: System/Libraries
Requires: %name-common = %EVR
Requires: glibc-gconv-modules
%description -n lib%{gname}-core
Core library for the Qt%major toolkit

%package -n lib%{gname}-gui
Summary: GUI support library for the Qt%major toolkit
Group: System/Libraries
Requires: %name-common = %EVR
%description -n lib%{gname}-gui
GUI support library for the Qt%major toolkit

%package -n lib%{gname}-dbus
Summary: DBus support library for the Qt%major toolkit
Group: System/Libraries
Requires: %name-common = %EVR
%description -n lib%{gname}-dbus
DBus support library for the Qt%major toolkit

%package -n lib%{gname}-network
Summary: Network support library for the Qt%major toolkit
Group: System/Libraries
Requires: %name-common = %EVR
%description -n lib%{gname}-network
Network support library for the Qt%major toolkit

%package -n lib%{gname}-opengl
Summary: OpenGL support library for the Qt%major toolkit
Group: System/Libraries
Requires: %name-common = %EVR
%description -n lib%{gname}-opengl
OpenGL support library for the Qt%major toolkit

%package -n lib%{gname}-xml
Summary: XML support library for the Qt%major toolkit
Group: System/Libraries
Requires: %name-common = %EVR
%description -n lib%{gname}-xml
XML support library for the Qt%major toolkit

%package -n lib%{gname}-concurrent
Summary: Multi-threading concurrence support library for the Qt%major toolkit
Group: System/Libraries
Requires: %name-common = %EVR
%description -n lib%{gname}-concurrent
Multi-threading concurrence support library for the Qt%major toolkit

%package -n lib%{gname}-printsupport
Summary: Printing support library for the Qt%major toolkit
Group: System/Libraries
Requires: %name-common = %EVR
%description -n lib%{gname}-printsupport
Printing support library for the Qt%major toolkit

%package -n lib%{gname}-test
Summary: Testing support library for the Qt%major toolkit
Group: System/Libraries
Requires: %name-common = %EVR
%description -n lib%{gname}-test
Testing support library for the Qt%major toolkit

%package -n lib%{gname}-widgets
Summary: Widgets library for the Qt%major toolkit
Group: System/Libraries
Requires: %name-common = %EVR
%description -n lib%{gname}-widgets
Widgets library for the Qt%major toolkit

%prep
%setup -n %rname-opensource-src-%version
%patch1 -p1 -b .lowmem
%patch10 -p1 -b .xcb
%patch1000 -p1 -b .ibase
%patch1001 -p1 -b .lcd
bin/syncqt.pl -private \
    -module QtCore \
    -module QtGui \
    -module QtXml \
    -module QtNetwork \
    -module QtSql \
    -module QtTest \
    -module QtDBus \
    -module QtConcurrent \
    -module QtPlatformSupport \
    -module QtWidgets \
    -module QtOpenGL \
    -module QtPrintSupport \
    ./
[ -e include/QtCore/QtCoreDepends ] || >include/QtCore/QtCoreDepends

# install optflags
%add_optflags %optflags_shared
sed -i "s|^\s*QMAKE_CFLAGS_RELEASE\s*+=.*$|QMAKE_CFLAGS_RELEASE += %optflags|" mkspecs/common/gcc-base.conf
sed -i "s|^\s*QMAKE_CFLAGS_RELEASE_WITH_DEBUGINFO\s*+=.*$|QMAKE_CFLAGS_RELEASE_WITH_DEBUGINFO += %optflags|" mkspecs/common/g++-base.conf

#sed -i -e "s|^\(QMAKE_LFLAGS_RELEASE.*\)|\1 $RPM_LD_FLAGS|" \
#  mkspecs/common/g++-unix.conf

# move some bundled libs to ensure they're not accidentally used
pushd src/3rdparty
mkdir UNUSED
mv freetype libjpeg libpng sqlite zlib xcb UNUSED/
popd

%build
unset QTDIR QTLIB QTINC
export QT_DIR="$PWD"
export PATH=$QT_DIR/bin:$PATH
export LD_LIBRARY_PATH=$QT_DIR/lib:$LD_LIBRARY_PATH
export QT_PLUGIN_PATH=$QT_DIR/plugins

./configure -v \
    -opensource \
    -confirm-license \
    -I/usr/include/pcre \
    -prefix %_qt5_prefix \
    -archdatadir %_qt5_archdatadir \
    -bindir %_qt5_bindir \
    -datadir %_qt5_datadir \
    -docdir %_qt5_docdir \
    -examplesdir %_qt5_examplesdir \
    -headerdir %_qt5_headerdir \
    -importdir %_qt5_importdir \
    -libdir %_qt5_libdir \
    -libexecdir %_qt5_libexecdir \
    -plugindir %_qt5_plugindir \
    -sysconfdir %_qt5_sysconfdir \
    -translationdir %_qt5_translationdir \
    -platform %platform \
    -release \
    -shared \
    -pkg-config \
    -largefile \
    -javascript-jit \
    -no-nis \
    -accessibility \
    -dbus-linked \
    -fontconfig \
    -glib \
    -gtkstyle \
    -iconv \
    -icu \
    -openssl \
    -optimized-qmake \
    -nomake examples \
    -nomake tests \
    -make tools \
    -no-pch \
    -no-rpath \
    -no-separate-debug-info \
    -no-strip \
    -reduce-relocations \
    -opengl %opengl_type \
    -system-sqlite \
    %{?_enable_sql_tds:-plugin-sql-tds}%{!?_enable_sql_tds:-no-sql-tds} \
    %{?_enable_sql_ibase:-plugin-sql-ibase}%{!?_enable_sql_ibase:-no-sql-ibase} \
    %{?_enable_sql_pgsql:-plugin-sql-psql}%{!?_enable_sql_pgsql:-no-sql-psql} \
    %{?_enable_sql_sqlite2:-plugin-sql-sqlite2}%{!?_enable_sql_sqlite2:-no-sql-sqlite2} \
    %{?_enable_sql_odbc:-plugin-sql-odbc}%{!?_enable_sql_odbc:-no-sql-odbc} \
    -system-libjpeg \
    -system-libpng \
    -system-pcre \
    -system-zlib \
    -xcb -system-xcb \
    -xkb -system-xkbcommon \
    #

%make_build
%if_disabled bootstrap
[ -d doc/qtcore ] || %make docs
%endif

%install
# uninstall optflags
sed -i "s|^\s*QMAKE_CFLAGS_RELEASE\s*+=.*$|QMAKE_CFLAGS_RELEASE += |" mkspecs/common/gcc-base.conf
sed -i "s|^\s*QMAKE_CFLAGS_RELEASE_WITH_DEBUGINFO\s*+=.*$|QMAKE_CFLAGS_RELEASE_WITH_DEBUGINFO += -O2 -g|" mkspecs/common/g++-base.conf

make install INSTALL_ROOT=%buildroot
%if_disabled bootstrap
[ -d doc/qtcore ] && %make INSTALL_ROOT=%buildroot install_docs ||:
rm -rf %buildroot/%_qt5_docdir/qtwidgets/*tutorials-addressbook*
%endif

# remove .la files
rm -rf %buildroot/%_qt5_libdir/*.la

# .pc
mkdir -p %buildroot/%_pkgconfigdir/
cat >%buildroot/%_pkgconfigdir/Qt%major.pc<<__EOF__
prefix=%_qt5_prefix
archdatadir=%_qt5_archdatadir
bindir=%_qt5_bindir
datadir=%_qt5_datadir

docdir=%_qt5_docdir
examplesdir=%_qt5_examplesdir
headerdir=%_qt5_headerdir
importdir=%_qt5_importdir
libdir=%_qt5_libdir
libexecdir=%_qt5_libexecdir
moc=%_qt5_bindir/moc
plugindir=%_qt5_plugindir
qmake=%_qt5_bindir/qmake
settingsdir=%_qt5_settingsdir
sysconfdir=%_qt5_sysconfdir
translationdir=%_qt5_translationdir

Name: Qt%major
Description: Qt%major Configuration
Version: %version
__EOF__

# rpm macros
install -d -m 0755 %buildroot/%_rpmmacrosdir/
cat >%buildroot/%_rpmmacrosdir/%gname <<__EOF__
%%_qt5 %_qt5
%%_qt5_epoch %{?epoch}%{!?epoch:0}
%%_qt5_version %version
%%_qt5_evr %EVR
%%_qt5_prefix %_qt5_prefix
%%_qt5_archdatadir %_qt5_archdatadir
%%_qt5_bindir %_qt5_bindir
%%_qt5_datadir %_qt5_datadir
%%_qt5_docdir %_qt5_docdir
%%_qt5_examplesdir %_qt5_examplesdir
%%_qt5_headerdir %_qt5_headerdir
%%_qt5_importdir %_qt5_importdir
%%_qt5_libdir %_qt5_libdir
%%_qt5_libdatadir %_qt5_libdatadir
%%_qt5_libexecdir %_qt5_libexecdir
%%_qt5_plugindir %_qt5_plugindir
%%_qt5_settingsdir %_qt5_settingsdir
%%_qt5_sysconfdir %_qt5_sysconfdir
%%_qt5_translationdir %_qt5_translationdir

%%_qt5_qmake %_qt5_bindir/qmake

__EOF__
cat %SOURCE1 >>%buildroot/%_rpmmacrosdir/%gname

# create/own dirs
mkdir -p %buildroot/{%_qt5_archdatadir/mkspecs/modules,%_qt5_importdir,%_qt5_libexecdir,%_qt5_plugindir/iconengines,%_qt5_translationdir,%_qt5_docdir}

# create compatibility symlinks to dirs
for d in imports libexec mkspecs plugins ; do
ln -s `relative %_qt5_archdatadir/$d %_qt5_prefix/$d` %buildroot/%_qt5_prefix/$d
done
ln -s `relative %_qt5_docdir %_qt5_prefix/doc` %buildroot/%_qt5_prefix/doc

# install binaries to %_bindir
mkdir %buildroot/%_bindir
ls -1d %buildroot/%_qt5_bindir/* | \
while read f ; do
    [ -f "$f" ] || continue
    fname=`basename $f`
    mv $f %buildroot/%_bindir/$fname-%gname
    ln -s `relative %_bindir/$fname-%gname %_qt5_bindir/$fname-%gname` %buildroot/%_qt5_bindir/$fname
done

# qtchooser conf
%if_enabled qtchooser
  mkdir -p %buildroot%_sysconfdir/xdg/qtchooser
  pushd    %buildroot%_sysconfdir/xdg/qtchooser
    echo "%_qt5_bindir" >  %{gname}.conf
    echo "%_qt5_prefix" >> %{gname}.conf
  popd
%endif

## .prl/.la files
# nuke .prl reference(s) to %%buildroot, excessive (.la-like) libs
pushd %buildroot/%_qt5_libdir
for prl_file in libQt%{major}*.prl ; do
  sed -i -e "/^QMAKE_PRL_BUILD_DIR/d" ${prl_file}
  if [ -f "$(basename ${prl_file} .prl).so" ]; then
    rm -fv "$(basename ${prl_file} .prl).la"
    sed -i -e "/^QMAKE_PRL_LIBS/d" ${prl_file}
  fi
done
popd

# install libs into qt prefix
mkdir -p %buildroot/%_qt5_prefix/lib
ls -1d %buildroot/%_qt5_libdir/* | \
while read f ; do
    [ -d "$f" ] && continue
    fname=`basename $f`
    ln -s `relative $f %buildroot/%_qt5_libdatadir/$fname` %buildroot/%_qt5_libdatadir/$fname
done


%if 0%{?qtchooser}
%files
# not editable config files, so not using %%config here
%dir %_sysconfdir/xdg/qtchooser
%_sysconfdir/xdg/qtchooser/*.conf
%endif

%files common
%doc LICENSE.* LGPL_EXCEPTION.txt
%dir %_qt5_docdir/
%dir %_qt5_importdir/
%dir %_qt5_translationdir/
%dir %_qt5_prefix/
%dir %_qt5_prefix/doc/
%dir %_qt5_prefix/imports/
%dir %_qt5_libdatadir/
%dir %_qt5_prefix/libexec/
%dir %_qt5_prefix/plugins/
%if "%_qt5_prefix" != "%_qt5_datadir"
%dir %_qt5_datadir/
%endif
%dir %_qt5_libexecdir/
%dir %_qt5_plugindir/
%dir %_qt5_plugindir/accessible/
%dir %_qt5_plugindir/bearer/
%dir %_qt5_plugindir/generic/
%dir %_qt5_plugindir/iconengines/
%dir %_qt5_plugindir/imageformats/
%dir %_qt5_plugindir/platforminputcontexts/
%dir %_qt5_plugindir/platforms/
%dir %_qt5_plugindir/platformthemes/
%dir %_qt5_plugindir/printsupport/
%dir %_qt5_plugindir/sqldrivers/

%files doc
%if_disabled bootstrap
%doc %_qt5_docdir/*
%exclude %_qt5_docdir/global/
%endif

%files -n rpm-macros-%gname
%_rpmmacrosdir/%gname

%files devel
%_qt5_docdir/global/
%dir %_qt5_bindir
%_bindir/moc*
%_qt5_bindir/moc*
%_bindir/qdbuscpp2xml*
%_qt5_bindir/qdbuscpp2xml*
%_bindir/qdbusxml2cpp*
%_qt5_bindir/qdbusxml2cpp*
%_bindir/qdoc*
%_qt5_bindir/qdoc*
%_bindir/qmake*
%_qt5_bindir/qmake*
%_bindir/rcc*
%_qt5_bindir/rcc*
%_bindir/syncqt*
%_qt5_bindir/syncqt*
%_bindir/uic*
%_qt5_bindir/uic*
%dir %_qt5_headerdir
%_qt5_headerdir/Qt*/
%dir %_qt5_prefix/mkspecs/
%_qt5_archdatadir/mkspecs/
%_qt5_libdatadir/libQt%{major}*.prl
%_qt5_libdir/libQt%{major}*.prl
%_qt5_libdatadir/libQt%{major}*.so
%_qt5_libdir/libQt%{major}*.so
%dir %_qt5_libdir/cmake/
%_qt5_libdir/cmake/Qt%{major}*/
%_pkgconfigdir/Qt%{major}.pc
%_pkgconfigdir/Qt%{major}.pc
%_pkgconfigdir/Qt%{major}Concurrent.pc
%_pkgconfigdir/Qt%{major}Core.pc
%_pkgconfigdir/Qt%{major}DBus.pc
%_pkgconfigdir/Qt%{major}Gui.pc
%_pkgconfigdir/Qt%{major}Network.pc
%_pkgconfigdir/Qt%{major}OpenGL.pc
%_pkgconfigdir/Qt%{major}PrintSupport.pc
%_pkgconfigdir/Qt%{major}Sql.pc
%_pkgconfigdir/Qt%{major}Test.pc
%_pkgconfigdir/Qt%{major}Widgets.pc
%_pkgconfigdir/Qt%{major}Xml.pc

%files devel-static
%_qt5_libdir/libQt%{major}*.a
%_qt5_libdatadir/libQt%{major}*.a
%_pkgconfigdir/Qt%{major}Bootstrap.pc
%_pkgconfigdir/Qt%{major}OpenGLExtensions.pc
%_pkgconfigdir/Qt%{major}PlatformSupport.pc

#%files -n %gname-sql

%if_enabled sql_ibase
%files -n %gname-sql-interbase
%_qt5_plugindir/sqldrivers/libqsqlibase.so
%endif

%files -n %gname-sql-mysql
%_qt5_plugindir/sqldrivers/libqsqlmysql.so

%if_enabled sql_odbc
%files -n %gname-sql-odbc
%_qt5_plugindir/sqldrivers/libqsqlodbc.so
%endif

%if_enabled sql_pgsql
%files -n %gname-sql-postgresql
%_qt5_plugindir/sqldrivers/libqsqlpsql.so
%endif

%if_enabled sql_tds
%files -n %gname-sql-tds
%_qt5_plugindir/sqldrivers/libqsqltds.so
%endif

%if_enabled sql_sqlite2
%files -n %gname-sql-sqlite2
%_qt5_plugindir/sqldrivers/libqsqlite2.so
%endif

# packaged with sql library
#%if_enabled sql_sqlite
#%files -n %gname-sql-sqlite
#%_qt5_plugindir/sqldrivers/libqsqlite.so
#%endif


%files -n lib%{gname}-core
%_qt5_libdir/libQt%{major}Core.so.*
%_qt5_libdatadir/libQt%{major}Core.so.*

%files -n lib%{gname}-concurrent
%_qt5_libdir/libQt%{major}Concurrent.so.*
%_qt5_libdatadir/libQt%{major}Concurrent.so.*

%files -n lib%{gname}-dbus
%_qt5_libdir/libQt%{major}DBus.so.*
%_qt5_libdatadir/libQt%{major}DBus.so.*

%files -n lib%{gname}-gui
%_qt5_libdir/libQt%{major}Gui.so.*
%_qt5_libdatadir/libQt%{major}Gui.so.*
%_qt5_plugindir/generic/*
%_qt5_plugindir/imageformats/*
%_qt5_plugindir/platforminputcontexts/*
%_qt5_plugindir/platforms/*
%_qt5_plugindir/platformthemes/*

%files -n lib%{gname}-network
%_qt5_libdir/libQt%{major}Network.so.*
%_qt5_libdatadir/libQt%{major}Network.so.*
%_qt5_plugindir/bearer/*

%files -n lib%{gname}-opengl
%_qt5_libdir/libQt%{major}OpenGL.so.*
%_qt5_libdatadir/libQt%{major}OpenGL.so.*

%files -n lib%{gname}-printsupport
%_qt5_libdir/libQt%{major}PrintSupport.so.*
%_qt5_libdatadir/libQt%{major}PrintSupport.so.*
%_qt5_plugindir/printsupport/*

%files -n lib%{gname}-sql
%_qt5_libdir/libQt%{major}Sql.so.*
%_qt5_libdatadir/libQt%{major}Sql.so.*
%_qt5_plugindir/sqldrivers/libqsqlite.so

%files -n lib%{gname}-test
%_qt5_libdir/libQt%{major}Test.so.*
%_qt5_libdatadir/libQt%{major}Test.so.*

%files -n lib%{gname}-widgets
%_qt5_libdir/libQt%{major}Widgets.so.*
%_qt5_libdatadir/libQt%{major}Widgets.so.*
%_qt5_plugindir/accessible/*

%files -n lib%{gname}-xml
%_qt5_libdir/libQt%{major}Xml.so.*
%_qt5_libdatadir/libQt%{major}Xml.so.*


%changelog
* Tue Nov 26 2013 Sergey V Turchin <zerg@altlinux.org> 5.1.1-alt4
- fix crash whith xcb-1.9.3 ABI change (FDO#71507)

* Tue Nov 26 2013 Sergey V Turchin <zerg@altlinux.org> 5.1.1-alt2.M70P.2
- build docs

* Mon Nov 25 2013 Sergey V Turchin <zerg@altlinux.org> 5.1.1-alt2.M70P.1
- built for M70P

* Fri Oct 25 2013 Sergey V Turchin <zerg@altlinux.org> 5.1.1-alt3
- turn on freetype lcdfilter

* Thu Oct 24 2013 Sergey V Turchin <zerg@altlinux.org> 5.1.1-alt2
- build docs

* Mon Sep 23 2013 Sergey V Turchin <zerg@altlinux.org> 5.1.1-alt1
- initial build

Name: unixODBC
Version: 2.2.12
Release: alt6

Summary: Unix ODBC driver manager and database drivers
Summary(ru_RU.UTF-8): Система управления драйверами ODBC для unix 
Group: Databases
License: LGPL
Url: http://www.unixODBC.org

Requires: lib%name = %version-%release
Provides: MyODBC = %version-%release

Source0: http://www.unixodbc.org/%name-%version.tar.gz

Source1: %name-odbcinst.ini
Source2: %name-DataManager.desktop
Source3: %name-ODBCConfig.desktop

Patch1: %name-depcomp.patch
Patch2: %name-parserupdate.patch
Patch3: %name-2.2.11-stricmp.patch
Patch4: %name-2.2.11-symbols.patch
Patch5: %name-2.2.12-alt-ltdl.patch

# Automatically added by buildreq on Mon Feb 14 2011
BuildRequires: flex gcc-c++ libltdl7-devel libqt3-devel libreadline-devel

%description
UnixODBC is a free/open and solution for ODBC. ODBC is an open
specifican for providing application developers with a predictable API
with which to access Data Sources. Data Sources include SQL Servers and
any Data Source with an ODBC Driver.

%description -l ru_RU.UTF-8
UnixODBC - это свободное ODBC решение.
ODBC представляет из себя открытую спецификацию для разработки
приложений с универсальным API для доступа к базам данных.
Базы данных включает в себя сервера SQL и другие источники данных,
поддерживаемые ODBC драйверами.

%package -n lib%name
Summary: Shared libraries for ODBC
Summary(ru_RU.UTF-8): Разделяемые библиотеки для ODBC
Group: Development/Databases
%ifarch x86_64
Provides: libodbc.so()(64bit) libodbcinst.so()(64bit)
%else
Provides: libodbc.so libodbcinst.so
%endif

%description -n lib%name
unixODBC aims to provide a complete ODBC solution for the Linux platform.
This package contains the shared libraries.

%description -n lib%name -l ru_RU.UTF-8
unixODBC представляет из себя полную спецификацию ODBC для Linux платформы.
Этот пакет содержит в себе раделяемые библиотеки.

%package -n lib%name-devel
Summary: Includes for ODBC development
Summary(ru_RU.UTF-8): Заголовочные файлы для разработки с использованием ODBC
Group: Development/Databases
Requires: lib%name = %version-%release

%description -n lib%name-devel
unixODBC aims to provide a complete ODBC solution for the Linux platform.
This package contains the include files for development.

%description -n lib%name-devel -l ru_RU.UTF-8
unixODBC представляет из себя полную спецификацию ODBC для Linux платформы.
Этот пакет содержит заголовочные файлы для разработки с использованием ODBC

%package gui-qt
Summary: ODBC configurator, Data Source browser and ODBC test tool based on Qt
Summary(ru_RU.UTF-8): Система управления ODBC, утилита для просмотра источника данных и тестовые утилиты для ODBC, основанные на Qt
Group: Databases
Requires: %name = %version-%release

%description gui-qt
unixODBC aims to provide a complete ODBC solution for the Linux platform.
This package contains two Qt based GUI programs for unixODBC:
ODBCConfig and DataManager

%description gui-qt -l ru_RU.UTF-8
unixODBC представляет из себя полную спецификацию ODBC для Linux платформы.
Этот пакет содержит основанные на QT утилиты для работы с unixODBC.

%prep
%setup -q
rm -r libltdl
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1

%build
export QTDIR=%_qt3dir
%autoreconf
%configure \
	--with-gnu-ld \
	--enable-threads \
	--enable-gui \
	--enable-drivers \
	--enable-ltdllib \
	--with-qt-libraries=%_qt3dir/lib \
	--disable-static
%make_build

%install
%makeinstall_std

install -pD -m644 %SOURCE1 %buildroot%_sysconfdir/odbcinst.ini
subst "s,@libdir@,%_libdir," %buildroot%_sysconfdir/odbcinst.ini

install -pD -m644 %SOURCE2 %buildroot%_desktopdir/DataManager.desktop
install -pD -m644 %SOURCE3 %buildroot%_desktopdir/ODBCConfig.desktop
install -pD -m644 DataManager/LinuxODBC.xpm %buildroot%_niconsdir/LinuxODBC.xpm
install -pD -m644 DataManager/ODBC.xpm %buildroot%_miconsdir/odbc.xpm

find doc -name Makefile\* -delete

%files
%doc AUTHORS COPYING README doc/AdministratorManual doc/UserManual doc/index.html doc/*.gif
%config(noreplace) %verify(not md5 size mtime) %_sysconfdir/odbc*.ini
%_bindir/dltest
%_bindir/isql
%_bindir/iusql
%_bindir/odbcinst

%files -n lib%name
%_libdir/lib*.so.*
%exclude %_libdir/libodbcinstQ*.so.*
%_libdir/libodbc.so
%_libdir/libodbcinst.so
%_libdir/libodbcpsql.so
%_libdir/libodbcpsqlS.so
%_libdir/libodbcmyS.so

%files -n lib%name-devel
%doc ChangeLog doc/ProgrammerManual doc/lst
%_includedir/*
%_bindir/odbc_config
%_libdir/lib*.so
%exclude %_libdir/libodbc.so
%exclude %_libdir/libodbcinst.so
%exclude %_libdir/libodbcpsql.so
%exclude %_libdir/libodbcpsqlS.so
%exclude %_libdir/libodbcmyS.so
%exclude %_libdir/libodbcinstQ*.so

%files gui-qt
%_bindir/odbctest
%_bindir/ODBCConfig
%_bindir/DataManager
%_bindir/DataManagerII
%_libdir/libodbcinstQ*
%_desktopdir/*.desktop
%_iconsdir/hicolor/*/apps/*.xpm

%changelog
* Mon Feb 14 2011 Alexey Tourbin <at@altlinux.ru> 2.2.12-alt6
- rebuilt for debuginfo
- fixed build with libtool-2.2/libltdl7

* Sun Nov 14 2010 Denis Smirnov <mithraen@altlinux.ru> 2.2.12-alt5.1.1
- rebuild (with the help of girar-nmu utility)

* Thu Oct 28 2010 Denis Smirnov <mithraen@altlinux.ru> 2.2.12-alt5.1
- rebuild (with the help of girar-nmu utility)

* Fri Aug 21 2009 Dmitry V. Levin <ldv@altlinux.org> 2.2.12-alt5
- Fixed build in new build environment by enforcing use of libtool-1.5.

* Sat Nov 22 2008 Valery Inozemtsev <shrek@altlinux.ru> 2.2.12-alt4
- removed obsolete %%post_ldconfig/%%postun_ldconfig calls

* Wed Apr 25 2007 Valery Inozemtsev <shrek@altlinux.ru> 2.2.12-alt3
- fixed MyODBC library name (close #11618)

* Wed Apr 11 2007 Valery Inozemtsev <shrek@altlinux.ru> 2.2.12-alt2
- fixed provides for x86_64

* Wed Feb 07 2007 Valery Inozemtsev <shrek@altlinux.ru> 2.2.12-alt1
- update to 2.2.12
- replace old menu to freedesktop menu
- spec cleanups
- update build dependencies
- disabled static
- fixed %%_libdir in odbcinst.ini

* Wed Apr 19 2006 Mikhail Zabaluev <mhz@altlinux.ru> 2.2.11-alt2.2
- NMU
- Moved the versionless soname provides to libunixODBC (bug 9342 comment 1)

* Fri Mar 31 2006 Mikhail Zabaluev <mhz@altlinux.ru> 2.2.11-alt2.1
- NMU
- Corrected the app-lib dependency structure (bug 9342)
- Added libodbcinst.so to the main package (bug 9343)
- Got rid of ugly filelists, use %%exclude instead
- Corrected library install scripts

* Wed Jan 25 2006 Anton Farygin <rider@altlinux.ru> 2.2.11-alt2
- fixed build for x86_64

* Tue Nov 22 2005 Anton Farygin <rider@altlinux.ru> 2.2.11-alt1
- new version

* Wed Jan 19 2005 ALT QA Team Robot <qa-robot@altlinux.org> 2.2.8-alt3.1
- Rebuilt with libstdc++.so.6.

* Thu May 13 2004 Anton Farygin <rider@altlinux.ru> 2.2.8-alt3
- sync with RH: 
    Backpatch fix for double-free error from upstream devel sources.

* Tue May 11 2004 Anton Farygin <rider@altlinux.ru> 2.2.8-alt2
- packages conflict fixed (libltdl, bugzilla #4070)

* Fri Apr 30 2004 Anton Farygin <rider@altlinux.ru> 2.2.8-alt1
- new version
- added patches from RH
- removed gui-gtk

* Wed Sep 25 2002 AEN <aen@altlinux.ru> 2.2.3-alt1
- new version

* Wed Sep 25 2002 AEN <aen@altlinux.ru> 2.2.1-alt2
- rebuilt with new Qt

* Thu Jul 04 2002 AEN <aen@logic.ru> 2.2.1-alt1
- new version

* Mon Apr 08 2002 AEN <aen@logic.ru> 2.2.0-alt4
- built odbc driver for MySQL

* Thu Mar 28 2002 AEN <aen@logic.ru> 2.2.0-alt3
- libodbcinstQ -> gui-qt

* Wed Feb 13 2002 AEN <aen@logic.ru> 2.2.0-alt2
- Typo in spec

* Sat Feb 09 2002 Rider <rider@altlinux.ru> 2.2.0-alt1
- 2.2.0

* Thu Jan 03 2002 Rider <rider@altlinux.ru> 2.1.1-alt1
- build section from MDK
- 2.1.1
- temporary removed QT based tools
- russan summary and description

* Thu Oct 11 2001 AEN <aen@logic.ru> 2.0.8-alt2
- rebuilt with libpng.so.3

* Sat Sep 08 2001 Rider <rider@altlinux.ru> 2.0.8-alt1
- buildreq fix
- 2.0.8

* Fri May 04 2001 Rider <rider@altlinux.ru> 2.0.6-alt1
- libifications
- 2.0.6
- devel-static package

* Sat Feb 17 2001 AEN <aen@logic.ru>
- group names fixed

* Wed Jan 17 2001 AEN <aen@logic.ru>
- RE adaptation
- build with GUI
- BuildReq : unixODBC

* Tue Jan 16 2001 Geoffrey Lee <snailtalk@mandrakesoft.com> 2.0.3-1mdk
- bump a new and shiny source into cooker.

* Sat Nov 25 2000 Geoffrey Lee <snailtalk@mandrakesoft.com> 1.8.13-1mdk
- new and shiny source bumped into cooker.

* Fri Aug 25 2000 Giuseppe GhibР <ghibo@mandrakesoft.com> 1.8.12-1mdk
- updated release.

* Wed Aug 02 2000 Stefan van der Eijk <s.vandereijk@chello.nl> 1.8.7-2mdk
- macroszifications
- BM
- Geoff <snailtalk@mandrakesoft.com> -- fix the doc kludge

* Thu Apr 20 2000 <ghibo@mandrakesoft.com> 1.8.7-1mdk
- updated version.

* Sat Apr 15 2000 <ghibo@mandrakesoft.com> 1.8.3-1mdk
- updated to new version.
- fixed group.

* Tue Oct 19 1999 <lenny@mandrakesoft.com>
- Specfile adaptation.
- First pasckage for Mandrake

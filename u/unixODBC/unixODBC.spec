%define abiversion 2
%def_with qt

Name:    unixODBC
Version: 2.3.4
Release: alt2

Summary: Unix ODBC driver manager and database drivers
Summary(ru_RU.UTF-8): Система управления драйверами ODBC для unix 
Group: Databases
License: LGPL
Url: http://www.unixODBC.org

Requires: lib%name%abiversion = %version-%release
Provides: MyODBC = %version-%release
Provides:  unixodbc = %version-%release
Obsoletes: unixodbc < %version-%release

Source0: http://www.unixodbc.org/%name-%version.tar.gz

Source1: %name-odbcinst.ini
Source2: %name-DataManager.desktop
Source3: %name-ODBCConfig.desktop

Patch1: %name-depcomp.patch
Patch3: %name-2.2.11-export-symbols.patch
Patch4: %name-2.2.11-symbols.patch
Patch5: %name-remove-rpath-to-libdir.patch
# Patches from Fedora
Patch11: keep-typedefs.patch
Patch12: so-version-bump.patch

%{?_with_qt:BuildRequires(pre): qt4-devel}
BuildRequires: flex gcc-c++ libltdl7-devel libreadline-devel
BuildRequires: chrpath

%description
UnixODBC is a free/open and solution for ODBC. ODBC is an open
specifican for providing application developers with a predictable API
with which to access Data Sources. Data Sources include SQL Servers and
any Data Source with an ODBC Driver.
You will also need the mysql-connector-odbc package if you want to
access a MySQL database, and/or the postgresql-odbc package for
PostgreSQL.

%description -l ru_RU.UTF-8
UnixODBC - это свободное ODBC-решение.
ODBC представляет из себя открытую спецификацию для разработки
приложений с универсальным API для доступа к базам данных.
Базы данных включает в себя серверы SQL и другие источники данных,
поддерживаемые ODBC-драйверами.

%package -n lib%name%abiversion
Summary: Shared libraries for ODBC
Summary(ru_RU.UTF-8): Разделяемые библиотеки для ODBC
Group: Development/Databases
Provides:  libunixodbc%abiversion = %version-%release
Obsoletes: libunixodbc%abiversion < %version-%release

%description -n lib%name%abiversion
unixODBC aims to provide a complete ODBC solution for the Linux
platform.  This package contains the shared libraries.

%description -n lib%name%abiversion -l ru_RU.UTF-8
unixODBC представляет из себя полную спецификацию ODBC для Linux
платформы.  Этот пакет содержит в себе разделяемые библиотеки.

%package -n lib%name-devel-compat
Summary: Compat libraries for Java build
Group: Development/Databases
Conflicts: lib%{name}1 < 2.2.12-alt8
Provides:  lib%name = %version-%release
Obsoletes: lib%name < %version-%release
%ifarch x86_64
Provides: libodbc.so()(64bit) libodbcinst.so()(64bit)
%else
Provides: libodbc.so libodbcinst.so
%endif

%description -n lib%name-devel-compat
Compat libraries for Java build.

%package -n lib%name-devel
Summary: Includes for ODBC development
Summary(ru_RU.UTF-8): Заголовочные файлы для разработки с использованием ODBC
Group: Development/Databases
Requires: lib%name%abiversion = %version-%release
Requires: lib%name-devel-compat = %version-%release

%description -n lib%name-devel
unixODBC aims to provide a complete ODBC solution for the Linux
platform.  This package contains the include files for development.

%description -n lib%name-devel -l ru_RU.UTF-8
unixODBC представляет из себя полную спецификацию ODBC для Linux
платформы.  Этот пакет содержит заголовочные файлы для разработки с
использованием ODBC

%prep
%setup -q
#patch1 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p2
%patch11 -p1
%patch12 -p1

chmod 0644 Drivers/MiniSQL/*.c
chmod 0644 Drivers/nn/*.c
chmod 0644 Drivers/template/*.c
chmod 0644 doc/ProgrammerManual/Tutorial/*.html
chmod 0644 doc/lst/*
chmod 0644 include/odbcinst.h

# Blow away the embedded libtool and replace with build system's libtool.
# (We will use the installed libtool anyway, but this makes sure they match.)
rm -rf config.guess config.sub install-sh ltmain.sh libltdl
# this hack is so we can build with either libtool 2.2 or 1.5
libtoolize --install || libtoolize

%build
export QTDIR=%_qt4dir
aclocal
automake --add-missing
autoconf

# unixODBC 2.2.14 is not aliasing-safe
CFLAGS="%{optflags} -fno-strict-aliasing"
CXXFLAGS="$CFLAGS"
export CFLAGS CXXFLAGS

%configure \
	--with-gnu-ld \
	:	--enable-threads \
	--enable-drivers \
	--enable-driverc \
	--enable-ltdllib \
%if_with qt
	--enable-gui \
	--with-qt-libraries=%_qt4dir/lib \
%endif
	--disable-static
%make_build

%install
%makeinstall_std

# Remove standard libdir from exacutables and library RPATH
chrpath -d %buildroot%_bindir/* %buildroot%_libdir/libodbccr.so*

install -pD -m644 %SOURCE1 %buildroot%_sysconfdir/odbcinst.ini
subst "s,@libdir@,%_libdir," %buildroot%_sysconfdir/odbcinst.ini

find doc -name Makefile\* -delete

%files
%doc AUTHORS COPYING README doc/AdministratorManual doc/UserManual doc/index.html doc/*.gif
%config(noreplace) %verify(not md5 size mtime) %_sysconfdir/odbc*.ini
%_bindir/dltest
%_bindir/isql
%_bindir/iusql
%_bindir/odbcinst
%_bindir/slencheck
%doc %_man1dir/*
%doc %_man5dir/*
%doc %_man7dir/*

%files -n lib%name%abiversion
%_libdir/lib*.so.*
%_libdir/libodbcpsql.so
%_libdir/libodbcpsqlS.so
%_libdir/libodbcmyS.so

%files -n lib%name-devel-compat
%_libdir/libodbc.so
%_libdir/libodbcinst.so

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

%changelog
* Thu Feb 23 2017 Michael Shigorin <mike@altlinux.org> 2.3.4-alt2
- BOOTSTRAP: introduce qt knob (on by default)

* Thu Aug 04 2016 Andrey Cherepanov <cas@altlinux.org> 2.3.4-alt1
- New version (ALT #32355)
- [patch] Remove rpath with default libdir

* Mon Dec 09 2013 Andrey Cherepanov <cas@altlinux.org> 2.3.2-alt1
- New version
- Exclude libunixodbc-devel-compat for Java build (ALT #29638)
- Package man pages

* Mon Jun 17 2013 Andrey Cherepanov <cas@altlinux.org> 2.3.1-alt4
- Move provides hacks for java to appropriate package
- Set conflict to old libunixODBC with duplicate files
- Remove obsolete rule to libunixODBC

* Mon Jun 17 2013 Andrey Cherepanov <cas@altlinux.org> 2.3.1-alt3
- Move *.so to libunixODBC-devel package
- Obsolete libunixODBC

* Thu Jun 13 2013 Andrey Cherepanov <cas@altlinux.org> 2.3.1-alt2
- according to shared libs policy

* Tue Jun 04 2013 Andrey Cherepanov <cas@altlinux.org> 2.3.1-alt1
- New version 2.3.1
- qt-gui is removed from sources

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

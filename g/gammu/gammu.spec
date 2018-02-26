%def_disable static

Name: gammu
Version: 1.32.0
Release: alt1

Summary: Mobile phones management utility
License: GPL
Group: Communications

Url: http://wammu.eu/gammu/
Source: http://dl.cihar.com/gammu/releases/%name-%version.tar.bz2
Packager: Michael Shigorin <mike@altlinux.org>

Requires: lib%name = %version-%release

%{?_enable_static:BuildRequires(pre): glibc-devel-static}

# Automatically added by buildreq on Tue Aug 23 2005
BuildRequires: libMySQL-devel libbluez-devel pkg-config zlib-devel cmake
BuildPreReq: libcurl-devel glib2-devel libgudev-devel doxygen
BuildPreReq: libdbi-devel libusb-devel

Summary(ru_RU.KOI8-R): Программа для работы с мобильными телефонами

%description
Gammu can do such things with cellular phones as making data
calls, updating the address book, changing calendar and ToDo
entries, sending and receiving SMS messages, loading and getting
ring tones and pictures (different types of logos), synchronizing
time, enabling NetMonitor, managing WAP settings and bookmarks
and much more (available functions depend on the phone model).
It can also make full backups and restore them.

It currently supports many Nokia phones and AT devices (such as
Siemens, Alcatel, Falcom, WaveCom, IPAQ, and other).

%description -l ru_RU.KOI8-R
Gammu - это программа для работы с мобильными телефонами.
В зависимости от модели телефона Gammu умеет: передавать данные,
обновлять телефонную книжку, управлять записями календаря и
списка дел, принимать и отправлять короткие сообщения (SMS),
загружать в аппарат а также считывать с него мелодии и картинки
(различные виды логотипов), синхронизировать время, включать
NetMonitor, управлять настройками WAP, закладками и ещё много
всего другого.  Кроме того, Gammu позволяет делать полные
резервные копии данных телефона c возможностью их восстановления
в случае необходимости.

На данный момент поддерживается множество моделей телефонов
Nokia, а также аппаратов, понимающих AT-команды (таких как
телефоны Siemens, Alcatel, Falcom, WaveCom, IPAQ и т.д.)

%package -n lib%name
Summary: Libraries used by %name
Summary(ru_RU.KOI8-R): Динамические библиотеки %name
Group: System/Libraries

%description -n lib%name
Libraries needed for %name.

%description -n lib%name -l ru_RU.KOI8-R
Библиотеки, необходимые для %name.

%package -n lib%name-devel
Summary: Headers to compile against the lib%name library
Summary(ru_RU.KOI8-R): Заголовочные файлы для сборки с библиотекой lib%name
Group: Development/C
Requires: lib%name = %version-%release

%description -n lib%name-devel
This package contains all files which one needs to compile
programs using the lib%name library.

%description -n lib%name-devel -l ru_RU.KOI8-R
Данный пакет содержит файлы, необходимые для сборки программ,
использующих библиотеку lib%name.

%package -n lib%name-devel-static
Summary: Static %name library
Summary(ru_RU.KOI8-R): Статическая библиотека %name
Group: Development/C
Requires: lib%name-devel = %version-%release

%description -n lib%name-devel-static
This package contains static %name library.

%description -n lib%name-devel-static -l ru_RU.KOI8-R
Данный пакет содержит статическую библиотеку %name.

%package -n python-module-gammu
Summary: Python module to communicate with mobile phones
Group: Development/Python
Obsoletes: python-gammu
Requires: libgammu = %version-%release

%setup_python_module python-gammu

%description -n python-module-gammu
This provides Python gammu module that can work with any phone
that Gammu supports - many Nokias, Siemens, Alcatel, ...

%package -n bash-completion-%name
Summary: bash completion for gammu
Group: Shells
BuildArch: noarch
Requires: bash-completion
Requires: %name = %version-%release

%description -n bash-completion-%name
Bash completion for gammu

%define _gammu_docdir %_defaultdocdir/%name-%version

%prep
%setup
# this is ALT specific, no sense to maintain a patch
sed -i 's,/var/lock/LCK\.\.,/var/lock/serial/LCK..,' \
	libgammu/device/devfunc.c

%build
mkdir build
pushd build
cmake   -DCMAKE_INSTALL_PREFIX="%_usr" \
	-DINSTALL_LIB_DIR=%_libdir \
	-DINSTALL_LIBDATA_DIR=%_libdir \
	-DINSTALL_DOC_DIR=%_gammu_docdir \
	-DMYSQL_CONFIG="%_bindir/mysql_config" \
	-DBUILD_PYTHON:FILEPATH=%_bindir/python \
	-DCMAKE_C_FLAGS:STRING="%optflags" \
	-DCMAKE_CXX_FLAGS:STRING="%optflags" \
%if_disabled static
	-DENABLE_SHARED=ON \
	-DBUILD_SHARED_LIBS=ON \
%endif
..
%make_build VERBOSE=1
popd

#%%check
#cd build-dir
#ctest -V

%install
pushd build
%make install DESTDIR=%buildroot
popd
mkdir -p %buildroot%_sysconfdir
sed -e 's|^port =.*$|port = /dev/ttyS0|' \
         -e 's|^connection =.*$|connection = dlr3|' \
         -e 's|^#use_locking =.*$|use_locking = yes|' \
         -e 's/$//' \
         < docs/config/gammurc > %buildroot%_sysconfdir/%{name}rc
chmod 644 %buildroot%_sysconfdir/%{name}rc

mkdir -p %buildroot%_gammu_docdir/other/
cp -R contrib/bash-completion %buildroot%_gammu_docdir/other/

%find_lang --output=%name.lang gammu

%files -f %name.lang
%_bindir/*
%config(noreplace) %_sysconfdir/%{name}rc
%_man1dir/*
%_man5dir/*
%_man7dir/*
%_datadir/%name/
%docdir %_gammu_docdir
%dir %_gammu_docdir
%_gammu_docdir/ChangeLog
%_gammu_docdir/COPYING
%_gammu_docdir/README*
%_gammu_docdir/examples
%_gammu_docdir/other
#dir %_gammu_docdir/symbian
#_gammu_docdir/symbian

%files -n lib%name
%_libdir/*.so.*

%files -n lib%name-devel
%_includedir/*
%_libdir/*.so
%_pkgconfigdir/*
%dir %_gammu_docdir
%_gammu_docdir/manual

%if_enabled static
%files -n lib%name-devel-static
%_libdir/*.a
%endif

%files -n python-module-gammu
%python_sitelibdir/gammu

%files -n bash-completion-%name
%_sysconfdir/bash_completion.d/%name

%changelog
* Wed Jun 27 2012 Michael Shigorin <mike@altlinux.org> 1.32.0-alt1
- 1.32.0

* Sat Oct 22 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.30.0-alt2.1
- Rebuild with Python-2.7

* Thu Sep 15 2011 Michael Shigorin <mike@altlinux.org> 1.30.0-alt2
- merged with forgotten 1.29.0-alt1.1

* Fri Jul 22 2011 Michael Shigorin <mike@altlinux.org> 1.30.0-alt1
- 1.30.0
  + S60 support
  + screnshot support for DCT4
  + improved Samsung support
  + ODBC support in SMSD

* Sun Mar 13 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.29.0-alt1.1
- Rebuilt for debuginfo

* Fri Jan 21 2011 Michael Shigorin <mike@altlinux.org> 1.29.0-alt1
- 1.29.0 (thanks force@ too)

* Sun Sep 19 2010 Michael Shigorin <mike@altlinux.org> 1.28.0-alt2
- rebuilt for Sisyphus, thanks george@
- built against libmysqlclient.so.16
- minor description cleanup

* Fri Sep 17 2010 Fr. Br. George <george@altlinux.ru> 1.28.0-alt1
- Version up

* Tue Nov 17 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.23.1-alt5.1
- Rebuilt with python 2.6

* Sun Nov 15 2009 Michael Shigorin <mike@altlinux.org> 1.23.1-alt5
- rebuilt against current libbluez (see also #22272)

* Thu Jul 23 2009 Michael Shigorin <mike@altlinux.org> 1.23.1-alt4
- applied repocop patch

* Wed Apr 08 2009 Michael Shigorin <mike@altlinux.org> 1.23.1-alt3
- merged python-module-gammu (following upstream merge)

* Tue Apr 07 2009 Michael Shigorin <mike@altlinux.org> 1.23.1-alt2
- added bash-completion-gammu subpackage
  (adapted from quilt.spec)

* Tue Apr 07 2009 Michael Shigorin <mike@altlinux.org> 1.23.1-alt1
- 1.23.1
- replaced patch with subst
- fixed paths
- added man5, man7 pages

* Wed Jan 07 2009 Michael Shigorin <mike@altlinux.org> 1.22.1-alt2
- merged spec with avm's git
- fixed shared library build
- merry Christmas!

* Sun Dec 28 2008 Michael Shigorin <mike@altlinux.org> 1.22.1-alt1
- 1.22.1
- changed Packager :(
- spec cleanup

* Tue Sep 02 2008 L.A. Kostis <lakostis@altlinux.ru> 1.20.0-alt1
- version 1.20.0.
- change Packager.
- remove obsoleted patches.

* Sun Aug 03 2008 Alexander Myltsev <avm@altlinux.ru> 1.20.0-alt1
- new version: bug fixes, better error messages

* Sat May 10 2008 Fr. Br. George <george@altlinux.ru> 1.19.0-alt1
- Version up

* Wed Feb 20 2008 Michael Shigorin <mike@altlinux.org> 1.13.90-alt3
- rebuild

* Tue Feb 19 2008 Grigory Batalov <bga@altlinux.ru> 1.13.90-alt2
- Fix build on x86_64: install library into %%_libdir.

* Sun Sep 16 2007 L.A. Kostis <lakostis@altlinux.ru> 1.13.90-alt1
- 1.13.90 (testing/unstable version).
- remove obsoleted patches (hope upstream fixed those).
- update buildreq (add cmake).
- move to cmake build.
- fix mysql detection (a bit hacky).

* Sun Jan 07 2007 L.A. Kostis <lakostis@altlinux.ru> 1.09.00-alt1
- 1.09.00.
- update alt-config patch.

* Fri Sep 08 2006 L.A. Kostis <lakostis@altlinux.ru> 1.07.00-alt1
- added patch fixing http://www.gammu.org/bugs/view.php?id=3 (by mike@).
- rebuild w/ new libbluez-devel.
- .spec cleanup.

* Sat Jul 01 2006 Michael Shigorin <mike@altlinux.org> 1.07.00-alt0.1
- 1.07.00 (NMU)
- added Gentoo limits-up patch
- added unpackaged files

* Sat Jun 03 2006 LAKostis <lakostis at altlinux.ru> 1.06.00-alt1
- NMU;
- version 1.06.00.

* Sat Apr 01 2006 LAKostis <lakostis at altlinux.ru> 1.05.00-alt1
- NMU;
- version 1.05.00;
- fix build with --as-needed.

* Sat Dec 31 2005 Dmitry Vukolov <dav@altlinux.ru> 1.04.0-alt1
- version 1.04.0

* Wed Oct 19 2005 Dmitry Vukolov <dav@altlinux.ru> 1.03.0-alt1
- version 1.03.0

* Tue Oct 04 2005 Dmitry Vukolov <dav@altlinux.ru> 1.02.20-alt1
- version 1.02.20
- applied a patch from Michal Cihar fixing library linking

* Thu Sep 29 2005 Dmitry Vukolov <dav@altlinux.ru> 1.02.16-alt1
- version 1.02.16

* Mon Sep 19 2005 Dmitry Vukolov <dav@altlinux.ru> 1.02.0-alt2
- applied the at-utf8.patch from Michal Cihar

* Tue Aug 23 2005 Dmitry Vukolov <dav@altlinux.ru> 1.02.0-alt1
- version 1.02.0
- MySQL BuildRequires fixed
- translation files removed temporarily

* Wed Apr 13 2005 Dmitry Vukolov <dav@altlinux.ru> 1.01.0-alt1
- version 1.01.0
- warning: connection fbusdku2 renamed to dku2phonet and fbusdku5 renamed
  to dku5fbus. make changes to .gammurc if necessary.

* Wed Mar 02 2005 Dmitry Vukolov <dav@altlinux.ru> 1.00.10-alt1
- version 1.00.10
- pic and mysql patches removed
- extra spec switches removed

* Sun Nov 28 2004 Dmitry Vukolov <dav@altlinux.ru> 0.99.6-alt2
- corrected BuildRequires

* Thu Nov 25 2004 Dmitry Vukolov <dav@altlinux.ru> 0.99.6-alt1
- version 0.99.6
- built with MySQL support

* Mon Oct 25 2004 Dmitry Vukolov <dav@altlinux.ru> 0.99-alt1
- new version

* Fri Sep 10 2004 Dmitry Vukolov <dav@altlinux.ru> 0.98-alt1
- new version

* Fri Aug 06 2004 Dmitry Vukolov <dav@altlinux.ru> 0.97-alt1
- version 0.97
- URL corrected
- removed GammuGUI
- new script: PhoneGetRecentFiles.pl

* Wed May 05 2004 Dmitry Vukolov <dav@altlinux.ru> 0.95-alt1
- new version
- for MySQL support rebuild using --with mysql option (disabled by default)

* Fri Mar 05 2004 Dmitry Vukolov <dav@altlinux.ru> 0.94-alt1
- new version

* Tue Feb 10 2004 Dmitry Vukolov <dav@altlinux.ru> 0.93-alt1
- new version

* Sun Jan 04 2004 Dmitry Vukolov <dav@altlinux.ru> 0.92-alt1
- new version

* Fri Dec 26 2003 Dmitry Vukolov <dav@altlinux.ru> 0.91-alt1
- new version

* Sat Nov 29 2003 Dmitry Vukolov <dav@altlinux.ru> 0.90-alt1
- new version
- new package: lib%name-devel-static (disabled by default)
- added "--enable static" support to the spec
- updated makefile-pic patch
- also package %name-config, smsdutil and %{name}gui

* Thu Nov 13 2003 Dmitry Vukolov <dav@altlinux.ru> 0.89-alt1
- new version
- added makefile-pic patch to get rid of text relocations in libGammu.so

* Mon Nov 03 2003 Dmitry Vukolov <dav@altlinux.ru> 0.88-alt1
- new version
- spec file corrections

* Mon Oct 20 2003 Dmitry Vukolov <dav@altlinux.ru> 0.87-alt1
- new version
- makefile-ldlibs patch merged upstream
- added "--with 7110incoming" support to the spec

* Sun Oct 12 2003 Dmitry Vukolov <dav@altlinux.ru> 0.86-alt1
- new version
- configure patch updated
- added makefile-ldlibs patch
- pkgconfig support
- updated BuildRequires

* Fri Oct 03 2003 Dmitry Vukolov <dav@altlinux.ru> 0.85-alt1
- new version

* Thu Sep 18 2003 Dmitry Vukolov <dav@altlinux.ru> 0.84-alt1
- new version
- corrected dependencies

* Tue Sep 09 2003 Dmitry Vukolov <dav@altlinux.ru> 0.83-alt1
- version 0.83
- added package lib%name-devel
- make use of the %%lang macro

* Tue Aug 05 2003 Dmitry Vukolov <dav@altlinux.ru> 0.81-alt1
- new version

* Sun Jul 27 2003 Dmitry Vukolov <dav@altlinux.ru> 0.80-alt1
- new version

* Thu Jul 10 2003 Dmitry Vukolov <dav@altlinux.ru> 0.79-alt1
- initial build for Sisyphus
- lock-path & configure patches


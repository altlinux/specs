BuildRequires: desktop-file-utils
Name: ananas
Version: 0.9.5
Release: alt7.1

Summary: Runtime and development environment of Finance Applications
Summary(ru_RU.UTF8): Среда разработки и исполнения прикладных решений автоматизации оперативного, бухгалтерского и других видов учета.

License: GPL
Url: http://ananas.lrn.ru/
Group: Office

Packager: Vitaly Lipatov <lav@altlinux.ru>

# checkout from CVSROOT=:pserver:anonymous@www.leaderit.ru:/var/cvs , module=%%name
Source: http://prdownloads.sf.net/ananasproject/%name-%version.tar.bz2
Patch0: ananas-0.9.5-alt-DSO.patch

Provides: ananas-engine-qt = %version
Obsoletes: ananas-engine-qt

Provides: ananas-extensions = %version
Obsoletes: ananas-extensions

Requires: MySQL-client

BuildRequires: gcc-c++ kdepim-devel libMySQL-devel libqt3-qsa-devel qt3-designer

%description
Ananas is an Accounting Application Framework for Small Businesses.

Developers
---------------
Valery Grazhdankin <vg at leaderit dot ru>
Andrey Paskal <app at lrn dot ru>
Andrey Strelnikov <avsone at yandex dot ru>
Pavel Mikolaychuk <Pashik at bk dot ru>
Alexander Kovalyov <cibfx at bk dot ru>
Grigory Panov <gr1313 at mail dot ru>

%description -l ru_RU.UTF8
Платформа Ананас предназначена для автомматизации малых и средних предприятий.
Обеспечивает автоматизацию ведения оперативного и бухгалтерского учета.
Платформа позволяет создавать приложения, поддерживающие многопользовательский
режим работы, сопровождается документацией на русском языке
имеет русифицированный графический интерфейс пользователя. Для ее
использования необходимо иметь установленную систему X Window System,
графическую среду KDE и сервер баз данных с поддержкой транзакций MySQL.
Пакет ananas необходимо установить, если вы собираетесь использовать
прикладное решение на платформе Ананас.

Разработчики
---------------
Валерий Гражданкин <vg at leaderit dot ru>
Андрей Паскаль <app at lrn dot ru>
Андрей Стрельников <avsone at yandex dot ru>
Павел Миколайчук <Pashik at bk dot ru>
Александр Ковалёв <cibfx at bk dot ru>
Григорий Панов <gr1313 at mail dot ru>

%package devel
Summary: Ananas development library. Static libs and C header files
Summary(ru_RU.UTF8):	Статические библиотеки и файлы определений на языке Cи.
Group: Development/Other

%description devel
Ananas development library. Static libs and C header files.

Developers
---------------
Valery Grazhdankin <vg at leaderit dot ru>
Andrey Paskal <app at lrn dot ru>
Andrey Strelnikov <avsone at yandex dot ru>
Pavel Mikolaychuk <Pashik at bk dot ru>
Alexander Kovalyov <cibfx at bk dot ru>
Grigory Panov <gr1313 at mail dot ru>

%description -l ru_RU.UTF8 devel
Статические библиотеки и файлы определений на языке C++.
ananas-devel необходимо установить, если вы планируете использовать библиотеки
Ананаса в своей C/C++ программе. Если вы планируете использовать прикладное
решение на платформе Ананас, то пакет не нужно устанавливать.

Разработчики
---------------
Валерий Гражданкин <vg at leaderit dot ru>
Андрей Паскаль <app at lrn dot ru>
Андрей Стрельников <avsone at yandex dot ru>
Павел Миколайчук <Pashik at bk dot ru>
Александр Ковалёв <cibfx at bk dot ru>
Григорий Панов <gr1313 at mail dot ru>

%package inventory
Summary: Scripts, Documents and Reports templates of Inventory system
Summary(ru_RU.UTF8):	Прикладная настройка для ведения простого складского учета.
Group: Office
BuildArch: noarch


Requires: %name >= %version
Requires: zip unzip

%description inventory
Scripts, Documents and Reports templates of Inventory Accounting system.

Developers
---------------
Valery Grazhdankin <vg at leaderit dot ru>
Andrey Paskal <app at lrn dot ru>
Andrey Strelnikov <avsone at yandex dot ru>
Pavel Mikolaychuk <Pashik at bk dot ru>
Alexander Kovalyov <cibfx at bk dot ru>
Grigory Panov <gr1313 at mail dot ru>

%description -l ru_RU.UTF8 inventory
Прикладная настройка для ведения простого складского учета.

Разработчики
---------------
Валерий Гражданкин <vg at leaderit dot ru>
Андрей Паскаль <app at lrn dot ru>
Андрей Стрельников <avsone at yandex dot ru>
Павел Миколайчук <Pashik at bk dot ru>
Александр Ковалёв <cibfx at bk dot ru>
Григорий Панов <gr1313 at mail dot ru>

%package extensions
Summary(ru_RU.UTF8):	Набор плагинов для Ананаса.
Summary:	Ananas plugins collection.
Group:		Office
Group(ru_RU.UTF8):	Приложения/Учет и Финансы

Requires: %name >= %version

%description -l ru_RU.UTF8 extensions
Набор плагинов для Ананаса.

Разработчики
---------------
Валерий Гражданкин <vg at leaderit dot ru>
Андрей Паскаль <app at lrn dot ru>
Андрей Стрельников <avsone at yandex dot ru>
Павел Миколайчук <Pashik at bk dot ru>
Александр Ковалёв <cibfx at bk dot ru>
Григорий Панов <gr1313 at mail dot ru>

%description extensions
Ananas plugins collection.

Developers
---------------
Valery Grazhdankin <vg at leaderit dot ru>
Andrey Paskal <app at lrn dot ru>
Andrey Strelnikov <avsone at yandex dot ru>
Pavel Mikolaychuk <Pashik at bk dot ru>
Alexander Kovalyov <cibfx at bk dot ru>
Grigory Panov <gr1313 at mail dot ru>

%prep
%setup
%patch0 -p2
find -type f | xargs sed -i "s|/usr/share/ananas/extensions|%_libdir/ananas/extensions|g"
find -type f | xargs sed -i "s|QString::QString|QString|g"

%build
export PATH=${PATH}:%_qt3dir/bin
#./configure
# try to SMP build with workaround
pushd src
qmake-qt3 src.pro -o Makefile
make qmake
subst 's,$(QTDIR)/bin/uic,$(QTDIR)bin/uic -nounload,' $(find . -name Makefile)
%make
popd
make tr

%install
export PATH=${PATH}:%_qt3dir/bin

%make_install install INSTALL_ROOT="%buildroot" LIBDIR=%_libdir BINDIR=%_bindir DOCDIR=%_docdir/%name-%version INCLUDEDIR=%_includedir/ananas

mkdir -p %buildroot%_sysconfdir/ananas/
mkdir -p %buildroot%_datadir/ananas/{translations,templates,inventory}
mkdir -p %buildroot{%_pixmapsdir,%_desktopdir}

cp -f translations/*.qm %buildroot%_datadir/ananas/translations
cp -f src/designer/templates/*.* %buildroot%_datadir/ananas/templates
cp -f applications/inventory/inventory.cfg %buildroot%_sysconfdir/ananas/
cp -f applications/inventory/inventory.rc %buildroot%_sysconfdir/ananas/
cp -f applications/inventory/inventory.sql %buildroot%_datadir/ananas/inventory
cp -f applications/inventory/inventory-demo.cfg %buildroot%_sysconfdir/ananas/
cp -f applications/inventory/inventory-demo.rc %buildroot%_sysconfdir/ananas/
cp -f applications/inventory/inventory-demo.sql %buildroot%_datadir/ananas/inventory
cp -f applications/inventory/inventory_pgsql.sql %buildroot%_datadir/ananas/inventory
cp -f applications/inventory/inventory_grouprc %buildroot%_sysconfdir/ananas
cp -f applications/inventory/templ_*.odt %buildroot%_datadir/ananas/inventory
cp -f applications/inventory/templ_*.ods %buildroot%_datadir/ananas/inventory
cp -f build/kde/images/*.png %buildroot%_pixmapsdir/

cp -f build/kde/ananas.desktop %buildroot%_desktopdir/
cp -f build/kde/ananas-designer.desktop %buildroot%_desktopdir/

# add link due broken linking ananas/ananas-designer with libananasplugin.so
mv %buildroot%_libdir/ananas/qt3plugins/designer/libananasplugin.so %buildroot%_libdir/libananasplugin.so
ln -s %_libdir/libananasplugin.so %buildroot%_libdir/ananas/qt3plugins/designer/libananasplugin.so
mkdir -p %buildroot%_qt3dir/plugins/sqldrivers/
ln -s %_libdir/ananas/qt3plugins/sqldrivers/libqsqlmysqlu.so %buildroot%_qt3dir/plugins/sqldrivers/libqsqlmysqlu.so

#cp -f src/extensions/libaexttext.so %buildroot%_libdir/ananas/extensions/
#cp -f src/extensions/libaextxml.so %buildroot%_libdir/ananas/extensions/
#cp -f src/extensions/libaextte.so %buildroot%_libdir/ananas/extensions/
#cp -f src/extensions/libaext_meta.so %buildroot%_libdir/ananas/extensions/

# FIXME: move install to make
install -m 0755 src/ananas/ananas %buildroot%_bindir/ananas
install -m 0755 src/admin/ananas-administrator %buildroot%_bindir/ananas-administrator
install -m 0755 src/webengine/ananas-webengine %buildroot%_bindir/ananas-webengine
desktop-file-install --dir %buildroot%_desktopdir \
	--remove-category=Application \
	--add-category=GUIDesigner \
	%buildroot%_desktopdir/ananas-designer.desktop

%post
#creates system base for mysql
mysqlshow -u root| grep ananas_system > /dev/null || mysqladmin -u root create ananas_system || :
#touch %buildroot%_sysconfdir/ananas/groupsrc

%post inventory
#cat %_datadir/ananas/inventory/groupsrc >> %_sysconfdir/ananas/groupsrc
mysql -u root -e "create database ananas_inventory character set utf8" > /dev/null 2>&1 && mysql -u root ananas_inventory < %_datadir/ananas/inventory/inventory.sql || :
mysql -u root -e "create database ananas_inventory_demo character set utf8" > /dev/null 2>&1 && mysql -u root ananas_inventory_demo < %_datadir/ananas/inventory/inventory-demo.sql || :

%files
%_bindir/ananas
%_bindir/ananas-administrator
%_bindir/ananas-designer
%_bindir/ananas-webengine
%_libdir/libananasplugin.so
#%%_qt3dir/plugins/designer/libananasplugin.so
%_qt3dir/plugins/sqldrivers/libqsqlmysqlu.so
%dir %_docdir/%name-%version/
%_docdir/%name-%version/ananas-*.sxw
%dir %_datadir/ananas/
%_libdir/ananas/
%_libdir/libananas.so*
%_datadir/ananas/translations/
%_datadir/ananas/templates/
%_pixmapsdir/*
%_desktopdir/*.desktop

%files devel
%_includedir/ananas/*.h
%_docdir/%name-%version/*.tex

%files inventory
%dir %_sysconfdir/ananas/
%_sysconfdir/ananas/inventory_grouprc
%_sysconfdir/ananas/inventory.*
%_sysconfdir/ananas/inventory-demo.*
%_datadir/ananas/inventory/

%changelog
* Tue Jun 12 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.5-alt7.1
- Fixed build

* Thu Sep 22 2011 Andrey Cherepanov <cas@altlinux.org> 0.9.5-alt7
- Fix database plugin placement

* Thu Sep 22 2011 Andrey Cherepanov <cas@altlinux.org> 0.9.5-alt6
- Add requires to libqt3-mysql (needed to database access)

* Tue Jun 07 2011 Repocop Q. A. Robot <repocop@altlinux.org> 0.9.5-alt5.qa1
- NMU (by repocop). See http://www.altlinux.org/Tools/Repocop
- applied repocop fixes:
  * freedesktop-desktop-file-proposed-patch for ananas
  * postclean-03-private-rpm-macros for the spec file

* Tue Feb 15 2011 Andrey Cherepanov <cas@altlinux.org> 0.9.5-alt5
- Return to Sisyphus
- Build ananas-inventory as noarch
- Put libananasplugin.so to proper placement

* Tue Nov 24 2009 Repocop Q. A. Robot <repocop@altlinux.org> 0.9.5-alt4.qa1
- NMU (by repocop): the following fixes applied:
  * update_menus for ananas
  * postclean-05-filetriggers for spec file

* Wed Jun 17 2009 Vitaly Lipatov <lav@altlinux.ru> 0.9.5-alt4
- just rebuild (ALT#20321)

* Wed Nov 12 2008 Vitaly Lipatov <lav@altlinux.ru> 0.9.5-alt3
- update buildreqs

* Thu May 29 2008 Vitaly Lipatov <lav@altlinux.ru> 0.9.5-alt2
- fix subdirs intersection

* Mon Dec 31 2007 Vitaly Lipatov <lav@altlinux.ru> 0.9.5-alt1
- new version 0.9.5 (with rpmrb script)

* Fri Jul 20 2007 Dmitry V. Levin <ldv@altlinux.org> 0.9.4b-alt1.1
- Fixed workaround for libananasplugin.so dependencies on multilib architectures.

* Fri Apr 27 2007 Vitaly Lipatov <lav@altlinux.ru> 0.9.4b-alt1
- new version

* Sat Jan 06 2007 Vitaly Lipatov <lav@altlinux.ru> 0.9.3-alt0.cvs20070106
- cvs build from 20070106
- rewrote spec, add packager
- add extensions package (place extensions to libdir/ananas)
- switch spec to utf8

* Sun May 28 2006 Valery Grazdankin <leader@altlinux.ru> 0.9.3-alt0.cvs20060528
  - Automatic generated cvs build

* Mon Mar 27 2006 Valery Grazdankin <leader@altlinux.ru> 0.9.3-alt1
  - Automatic generated cvs build

* Tue Feb 21 2006 Valery Grazdankin <leader@altlinux.ru> 0.9.2-alt1
  + Add ananas extensions plugin system.

* Thu Jan 05 2006 Grigory Panov <gr1313 at mail dot ru> 0.9.1-alt1
  + Merge with st05 branch

* Wed Jun 06 2005 Valery Grazdankin <leader@altlinux.ru> 0.4.2-alt1
  + Files list was changed in the inventory package

* Fri May 06 2005 Valery Grazdankin <leader@altlinux.ru> 0.4.2-alt1
  + Added support some configuration files

* Thu May 05 2005 Andrey Paskal <app at lrn dot ru> 0.4.2-alt1
  + rpm build procedure was changed. After install ananas-inventory.*rpm
  we can immediately to work with "Deport accouning" configuration ,
  by running ananas-engine.
  + Debugged (by gr) report procession in OpenOffice format under Linux.

* Sat Mar 19 2005 Grigory Panov <gr1313 at mail dot ru> 0.4.2-alt1
  + Added template in OpenOffice format for ananas-inventory
  + Added section for remove files and directories after deinstallation
  + Added ananas-engine-qt requires to ananas-inventory package

* Tue Mar 15 2005 Valery Grazdankin <leader@altlinux.ru> 0.4.2-alt1
  + File name ananasrc changed to groupsrc
  + groupsrc have Unix file format now

* Sun Nov 21 2004 Valery Grazdankin <leader@altlinux.ru> 0.4.2-alt1
  + Correct installation procedure

* Fri Nov 05 2004 Valery Grazdankin <leader@altlinux.ru> 0.4.2-alt1
  + Added spec file for build ALT Linux packages.
  + win32 version build completed. Ananas - is multitarget application now
